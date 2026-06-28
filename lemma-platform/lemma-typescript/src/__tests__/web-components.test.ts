// @vitest-environment jsdom
import { beforeAll, describe, expect, it } from "vitest";
import { defineLemmaElements } from "../ui/index.js";

describe("lemma web components", () => {
  beforeAll(() => {
    (window as unknown as { __LEMMA_CONFIG__: unknown }).__LEMMA_CONFIG__ = {
      podId: "pod-1",
      apiUrl: "http://localhost:8710",
      authUrl: "http://localhost:8710",
    };
    defineLemmaElements();
  });

  it("registers the custom elements", () => {
    expect(customElements.get("lemma-agent-task")).toBeTruthy();
    expect(customElements.get("lemma-agent-thread")).toBeTruthy();
  });

  it("defineLemmaElements is idempotent", () => {
    expect(() => defineLemmaElements()).not.toThrow();
  });

  it("renders an idle agent-task with a themeable run button (no network)", () => {
    const el = document.createElement("lemma-agent-task");
    el.setAttribute("agent", "classify");
    document.body.appendChild(el);

    const root = el.shadowRoot;
    expect(root).toBeTruthy();
    expect(root?.querySelector('[part="root"]')).toBeTruthy();
    const runButton = root?.querySelector('[part="run-button"]');
    expect(runButton?.textContent).toContain("Run");
  });

  it("renders an agent-thread composer", () => {
    const el = document.createElement("lemma-agent-thread");
    el.setAttribute("agent", "support");
    document.body.appendChild(el);

    const root = el.shadowRoot;
    expect(root?.querySelector('[part="composer"]')).toBeTruthy();
    expect(root?.querySelector('[part="input"]')).toBeTruthy();
    expect(root?.querySelector('[part="messages"]')).toBeTruthy();
  });
});
