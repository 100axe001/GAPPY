import type { GeneratedClientAdapter } from "../generated.js";
import { AgentsService } from "../openapi_client/services/AgentsService.js";
import type { CreateAgentRequest } from "../openapi_client/models/CreateAgentRequest.js";
import type { AgentPermissionsReplaceRequest } from "../openapi_client/models/AgentPermissionsReplaceRequest.js";
import type { UpdateAgentRequest } from "../openapi_client/models/UpdateAgentRequest.js";
import type { ConversationsNamespace } from "./conversations.js";

export interface RunAgentOptions {
  title?: string;
  metadata?: Record<string, unknown>;
  /** Stream tokens instead of awaiting the full reply. */
  stream?: boolean;
  signal?: AbortSignal;
}

export class AgentsNamespace {
  constructor(
    private readonly client: GeneratedClientAdapter,
    private readonly podId: () => string,
    // Lazy accessor — conversations is constructed alongside agents on the client.
    private readonly conversations?: () => ConversationsNamespace,
  ) {}

  list(options: { limit?: number; pageToken?: string } = {}) {
    return this.client.request(() => AgentsService.agentList(this.podId(), options.pageToken, options.limit ?? 100));
  }

  /**
   * Run an agent on a single message (the `.run` verb, alongside
   * `functions.run` / `datastore.query`). Note the return contract differs:
   * those return the result directly, whereas an agent reply is asynchronous —
   * this opens a fresh conversation, sends `message`, and returns the created
   * conversation (read the reply via `client.conversations.messages.list(conv.id)`).
   * With `stream: true` it returns the SSE stream so you can consume tokens as
   * they arrive.
   */
  async run(agentName: string, message: string, options: RunAgentOptions = {}) {
    if (!this.conversations) {
      throw new Error(
        "agents.run requires the conversations namespace — call it via client.agents.run().",
      );
    }
    const conversations = this.conversations();
    const conversation = await conversations.createForAgent(agentName, {
      title: options.title,
      metadata: options.metadata,
    });
    if (options.stream) {
      return conversations.sendMessageStream(
        conversation.id,
        { content: message },
        { signal: options.signal },
      );
    }
    await conversations.messages.send(conversation.id, { content: message });
    return conversation;
  }
  create(payload: CreateAgentRequest) {
    return this.client.request(() => AgentsService.agentCreate(this.podId(), payload));
  }
  get(agentName: string) {
    return this.client.request(() => AgentsService.agentGet(this.podId(), agentName));
  }
  update(agentName: string, payload: UpdateAgentRequest) {
    return this.client.request(() => AgentsService.agentUpdate(this.podId(), agentName, payload));
  }
  delete(agentName: string) {
    return this.client.request(() => AgentsService.agentDelete(this.podId(), agentName));
  }

  readonly permissions = {
    get: (agentName: string) =>
      this.client.request(() => AgentsService.agentPermissionsGet(this.podId(), agentName)),

    replace: (agentName: string, payload: AgentPermissionsReplaceRequest) =>
      this.client.request(() => AgentsService.agentPermissionsReplace(this.podId(), agentName, payload)),
  };
}
