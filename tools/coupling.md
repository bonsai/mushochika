# coupling — mushochika ⇄ mimicme 疎結合の境界

> 本repo と mimicme（およびその運び手 copyrobot）の関係を**一方向・ファイル境界のみ**に固定する。
> 関係の変更は必ず本ファイルを起点に議論する。実装知識の横断を防ぐのが目的。

## 関係図（データフロー）

> 機械可読版（nodes/edges）は **`coupling.graph.yaml`** が正。下図は人間用の要約で、
> 差が出たときは yaml を基準に coupling.md を直す。

```
~/repo/data/prompts.db  (ro・外部所有・唯一の共有物)
   │
   ├─→ mimicme   [学習]   ~/.opencode/skills/mimicme/
   │     └─→ models/ 保存（scaler+kmeans）   ★所有: mimicme
   │              ▲
   ├─→ copyrobot [振る舞い] ~/repo/ore-copy/copyrobot.py（モデル ro 参照）
   │     └─→ md 出力（数字・振り返り）
   │              │
   └─→ mushochika 検証コマンド（sqlite ro）  ~/repo/mushochika/
                     │
                     ▼
              mushochika: md を受け取り FACTS / スピーチへ束ねる
```

- mimicme と mushochika の間に**直接の線はない**。両者が会うのは prompts.db の上だけ。
- mushochika が受け取るのは **md（人語で書かれた数字と原稿）のみ**。モデルもクラスタも見ない。

## 境界ルール

1. **共有物は prompts.db のみ**。両者とも読み取り専用（ro）。相互書き込みなし。
2. **所有の分離**
   - モデル・学習中間データ → mimicme（`models/`, `localbqml_data/`）
   - 数字・物語・原稿（md） → mushochika
   - DBスキーマ・設計知識 → `~/repo/ore-copy/DESIGN.md`（実装側の知識）
3. **インタフェースはファイルのみ**。import・関数呼び出し・実装知識の横断なし。
   - mimicme / copyrobot は mushochika の原稿文言を知らない（学習・出力に混ぜない）
   - mushochika はモデルの読み方・意味を知らない（数字は md 経由で受け取る）
4. **ライフサイクル分離**
   - mimicme 再学習（`init`）→ `models/` が変わるだけ。mushochika の md は不変。
   - prompts.db が増える → copyrobot 側の再出力（reflect）→ mushochika は受け取り直すだけ。
   - どちらかを壊しても片方に波及しない。再現は常に prompts.db から。

## 契約点（ファイルインタフェース一覧）

| 項目 | 場所 | 所有者 | 方向 |
|---|---|---|---|
| prompts.db | `~/repo/data/prompts.db` | 外部（生成物） | 両者 ro |
| models/ | `~/.opencode/skills/mimicme/models/` | mimicme | copyrobot のみ参照 |
| md 出力 | copyrobot 生成物 | copyrobot | mushochika へ（受け取り） |
| mushochika md | `~/repo/mushochika/` | mushochika | 末端。他へ流れない |

## 禁止

- mushochika が `models/` を直接読んで数字を捏造する
- mimicme / copyrobot が mushochika の原稿・スピーチ文言を学習データに混ぜる
- 誰かが prompts.db に書き込む

## 現状注記（2026-09-07）

- FACTS.md / GLOSSARY.md に旧称 `ore-copy.py`・`~/repo/ore-copy/reflection/` の参照が残る。
  実体は `copyrobot.py`（`ore-copy/` 直下）。参照の書き換えは未実施（候補）。
- mushochika は単独 .git 未作成（`~/repo` 直下の素 md）。push 未。
