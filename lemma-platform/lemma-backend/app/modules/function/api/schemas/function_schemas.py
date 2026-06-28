from uuid import UUID
from typing import Optional, Dict, Any, List

from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.core.authorization.context import ResourceType, ResourceVisibility
from app.core.authorization.grants import ensure_grant_uses_resource_name
from app.modules.function.domain.entities import FunctionStatus, FunctionRunStatus, FunctionType


class CreateFunctionRequest(BaseModel):
    """Request to create a function.

    Input and output schemas are derived from the submitted code and returned
    on the function response. They are not accepted in create requests.
    """

    model_config = ConfigDict(extra="forbid")

    name: str
    description: Optional[str] = None
    icon_url: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    code: Optional[str] = Field(
        default=None,
        description=(
            "Python source for the function. When provided, the platform analyzes "
            "the code and populates input_schema, output_schema, and config_schema "
            "on the returned function."
        ),
    )
    type: FunctionType = FunctionType.API
    visibility: ResourceVisibility = ResourceVisibility.POD


class UpdateFunctionRequest(BaseModel):
    """Request to update a function."""

    description: Optional[str] = None
    icon_url: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    code: Optional[str] = Field(
        default=None,
        description=(
            "Updated Python source for the function. When provided, the platform "
            "re-analyzes the code and refreshes input_schema, output_schema, and "
            "config_schema on the returned function."
        ),
    )
    type: Optional[FunctionType] = None
    visibility: Optional[ResourceVisibility] = None


class ExecuteFunctionRequest(BaseModel):
    """Request to execute a function."""

    input_data: Dict[str, Any] = Field(default_factory=dict)


class FunctionResourcePermissionRequest(BaseModel):
    resource_type: ResourceType
    resource_name: str
    permission_ids: List[str] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def _require_resource_name(cls, data: object) -> object:
        return ensure_grant_uses_resource_name(data)


class FunctionPermissionsReplaceRequest(BaseModel):
    grants: List[FunctionResourcePermissionRequest] = Field(default_factory=list)


class FunctionResourcePermissionResponse(BaseModel):
    resource_type: ResourceType
    resource_name: str
    permission_ids: List[str] = Field(default_factory=list)


class FunctionPermissionsResponse(BaseModel):
    function_id: UUID
    function_name: str
    grants: List[FunctionResourcePermissionResponse] = Field(default_factory=list)


class FunctionResponse(BaseModel):
    """Function response."""

    id: UUID
    pod_id: UUID
    user_id: UUID
    name: str
    description: Optional[str] = None
    icon_url: Optional[str] = None
    input_schema: Dict[str, Any] = Field(
        description="Input JSON schema derived from the function code."
    )
    output_schema: Dict[str, Any] = Field(
        description="Output JSON schema derived from the function code."
    )
    config_schema: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional configuration schema derived from the function code.",
    )
    config: Optional[Dict[str, Any]] = None
    type: FunctionType
    status: FunctionStatus
    visibility: str = "POD"
    code_path: Optional[str] = None
    code_hash: Optional[str] = None
    code: Optional[str] = (
        None  # Include code content if requested? Controller usually handles this.
    )
    python_packages: List[str] = Field(
        default_factory=list,
        description="pip dependencies declared in the code's #python_packages header.",
    )
    created_at: Any
    updated_at: Any

    model_config = {"from_attributes": True}


class FunctionActionResponse(FunctionResponse):
    allowed_actions: List[str] = Field(default_factory=list)


class FunctionDetailResponse(FunctionActionResponse):
    permissions: FunctionPermissionsResponse


class FunctionSummaryResponse(BaseModel):
    """Lean function shape for list responses.

    Omits the heavy `input_schema` / `output_schema` / `config_schema` (full JSON
    schemas derived from the function code) and `code` — fetch those from
    `function.get`.
    """

    model_config = {"from_attributes": True}

    id: UUID
    pod_id: UUID
    user_id: UUID
    name: str
    description: Optional[str] = None
    icon_url: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    type: FunctionType
    status: FunctionStatus
    visibility: str = "POD"
    code_path: Optional[str] = None
    code_hash: Optional[str] = None
    python_packages: List[str] = Field(default_factory=list)
    created_at: Any
    updated_at: Any
    allowed_actions: List[str] = Field(default_factory=list)


class FunctionListResponse(BaseModel):
    """List of functions."""

    items: List[FunctionSummaryResponse]
    limit: int
    next_page_token: Optional[str] = None


class FunctionRunResponse(BaseModel):
    """Function run response."""

    id: UUID
    function_id: UUID
    user_id: UUID
    input_data: Optional[Dict[str, Any]] = None
    output_data: Optional[Dict[str, Any]] = None
    status: FunctionRunStatus
    user_email: Optional[str] = None
    job_id: Optional[str] = None
    workspace_session_id: Optional[str] = None
    workspace_process_id: Optional[str] = None
    error: Optional[str] = None
    logs: Optional[str] = None
    started_at: Any
    completed_at: Any
    created_at: Any

    model_config = {"from_attributes": True}


class FunctionRunSummaryResponse(BaseModel):
    """Function run summary for list responses."""

    id: UUID
    function_id: UUID
    user_id: UUID
    status: FunctionRunStatus
    started_at: Any
    completed_at: Any
    created_at: Any

    model_config = {"from_attributes": True}


class FunctionRunListResponse(BaseModel):
    """List of function runs."""

    items: List[FunctionRunSummaryResponse]
    limit: int
    next_page_token: Optional[str] = None


class FunctionMessageResponse(BaseModel):
    """Simple function action response."""

    message: str
