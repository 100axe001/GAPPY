import type { GeneratedClientAdapter } from "../generated.js";
import type { HttpClient } from "../http.js";
import { PodPermissionsService } from "../openapi_client/services/PodPermissionsService.js";

export interface PodEffectivePermissionsResponse {
  pod_id: string;
  actions: string[];
}

export class PodPermissionsNamespace {
  constructor(
    private readonly client: GeneratedClientAdapter,
    private readonly http: HttpClient,
    private readonly podId: () => string,
  ) {}

  catalog(podId?: string) {
    return this.client.request(() => PodPermissionsService.podPermissionsCatalog(podId ?? this.podId()));
  }

  me(podId?: string) {
    const targetPodId = encodeURIComponent(podId ?? this.podId());
    return this.http.request<PodEffectivePermissionsResponse>("GET", `/pods/${targetPodId}/permissions/me`);
  }
}
