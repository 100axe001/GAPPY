from datetime import datetime
from typing import Annotated, Any, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.core.authorization.context import ResourceVisibility
from app.modules.workflow.domain.flow import (
    FlowEntity,
    WorkflowMode,
)
from app.modules.workflow.domain.graph import WorkflowEdge
from app.modules.workflow.domain.run import (
    FlowRunEntity,
    FlowRunStatus,
    StepStatus,
)
from app.modules.workflow.domain.wait import (
    WorkflowRunWaitEntity,
    WorkflowRunWaitStatus,
    WorkflowRunWaitType,
)
from app.modules.workflow.domain.start import (
    DataStoreFlowStart,
    EventFlowStart,
    FlowStart,
    FlowStartType,
    ScheduledFlowStart,
)
from app.modules.workflow.domain.nodes import (
    AgentNode,
    DecisionNode,
    EndNode,
    FormNode,
    FunctionNode,
    LoopNode,
    WaitUntilNode,
    WorkflowNode,
)


class ScheduledFlowStartInput(ScheduledFlowStart):
    model_config = ConfigDict(title="ScheduledFlowStartInput")


class EventFlowStartInput(EventFlowStart):
    model_config = ConfigDict(title="EventFlowStartInput")


class DataStoreFlowStartInput(DataStoreFlowStart):
    model_config = ConfigDict(title="DataStoreFlowStartInput")


class ManualWorkflowStartInput(BaseModel):
    type: Literal[FlowStartType.MANUAL] = Field(
        default=FlowStartType.MANUAL,
        description="Manual workflow start with no configuration payload.",
    )
    config: None = Field(
        default=None,
        description="Always `null` for manual workflow starts.",
    )

    model_config = ConfigDict(title="ManualWorkflowStartInput")


class ScheduledWorkflowStartInput(BaseModel):
    type: Literal[FlowStartType.SCHEDULED] = Field(
        default=FlowStartType.SCHEDULED,
        description="Scheduled workflow start.",
    )
    config: ScheduledFlowStartInput = Field(
        ...,
        description="Scheduled workflow definition payload.",
    )

    model_config = ConfigDict(title="ScheduledWorkflowStartInput")


class EventWorkflowStartInput(BaseModel):
    type: Literal[FlowStartType.EVENT] = Field(
        default=FlowStartType.EVENT,
        description="Event-triggered workflow start.",
    )
    config: EventFlowStartInput = Field(
        ...,
        description="Connector trigger configuration for this workflow.",
    )

    model_config = ConfigDict(title="EventWorkflowStartInput")


class DataStoreWorkflowStartInput(BaseModel):
    type: Literal[FlowStartType.DATASTORE_EVENT] = Field(
        default=FlowStartType.DATASTORE_EVENT,
        description="Datastore-event workflow start.",
    )
    config: DataStoreFlowStartInput = Field(
        ...,
        description="Datastore trigger configuration for this workflow.",
    )

    model_config = ConfigDict(title="DataStoreWorkflowStartInput")


WorkflowStartInput = Annotated[
    (
        ManualWorkflowStartInput
        | ScheduledWorkflowStartInput
        | EventWorkflowStartInput
        | DataStoreWorkflowStartInput
    ),
    Field(discriminator="type"),
]


class ScheduledFlowStartOutput(ScheduledFlowStart):
    model_config = ConfigDict(from_attributes=True, title="ScheduledFlowStartOutput")


class EventFlowStartOutput(EventFlowStart):
    model_config = ConfigDict(from_attributes=True, title="EventFlowStartOutput")


class DataStoreFlowStartOutput(DataStoreFlowStart):
    model_config = ConfigDict(from_attributes=True, title="DataStoreFlowStartOutput")


class ManualWorkflowStartOutput(BaseModel):
    type: Literal[FlowStartType.MANUAL] = Field(
        default=FlowStartType.MANUAL,
        description="Manual workflow start with no configuration payload.",
    )
    config: None = Field(
        default=None,
        description="Always `null` for manual workflow starts.",
    )

    model_config = ConfigDict(from_attributes=True, title="ManualWorkflowStartOutput")


