---
name: lemma-widget
description: "Create inline Lemma widgets for pod conversations via display_resource(type=\"WIDGET\"): self-contained HTML/SVG/Chart.js/React-CDN visuals — dashboards, data cards, forms, charts — powered by the browser Lemma SDK at /public/sdk/lemma-client.js (tables, records, files, functions, agents, conversations, datastore queries) and the lemma-ui.js agent web components. A widget is the same artifact as an HTML app and can be saved as one."
---

# Lemma Widget

Use this skill whenever you render an inline widget with
`display_resource(type="WIDGET")`, especially when it should visualize or act on
**live pod data**.

A widget is **the same artifact as an HTML app** — the host serves it and injects
pod context the same way, so a widget can later be **saved as an app verbatim**.
Author it the way you'd author an app: self-contained, pod-authenticated, reading
`window.__LEMMA_CONFIG__`. (For a full multi-page product, build an app instead —
see `lemma-builder/references/apps.md`.)

Keep explanation in your assistant text; put only renderable HTML/SVG in the widget's
`content`. Do not include `<!doctype>`, `<html>`, `<head>`, or `<body>`.

## The model, from inside a widget

(Grounds in `lemma-builder/references/pod-model.md`.) A widget is
**pod-authenticated**: it runs as the signed-in user and sees exactly what the pod
model allows — nothing extra.

- **Identity & RLS.** SDK calls run as the current user. An **RLS-on** table
  returns only their rows; a **shared** table returns the team's rows. You never
  set `user_id` — the backend scopes reads/writes. When an *agent* renders or opens
  the widget, it acts as the delegated user with that user's grants.
- **Files & search.** `client.files` reads the same tree: shared `/…` (e.g.
  `/knowledge`) and personal `/me` (owner-only) — **no `/pod` prefix**. Same
  auto-indexed documents, same scoped search, same derived `…/document.md` /
  `…/pages/*.jpg` artifacts.
- **Connectors.** `client.connectors.operations.execute(...)` runs an operation on
  the user's connected account (delegated) — the widget never holds credentials.
- **Realtime, not polling.** A *live* widget subscribes to the table stream —
  `useLiveRecords` (React) or `client.datastore.watchChanges` (any) merge row deltas in
  place. Never refetch on a `setInterval` (it flickers); see
  `lemma-builder/references/apps.md` → "Calling the API well".
- **Runtime context, injected.** The host injects `window.__LEMMA_CONFIG__`
  (`podId` / `apiUrl` / `authUrl`) at serve time, so
  `new window.LemmaClient.LemmaClient()` takes **no arguments** — it reads the pod
  context automatically and runs unchanged across local / staging / cloud (and as a
  saved app). The SDK sends `credentials: "include"`; you never manage tokens.

## First steps

Inspect the selected pod before writing data-backed widgets — learn the tables and
columns you'll bind to:

```bash
lemma pods list                                  # marks the active pod
lemma pods describe
lemma tables list
lemma query run "select * from <table> limit 5"
```

Then write a self-contained, pod-aware widget. Adapt this starter — change the
table/column names, palette, and labels; keep the structure:

