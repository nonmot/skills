# リポジトリ運用

## 構成

- 配布するスキルはそれぞれ `skills/<skill-name>/` に置く。
- すべてのスキルに `SKILL.md` を置き、frontmatter に `name` と発動条件を区別できる `description` を必ず書く。
- スキル名は英小文字・数字・ハイフンのみを使う。フォルダ名と frontmatter の `name` は一致させる。
- `scripts/`、`references/`、`assets/` は、そのスキルの動作を直接支える場合だけ追加する。

## スキルを追加する

1. `skills/<skill-name>/SKILL.md` を作成する。
2. エージェントの判断を改善する、タスク固有の指示・制約・参照先だけを書く。
3. 配布ライセンスを決め、スキルの frontmatter に `license` として記載する。
4. 公開前にすべてのスキルを検証する。

   ```bash
   gh skills publish --dry-run
   ```

## 公開

変更を GitHub に push し、検証が通ったあとでリリースを作成する。

```bash
gh skills publish --tag v0.1.0
```

初回の対話式リリースでは、`agent-skills` リポジトリトピックを追加できる。バージョンを明示しない導入では最新リリースのタグが使われ、リリースがなければデフォルトブランチの最新コミットが使われる。
