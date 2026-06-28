"""Advisory lint for app/widget HTML against the unified browser-SDK contract.

These checks are *advisory*: they surface common authoring mistakes so an author
(often an agent) can fix them. They never reject an upload — the caller logs the
warnings. (The previous version validated the retired `@lemma/pod-client` SDK and
was never wired into any code path.)

Unified contract — see `lemma-typescript/src/browser.ts` and the `lemma-widget` /
`lemma-builder` skills. The SDK is served only from the API origin, so the URL is
built from the injected ``window.__LEMMA_CONFIG__.apiUrl`` (a relative
``/public/sdk/...`` src 404s on app subdomains) and the body boots in ``onload``:

    <script>
      (function () {
        var cfg = window.__LEMMA_CONFIG__ || {};
        var base = (cfg.apiUrl || window.location.origin).replace(/\\/$/, "");
        var s = document.createElement("script");
        s.src = base + "/public/sdk/lemma-client.js";
        s.onload = boot;
        document.head.appendChild(s);
      })();
      function boot() {
        const client = new window.LemmaClient.LemmaClient();  // reads window.__LEMMA_CONFIG__
      }
    </script>
"""

from __future__ import annotations

import re

# (pattern, advisory message). Order is fixed for deterministic output.
_LINT_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (
        re.compile(r"@babel/standalone|type\s*=\s*['\"]text/babel['\"]", re.IGNORECASE),
        "Runtime Babel (`@babel/standalone` / `text/babel`) is not supported for apps — precompile JSX or use plain JS.",
    ),
    (
        re.compile(r"@lemma/pod-client|\bLemmaPodClient\b|\bcreateIframeTokenProvider\b"),
        "Uses the retired `@lemma/pod-client` SDK. Load `/public/sdk/lemma-client.js` and use "
        "`new window.LemmaClient.LemmaClient()` instead.",
    ),
    (
        re.compile(
            r"<script[^>]+src=['\"][^'\"]*/(?:public/sdk|sdk)/pod-client\.js['\"]",
            re.IGNORECASE,
        ),
        "Loads the retired `pod-client.js`. Use `<script src=\"/public/sdk/lemma-client.js\"></script>`.",
    ),
    (
        # Hardcoded absolute host on the SDK script (e.g. the app's own
        # subdomain, which does not serve /public/sdk — nor does pointing a local
        # app at a prod host). Build the URL from window.__LEMMA_CONFIG__.apiUrl.
        re.compile(
            r"<script[^>]+src=['\"]https?://[^'\"]*/public/sdk/lemma-client\.js['\"]",
            re.IGNORECASE,
        ),
        "Hardcodes an absolute host for the SDK script. Build the URL from "
        "`window.__LEMMA_CONFIG__.apiUrl` (the API origin) and load it in a dynamically "
        "created `<script>` that boots in `onload` — never the app's own subdomain.",
    ),
    (
        # Relative SDK src. The bundles are served ONLY from the API origin; an app
        # subdomain does not serve /public/sdk, so a relative src 404s the moment
        # a widget/app is deployed to its own host. Build from cfg.apiUrl instead.
        re.compile(
            r"<script[^>]+src=['\"]/(?:public/sdk|sdk)/lemma-(?:client|ui)\.js['\"]",
            re.IGNORECASE,
        ),
        "Loads an SDK bundle (`lemma-client.js` / `lemma-ui.js`) with a relative "
        "`/public/sdk/...` src, which 404s on app subdomains (only the API origin serves "
        "the SDK). Build the URL from `window.__LEMMA_CONFIG__.apiUrl` and boot in the "
        "script's `onload` — see the `lemma-widget` skill's \"Loading the SDK\".",
    ),
    (
        # `new window.LemmaClient(` (constructor missing the inner class). The
        # correct double form `new window.LemmaClient.LemmaClient(` does not match,
        # because `window.LemmaClient` there is followed by `.`, not `(`.
        re.compile(r"new\s+window\.LemmaClient\s*\("),
        "`new window.LemmaClient(...)` references the namespace object, not the constructor — "
        "use `new window.LemmaClient.LemmaClient()`.",
    ),
)

# A hardcoded pod id handed to the client; the host injects window.__LEMMA_CONFIG__.
_HARDCODED_POD_ID = re.compile(
    r"podId\s*:\s*['\"][0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}['\"]"
)


def lint_app_html(html: str) -> list[str]:
    """Return advisory warnings for app/widget HTML. Never raises; ``[]`` == clean."""
    warnings: list[str] = []
    for pattern, message in _LINT_PATTERNS:
        if pattern.search(html):
            warnings.append(message)
    if _HARDCODED_POD_ID.search(html):
        warnings.append(
            "Hardcoded pod id passed to the SDK. Construct "
            "`new window.LemmaClient.LemmaClient()` with no args; the host injects "
            "`window.__LEMMA_CONFIG__`."
        )
    return warnings
