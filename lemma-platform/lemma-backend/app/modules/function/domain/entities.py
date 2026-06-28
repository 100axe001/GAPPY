"""Function domain entities."""

from datetime import datetime
from enum import Enum
from typing import ClassVar
from uuid import UUID

from pydantic import BaseModel, Field, PrivateAttr

from app.core.authorization.context import ResourceType
from app.core.domain.events import DomainEvent


class FunctionStatus(str, Enum):
    """Status of a function."""

    DRAFT = "DRAFT"
    CODE_GENERATION = "CODE_GENERATION"
    READY = "READY"
    ERROR = "ERROR"


class FunctionRunStatus(str, Enum):
    """Status of a function run."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class FunctionType(str, Enum):
    """Execution mode for a function."""

    API = "API"
    JOB = "JOB"


class FunctionEntity(BaseModel):
    """Function entity representing a programmatic task."""

    resource_type: ClassVar[ResourceType] = ResourceType.FUNCTION

    id: UUID | None = None
    pod_id: UUID
    user_id: UUID
    name: str
    description: str | None = None
    icon_url: str | None = None
    input_schema: dict = Field(default_factory=dict)
    output_schema: dict = Field(default_factory=dict)
    config_schema: dict | None = None
    code_path: str | None = None
    code_hash: str | None = None
    code: str | None = None
    config: dict | None = None
    type: FunctionType = FunctionType.API
    status: FunctionStatus = FunctionStatus.DRAFT
    visibility: str = "POD"
    # pip dependencies declared in the code's `#python_packages:` header; the
    # agentbox function executor installs these before running the function.
    python_packages: list[str] = Field(default_factory=list)
    allowed_actions: list[str] = Field(default_factory=list)
    # Timestamps
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}


class FunctionUpdateEntity(BaseModel):
    """Entity for updating function fields."""

    description: str | None = None
    icon_url: str | None = None
    code: str | None = None
    config: dict | None = None
    type: FunctionType | None = None
    visibility: str | None = None
    model_config = {"from_attributes": True}



class RunAsWorkload(BaseModel):
    """Identifies the calling workload so its cached token is reused for execution."""

    workload_type: str
    workload_id: UUID
    workload_name: str | None = None


class FunctionRunEntity(BaseModel):
    """Function run entity representing an execution."""

    _domain_events: list[DomainEvent] = PrivateAttr(default_factory=list)

    id: UUID | None = None
    function_id: UUID
    user_id: UUID
    input_data: dict | None = None
    output_data: dict | None = None
    status: FunctionRunStatus = FunctionRunStatus.PENDING
    user_email: str | None = None
    job_id: str | None = None
    workspace_session_id: str | None = None
    workspace_process_id: str | None = None
    error: str | None = None
    logs: str | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}

    def add_event(self, event: DomainEvent) -> None:
        self._domain_events.append(event)

    def collect_events(self) -> list[DomainEvent]:
        events = self._domain_events.copy()
        self._domain_events.clear()
        return events
