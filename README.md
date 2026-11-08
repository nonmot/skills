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

## 外部スキル

次のスキルはこのリポジトリには含めず、配布元を参照してください。

| スキル | 配布元 |
| --- | --- |
| `stop-ai-slop-jp` | [iKora128/stop-ai-slop-jp](https://github.com/iKora128/stop-ai-slop-jp) |
| `grill-with-docs` | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) |
| `gh-stack` | [github/gh-stack](https://github.com/github/gh-stack) |
| Hunk review skill | [Hunk documentation](https://www.hunk.dev/docs/agents/review-skill/) |

## 導入

GitHub CLI にログイン済みであることを確認してください。

```bash
gh auth login
```

### Codex のプロジェクトへ導入

対象プロジェクトのルートで実行します。`<skill-name>` を「利用できるスキル」表の名前に置き換えてください。スキルは `.agents/skills/<skill-name>/` に導入されます。

```bash
gh skills install nonmot/skills <skill-name> --agent codex --scope project
```

たとえば `github-pr` を導入する場合:

```bash
gh skills install nonmot/skills github-pr --agent codex --scope project
```

### Codex で常に使えるように導入

```bash
gh skills install nonmot/skills <skill-name> --agent codex --scope user
```

`gh skill` と `gh skills` は同じコマンドです。ほかの対応エージェントに導入する場合は、`--agent codex` をそのエージェント名に変更してください。

## 内容の確認と更新

導入前にスキルの内容を確認できます。

```bash
gh skills preview nonmot/skills <skill-name>
```

導入済みスキルの一覧と更新には、次を使います。

```bash
gh skills list
gh skills update --all
```
