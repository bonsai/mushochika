# ムショチカ素材: 無職期間の活動サマリ

Generated: 2026-06-01
Sources: crush AI会話履歴, opencode セッションログ, git log, DATA/kanban/, DATA/raw/, Skills/

## 期間

2026-05-19 〜 2026-06-01 （推定、記録が残っている範囲）

## カテゴリ別活動

### 1. システム開発

| プロジェクト | 説明 | 技術 |
|-------------|------|------|
| shinjuku-eiga | 新宿ミニシアター5館の週間スケジュール自動生成＋公開 | SQLite/Python/MCP/GitHub Pages |
| WordMesh | キーワード接続記憶学習システム（設計完了） | JS/Python/FTS5 |
| crush-plan | opencodeとcrushの役割分担設計 | Markdown |
| eclipse-mcp | Eclipse連携MCP | Java/MCP |
| local-rag | ローカルRAG基盤 | Python/SQLite |
| shiri | （プロジェクト） | - |

### 2. スキル/ツール開発（15+個）

- mcp-doctor — 全MCPヘルスチェック・自動修復
- quiz-maker — DATA/kanban からクイズ生成・管理
- seed-db — questions.json → SQLite DB
- weave-wiki — Wiki知識ベース構築・更新
- make-sf — SFショートストーリー生成
- make-design — 設計書生成
- make-idea — アイデア発案
- word-graph — 単語出現頻度分析＋可視化
- md-table-align — Markdownテーブル整形（CJK対応）
- tts-read — Windows TTS読み上げ
- qr-code — QRコード生成＋CLI表示
- sendto-phone — スマホにファイル転送
- kanban-updater — KANBAN進捗自動更新
- package-manager — インストール手段提案
- view-kanban — KANBAN進捗把握
- doc-watch — 文書変更検出・DB同期
- dashboard-summary — 毎朝スピーチ原稿生成
- ntp-jitter — NTPジッター可視化（p5.js）
- win-unix-utils — WindowsにUnixコマンド導入
- clip-writer — クリップボード監視自動保存
- plagger-gen-plugin / plagger-yaml / plagger-plugin-pr — Plagger連携

### 3. AI連携基盤構築

- **crush** + **opencode** のハイブリッド運用確立
- サブエージェント定義（refactor, mcp-doctor）
- MCPサーバー群の整備・管理
- キーワード抽出 → 洞察生成 → Wiki自動構築 のパイプライン
- FTS5全文検索＋ベクトル検索のDB基盤

### 4. 学習・研究

- **Java**: Eclipse, クラス設計, 継承, JAR, CLASSPATH, コンパイル実行
- **Go**: MCPサーバ, Dockerビルド, デバッグ
- **LLM**: MCP連携, Ollama, モデル管理
- **哲学**: ウィトゲンシュタイン後期哲学 × 言語ゲーム × オブジェクト指向 × 世界モデル
- **DAG**, パーサーvsシリアライザー, メソッドチェーン

### 5. 創作

- 星新一風ショートショート（DATA/novel/ に複数作品）
- 言語哲学×LLM×世界模型の会話小説試作
- 残響書（文学プロジェクト, v1〜v3）
- SF翻訳エッセイ

### 6. 実存的活動

- ディレクトリ構成の大規模整理（BRAIN/ → DATA/ 統合）
- ADR作成・管理（アーキテクチャ決定記録）
- 日常メモの体系化（日次セッションログ）
- パッケージ管理手法の比較研究（winget/choco/scoop/APT）

## ムショチカ提案

### 提案1：技術基盤構築型
> 「無職期間中、LLMをプラットフォームとして、15以上の自動化スキル・ツールをゼロから設計・実装。キーワード抽出→洞察生成→Wiki構築→クイズ生成→物語創作までを繋ぐナレッジパイプラインを確立しました。また新宿ミニシアターのスケジュール公開システムをPython/SQLite/GitHub Actionsで構築し、公開運用しています。」

### 提案2：学習×創作ハイブリッド型
> 「Java/Go/Pythonの実践を通じてLLM連携アーキテクチャを学びながら、ウィトゲンシュタイン言語哲学とオブジェクト指向の接続を探究。学んだ知識はSF小説やナレッジベースとしてアウトプットし、『学び→創り→公開』のサイクルを確立しました。」

### 提案3：プロダクト志向型
> 「『情報過多による意思決定麻痺』という自身の課題を解決するため、日次メモ→キーワード抽出→知識ベース化→クイズ/物語での反復接触という一貫したパーソナルナレッジマネジメント（PKM）基盤を構築。現在6つのアクティブプロジェクトを平行開発中。」
