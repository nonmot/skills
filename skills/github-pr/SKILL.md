---
name: github-pr
description: Create a GitHub Pull Request using the gh command with an auto-generated title and description based on git history. Use this skill whenever the user says "PR作って", "PRを作成して", "create a PR", "open a pull request", "プルリクエスト作って", or anything implying they want to open a PR on GitHub. Always use this skill — don't just run gh commands directly.
---

# GitHub PR Skill

Help the user create a well-structured GitHub Pull Request using `gh pr create`.

## Workflow

### 1. Gather context

Run these in parallel:

```bash
git branch --show-current          # current branch name
git log main..HEAD --oneline       # commits on this branch
git diff main...HEAD               # full diff vs main
gh pr list --state open --limit 5  # check for existing PRs
```

If already on `main`, tell the user and stop — they need to switch to a feature branch first.

If a PR already exists for this branch, show its URL and stop. Do not modify an
existing PR unless the user explicitly asks to do so.

### 2. Determine the base branch

Default base branch is `main`. If the repo uses a different default (e.g., `master`, `develop`), use that instead. You can check with:

```bash
gh repo view --json defaultBranchRef --jq '.defaultBranchRef.name'
```

### 3. Analyze and create the PR

Read the commits and diff carefully. Generate:

**Title** — Conventional Commits format, under 72 characters:
```
<type>(<scope>): <subject>
```

**Body** — structured summary in Japanese (or English if the user writes in English):
```markdown
## 概要
<!-- 何をしたか、なぜしたか -->

## 変更内容
<!-- 箇条書きで主な変更点 -->

## 確認事項
<!-- レビュアーに見てほしい点、注意点 -->
```

Pick `<type>` from: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Create the PR immediately after generating the title and body. Do not ask the
user to confirm the draft. If the user has supplied a title or body, use it;
otherwise use the generated draft.

```bash
gh pr create \
  --title "<title>" \
  --body "$(cat <<'EOF'
<body>
EOF
)"
```

After creating, show the PR URL clearly:

```
PR作成完了！
https://github.com/owner/repo/pull/123
```

## Conventional Commits cheat sheet

| Type | When to use |
|------|-------------|
| `feat` | New feature or capability |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, whitespace (no logic change) |
| `refactor` | Code restructure without behavior change |
| `test` | Adding or updating tests |
| `chore` | Build, deps, config, maintenance |

## Notes

- Never add `Co-Authored-By` trailers to the PR body
- If `gh` is not authenticated, tell the user to run `gh auth login` first
- If the branch has no upstream, push it first: `git push -u origin <branch>`
