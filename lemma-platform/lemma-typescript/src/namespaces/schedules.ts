import type { GeneratedClientAdapter } from "../generated.js";
import type { CreateScheduleRequest } from "../openapi_client/models/CreateScheduleRequest.js";
import type { ScheduleType } from "../openapi_client/models/ScheduleType.js";
import type { UpdateScheduleRequest } from "../openapi_client/models/UpdateScheduleRequest.js";
import { SchedulesService } from "../openapi_client/services/SchedulesService.js";

export interface ScheduleListOptions {
  scheduleType?: ScheduleType | null;
  isActive?: boolean | null;
  agentName?: string | null;
  workflowName?: string | null;
  name?: string | null;
  limit?: number;
  pageToken?: string | null;
}

export class SchedulesNamespace {
  constructor(
    private readonly client: GeneratedClientAdapter,
    private readonly podId: () => string,
  ) {}

  list(options: ScheduleListOptions = {}) {
    return this.client.request(() =>
      SchedulesService.scheduleList(
        this.podId(),
        options.scheduleType,
        options.isActive,
        options.agentName,
        options.workflowName,
        options.name,
        options.limit ?? 100,
        options.pageToken,
      ),
    );
  }

  create(payload: CreateScheduleRequest) {
    return this.client.request(() => SchedulesService.scheduleCreate(this.podId(), payload));
  }

  get(scheduleId: string) {
    return this.client.request(() => SchedulesService.scheduleGet(this.podId(), scheduleId));
  }

  update(scheduleId: string, payload: UpdateScheduleRequest) {
    return this.client.request(() => SchedulesService.scheduleUpdate(this.podId(), scheduleId, payload));
  }

  delete(scheduleId: string) {
    return this.client.request(() => SchedulesService.scheduleDelete(this.podId(), scheduleId));
  }
}