class ScheduledWorkflowStartOutput(BaseModel):
    type: Literal[FlowStartType.SCHEDULED] = Field(
        default=FlowStartType.SCHEDULED,
        description="Scheduled workflow start.",
    )
    config: ScheduledFlowStartOutput = Field(
        ...,
        description="Scheduled workflow definition payload.",
    )

    model_config = ConfigDict(
        from_attributes=True,
        title="ScheduledWorkflowStartOutput",
    )


class EventWorkflowStartOutput(BaseModel):
    type: Literal[FlowStartType.EVENT] = Field(
        default=FlowStartType.EVENT,
        description="Event-triggered workflow start.",
    )
    config: EventFlowStartOutput = Field(
        ...,
        description="Connector trigger configuration for this workflow.",
    )

    model_config = ConfigDict(
        from_attributes=True,
        title="EventWorkflowStartOutput",
    )


class DataStoreWorkflowStartOutput(BaseModel):
    type: Literal[FlowStartType.DATASTORE_EVENT] = Field(
        default=FlowStartType.DATASTORE_EVENT,
        description="Datastore-event workflow start.",
    )
    config: DataStoreFlowStartOutput = Field(
        ...,
        description="Datastore trigger configuration for this workflow.",
    )

    model_config = ConfigDict(
        from_attributes=True,
        title="DataStoreWorkflowStartOutput",
    )


WorkflowStartOutput = Annotated[
    (
        ManualWorkflowStartOutput
        | ScheduledWorkflowStartOutput
        | EventWorkflowStartOutput
        | DataStoreWorkflowStartOutput
    ),
    Field(discriminator="type"),
]


def workflow_start_input_to_domain(
    start: WorkflowStartInput | None,
) -> FlowStart | None:
    if start is None:
        return None

    if isinstance(start, ManualWorkflowStartInput):
        return FlowStart(type=FlowStartType.MANUAL, config=None)

    if isinstance(start, ScheduledWorkflowStartInput):
        return FlowStart(
            type=FlowStartType.SCHEDULED,
            config=ScheduledFlowStart.model_validate(start.config.model_dump()),
        )

    if isinstance(start, EventWorkflowStartInput):
        return FlowStart(
            type=FlowStartType.EVENT,
            config=EventFlowStart.model_validate(start.config.model_dump()),
        )

    return FlowStart(
        type=FlowStartType.DATASTORE_EVENT,
        config=DataStoreFlowStart.model_validate(start.config.model_dump()),
    )


def workflow_start_output_from_domain(
    start: FlowStart | None,
) -> WorkflowStartOutput | None:
    if start is None:
        return None

    if start.type == FlowStartType.MANUAL:
        return ManualWorkflowStartOutput()

    if start.type == FlowStartType.SCHEDULED:
        return ScheduledWorkflowStartOutput(
            config=ScheduledFlowStartOutput.model_validate(start.config),
        )

    if start.type == FlowStartType.EVENT:
        return EventWorkflowStartOutput(
            config=EventFlowStartOutput.model_validate(start.config),
        )

    return DataStoreWorkflowStartOutput(
        config=DataStoreFlowStartOutput.model_validate(start.config),
    )


class WorkflowCreateRequest(BaseModel):
    name: str = Field(..., description="Workflow name.")
    description: str | None = Field(
        default=None,
        description="Optional workflow description.",
    )
    icon_url: str | None = Field(
        default=None,
        description="Optional public icon URL for the workflow.",
    )
    start: WorkflowStartInput | None = Field(
        default=None,
        description=(
            "Start configuration. If omitted, the workflow can be started manually via `workflow.start`."
        ),
    )
    mode: WorkflowMode = Field(
        default=WorkflowMode.GLOBAL,
        description=(
            "Workflow schedule ownership mode. `GLOBAL` means one pod-level workflow "
            "schedule is allowed; `USER` is reserved for per-user schedule ownership."
        ),
    )
    visibility: ResourceVisibility = ResourceVisibility.POD
    nodes: list[WorkflowNode] = Field(
        default_factory=list,
        description=(
            "Optional initial graph nodes. When provided, the graph is stored at "
            "creation time so a separate `workflow.graph.update` call is not "
            "required. Omit (or pass an empty list) to create a shell and upload "
            "the graph later. Node `input_mapping` entries must use explicit typed "
            'bindings like `{"type": "expression", "value": "start.payload.x"}`.'
        ),
    )
    edges: list[WorkflowEdge] = Field(
        default_factory=list,
        description="Optional initial graph edges connecting the provided nodes.",
    )


