# Recipe — files in an app (upload, search, view a page)

Upload a document, search the pod's index, and show a converted page. (← `apps.md`)

## The model (see `files.md`)

Document uploads are **auto-indexed** and gain derived child artifacts:
`…/document.md` (converted markdown, `<!-- PAGE N -->` markers) and
`…/pages/page_0001.jpg` (rendered page images). Search returns chunks **with page
numbers**, scoped by folder. Data files (CSV/images/…) are stored but not indexed.

## Upload

```tsx
import { useUploadFile } from "lemma-sdk/react";
const { upload, isUploading } = useUploadFile({ client, podId: client.podId });
await upload({ path: "/knowledge", file });   // a File/Blob; indexing starts automatically
```

## Scoped search

```tsx
import { useFileSearch } from "lemma-sdk/react";
const { results } = useFileSearch({
  client, podId: client.podId,
  query: "refund policy",
  scopePath: "/knowledge/billing",   // SUBTREE by default: folder + everything under it
  method: "HYBRID",                  // or VECTOR | TEXT
});
// each result: { path, content, score, page_number, page_end } → deep-link to the page
```

## Show converted markdown / a page image

```tsx
import { useFilePreview } from "lemma-sdk/react";
const { markdown, pageCount } = useFilePreview({ client, podId: client.podId, path: "/knowledge/report.pdf" });

// render a specific rendered page as an image (a child artifact of the document):
const { url } = await client.files.getUrl("/knowledge/report.pdf/pages/page_0003.jpg");
// <img src={url} alt="page 3" />
```

For agents/CLI (not the app), the same page image is what **view-image** reads
directly — `lemma file child /knowledge/report.pdf/pages/page_0003.jpg page3.jpg`
then view it; or `lemma file cat /knowledge/report.pdf --mode markdown --pages 3-7`
for the text of a page range. See `files.md` and the `lemma-user` skill.

> Exact fields: `cat /sdk/lemma-typescript/src/react/{useFileSearch,useFilePreview,useUploadFile}.ts`
> and `src/namespaces/files.ts`.
