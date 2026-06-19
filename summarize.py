#!/usr/bin/env python3
"""
活動サマリ エージェント
マークダウンレポート or テキストプロンプトから活動データを抽出し
SQLite に蓄積、定量サマリを標準出力する。

使い方:
  python summarize.py                  # カレントの *.md を処理
  python summarize.py path/to/rep.md  # ファイル指定
  echo "今日XXを作った" | python summarize.py --prompt  # 自由文
  python summarize.py --stats          # 蓄積データの統計だけ表示
"""

import re
import sqlite3
import sys
import textwrap
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "activity_summary.db"


# ──────────────────────────────────────────────
# DB 初期化
# ──────────────────────────────────────────────

SCHEMA = """
CREATE TABLE IF NOT EXISTS sessions (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file  TEXT    NOT NULL,
    period_start TEXT,
    period_end   TEXT,
    created_at   TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id  INTEGER NOT NULL REFERENCES sessions(id),
    name        TEXT    NOT NULL,
    item_count  INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS items (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL REFERENCES categories(id),
    name        TEXT    NOT NULL,
    description TEXT,
    tech_stack  TEXT
);
"""


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    conn.commit()
    return conn


# ──────────────────────────────────────────────
# マークダウン パーサー
# ──────────────────────────────────────────────

def _parse_period(text: str) -> tuple[str, str]:
    m = re.search(r'(\d{4}-\d{2}-\d{2})\s*[〜~]\s*(\d{4}-\d{2}-\d{2})', text)
    return (m.group(1), m.group(2)) if m else ("", "")


def _table_rows(block: str) -> list[dict]:
    rows, headers = [], []
    for line in block.splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not headers:
            headers = cells
        else:
            rows.append(dict(zip(headers, cells)))
    return rows


def _bullet_items(block: str) -> list[str]:
    out = []
    for line in block.splitlines():
        m = re.match(r'^\s*[-*]\s+\*{0,2}(.+?)\*{0,2}(?:\s*[—─\-]+.*)?$', line)
        if m:
            name = m.group(1).split("（")[0].split(" — ")[0].split("—")[0].strip()
            if name:
                out.append(name)
    return out


