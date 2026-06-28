import type { LemmaClient } from "../client.js";

type LemmaClientCtor = new (overrides?: { podId?: string }) => LemmaClient;

// Resolve the client from the already-loaded base bundle (window.LemmaClient)
// rather than importing the implementation — so lemma-ui.js stays lean and does
// NOT re-bundle the client + supertokens. A no-build app loads lemma-client.js
// first (it injects window.__LEMMA_CONFIG__), then this opt-in UI bundle.
function clientConstructor(): LemmaClientCtor {
  const globalLemma = (globalThis as { LemmaClient?: { LemmaClient?: LemmaClientCtor } }).LemmaClient;
  const ctor = globalLemma?.LemmaClient;
  if (!ctor) {
    throw new Error(
      "window.LemmaClient is unavailable — load /public/sdk/lemma-client.js before lemma-ui.js.",
    );
  }
  return ctor;
}

/**
 * Build a pod-scoped client for a web component. The host injects
 * `window.__LEMMA_CONFIG__` (podId/apiUrl/authUrl), so no args are needed; a
 * `pod` attribute overrides the pod id.
 */
export function resolveUiClient(podId?: string | null): LemmaClient {
  const Ctor = clientConstructor();
  return podId ? new Ctor({ podId }) : new Ctor();
}
