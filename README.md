# bonsai/mushochika

## 無尽知化 — Vibe Coding × Agent Construction × Ontology Design

`mushochika` は、求人・仕事・経験を、**知識・Ontology・Agentへ変換していくための求人資料基盤**です。

## 積み上げてきた職能

### 1. Vibe Coding

AIとの対話を開発プロセスそのものに組み込み、実際に動くものを作る。

```text
考える → AIに伝える → コード生成 → 実行 → エラー → 修正 → commit → push
```

重要なのはコード生成ではなく、**仮説から実装、実行、改善までを自走すること**です。

### 2. Agent Construction

Agentをチャットボットではなく、目的を持って判断し、道具を使い、結果を残す主体として設計する。

```text
Intent
  ↓
Agent
  ↓
Tool
  ↓
Workflow
  ↓
Execution
  ↓
Evidence / Outcome
```

Repository、Intent、Tool、Workflow、Evidenceを組み合わせ、実際に動くAgentシステムへ落とし込む。

### 3. Ontology Design

AIに何をさせるかだけでなく、**対象となる世界をどう定義するか**を設計する。

```text
Entity
 ├─ Concept
 ├─ Actor
 ├─ Goal
 ├─ Intent
 ├─ Tool
 ├─ Agent
 ├─ Workflow
 ├─ Evidence
 └─ Outcome
```

さらに、概念間の関係を明示する。

- `defines`
- `provides`
- `consumes`
- `observes`
- `analyzes`
- `plans`
- `generates`
- `executes`
- `produces`
- `verifies`
- `coordinates`

## 職能モデル

> **Vibe Coding × Agent Construction × Ontology Design**

AIを使ってコードを書く、Agentを構築する、そして「何をどう定義するか」を設計する。この3つを分離せず、一つの実践的な職能として扱う。

```text
現場の課題
   ↓
Problem
   ↓
Ontology — 意味・対象・関係
   ↓
Intent — 目的・制約
   ↓
Agent — 判断・計画
   ↓
Tool — 道具・能力
   ↓
Workflow
   ↓
Execution
   ↓
Evidence
   ↓
Knowledge
   ↓
Ontology / Agent 更新
```

## Repository Engineering

Repositoryを単なるソースコード置き場ではなく、**知識・定義・データ・Agent・Workflow・Evidenceを組織する基本単位**として扱う。

```text
Repository
  ↓
README / Code / Issues / Workflows
  ↓
Observed Facts
  ↓
Semantic Declaration
  ↓
Agent / Workflow
  ↓
Evidence
```

`bonsai/ecosystem.md` はRepositoryの意味と関係を宣言し、`bonsai/repos` はRepositoryの観測データを扱う。

## 求人文書の基本モデル

求人を「応募する／しない」だけで終わらせず、職業を知識グラフの入口として扱う。

```text
求人票
  ↓
仕事内容
  ↓
必要な能力
 ├─ Knowledge
 ├─ Skill
 ├─ Tool
 ├─ Qualification
 └─ Experience
  ↓
実際の仕事
  ↓
Evidence
  ↓
Knowledge
  ↓
次の仕事
```

## 求人資料スキーマ

```yaml
job:
  title: "職種名"
  employer: "企業"
  work:
    - task: "具体的な業務"
      context: "現場・顧客・設備など"
  knowledge:
    - domain: "業務知識"
  skills:
    - name: "技能"
  tools:
    - name: "使用する道具"
  qualifications:
    - name: "資格"
  experience:
    - years: 3
      domain: "関連業務"
  evidence:
    - source: "求人文書"
```

## 宣言と観測を分離する

```text
求人票          = declared requirement
実際の仕事内容  = observed work
応募者の能力    = candidate evidence
入社後の経験    = experience evidence
```

求人の記載と実際の仕事の差分も、次の知識になります。

## 無尽知化

仕事を経験して終わりにせず、経験を次の仕事で使える知識へ変換する。

```text
仕事
 ↓
経験
 ↓
コード / Repository
 ↓
Evidence
 ↓
Ontology
 ↓
Knowledge
 ↓
Agent
 ↓
次の仕事
 ↺
```

> **経験を消費して終わらせず、次の仕事に使える知識へ変換する。**

これが `mushochika` の中心思想です。

## 求める人材像

### Builder

仕様を待つだけではなく、自分で仮説を立て、AIを使い、動くものまで持っていける。

### Agent Engineer

Agent、Tool、Workflowの境界を理解し、複数のAgentや道具を組み合わせられる。

### Ontology Engineer

曖昧な要求を概念・属性・関係・制約に分解し、人間と機械の双方が扱える定義にできる。

### Field Engineer

現場の問題から出発し、技術を目的化せず、成果につながる手段として選択できる。

## 技術は手段

特定の言語やモデルの暗記を職能の中心に置かない。

```text
Language / Framework / LLM / Database / API
                    ↓
                   Tool
                    ↓
               Capability
                    ↓
                 Intent
                    ↓
                 Outcome
```

言語、LLM、DB、Workflow engineなどは交換可能な道具として扱う。

## 求人と能力の接続

```text
求人票
  ↓
Job Ontology
  ↓
Required Skills
  ↓
Tools / Methods / Knowledge
  ↓
Candidate Evidence
  ↓
Skill Gap
  ↓
Learning / Assignment
```

「AI経験あり」ではなく、**何を作り、何を定義し、何を実行し、どんなEvidenceを残したか**で能力を評価する。

## 関連Repository

- `bonsai/ecosystem.md` — Repositoryの意味・関係
- `bonsai/intent` — Intent Ontology
- `bonsai/world-ontology` — 世界・対象のOntology
- `bonsai/repos` — Repository観測データ
- `bonsai/agent` — Agent
- `bonsai/soshiki` — Agent組織
- `bonsai/aw` — Agentic Workflow
- `bonsai/yaml-as-agent` — 宣言的Agent
- `bonsai/ds-agent` — データ分析・Evidence

## Positioning

> **AIを使ってコードを書く人から、AIとともに意味・Agent・組織・仕事そのものを設計する人へ。**

`mushochika` は、この実践的な職能と求人を接続するための資料基盤です。