def parse_markdown(content: str) -> dict:
    data: dict = {"period_start": "", "period_end": "", "categories": []}

    period_sec = re.search(r'## 期間\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if period_sec:
        data["period_start"], data["period_end"] = _parse_period(period_sec.group(1))

    for m in re.finditer(r'### \d+\.\s+(.+?)\n(.*?)(?=\n###|\n##|\Z)', content, re.DOTALL):
        cat_name = m.group(1).strip()
        body = m.group(2)
        if "|" in body:
            rows = _table_rows(body)
            first_key = list(rows[0].keys())[0] if rows else "名前"
            items = [
                {
                    "name": r.get("プロジェクト", r.get(first_key, "")).strip(),
                    "description": r.get("説明", "").strip(),
                    "tech_stack": r.get("技術", "").strip(),
                }
                for r in rows if r.get("プロジェクト", r.get(first_key, "")).strip()
            ]
        else:
            items = [{"name": n, "description": "", "tech_stack": ""} for n in _bullet_items(body)]

        data["categories"].append({
            "name": cat_name,
            "items": items,
            "item_count": len(items),
        })
    return data


# ──────────────────────────────────────────────
# 自由文プロンプト パーサー（簡易推定）
# ──────────────────────────────────────────────

# カテゴリ推定キーワードマップ
_CAT_KEYWORDS = {
    "システム開発": ["作った", "実装", "開発", "build", "作成", "構築", "スクリプト", "ツール", "アプリ", "システム"],
    "スキル/ツール開発": ["スキル", "コマンド", "CLI", "自動化", "プラグイン", "拡張"],
    "AI連携基盤": ["AI", "LLM", "MCP", "エージェント", "プロンプト", "モデル", "RAG"],
    "学習・研究": ["学んだ", "勉強", "調べた", "読んだ", "研究", "理解", "わかった"],
    "創作": ["書いた", "小説", "詩", "創作", "ストーリー", "文章"],
    "その他": [],
}


def _infer_category(text: str) -> str:
    for cat, kws in _CAT_KEYWORDS.items():
        if cat == "その他":
            continue
        if any(kw in text for kw in kws):
            return cat
    return "その他"


def parse_prompt(text: str) -> dict:
    """自由文テキストから活動を推定する。"""
    today = datetime.now().strftime("%Y-%m-%d")
    categories: dict[str, list] = {}

    # 文・箇条書きに分割
    entries = re.split(r'[。\n,、]', text)
    for entry in entries:
        entry = entry.strip()
        if len(entry) < 4:
            continue
        # 名詞ぽい部分を名前として抽出（「を」「が」の前まで）
        name_m = re.match(r'(.+?)[をがはで]', entry)
        name = name_m.group(1).strip() if name_m else entry[:20]
        cat = _infer_category(entry)
        categories.setdefault(cat, []).append({
            "name": name,
            "description": entry,
            "tech_stack": "",
        })

    result: dict = {"period_start": today, "period_end": today, "categories": []}
    for cat_name, items in categories.items():
        result["categories"].append({
            "name": cat_name,
            "items": items,
            "item_count": len(items),
        })
    return result


# ──────────────────────────────────────────────
# DB 書き込み
# ──────────────────────────────────────────────

def store(conn: sqlite3.Connection, source: str, data: dict) -> int:
    cur = conn.execute(
        "INSERT INTO sessions (source_file, period_start, period_end, created_at) VALUES (?,?,?,?)",
        (source, data["period_start"], data["period_end"], datetime.now().isoformat()),
    )
    sid = cur.lastrowid
    for cat in data["categories"]:
        cur2 = conn.execute(
            "INSERT INTO categories (session_id, name, item_count) VALUES (?,?,?)",
            (sid, cat["name"], cat["item_count"]),
        )
        cid = cur2.lastrowid
        for item in cat["items"]:
            conn.execute(
                "INSERT INTO items (category_id, name, description, tech_stack) VALUES (?,?,?,?)",
                (cid, item["name"], item["description"], item["tech_stack"]),
            )
    conn.commit()
    return sid


# ──────────────────────────────────────────────
# サマリ表示
# ──────────────────────────────────────────────

W = 62


def _bar(n: int, max_n: int, width: int = 20) -> str:
    filled = round(n / max_n * width) if max_n else 0
    return "█" * filled + "░" * (width - filled)


def print_session_summary(conn: sqlite3.Connection, sid: int):
    s = conn.execute("SELECT * FROM sessions WHERE id=?", (sid,)).fetchone()
    cats = conn.execute(
        "SELECT * FROM categories WHERE session_id=? ORDER BY item_count DESC", (sid,)
    ).fetchall()

    total = sum(c["item_count"] for c in cats)
    max_n = cats[0]["item_count"] if cats else 1

    print("=" * W)
    print("  活動サマリ（定量レポート）")
    print("=" * W)
    print(f"  ソース    : {s['source_file']}")
    print(f"  期間      : {s['period_start']} 〜 {s['period_end']}")
    print(f"  集計日時  : {s['created_at'][:16]}")
    print(f"  総活動数  : {total} 件")
    print()
    print(f"  {'カテゴリ':<18}  {'件数':>4}  グラフ")
    print("  " + "─" * (W - 4))

    for cat in cats:
        bar = _bar(cat["item_count"], max_n)
        print(f"  {cat['name']:<18}  {cat['item_count']:>4}件  {bar}")
        items = conn.execute(
            "SELECT name, tech_stack FROM items WHERE category_id=?", (cat["id"],)
        ).fetchall()
        for item in items:
            tech = f"  [{item['tech_stack']}]" if item["tech_stack"] else ""
            print(f"       ・{item['name']}{tech}")

    print()


def print_cumulative_stats(conn: sqlite3.Connection):
    sessions = conn.execute("SELECT COUNT(*) as n FROM sessions").fetchone()["n"]
    if sessions == 0:
        print("  蓄積データなし")
        return

    print("=" * W)
    print("  累計統計（全セッション）")
    print("=" * W)
    print(f"  セッション数  : {sessions} 回")

    totals = conn.execute("""
        SELECT c.name, SUM(c.item_count) as total
        FROM categories c
        GROUP BY c.name
        ORDER BY total DESC
    """).fetchall()
    grand_total = sum(r["total"] for r in totals)
    print(f"  総活動件数    : {grand_total} 件")
    print()
    print(f"  {'カテゴリ':<18}  {'累計':>4}  {'割合':>5}")
    print("  " + "─" * (W - 4))
    for r in totals:
        pct = r["total"] / grand_total * 100 if grand_total else 0
        print(f"  {r['name']:<18}  {r['total']:>4}件  {pct:>4.0f}%")

    print()
    print("  最近のセッション")
    print("  " + "─" * (W - 4))
    recent = conn.execute(
        "SELECT id, source_file, created_at FROM sessions ORDER BY id DESC LIMIT 5"
    ).fetchall()
    for r in recent:
        print(f"  [{r['id']:>3}] {r['created_at'][:16]}  {r['source_file']}")
    print("=" * W)


# ──────────────────────────────────────────────
# メイン
# ──────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    conn = get_conn()

    # --stats のみ
    if "--stats" in args:
        print_cumulative_stats(conn)
        conn.close()
        return

    # --prompt: stdin から自由文
    if "--prompt" in args:
        text = sys.stdin.read().strip()
        if not text:
            print("エラー: 標準入力が空です", file=sys.stderr)
            sys.exit(1)
        data = parse_prompt(text)
        sid = store(conn, "(prompt)", data)
        print(f"[インポート] prompt → session_id={sid}")
        print_session_summary(conn, sid)
        print_cumulative_stats(conn)
        conn.close()
        return

    # ファイル指定 or カレントの *.md を処理
    if args:
        md_files = [Path(a) for a in args if not a.startswith("--")]
    else:
        md_files = sorted(Path(__file__).parent.glob("*.md"))

    if not md_files:
        print("エラー: .md ファイルが見つかりません", file=sys.stderr)
        sys.exit(1)

    processed = False
    for md_file in md_files:
        if not md_file.exists():
            print(f"スキップ: {md_file} (存在しない)", file=sys.stderr)
            continue

        existing = conn.execute(
            "SELECT id FROM sessions WHERE source_file=?", (md_file.name,)
        ).fetchone()
        if existing:
            print(f"[スキップ] {md_file.name} は既にインポート済み (id={existing['id']})")
            sid = existing["id"]
        else:
            content = md_file.read_text(encoding="utf-8")
            data = parse_markdown(content)
            if not data["categories"]:
                print(f"[スキップ] {md_file.name}: カテゴリ未検出")
                continue
            sid = store(conn, md_file.name, data)
            print(f"[インポート] {md_file.name} → session_id={sid}")

        print_session_summary(conn, sid)
        processed = True

    if processed:
        print_cumulative_stats(conn)

    conn.close()


if __name__ == "__main__":
    main()
