# nonmot's Skills

AI エージェント向けスキルをまとめるリポジトリです。

## 導入

GitHub に公開した後、利用者は必要なスキルだけを導入できます。

```bash
npx skills add <GitHubユーザー名>/<リポジトリ名>@github-pr
```

たとえばこのリポジトリが `octo-org/personal-agent-skills` なら、次のようになります。

```bash
npx skills add octo-org/personal-agent-skills@github-pr
```

`<GitHubユーザー名>/<リポジトリ名>` は、GitHub で作成・push した実際の名前に置き換えます。導入先のエージェント環境が Skills CLI を使えることを前提にしています。

## 構成

```text
skills/
└── github-pr/                 # 動作確認用のスキル
    └── SKILL.md               # 必須: スキル本体
```

## スキルを追加する

1. `skills/` の下に、英小文字・数字・ハイフンだけからなる名前でフォルダを作る。
2. `SKILL.md` に `name` と、発動条件がわかる `description` を YAML frontmatter として書く。
3. 指示本文には、エージェントにとって固有で役立つ手順・制約だけを書く。必要になってから `scripts/`、`references/`、`assets/` を加える。
4. 作成後に次で検証する。

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/<skill-name>
```

## 含めやすいスキルの例

- 定期作業: リリースノート作成、週報、ブランチ整理
- 開発規約: プロジェクト固有のテスト・レビュー・デプロイ手順
- 成果物: 提案書、議事録、CSV/Excel、PDF の定型処理
- 外部サービス: API の安全な操作手順（認証方法・確認項目・停止条件を明記）

最初の `github-pr` は、Git の履歴からタイトル・説明文を作り、`gh pr create` で Pull Request を作成するスキルです。利用には GitHub CLI の認証が必要です。
