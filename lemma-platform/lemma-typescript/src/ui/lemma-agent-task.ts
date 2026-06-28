import { AgentController, selectAgentTask } from "../core/agent/index.js";
import { resolveUiClient } from "./client.js";
import { BASE_STYLES, HTMLElementBase, escapeHtml } from "./shared.js";

const STYLE = `
${BASE_STYLES}
.wrap {
  display: flex;
  flex-direction: column;
  gap: var(--lemma-gap);
  padding: 16px;
  background: var(--lemma-bg);
  border: 1px solid var(--lemma-border);
  border-radius: var(--lemma-radius);
}
.stream { white-space: pre-wrap; color: var(--lemma-muted); }
.output {
  margin: 0;
  padding: 12px;
  background: var(--lemma-surface);
  border-radius: calc(var(--lemma-radius) - 4px);
  white-space: pre-wrap;
  overflow-x: auto;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 13px;
}
.output.text { font-family: var(--lemma-font); font-size: 14px; }
.error { color: #b91c1c; }
.hint { color: var(--lemma-muted); }
.row { display: flex; justify-content: flex-end; }
`;

/**
 * `<lemma-agent-task agent="classify" input='...' auto-run>` — the inline
 * working→output preset as a no-build custom element. Drives an AgentController,
 * renders the activity then the (schema-parsed) output, and emits a
 * `lemma-output` event when the run settles. Theme via CSS vars + ::part.
 */
export class LemmaAgentTaskElement extends HTMLElementBase {
  static get observedAttributes(): string[] {
    return ["agent", "pod", "input", "auto-run", "parse-output"];
  }

  private controller: AgentController | null = null;
  private unsubscribe: (() => void) | null = null;
  private dispatchedFor = "";
  private readonly view: ShadowRoot;

  constructor() {
    super();
    this.view = this.attachShadow({ mode: "open" });
  }

  connectedCallback(): void {
    this.render();
    if (this.hasAttribute("auto-run")) void this.run();
  }

  disconnectedCallback(): void {
    this.teardown();
  }

  attributeChangedCallback(name: string): void {
    if (name === "agent" || name === "pod") {
      this.teardown();
    }
    if (this.isConnected) this.render();
  }

  /** Start a fresh run. Without an argument it uses the `input` attribute. */
  async run(input?: string): Promise<void> {
    const controller = this.ensureController();
    this.dispatchedFor = "";
    await controller.createConversation({ setActive: true });
    await controller.sendMessage(input ?? this.getAttribute("input") ?? "");
  }

  private ensureController(): AgentController {
    if (!this.controller) {
      this.controller = new AgentController({
        client: resolveUiClient(this.getAttribute("pod")),
        scope: { agentName: this.getAttribute("agent") },
      });
      this.unsubscribe = this.controller.subscribe(() => this.render());
    }
    return this.controller;
  }

  private teardown(): void {
    this.unsubscribe?.();
    this.unsubscribe = null;
    this.controller?.destroy();
    this.controller = null;
  }

  private render(): void {
    const parseOutput = this.getAttribute("parse-output") !== "false";
    const view = this.controller
      ? selectAgentTask(this.controller.getState(), { parseOutput })
      : null;
    const status = view?.status ?? "idle";

    let body: string;
    if (status === "running") {
      const stream = view?.streamingText
        ? `<div part="stream" class="stream">${escapeHtml(view.streamingText)}</div>`
        : "";
      body = `<div part="activity" class="activity">${escapeHtml(view?.activity || "Working…")}</div>${stream}`;
    } else if (status === "done") {
      body = view?.output != null
        ? `<pre part="output" class="output">${escapeHtml(JSON.stringify(view.output, null, 2))}</pre>`
        : `<div part="output" class="output text">${escapeHtml(view?.outputText || "")}</div>`;
    } else if (status === "error") {
      body = `<div part="error" class="error">${escapeHtml(view?.error?.message || "Something went wrong.")}</div>`;
    } else {
      body = `<div part="hint" class="hint">Ready to run.</div>`;
    }

    const showRun = !this.hasAttribute("auto-run") && status !== "running";
    const runRow = showRun
      ? `<div class="row"><button part="run-button" data-run type="button">${status === "idle" ? "Run" : "Run again"}</button></div>`
      : "";

    this.view.innerHTML = `<style>${STYLE}</style><div part="root" class="wrap">${body}${runRow}</div>`;
    this.view.querySelector("[data-run]")?.addEventListener("click", () => void this.run());

    if (status === "done" && this.controller) {
      const key = this.controller.getState().conversationId ?? "";
      if (key && this.dispatchedFor !== key) {
        this.dispatchedFor = key;
        this.dispatchEvent(
          new CustomEvent("lemma-output", {
            detail: { output: view?.output ?? null, text: view?.outputText ?? "" },
            bubbles: true,
          }),
        );
      }
    }
  }
}
