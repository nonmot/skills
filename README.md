# nonmot's Skills

GitHub CLI の Agent Skills 機能で導入できる、AI エージェント向けスキル集です。

## 利用できるスキル

| スキル | 内容 |
| --- | --- |
| `github-pr` | Git の履歴から Pull Request のタイトル・本文を作り、`gh pr create` で PR を作成する |

## 導入

GitHub CLI にログイン済みであることを確認してください。

```bash
gh auth login
```

### Codex のプロジェクトへ導入

対象プロジェクトのルートで実行します。スキルは `.agents/skills/github-pr/` に導入されます。

```bash
gh skills install nonmot/skills github-pr --agent codex --scope project
```

### Codex で常に使えるように導入

```bash
gh skills install nonmot/skills github-pr --agent codex --scope user
```

`gh skill` と `gh skills` は同じコマンドです。ほかの対応エージェントに導入する場合は、`--agent codex` をそのエージェント名に変更してください。

## 内容の確認と更新

導入前にスキルの内容を確認できます。

```bash
gh skills preview nonmot/skills github-pr
```

導入済みスキルの一覧と更新には、次を使います。

```bash
gh skills list
gh skills update --all
```
