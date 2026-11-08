---
name: weekly-note
description: Create a weekly note in an Obsidian vault's 02_Weekly folder when the user asks to create a weekly note for that vault.
license: MIT
---

# Weekly Note

This skill is for an Obsidian vault that stores weekly notes in `02_Weekly/`. Use it for requests such as 「今週のweekly note作って」, 「週次ノート作成」, 「ウィークリー作って」, or 「W○○のノート作って」.

## Create the note

1. Use the current date to calculate the target week with Sunday as the first day. A Sunday begins its own week. Name the file `YYYY-WWW` (for example, `2026-W20`) and format the displayed range from Sunday through Saturday. If the target already exists, ask before overwriting it.
2. Read the immediately preceding `02_Weekly/YYYY-WWW.md` and carry forward only unchecked (`- [ ]`) and in-progress (`- [-]`) TODOs.
3. Use the connected Google Calendar tool to list events from Sunday 00:00 through the following Sunday 00:00 in `Asia/Tokyo`, sorted by start time. Use the calendar connector available in the current environment; if none is connected, say so and create the note without calendar events.
4. Write `02_Weekly/YYYY-WWW.md` directly—do not use the `obsidian` CLI—with this structure:

```markdown
---
id: YYYY-WWW
aliases: []
tags:
  - weekly
---

# YYYY-WWW

**M/D (曜) 〜 M/D (曜)**

## 今週の予定

- **M/D (曜)** イベント名 HH:MM〜HH:MM

## TODO

- [ ] タスク
- [-] 進行中タスク

## 今週学んだこと

## 振り返り

## 来週やること

- [ ]
```

Use Japanese weekday labels（月・火・水・木・金・土・日） and add `・祝` for public holidays. Omit times for all-day events. Report the new path and the counts of carried-forward TODOs and calendar events.
