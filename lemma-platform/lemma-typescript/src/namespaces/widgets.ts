import type { HttpClient } from "../http.js";

export class WidgetsNamespace {
  constructor(
    private readonly http: HttpClient,
    private readonly podId: () => string,
  ) {}

  /**
   * Mint a short-lived, signed embed URL for a conversation widget. The widget
   * serve route is authenticated; this returns a URL the iframe can load even
   * when the session cookie is not sent in a cross-site/embedded context.
   */
  embedUrl(payload: {
    conversation_id: string;
    tool_call_id: string;
  }): Promise<{ url: string }> {
    return this.http.request(
      "POST",
      `/pods/${this.podId()}/widgets/${payload.conversation_id}/${payload.tool_call_id}/embed-token`,
    ) as Promise<{ url: string }>;
  }
}
