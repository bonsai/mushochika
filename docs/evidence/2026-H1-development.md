# 2026 H1 Development Evidence

期間: 2026-01-01 — 2026-06-30

## 目的

この資料は、`mushochika` の「経験 → Repository → Evidence → Knowledge」という職能モデルを、2026年前半の実際のGitHub開発履歴で裏付けるためのEvidenceである。

月史そのものではなく、**観測可能な開発活動を定量・定性の両方で残す**。

## 定量Evidence

GitHubの `bonsai` organization について、`author:bonsai` と月別の `committer-date` を条件にcommit検索を行った。

| 月 | 検索で確認できたcommit | 備考 |
|---|---:|---|
| 2026-01 | 35 | 検索結果上限未到達 |
| 2026-02 | 120以上 | 2/1–14だけで100件、2/15–28で20件 |
| 2026-03 | 81 | 検索結果上限未到達 |
| 2026-04 | 64 | 検索結果上限未到達 |
| 2026-05 | 200以上 | 前半100件、後半100件で上限到達 |
| 2026-06 | 200以上 | 前半100件、後半100件で上限到達 |
| **H1** | **700以上** | GitHub検索で確認できた下限 |

### 注意

これは「実際の総commit数」ではなく、GitHub検索で確認できた**最低観測値**である。

特に2月・5月・6月は検索結果上限に達しているため、実数はこれより多い。

GitHub自身もrepository statistics APIを提供しており、weekly commit activity、last-year commit activity、contributor activityなどを取得できる。統計にはmerge commitなどの除外ルールがあるため、検索結果とGitHub Graphの数字は同一ではない。citeturn0search0turn0search3

## 定性Evidence

### 1月 — 記録・知識・自動化の入口

`vemo`、`LegalRAG`、`HelloGithubActions`、`MindMutant`、`plagger` など。

- Voice Memo
- RAG / knowledge
- GitHub Actions
- Web / Vercel
- CLI

が別々のrepoとして現れた。

**input → data/knowledge → Web/automation**

という原型。

### 2月 — AI処理系の具体化

`snsw`、`vcrora`、`vons-ai`、`vonsai-vsx-extension`、`oven`、`fatcat` など。

- TTS fine-tuning
- LoRA
- audio pipeline
- XTTS-v2 / RVC
- VS Code extension
- JSON / Webview / API
- Bun / Deno

が実装対象になった。

**model → pipeline → tool → UI**

へ進んだ。

### 3月 — Agentを開発主体として扱う

`adev`、`agent-pair-program`、`ar-nawa`、`unicode-mahjong`、`tategu-gen`、`mycarr` など。

特に `adev` のAgent Era向けPlaggerと `ask_user_question` は、人間との対話をworkflowの一部として扱う方向を示す。

**User → Agent → Tool → Action**

の原型。

### 4月 — MCP / orchestration

`line-building-law-bot`、`road-traffic-law-mcp`、`law-assistant-mcp`、`dq-party-chat`、`monju`、`.qwen-monorepo`、`qween` など。

- 法令知識をMCP toolへ
- 複数Agentによるdeliberation
- Agent delegation
- metrics / observability
- skill / orchestrator

へ進んだ。

**Knowledge → MCP → Agent → orchestration → UI**

が明確になる。

### 5月 — 高頻度の小規模実験

`cit`、`fontgen`、`yumeya`、`ikutsu`、`kidoairaku`、`dopeness`、`rainbow-clock`、`event-crawler-gs`、`plego`、`top-songs` など。

Web / AI / game / event / music / dataを小さなrepoとして高速に実装・deploy・修正した。

**idea → repo → AI/API/UI → deploy → error → fix → next**

というVibe Codingの実績が蓄積した。

### 6月 — 責務分離

`dj-kpop` / `dj-kpop-ai`、`voodoo-todo` / `voodoo-todo-agent`、`sync-repos`、`hormon`、`worldmodel-pm` など。

- V1 / V2
- UI / API / Agent / MCP / CLI
- planning / implementation
- internal data / GitHub backup
- repository sync

の責務を分離する方向が強くなった。

**product → API → Agent/MCP → CLI**

という構造が見えてきた。

## H1の変化

```
1月
memo / knowledge / Web / Actions
        ↓
2月
AI model / data / pipeline / tool
        ↓
3月
Agent / user question / workflow
        ↓
4月
MCP / multi-agent / orchestration
        ↓
5月
rapid repo experiments / deploy / error / fix
        ↓
6月
responsibility separation / Agent / MCP / sync
```

したがって2026年前半は、単純な「AIを使った開発量」ではなく、

**AI利用 → tool化 → Agent化 → MCP化 → workflow化 → Repository Engineering**

という職能の変化としてEvidence化できる。

## mushochikaとの接続

```
求人票
  ↓
必要能力
  ↓
Candidate Evidence
  ↓
実際のRepository
  ↓
Commit / Issue / Workflow
  ↓
Observed Facts
  ↓
Skill / Knowledge
  ↓
Ontology
```

このH1資料では、Repositoryを「作品一覧」ではなく、**実際に何を作り、何を接続し、どの問題を解決してきたかを観測するEvidence source**として扱う。

### Evidenceの種類

- `Repository`: 何を作ったか
- `Commit`: 何を変更したか
- `Issue`: 何を問題として定義したか
- `Workflow`: 何を自動化したか
- `Error / Fix`: 何を改善したか
- `Artifact`: 何を成果物として残したか
- `Ontology`: 何を意味として定義したか

## Source

- GitHub `bonsai` organization commit history
- `bonsai/dev-recap/.journal/month/2026-M01.md` ～ `2026-M06.md`
- GitHub REST repository statistics documentation

> この資料は、確認できたGitHub evidenceを基にしたH1 snapshot。検索上限によりcommit総数は下限表示としている。