```html
<style>
  .lw { --ink:#1c1a17; --muted:#6f6658; --line:#ece6da; --card:#fffdf8; --paper:#faf8f3;
        --a1:#c9a227; --a2:#c2683f; --a3:#5c7a53; --a4:#3b6ea5;
        font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
        color: var(--ink); display: block; }
  .lw-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; }
  .lw-card { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:14px 16px; }
  .lw-label { font-size:12px; letter-spacing:.04em; text-transform:uppercase; color:var(--muted); }
  .lw-value { font-size:26px; font-weight:600; line-height:1.1; margin-top:6px; font-variant-numeric:tabular-nums; }
  .lw-muted { color:var(--muted); font-size:13px; }
</style>
<div class="lw"><div id="lw-root" class="lw-muted">Loading…</div></div>
<script>
  // Load the SDK from the API origin in window.__LEMMA_CONFIG__, then boot.
  // A relative src 404s once this widget is saved as an app: the app subdomain
  // does not serve /public/sdk. See "Loading the SDK" below.
  (function () {
    var cfg = window.__LEMMA_CONFIG__ || {};
    var base = (cfg.apiUrl || window.location.origin).replace(/\/$/, "");
    var s = document.createElement("script");
    s.src = base + "/public/sdk/lemma-client.js";
    s.onload = boot;
    s.onerror = function () {
      document.getElementById("lw-root").textContent = "Couldn't load the Lemma SDK.";
    };
    document.head.appendChild(s);
  })();
  async function boot() {
    const root = document.getElementById("lw-root");
    try {
      const client = new window.LemmaClient.LemmaClient();        // reads window.__LEMMA_CONFIG__ — no args
      const rows = (await client.records.list("tickets", { limit: 100 })).items || [];
      const fmt = new Intl.NumberFormat();
      const by = {};                                              // group by a column you saw in `lemma tables list`
      rows.forEach(r => { const k = (r.data?.status ?? r.status) ?? "—"; by[k] = (by[k] || 0) + 1; });
      const cards = [`<div class="lw-card"><div class="lw-label">Tickets</div><div class="lw-value">${fmt.format(rows.length)}</div></div>`]
        .concat(Object.entries(by).slice(0, 3).map(([k, n]) =>
          `<div class="lw-card"><div class="lw-label">${k}</div><div class="lw-value">${fmt.format(n)}</div></div>`));
      root.outerHTML = `<div class="lw-grid">${cards.join("")}</div>`;
    } catch (e) {
      root.textContent = (e && e.message) || "Unable to load data.";
    }
  }
</script>
```

### Loading the SDK

`lemma-client.js` is the single unified browser SDK (built from `lemma-typescript`;
it also exposes a legacy `window.Lemma` alias). It is served **only from the API
origin** — the app subdomain a saved widget runs on does not serve `/public/sdk`,
so a relative `<script src="/public/sdk/lemma-client.js">` 404s the moment a widget
is promoted to an app. **Always build the URL from the injected
`window.__LEMMA_CONFIG__.apiUrl` and boot in `onload`:**

```html
<script>
  (function () {
    var cfg = window.__LEMMA_CONFIG__ || {};
    var base = (cfg.apiUrl || window.location.origin).replace(/\/$/, "");
    var s = document.createElement("script");
    s.src = base + "/public/sdk/lemma-client.js";   // API origin, works in every environment
    s.onload = boot;                                 // run your widget body here
    s.onerror = function () { /* render an error state */ };
    document.head.appendChild(s);
  })();
  function boot() {
    const client = new window.LemmaClient.LemmaClient();   // reads window.__LEMMA_CONFIG__ — no args
    // …
  }
</script>
```

