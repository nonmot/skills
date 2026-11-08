---
name: meeting-minutes
description: Create structured Japanese meeting minutes from Meetily recording transcripts when the user asks for minutes, a meeting summary, or a transcript-based summary.
license: MIT
---

# Meeting Minutes

Read Meetily transcripts and turn them into useful minutes, not a cleaned-up transcript. Recordings live under `~/Movies/meetily-recordings`; use the bundled `scripts/load_transcript.py` from this skill's directory to list or load them.

```bash
python3 scripts/load_transcript.py --list
python3 scripts/load_transcript.py --latest
python3 scripts/load_transcript.py "/path/to/recording-directory"
```

If the user does not name a meeting, use the latest recording. If multiple candidates remain ambiguous, show the list and ask which meeting to use. The script prints meeting metadata and timestamped utterances; `[?]` marks low-confidence transcription.

Read the whole transcript, then identify the meeting's purpose, themes, decisions, unresolved points, and action items. Infer speakers only when the context supports it; otherwise leave the person unspecified or use a role. Remove fillers, repetitions, and casual digressions. Preserve important numbers, dates, and amounts; mark uncertain important facts as `(要確認)`.

By default, return the following Markdown in the conversation. Save a file only on request; when no location is given, ask before choosing one.

```markdown
# 議事録: <会議名または内容からのタイトル>

- **日時**: YYYY-MM-DD HH:MM〜HH:MM（録音 XX分）
- **参加者**: <推測できる範囲。なければ（記録なし）>

## 概要
<目的と結論を3〜5文>

## 議題ごとの要点
### 1. <議題>
- <要点>

## 決定事項
- <決定>

## アクションアイテム
| 内容 | 担当 | 期限 |
| --- | --- | --- |
| ... | ... | ... |

## 保留・要確認事項
- <未決事項>
```

Do not invent action items, owners, deadlines, attendees, or decisions. If the meeting has no actions or is mainly casual conversation, say so plainly.
