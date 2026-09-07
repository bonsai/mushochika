# bonsai/mushochika

## 無尽知化 — 求人・仕事を「知識の成長」に変える

`mushochika` は、求人票を単なる募集文書としてではなく、**仕事・現場・道具・知識・経験を構造化するための資料**として扱うためのリポジトリです。

求人から読み取れる「何をするか」「何が必要か」「何を学べるか」を整理し、仕事を起点に知識を増やしていきます。

## 求人文書の基本モデル

```text
求人票
  ↓
仕事内容
  ↓
必要な能力
  ├─ 知識
  ├─ 技術
  ├─ 道具
  ├─ 資格
  └─ 現場経験
  ↓
仕事の実態
  ↓
学習項目
  ↓
知識・経験の蓄積
  ↓
次の仕事
```

求人を「応募する／しない」だけで終わらせず、**職業を知識グラフの入口**として扱います。

## 目的

- 求人文書を構造化する
- 職種・業務・スキル・資格・道具を分離する
- 求人と実際の仕事の差を記録する
- 仕事から学習項目を抽出する
- 複数求人から共通スキルを発見する
- キャリアを「求人の集合」ではなく「知識の成長」として捉える

## 求人資料のスキーマ

```yaml
job:
  title: "職種名"
  employer: "企業"
  location: "勤務地"

  work:
    - task: "具体的な業務"
      frequency: "daily"
      context: "現場・顧客・設備など"

  knowledge:
    - domain: "業務知識"
      level: "required"

  skills:
    - name: "技能"
      level: "required"

  tools:
    - name: "使用する道具"
      category: "software | hardware | equipment | service"

  qualifications:
    - name: "資格"
      required: false

  experience:
    - years: 3
      domain: "関連業務"

  learning:
    - topic: "入社前に学ぶこと"
    - topic: "入社後に学ぶこと"

  evidence:
    - source: "求人文書"
      observed_at: "YYYY-MM-DD"
```

## 仕事を5つに分解する

求人を見るときは、最低限次の5要素に分解します。

| 要素 | 問い |
|---|---|
| Work | 実際に何をするか？ |
| Knowledge | 何を知っている必要があるか？ |
| Skill | 何ができる必要があるか？ |
| Tool | 何を使うのか？ |
| Evidence | その要求は何に基づくのか？ |

この分離により、**「経験年数」と「本当に必要な能力」を分離**できます。

## Bonsai ecosystemとの関係

`mushochika` は求人・仕事を扱うドメイン資料です。

```text
bonsai/ecosystem.md
        │
        │ semantic definitions
        ▼
   mushochika
        │
        ├── Job
        ├── Work
        ├── Skill
        ├── Knowledge
        ├── Tool
        ├── Qualification
        └── Evidence
```

`mushochika` 自身が基盤Ontologyを再定義するのではなく、`intent`、`world-ontology`、`ecosystem` の定義を利用して、**求人・職業領域を専門化**します。

## 無尽知化

ここでいう無尽知化とは、仕事を経験するたびに知識を消費するのではなく、

> **仕事 → 経験 → 記録 → 構造化 → 知識 → 次の仕事**

という循環を作ることです。

```text
              ┌──────────────┐
              │    求人      │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │    仕事      │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │    経験      │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │    記録      │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │    知識      │
              └──────┬───────┘
                     │
                     └──────→ 次の求人
```

## 求人資料としての利用

求人文書は、以下の用途に使えます。

1. **応募判断** — 自分の能力と求人要求を比較する
2. **職種研究** — 同じ職種の複数求人を比較する
3. **学習計画** — 不足している知識・技能を抽出する
4. **キャリア設計** — 次に獲得すべき能力を決める
5. **企業研究** — 企業が現場で何を要求しているかを見る
6. **エージェント支援** — 求人と人材の意味的マッチングに利用する

## データの原則

求人情報には「宣言」と「観測」を混在させません。

```text
求人票の記載       = declared requirement
実際の仕事内容     = observed work
応募者の能力       = candidate evidence
入社後の経験       = experience evidence
```

これらを分離することで、求人票と実際の仕事の差分も知識になります。

## 将来のagent利用

```text
Job Document
     ↓
Parser
     ↓
Job Schema
     ↓
Ontology mapping
     ↓
Skill / Knowledge graph
     ↓
Candidate profile
     ↓
Gap analysis
     ↓
Learning plan
     ↓
Career agent
```

Agentは求人の意味を勝手に変更するのではなく、宣言された求人要件と蓄積された証拠を比較して支援します。

## Core principle

> **求人は仕事の入口であり、仕事は知識を増やす入口である。**

`mushochika` は、求人文書をキャリアと知識の成長につなげるための資料基盤です。
