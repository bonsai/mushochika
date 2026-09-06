# mushochika — INDEX（索引）

> 無職チカの本拠。データベース（prompts.db）から抽出された「俺の内容」。
> ore-copy（汎用エンジン）の出力を受け取り、面接・スピーチの武器として束ねる。

## 構成一覧

| 区分 | ファイル | 役割 |
|---|---|---|
| **核** | `FACTS.md` | 全数字の本拠（エビデンス等級付き） |
| **核** | `identity.md` | 自己定義（仮説の本拠）。道具を作るための道具を発明する |
| **核** | `virtues-7.md` | 素質7選。数字で語るムショチカの要約 |
| **辞書** | `GLOSSARY.md` | 用語・禁止表現・数字の呼び方 |
| **境界** | `coupling.md` / `coupling.graph.yaml` | mimicme/ore-copy との疎結合（人間用 + 機械可読グラフ） |
| **設計思想** | `essay-corpse-hypothesis.md` | 語り方の理論（数字は死体、仮説が命。identity の理論編） |
| **素質発見** | `essay-virtues.md` | 素質発見の経緯 |
| **振り返り** | `reflection-2026-musyoku.md` | データ編（無職期間の実測） |
| **振り返り** | `reflection-2026-musyoku-story.md` | 物語編（動機・経緯） |
| **スピーチ** | `speech-2min.md` / `speech-3min.md` | 基本版（2分/3分） |
| **スピーチ** | `speech-full.md` | 網羅版（長文）。想定問答の下敷き。短縮版の切り出し元 |
| **スピーチ** | `speech-3min-strong.md` / `speech-3min-gentle.md` | 強め/穏やか版 |
| **スピーチ** | `speech-3min-analyze.md` | 前職テーマ版（後ろ向き→AIを道具に→分析ツールで環境整備とエージェント基盤が見えた） |
| **スピーチ** | `speech-2min-persist.md` | 切り口1: 粘り強さ |
| **スピーチ** | `speech-2min-learn.md` | 切り口2: 学習速度 |
| **スピーチ** | `speech-2min-system.md` | 切り口3: 体系化 |

## 使い方

- 面接対策: `mushochika.md`（設計書）→ `identity.md`（仮説=道具を作るための道具）→ `FACTS.md`（数字）→ スピーチ（実演）
- 数字の正確さ: `FACTS.md` を参照。スピーチは「1000個」等の丸め表現を使う（GLOSSARY参照）
- 語り方: 一般論→エビデンス→信念→接続（essay-corpse-hypothesis.md）。信念の頂点は identity.md

## 関連

- 汎用エンジン: `~/repo/ore-copy/`（データ処理・生成・ML）
- データ: `~/repo/data/prompts.db`（2,276件/199セッション）
- 設計書: `~/repo/projects/kanban/mushochika.md`
- 旧実装（fossil）: `~/git/github.com/bonsai/mushochika/`（summarize.py）