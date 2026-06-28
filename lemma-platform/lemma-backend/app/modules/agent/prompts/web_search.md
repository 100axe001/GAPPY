## Web Search

You may use web search when the task requires current or external information. Prefer CLI search first, then save useful pages locally when you need to read, cite, or preserve sources.

Common web search commands:

```bash
lemma tools web-search "query terms" --limit 5
lemma tools run web-search --data '{"query":"query terms","max_results":3}'
```

Use `lemma tools web-search` for raw search results with URLs and snippets. For deeper work, follow promising URLs and keep source artifacts.

Common page capture commands:

```bash
save-webpage https://example.com/article --formats markdown,pdf,jpeg --out research
save-webpage https://example.com/article --formats md --name article-notes
```

Use `save-webpage` when rendered page content, markdown, PDF, or screenshots matter. Upload durable research artifacts to `/me/...` or `/pod/...` when the user or pod should be able to retrieve them later.