class WorkflowUpdateRequest(BaseModel):
    description: str | None = Field(
        default=None,
        description="Updated workflow description.",
    )
    icon_url: str | None = Field(
        default=None,
        description="Updated public icon URL for the workflow.",
    )
    mode: WorkflowMode | None = Field(
        default=None,
        description="Updated workflow schedule ownership mode.",
    )
    start: WorkflowStartInput | None = Field(
        default=None,
        description="Updated start trigger configuration.",
    )
    visibility: ResourceVisibility | None = None


class WorkflowGraphUpdateRequest(BaseModel):
    """Named request body for replacing a workflow graph."""

    nodes: list[WorkflowNode] = Field(
        ...,
        description=(
            "Complete node list for the workflow graph. Agent/function `input_mapping` "
            "entries must use explicit typed bindings like "
            '`{"type": "expression", "value": "start.payload.issue.key"}` or '
            '`{"type": "literal", "value": "finance"}`.'
        ),
    )
    edges: list[WorkflowEdge] = Field(
        ...,
        description="Complete edge list connecting the provided nodes.",
    )
    start: WorkflowStartInput | None = Field(
        default=None,
        description="Optional replacement start configuration stored with the graph.",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "nodes": [
                    {
                        "id": "collect_context",
                        "type": "FUNCTION",
                        "config": {
                            "function_name": "summarize-ticket",
                            "input_mapping": {
                                "ticket_key": {
                                    "type": "expression",
                                    "value": "start.payload.ticket.key",
                                },
                                "channel": {"type": "literal", "value": "support"},
                            },
                        },
                    }
                ],
                "edges": [],
                "start": {
                    "type": "DATASTORE_EVENT",
                    "config": {
                        "table_name": "expenses",
                        "operations": ["INSERT", "UPDATE", "DELETE"],
                    },
                },
            }
        }
    }


class FormNodeResponse(FormNode):
    model_config = ConfigDict(from_attributes=True, title="FormNodeResponse")


class AgentNodeResponse(AgentNode):
    model_config = ConfigDict(from_attributes=True, title="AgentNodeResponse")


class FunctionNodeResponse(FunctionNode):
    model_config = ConfigDict(from_attributes=True, title="FunctionNodeResponse")


class DecisionNodeResponse(DecisionNode):
    model_config = ConfigDict(from_attributes=True, title="DecisionNodeResponse")


class LoopNodeResponse(LoopNode):
    model_config = ConfigDict(from_attributes=True, title="LoopNodeResponse")


class WaitUntilNodeResponse(WaitUntilNode):
    model_config = ConfigDict(from_attributes=True, title="WaitUntilNodeResponse")


class EndNodeResponse(EndNode):
    model_config = ConfigDict(from_attributes=True, title="EndNodeResponse")


WorkflowNodeResponse = Annotated[
    (
        FormNodeResponse
        | AgentNodeResponse
        | FunctionNodeResponse
        | DecisionNodeResponse
        | LoopNodeResponse
        | WaitUntilNodeResponse
        | EndNodeResponse
    ),
    Field(discriminator="type"),
]


class FlowResponse(BaseModel):
    id: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None
    name: str
    description: str | None = None
    icon_url: str | None = None
    pod_id: UUID
    nodes: list[WorkflowNodeResponse] = Field(default_factory=list)
    edges: list[WorkflowEdge] = Field(default_factory=list)
    start: WorkflowStartOutput | None = None
    is_active: bool = True
    mode: WorkflowMode = WorkflowMode.GLOBAL
    visibility: str = "POD"

    model_config = ConfigDict(from_attributes=True, title="FlowResponse")


class FlowDetailResponse(FlowResponse):
    allowed_actions: list[str] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True, title="FlowDetailResponse")


