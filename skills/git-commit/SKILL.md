---
name: git-commit
description: Generate a Conventional Commit and commit all staged and unstaged changes when the user asks to commit changes or draft a commit message.
license: MIT
---

# Git Commit

Create one well-formed Conventional Commit for all current changes. Do not ask for confirmation.

1. Run `git diff HEAD`. If there are no changes, tell the user and stop.
2. Read the diff and choose a concise imperative message: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, or `chore`; use an optional scope only when it clarifies the change. Keep the subject lowercase, without a period, and under 72 characters.
3. Run `git add -A`, then commit immediately. Add a concise body only when it materially helps explain a substantial change.
4. Report the resulting hash and message with `git log -1 --oneline`.

Do not add `Co-Authored-By` trailers.
