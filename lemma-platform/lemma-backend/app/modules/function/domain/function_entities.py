from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field

from app.core.domain.entity import Entity


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


class FunctionEntity(Entity):
    """Function entity representing a programmatic task."""

    pod_id: UUID
    user_id: UUID
    name: str
    description: str | None = None
    input_schema: dict = Field(default_factory=dict)
    output_schema: dict = Field(default_factory=dict)
    config_schema: dict | None = None
    code_path: str | None = None
    config: dict | None = None
    status: FunctionStatus = FunctionStatus.DRAFT


class FunctionUpdateEntity(BaseModel):
    """Entity for updating function fields."""

    name: str | None = None
    description: str | None = None
    input_schema: dict | None = None
    output_schema: dict | None = None
    config: dict | None = None
    status: FunctionStatus | None = None

    model_config = {"from_attributes": True}


class FunctionRunEntity(Entity):
    """Function run entity representing an execution."""

    function_id: UUID
    user_id: UUID
    input_data: dict | None = None
    output_data: dict | None = None
    status: FunctionRunStatus = FunctionRunStatus.PENDING
    error: str | None = None
    logs: str | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
