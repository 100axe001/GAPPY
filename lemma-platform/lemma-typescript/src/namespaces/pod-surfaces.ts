import type { GeneratedClientAdapter } from "../generated.js";
import type { SurfaceUpsertRequest } from "../openapi_client/models/SurfaceUpsertRequest.js";
import { AgentSurfacesService } from "../openapi_client/services/AgentSurfacesService.js";

/**
 * Agent surfaces, addressed by platform (a surface is unique per pod+platform).
 *
 * One `upsert` write covers create, config/channel edits, account and
 * credential changes, and enable/disable (via `is_enabled`). `delete` removes
 * the surface and frees its account for reuse. `setup` merges live readiness,
 * admin-consent, and the platform checklist into one read.
 */
export class PodSurfacesNamespace {
  constructor(private readonly client: GeneratedClientAdapter) {}

  list(
    podId: string,
    options: { limit?: number; pageToken?: string; cursor?: string } = {},
  ) {
    return this.client.request(() =>
      AgentSurfacesService.agentSurfaceList(
        podId,
        options.limit ?? 100,
        options.pageToken ?? options.cursor,
      ),
    );
  }

  upsert(podId: string, platform: string, payload: SurfaceUpsertRequest) {
    return this.client.request(() =>
      AgentSurfacesService.agentSurfaceUpsert(podId, platform, payload),
    );
  }

  get(podId: string, platform: string) {
    return this.client.request(() => AgentSurfacesService.agentSurfaceGet(podId, platform));
  }

  delete(podId: string, platform: string) {
    return this.client.request(() => AgentSurfacesService.agentSurfaceDelete(podId, platform));
  }

  setup(podId: string, platform: string) {
    return this.client.request(() => AgentSurfacesService.agentSurfaceSetup(podId, platform));
  }

  channels(podId: string, platform: string) {
    return this.client.request(() =>
      AgentSurfacesService.agentSurfaceChannels(podId, platform),
    );
  }
}
