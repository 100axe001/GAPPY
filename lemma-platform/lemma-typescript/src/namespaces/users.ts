import type { GeneratedClientAdapter } from "../generated.js";
import type { UserProfileRequest } from "../openapi_client/models/UserProfileRequest.js";
import { UsersService } from "../openapi_client/services/UsersService.js";

export class UsersNamespace {
  constructor(private readonly client: GeneratedClientAdapter) {}

  current() {
    return this.client.request(() => UsersService.userCurrentGet());
  }

  getProfile() {
    return this.client.request(() => UsersService.userProfileGet());
  }

  upsertProfile(payload: UserProfileRequest) {
    return this.client.request(() => UsersService.userProfileUpsert(payload));
  }
}
