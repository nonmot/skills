# nonmot's Skills

GitHub CLI の Agent Skills 機能で導入できる、AI エージェント向けスキル集です。

## 利用できるスキル

| スキル | 内容 |
| --- | --- |
| `git-commit` | 変更内容から Conventional Commit を作成する |
| `github-pr` | Git の履歴から Pull Request のタイトル・本文を作り、`gh pr create` で PR を作成する |
| `it-trends` | 国内外の主要ソースから日次ITトレンドを収集・要約する |
| `meeting-minutes` | Meetily の文字起こしから構造化した議事録を作成する |
| `weekly-note` | Obsidian 保管庫の週次ノートを作成する |

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
