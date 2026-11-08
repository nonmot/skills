---
name: it-trends
description: Collect and summarize today's notable IT trends from Hacker News, GitHub, Lobsters, Hugging Face, Qiita, and Zenn when the user requests tech news or an IT-trend roundup.
license: MIT
---

# IT Trends Daily Roundup

Produce one Markdown briefing in the conversation; do not create a file unless requested. It should be scannable in about a minute and prioritize AI/LLM, cloud and infrastructure, security, and other high-signal technology news. Exclude career advice, memes, and low-signal community drama.

## Collection

Fetch these sources in parallel in one batch. Ask each fetch for titles, individual-item URLs, and one-line context.

| Source | URL |
| --- | --- |
| Hacker News | `https://hn.algolia.com/api/v1/search?tags=front_page` |
| GitHub Trending | `https://github.com/trending?since=daily` |
| Lobsters | `https://lobste.rs/` |
| Hugging Face Papers | `https://huggingface.co/papers` |
| Security on HN | `https://hn.algolia.com/api/v1/search_by_date?tags=story&query=security&numericFilters=points>50` |
| Qiita | `https://qiita.com/` |
| Zenn | `https://zenn.dev/api/articles?order=daily&count=15` |

Prefer stable APIs, JSON, or RSS over HTML scraping. Do not use Reddit: it is not reliably fetchable. A failed or unusable source should be noted briefly without blocking the rest of the briefing.

Every link must point to an individual article, repository, paper, or post—never a site homepage or listing. For HN use a story's `url`, or `https://news.ycombinator.com/item?id={objectID}` for self-posts. Build Zenn URLs as `https://zenn.dev` plus the API `path`; use Qiita's individual article URLs. Do not invent missing links; omit the item or refetch it. Use individual URLs for GitHub, Hugging Face, and Lobsters as well.

## Synthesis and output

Group related items, deduplicate the same story across sources, and put the highest-signal topics first. Use this structure with the current date:

```markdown
# IT Trends — YYYY-MM-DD

## 🤖 AI / LLM
- **[Title](url)** — Why it matters. *(source: HN 420pts)*

## ☁️ Cloud / Infrastructure
...

## 🔒 Security
...

## 🌐 General / Notable
...

## 🇯🇵 Japan (Qiita / Zenn)
...

---
*Sources scanned: HN, GitHub Trending, Lobsters, HuggingFace Papers, Qiita, Zenn*
```

Use three to six one-line bullets per section when there is enough signal. If not, write `_今日は目立った話題なし_` rather than padding. Keep the whole briefing to roughly 40 bullets or fewer, include signal metrics where available, and make each summary explain significance rather than restating its title. For a follow-up about an item, fetch that individual item and give an on-demand deeper summary.
