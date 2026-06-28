// Vanilla web components for no-build HTML apps. Framework-agnostic, built on
// the agent core; theme via CSS custom properties + ::part(...). Workflow ships
// no web component by design (too bespoke) — apps use the core helpers.
import { LemmaAgentTaskElement } from "./lemma-agent-task.js";
import { LemmaAgentThreadElement } from "./lemma-agent-thread.js";

export { LemmaAgentTaskElement } from "./lemma-agent-task.js";
export { LemmaAgentThreadElement } from "./lemma-agent-thread.js";

const REGISTRY: Array<[string, CustomElementConstructor]> = [
  ["lemma-agent-task", LemmaAgentTaskElement],
  ["lemma-agent-thread", LemmaAgentThreadElement],
];

/** Register the Lemma custom elements. Idempotent and SSR/Node-safe (no-ops when
 * `customElements` is unavailable). The lemma-ui browser bundle calls this on
 * load; Vite apps can import and call it themselves. */
export function defineLemmaElements(registry?: CustomElementRegistry): void {
  const target = registry ?? (typeof customElements !== "undefined" ? customElements : undefined);
  if (!target) return;
  for (const [name, ctor] of REGISTRY) {
    if (!target.get(name)) target.define(name, ctor);
  }
}
