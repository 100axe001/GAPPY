import type { GeneratedClientAdapter } from "../generated.js";
import type { PodJoinRequestApproveRequest } from "../openapi_client/models/PodJoinRequestApproveRequest.js";
import type { PodJoinRequestStatus } from "../openapi_client/models/PodJoinRequestStatus.js";
import { OrganizationRole } from "../openapi_client/models/OrganizationRole.js";
import { PodRole } from "../openapi_client/models/PodRole.js";
import { PodJoinRequestsService } from "../openapi_client/services/PodJoinRequestsService.js";

export class PodJoinRequestsNamespace {
  constructor(private readonly client: GeneratedClientAdapter) {}

  create(podId: string) {
    return this.client.request(() => PodJoinRequestsService.podJoinRequestCreate(podId));
  }

  me(podId: string) {
    return this.client.request(() => PodJoinRequestsService.podJoinRequestMe(podId));
  }

  list(
    podId: string,
    options: {
      status?: PodJoinRequestStatus;
      limit?: number;
      pageToken?: string;
      cursor?: string;
    } = {},
  ) {
    return this.client.request(() =>
      PodJoinRequestsService.podJoinRequestList(
        podId,
        options.status,
        options.limit ?? 100,
        options.pageToken ?? options.cursor,
      ),
    );
  }

  approve(
    podId: string,
    joinRequestId: string,
    payload: PodJoinRequestApproveRequest = {},
  ) {
    return this.client.request(() =>
      PodJoinRequestsService.podJoinRequestApprove(podId, joinRequestId, {
        org_role: payload.org_role ?? OrganizationRole.ORG_MEMBER,
        pod_role: payload.pod_role ?? PodRole.POD_USER,
      }),
    );
  }
}