Never hardcode an absolute host (especially the app's own subdomain), and never use
a relative SDK src. Don't inline or reimplement SDK helpers.

## SDK map

Once `boot()` runs (SDK loaded), `const client = new window.LemmaClient.LemmaClient();`
then call any namespace:

```js
await client.tables.list();
await client.tables.get("tickets");

await client.records.list("tickets", { limit: 100, sort: [{ field: "created_at", direction: "desc" }] });
await client.records.list("tickets", {
  filters: [{ field: "status", op: "eq", value: "open" }],
  sort: [{ field: "created_at", direction: "desc" }],
  limit: 50,
});
await client.records.get("tickets", "record-id");
await client.records.create("tickets", { title: "Follow up", status: "open" });
await client.records.update("tickets", "record-id", { status: "done" });

await client.datastore.query("select status, count(*) as total from tickets group by status");

await client.files.list({ directoryPath: "/knowledge", limit: 50 });        // shared tree (no /pod prefix)
await client.files.list({ directoryPath: "/me", limit: 50 });               // personal tree
await client.files.search("quarterly planning", { limit: 10 });
await client.files.get("/knowledge/brief.md");
await client.files.getUrl("/knowledge/chart.png");                          // { url, app_url, expires_at }
await client.files.createSignedUrl("/knowledge/chart.png", { expiresSeconds: 3600, maxHits: 50 }); // public, hit-capped
await client.files.converted.render("/knowledge/report.pdf");              // converted markdown / page render

await client.functions.list();
await client.functions.runs.create("score_ticket", { input: { record_id: "..." } });

await client.agents.list();
await client.conversations.list({ limit: 10 });
```

RLS applies to every call: records and `datastore.query` over RLS tables return
only the signed-in user's rows automatically — no per-user `WHERE` needed. For
aggregates, joins, trends, and chart prep, prefer `client.datastore.query(sql)`
over fetching many pages and aggregating in the browser.

## Agent web components (drop-in, no framework)

To put an agent in a widget without hand-rolling chat or a working/output UI, load
the **opt-in** UI bundle *after* the client bundle and use the custom elements.
They drive the same agent core the product uses, register themselves on load, and
read the injected `window.__LEMMA_CONFIG__` (no auth wiring):

```html
<script>
  // Load the client bundle, then the opt-in UI bundle — both from the API origin
  // in window.__LEMMA_CONFIG__ (a relative src 404s once saved as an app). The
  // custom elements register on load and upgrade the tags already in the DOM.
  (function () {
    var cfg = window.__LEMMA_CONFIG__ || {};
    var base = (cfg.apiUrl || window.location.origin).replace(/\/$/, "");
    function load(path, next) {
      var s = document.createElement("script");
      s.src = base + path; s.onload = next || null; document.head.appendChild(s);
    }
    load("/public/sdk/lemma-client.js", function () {   // first: window.LemmaClient + config
      load("/public/sdk/lemma-ui.js");                  // then: registers the elements
    });
  })();
</script>

<!-- One-shot run → working state → final output (JSON-pretty if the agent returns structured output) -->
<lemma-agent-task agent="classify" input='{"id":"123"}' auto-run></lemma-agent-task>

<!-- Full chat → message list + composer; conversation created on first send -->
<lemma-agent-thread agent="support" style="height:480px"></lemma-agent-thread>
```

- `<lemma-agent-task>` — attrs `agent`, `pod` (optional), `input` (string/JSON),
  `auto-run`, `parse-output` (default `true`); JS `el.run(input?)`; emits
  `lemma-output` (`detail: { output, text }`) when the run settles.
- `<lemma-agent-thread>` — attrs `agent`, `pod`, `conversation-id` (optional;
  auto-creates on first send); JS `el.send(text)`.
- **Theming.** Both render in Shadow DOM and are themed by CSS custom properties on
  the host — override `--lemma-bg`, `--lemma-surface`, `--lemma-border`,
  `--lemma-fg`, `--lemma-muted`, `--lemma-accent`, `--lemma-accent-fg`,
  `--lemma-radius`, `--lemma-font` (or target `::part(message|composer|input|output|run-button|…)`).
  No component edits.
- `lemma-ui.js` is **opt-in** (it does not re-bundle the client/auth) — only load it
  when you use the elements. For bespoke layouts, use `client.agents.*` /
  `client.conversations.*` directly. (Same components, deeper guidance:
  `lemma-builder/references/app-recipes/agent-chat.md`.)

## Design — principles, not a fixed system

A widget should be **calm, legible, and mobile-friendly**. These are principles —
pick a look that fits the pod; you're not required to adopt any one design system.

- **Self-contained only.** The widget renders in its **own iframe** — host/frontend
  CSS variables (`var(--color-*)`, `var(--border-radius-*)`, `var(--font-*)`) **do
  not exist there**. Referencing them yields broken, unstyled output, and breaks the
  widget when saved as an app. Define your own tokens in a leading `<style>` block;
  set explicit colors and a `font-family`; don't rely on inherited host styles.
- **Calm and intentional.** Compact, useful, generous whitespace. A clean warm-light
  palette reads well (the starter's `--ink`/`--muted`/`--line`/`--card` + 2–4
  accents); avoid a rainbow. Sentence case; no prose paragraphs inside the widget —
  put explanation in assistant text.
- **Legible.** Cards: own background, `1px` border in your line color, `~14px`
  radius, `~14–16px` padding. Metric: uppercase ~12px muted label, ~26px/600 value,
  `font-variant-numeric: tabular-nums`. Format every visible number with
  `Intl.NumberFormat`, `.toFixed`, or `Math.round`.
- **Mobile-friendly.** `display:block; width:100%`; no fixed positioning, no nested
  scroll areas. Grids with `repeat(auto-fit, minmax(160px, 1fr))` and `minmax(0, 1fr)`
  stay readable narrow.
- **Progressive.** Start with visible HTML and styles; put scripts last so
  something useful appears while streaming. Always render loading, empty, and error
  states.

## Chart widgets

Use Chart.js for most charts:

```html
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:16px;" id="stats"></div>
<div style="position:relative;width:100%;height:300px;"><canvas id="chart"></canvas></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js" onload="init()"></script>
<script>
// Load the SDK from the API origin (see "Loading the SDK"); init() guards on both
// window.Chart and window.LemmaClient, so whichever loads last kicks it off.
(function () {
  var cfg = window.__LEMMA_CONFIG__ || {};
  var base = (cfg.apiUrl || window.location.origin).replace(/\/$/, "");
  var s = document.createElement("script");
  s.src = base + "/public/sdk/lemma-client.js";
  s.onload = init;
  document.head.appendChild(s);
})();
let started = false;
let client;
const colors = ["#378ADD", "#1D9E75", "#D85A30", "#7F77DD"];

async function init() {
  if (started || !window.Chart || !window.LemmaClient) return;
  started = true;
  client = new window.LemmaClient.LemmaClient();
  const result = await client.datastore.query("select status, count(*) as total from tickets group by status");
  const rows = result.rows || result.items || [];
  const total = rows.reduce((sum, row) => sum + Number(row.total || 0), 0);
  document.getElementById("stats").innerHTML =
    `<div style="background:#fffdf8;border:1px solid #ece6da;border-radius:14px;padding:14px 16px;color:#1c1a17;">
      <div style="font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:#6f6658;">Total</div>
      <div style="font-size:26px;font-weight:600;">${new Intl.NumberFormat().format(total)}</div>
    </div>`;
  new Chart(document.getElementById("chart"), {
    type: "bar",
    data: {
      labels: rows.map(row => row.status || "Unknown"),
      datasets: [{ data: rows.map(row => Number(row.total || 0)), backgroundColor: colors }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: { y: { ticks: { precision: 0 } } }
    }
  });
}
if (window.Chart) init();
</script>
```

Chart rules:

- Wrap each `<canvas>` in a `position:relative` div with explicit height. Do not set
  height on the canvas.
- Disable the Chart.js default legend and build an HTML legend when categories need
  labels or percentages.
- Horizontal bars: height at least `(bar_count * 40) + 80`.
- Chart.js canvas can't read CSS variables reliably; use stable hex colors for
  datasets.

## React and Tailwind

Prefer plain HTML/CSS/JS for speed and reliability. Use React only when the widget
has meaningful component state. Load React from an allowed CDN, then render:

```html
<div id="root"></div>
<script src="https://cdn.jsdelivr.net/npm/react@18/umd/react.production.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/react-dom@18/umd/react-dom.production.min.js"></script>
<script>
// Load the SDK from the API origin (see "Loading the SDK"), then mount.
(function () {
  var cfg = window.__LEMMA_CONFIG__ || {};
  var base = (cfg.apiUrl || window.location.origin).replace(/\/$/, "");
  var s = document.createElement("script");
  s.src = base + "/public/sdk/lemma-client.js";
  s.onload = boot;
  document.head.appendChild(s);
})();
function boot() {
const { useEffect, useState } = React;
const client = new window.LemmaClient.LemmaClient();
function App() {
  const [items, setItems] = useState([]);
  useEffect(() => { client.records.list("tickets", { limit: 20 }).then(r => setItems(r.items || [])); }, []);
  return React.createElement("div", { style: { color: "#1c1a17", fontFamily: "ui-sans-serif, system-ui, sans-serif" } }, `${items.length} tickets`);
}
ReactDOM.createRoot(document.getElementById("root")).render(React.createElement(App));
}
</script>
```

Tailwind CDN is fine for mockups and quick visual composition, but a self-contained
`<style>` block with your own tokens is preferred — it stays portable when saved as
an app:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

## Interactions

- Local JS for filtering, sorting, toggles, calculations, chart-mode switches.
- `sendPrompt(text)` for actions that should ask the agent to reason, explain,
  drill down, or do multi-step work — and `lemma.submit(payload)` to send structured
  input back (forms, picks, confirmations). See *Submitting back to the chat*.
- SDK mutations only for clear user actions — label buttons with direct verbs; keep
  destructive actions out of widgets unless the user explicitly asked for them.

## Submitting back to the chat

A widget can send a value back into the conversation; the agent reads it and continues.
Two globals are injected into **every** served widget — you don't add them, the host's
submit bridge does:

- `window.lemma.submit(payload)` — send a structured object (a form's answers, a picked
  row, a confirmation).
- `sendPrompt(text)` — send a plain-text instruction. Use this for "ask the agent to do
  X"; use `lemma.submit` for "here are my structured answers."

**The round-trip.** Whether the widget is embedded in the conversation (the bridge posts
to the parent frame) or opened standalone from a surface link (the bridge POSTs the
widget submit endpoint with the page's signed token), the backend does the same thing: it
appends a **new user message** to the conversation — body is `text` if you passed one,
otherwise the JSON of `payload` — and **starts a new agent run**. There is no separate
"widget callback"; a submission is just another user turn.

So design the submit as the message you want the agent to act on, and write the agent's
instruction to expect it (e.g. "the user may submit a form; the message will contain the
chosen fields as JSON"). Keep submits intentional — one clear action per submit, labelled
with a direct verb; don't auto-submit on render.

An agent renders a submitting widget with
`display_resource(type="WIDGET", interactive=true, …)`; `interactive=true` is the signal
that the widget submits back. The submit bridge is injected into every served widget
automatically — you never wire it. (Chat-level round-trip + the endpoints:
`lemma-builder/references/agent-tools.md`.)

## Output checklist

Before calling `display_resource` with `type="WIDGET"`:

- `content` is an HTML/SVG fragment, not a full HTML document, and works without secrets.
- `loading_messages` (optional) is 1–4 short messages shown while the widget renders.
- The SDK URL is built from `window.__LEMMA_CONFIG__.apiUrl` and the body boots in
  `onload` — never a relative `/public/sdk/...` src (404s once saved as an app) and
  never a hardcoded absolute host. See "Loading the SDK".
- File paths use shared `/…` and personal `/me` — never `/pod/...`.
- Any pod id came from runtime config, not a hardcoded value.

## See also

- A widget as a full app → `lemma-builder/references/apps.md`
- Agent chat in HTML/React → `lemma-builder/references/app-recipes/agent-chat.md`
- Interaction/voice/approval tools & the submit round-trip →
  `lemma-builder/references/agent-tools.md`
- The pod model → `lemma-builder/references/pod-model.md`
- Operate the pod from the CLI → the `lemma-user` skill
