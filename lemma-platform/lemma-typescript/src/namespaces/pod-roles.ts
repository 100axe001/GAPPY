import type { GeneratedClientAdapter } from "../generated.js";
import type { PodRoleCreateRequest } from "../openapi_client/models/PodRoleCreateRequest.js";
import type { PodRolePermissionsReplaceRequest } from "../openapi_client/models/PodRolePermissionsReplaceRequest.js";
import { PodRolesService } from "../openapi_client/services/PodRolesService.js";

export class PodRolesNamespace {
  constructor(private readonly client: GeneratedClientAdapter, private readonly podId: () => string) {}

  list(podId?: string) {
    return this.client.request(() => PodRolesService.podRolesList(podId ?? this.podId()));
  }

  create(payload: PodRoleCreateRequest, podId?: string) {
    return this.client.request(() => PodRolesService.podRolesCreate(podId ?? this.podId(), payload));
  }

  update(roleName: string, payload: PodRoleCreateRequest, podId?: string) {
    return this.client.request(() => PodRolesService.podRolesUpdate(podId ?? this.podId(), roleName, payload));
  }

  delete(roleName: string, podId?: string) {
    return this.client.request(() => PodRolesService.podRolesDelete(podId ?? this.podId(), roleName));
  }

  readonly permissions = {
    get: (roleName: string, podId?: string) =>
      this.client.request(() => PodRolesService.podRolePermissionsGet(podId ?? this.podId(), roleName)),

    replace: (roleName: string, payload: PodRolePermissionsReplaceRequest, podId?: string) =>
      this.client.request(() =>
        PodRolesService.podRolePermissionsReplace(podId ?? this.podId(), roleName, payload),
      ),
  };
}
