import type { GeneratedClientAdapter } from "../generated.js";
import type { PodMemberAddRequest } from "../openapi_client/models/PodMemberAddRequest.js";
import type { PodRole } from "../openapi_client/models/PodRole.js";
import { PodMembersService } from "../openapi_client/services/PodMembersService.js";

export class PodMembersNamespace {
  constructor(private readonly client: GeneratedClientAdapter) {}

  list(
    podId: string,
    options: { limit?: number; pageToken?: string; cursor?: string } = {},
  ) {
    return this.client.request(() =>
      PodMembersService.podMemberList(podId, options.limit ?? 100, options.pageToken ?? options.cursor),
    );
  }

  add(podId: string, payload: PodMemberAddRequest) {
    return this.client.request(() => PodMembersService.podMemberAdd(podId, payload));
  }

  get(podId: string, podMemberId: string) {
    return this.client.request(() => PodMembersService.podMemberGet(podId, podMemberId));
  }

  lookupByEmail(podId: string, email: string) {
    return this.client.request(() => PodMembersService.podMemberLookupByEmail(podId, email));
  }

  lookupByUserId(podId: string, userId: string) {
    return this.client.request(() => PodMembersService.podMemberLookupByUserId(podId, userId));
  }

  updateRole(podId: string, podMemberId: string, role: PodRole) {
    return this.client.request(() =>
      PodMembersService.podMemberUpdateRoles(podId, podMemberId, { roles: [role] }),
    );
  }

  updateRoles(podId: string, podMemberId: string, roles: string[]) {
    return this.client.request(() =>
      PodMembersService.podMemberUpdateRoles(podId, podMemberId, { roles }),
    );
  }

  remove(podId: string, podMemberId: string) {
    return this.client.request(() => PodMembersService.podMemberRemove(podId, podMemberId));
  }
}
