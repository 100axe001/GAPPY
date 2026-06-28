import type { GeneratedClientAdapter } from "../generated.js";
import type { ResourceAccessGrantRequest } from "../openapi_client/models/ResourceAccessGrantRequest.js";
import type { ResourceType } from "../openapi_client/models/ResourceType.js";
import { PodResourceAccessService } from "../openapi_client/services/PodResourceAccessService.js";

export class ResourceAccessNamespace {
  constructor(private readonly client: GeneratedClientAdapter, private readonly podId: () => string) {}

  get(resourceType: ResourceType | string, resourceName: string, podId?: string) {
    return this.client.request(() =>
      PodResourceAccessService.podResourceAccessGet(podId ?? this.podId(), resourceType as ResourceType, resourceName),
    );
  }

  replaceGrant(
    resourceType: ResourceType | string,
    resourceName: string,
    granteeType: string,
    granteeId: string,
    payload: ResourceAccessGrantRequest,
    podId?: string,
  ) {
    return this.client.request(() =>
      PodResourceAccessService.podResourceAccessGrantReplace(
        podId ?? this.podId(),
        resourceType as ResourceType,
        resourceName,
        granteeType,
        granteeId,
        payload,
      ),
    );
  }

  deleteGrant(
    resourceType: ResourceType | string,
    resourceName: string,
    granteeType: string,
    granteeId: string,
    podId?: string,
  ) {
    return this.client.request(() =>
      PodResourceAccessService.podResourceAccessGrantDelete(
        podId ?? this.podId(),
        resourceType as ResourceType,
        resourceName,
        granteeType,
        granteeId,
      ),
    );
  }
}
