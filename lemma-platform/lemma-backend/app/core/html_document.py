"""Wrap an HTML fragment into a full standalone document.

Conversation widgets are authored as HTML *fragments* (no doctype/html/head/
body — the display_resource tool enforces this). To serve a widget the same way a
app is served — a full page the browser SDK can run in — the fragment is
wrapped into a complete document here. The same wrapper is reused when a widget
is promoted to an app, so the promoted artifact is identical to what was shown.

Pod context (window.__LEMMA_CONFIG__) is injected separately by
app.core.runtime_config; this module only builds the document shell.

See docs/app-widget-unification.md.
"""

from __future__ import annotations

import re

# Content that already declares a full document is served as-is (only config is
# injected). Mirrors the frontend's normalizeWidgetContent check.
_FULL_DOC_RE = re.compile(r"<!doctype|<html[\s>]|<body[\s>]", re.IGNORECASE)

# Posts the rendered height to the embedding parent so an in-conversation iframe
# can size to content. Host-side shim — kept out of the artifact so a promoted
# standalone app simply never includes it.
_HEIGHT_BRIDGE = """
    <script data-lemma-embed-bridge>
      (function () {
        var post = function () {
          var h = Math.max(
            document.documentElement.scrollHeight || 0,
            document.body ? document.body.scrollHeight : 0,
            240
          );
          parent.postMessage({ type: "lemma-widget-height", height: h }, "*");
        };
        window.addEventListener("load", post);
        try { new ResizeObserver(post).observe(document.documentElement); } catch (e) {}
        post();
      })();
    </script>"""

# Universal submit bridge: lets a widget send a value back to the chat via
# window.lemma.submit(payload) or sendPrompt(text). Embedded in a conversation
# iframe it posts to the parent (lemma-os turns it into a chat message); opened
# standalone (e.g. from a surface) it POSTs to the widget submit endpoint, reusing
# this page's own ?token= for auth. Inert unless the widget calls it, so it is
# safe to include on every widget (charts simply never call submit).
_SUBMIT_BRIDGE = """
    <script data-lemma-submit-bridge>
      (function () {
        function send(payload, text) {
          var msg = { type: "lemma-widget-submit", payload: payload, text: text || null };
          if (window.parent && window.parent !== window) {
            window.parent.postMessage(msg, "*");
            return Promise.resolve({ ok: true, mode: "embed" });
          }
          var loc = window.location;
          var url = loc.pathname.replace(/\\/$/, "") + "/submit" + loc.search;
          return fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ payload: payload, text: text || null })
          }).then(function (r) { return { ok: r.ok, status: r.status, mode: "standalone" }; });
        }
        window.lemma = window.lemma || {};
        window.lemma.submit = function (payload) { return send(payload, null); };
        if (typeof window.sendPrompt !== "function") {
          window.sendPrompt = function (text) { return send(null, text); };
        }
      })();
    </script>"""

# Minimal, non-opinionated reset only — the widget/app owns its own typography,
# colors, and layout (so it looks intentional standalone and stays portable).
_RESET_STYLES = """
      *, *::before, *::after { box-sizing: border-box; }
      html, body { margin: 0; }
      img, svg, canvas, video { max-width: 100%; }
      button, input, select, textarea { font: inherit; }"""

# Embedding chrome: only applied to the in-conversation iframe so the widget
# blends into the conversation surface. A standalone (promoted) app gets none of
# this — it owns the full page.
_EMBED_STYLES = """
      html, body { min-height: 100%; background: transparent; }
      body { padding: 16px; }"""


def _escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def wrap_html_fragment(content: str, *, title: str = "", embed: bool = True) -> str:
    """Wrap a fragment into a full HTML document.

    - ``embed=True`` (in-conversation widget): transparent page + a height bridge
      so the embedding iframe can auto-size.
    - ``embed=False`` (standalone / promoted app): same shell, no height bridge.

    Content that already declares ``<!doctype>``/``<html>``/``<body>`` is returned
    unchanged — it is already a full document.
    """
    fragment = (content or "").strip()
    if _FULL_DOC_RE.search(fragment):
        return fragment

    # Height bridge only for the in-conversation iframe; submit bridge always (it
    # works both embedded — postMessage — and standalone — POST — and is inert
    # until the widget calls window.lemma.submit / sendPrompt).
    bridge = (_HEIGHT_BRIDGE if embed else "") + _SUBMIT_BRIDGE
    styles = _RESET_STYLES + (_EMBED_STYLES if embed else "")
    return f"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{_escape(title)}</title>
    <style>{styles}
    </style>
  </head>
  <body>
    {fragment}{bridge}
  </body>
</html>"""
