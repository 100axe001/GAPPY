import type { GeneratedClientAdapter } from "../generated.js";
import type { DatastoreQueryRequest } from "../openapi_client/models/DatastoreQueryRequest.js";
import type { DatastoreQueryResponse } from "../openapi_client/models/DatastoreQueryResponse.js";
import { QueryService } from "../openapi_client/services/QueryService.js";
import {
  watchDatastoreChanges,
  type ChangeStreamHandle,
  type ChangeStreamTokenProvider,
  type WatchChangesOptions,
} from "../datastore-changes.js";

export class DatastoreNamespace {
  constructor(
    private readonly client: GeneratedClientAdapter,
    private readonly podId: () => string,
    private readonly apiUrl: string,
    private readonly auth: ChangeStreamTokenProvider,
  ) {}

  query(request: string | DatastoreQueryRequest): Promise<DatastoreQueryResponse> {
    const payload = typeof request === "string" ? { query: request } : request;
    return this.client.request(() => QueryService.queryExecute(this.podId(), payload));
  }

  /**
   * Stream live record changes (insert/update/delete) over a WebSocket.
   *
   * Returns a handle; call `handle.close()` (or abort `options.signal`) to stop.
   * RLS tables deliver only the caller's own rows; shared tables deliver all
   * members' changes. Reconnects automatically and resumes from the last change.
   */
  watchChanges(options: WatchChangesOptions): ChangeStreamHandle {
    return watchDatastoreChanges(this.apiUrl, this.auth, this.podId(), options);
  }
}