class FlowSummaryResponse(BaseModel):
    """Lean workflow shape for list responses.

    Omits the full graph (`nodes`/`edges`/`start`) — fetch those from
    `workflow.get`. Carries cheap derived `node_count`/`node_types` so list
    views can show step counts and participant badges without the graph.
    """

    id: UUID
    created_at: datetime | None = None
    updated_at: datetime | None = None
    name: str
    description: str | None = None
    icon_url: str | None = None
    pod_id: UUID
    is_active: bool = True
    mode: WorkflowMode = WorkflowMode.GLOBAL
    visibility: str = "POD"
    node_count: int = 0
    node_types: list[str] = Field(default_factory=list)
    allowed_actions: list[str] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True, title="FlowSummaryResponse")


class WorkflowListResponse(BaseModel):
    items: list[FlowSummaryResponse]
    limit: int
    next_page_token: str | None = None

    model_config = ConfigDict(from_attributes=True)


class WorkflowRunSummaryResponse(BaseModel):
    id: UUID
    flow_id: UUID
    pod_id: UUID
    user_id: UUID
    start_type: str = "MANUAL"
    schedule_event_id: str | None = None
    status: FlowRunStatus = FlowRunStatus.PENDING
    current_node_id: str | None = None
    error: str | None = None
    failed_node_id: str | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class StepRecordResponse(BaseModel):
    step_index: int
    node_id: str
    status: StepStatus
    started_at: datetime
    completed_at: datetime | None = None
    output_data: Any | None = None
    error: str | None = None

    model_config = ConfigDict(from_attributes=True)


class WorkflowRunWaitResponse(BaseModel):
    id: UUID
    run_id: UUID
    flow_id: UUID
    pod_id: UUID
    node_id: str
    wait_type: WorkflowRunWaitType
    status: WorkflowRunWaitStatus
    assigned_pod_member_id: UUID | None = None
    external_ref: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime | None = None
    completed_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class WorkflowRunResponse(WorkflowRunSummaryResponse):
    """Full run state. `execution_context` is the same flat view that
    workflow expressions resolve against (`<node_id>.<field>`, `start.*`,
    `loop.*`). `active_wait` is set when the run is suspended, including
    WAITING form waits and RUNNING platform waits."""

    execution_context: dict[str, Any] = Field(default_factory=dict)
    step_history: list[StepRecordResponse] = Field(default_factory=list)
    active_wait: WorkflowRunWaitResponse | None = None


class WorkflowRunFormSubmitRequest(BaseModel):
    """Canonical form submission payload — identical across web, SDKs, CLI."""

    node_id: str = Field(
        ...,
        description=(
            "Id of the FORM node being submitted. Must match the run's active "
            "wait; mismatches return 422."
        ),
    )
    inputs: dict[str, Any] = Field(
        default_factory=dict,
        description="Form field values keyed by field name.",
    )

    model_config = ConfigDict(extra="forbid")


class WorkflowRunListResponse(BaseModel):
    items: list[WorkflowRunSummaryResponse]
    limit: int
    next_page_token: str | None = None


class WorkflowRunWaitAssignment(BaseModel):
    wait: WorkflowRunWaitResponse
    run: WorkflowRunSummaryResponse


class WorkflowRunWaitAssignmentListResponse(BaseModel):
    items: list[WorkflowRunWaitAssignment]
    limit: int
    next_page_token: str | None = None


def flow_response_from_domain(workflow: FlowEntity) -> FlowResponse:
    payload = workflow.model_dump(mode="python")
    payload["start"] = workflow_start_output_from_domain(workflow.start)
    return FlowResponse.model_validate(payload)


def run_response_from_domain(
    run: FlowRunEntity,
    active_wait: WorkflowRunWaitEntity | None = None,
) -> WorkflowRunResponse:
    return WorkflowRunResponse(
        id=run.id,
        flow_id=run.flow_id,
        pod_id=run.pod_id,
        user_id=run.user_id,
        start_type=run.start_type,
        schedule_event_id=run.schedule_event_id,
        status=run.status,
        current_node_id=run.current_node_id,
        error=run.error,
        failed_node_id=run.failed_node_id,
        started_at=run.started_at,
        completed_at=run.completed_at,
        created_at=run.created_at,
        updated_at=run.updated_at,
        execution_context=run.execution_context.to_view(),
        step_history=[
            StepRecordResponse.model_validate(step) for step in run.step_history
        ],
        active_wait=(
            WorkflowRunWaitResponse.model_validate(active_wait)
            if active_wait is not None
            else None
        ),
    )
