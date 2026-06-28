import type { GeneratedClientAdapter } from "../generated.js";
import type { HttpClient } from "../http.js";
import type { CreateAppRequest } from "../openapi_client/models/CreateAppRequest.js";
import type { AppBundleUploadRequest } from "../openapi_client/models/AppBundleUploadRequest.js";
import type { UpdateAppRequest } from "../openapi_client/models/UpdateAppRequest.js";
import { AppsService } from "../openapi_client/services/AppsService.js";

export class AppsNamespace {
  constructor(
    private readonly client: GeneratedClientAdapter,
    private readonly http: HttpClient,
    private readonly podId: () => string,
  ) {}

  list(options: { limit?: number; pageToken?: string } = {}) {
    return this.client.request(() => AppsService.appList(this.podId(), options.limit ?? 100, options.pageToken));
  }
  create(payload: CreateAppRequest) {
    return this.client.request(() => AppsService.appCreate(this.podId(), payload));
  }
  get(name: string) {
    return this.client.request(() => AppsService.appGet(this.podId(), name));
  }
  update(name: string, payload: UpdateAppRequest) {
    return this.client.request(() => AppsService.appUpdate(this.podId(), name, payload));
  }
  delete(name: string) {
    return this.client.request(() => AppsService.appDelete(this.podId(), name));
  }

  /** Promote a conversation widget into a persisted app (save as app). */
  createFromWidget(payload: {
    conversation_id: string;
    tool_call_id: string;
    name: string;
    public_slug?: string;
    description?: string;
    visibility?: string;
  }): Promise<unknown> {
    return this.http.request("POST", `/pods/${this.podId()}/apps/from-widget`, {
      body: payload,
    });
  }

  readonly assets = {
    get: (name: string, path?: string): Promise<string> =>
      this.http.request("GET", `/pods/${this.podId()}/apps/${name}/assets${path ? `/${path.replace(/^\/+/, "")}` : ""}`),
  };

  readonly bundle = {
    upload: (name: string, payload: AppBundleUploadRequest) =>
      this.client.request(() => AppsService.appBundleUpload(this.podId(), name, payload)),
  };

  readonly source = {
    download: (name: string): Promise<Blob> =>
      this.http.requestBytes("GET", `/pods/${this.podId()}/apps/${name}/source/archive`),
  };

  readonly dist = {
    download: (name: string): Promise<Blob> =>
      this.http.requestBytes("GET", `/pods/${this.podId()}/apps/${name}/dist/archive`),
  };
}
