// Shared bits for the vanilla web components. No framework — these run from the
// opt-in lemma-ui bundle in a no-build HTML app.

/** Node/SSR-safe base: `class extends HTMLElement` throws when HTMLElement is
 * undefined (Node), so fall back to a dummy. Element methods only run in the
 * browser (connectedCallback), so the dummy is never exercised there. */
export const HTMLElementBase: typeof HTMLElement =
  typeof HTMLElement !== "undefined"
    ? HTMLElement
    : (class {} as unknown as typeof HTMLElement);

export function escapeHtml(value: string): string {
  return value.replace(
    /[&<>"']/g,
    (char) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" } as Record<string, string>)[char]!,
  );
}

// Host styles + the themeable CSS custom properties. Apps override any var (or
// target ::part(...)) without touching the components — themed by default, fully
// overridable. Kept neutral so it never reads as "the one Lemma look".
export const BASE_STYLES = `
:host {
  --lemma-font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --lemma-fg: #18181b;
  --lemma-muted: #71717a;
  --lemma-bg: #ffffff;
  --lemma-surface: #f4f4f5;
  --lemma-border: #e4e4e7;
  --lemma-accent: #4f46e5;
  --lemma-accent-fg: #ffffff;
  --lemma-radius: 12px;
  --lemma-gap: 10px;
  display: block;
  font-family: var(--lemma-font);
  color: var(--lemma-fg);
  font-size: 14px;
  line-height: 1.5;
}
* { box-sizing: border-box; }
button {
  font: inherit;
  cursor: pointer;
  border: 0;
  border-radius: calc(var(--lemma-radius) - 6px);
  padding: 8px 14px;
  background: var(--lemma-accent);
  color: var(--lemma-accent-fg);
  transition: opacity 120ms ease;
}
button:disabled { opacity: 0.5; cursor: default; }
.activity { color: var(--lemma-muted); }
`;
