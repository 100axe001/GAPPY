from pydantic import BaseModel, ConfigDict
from typing import Optional, Any, Dict, List, Union
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class ItemCreate(BaseModel):
    type: str
    title: str
    content: Optional[str] = None
    status: Optional[str] = "todo"
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    metadata_json: Optional[Dict[str, Any]] = None

class ItemUpdate(BaseModel):
    type: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    metadata_json: Optional[Dict[str, Any]] = None

class ItemResponse(BaseModel):
    id: str
    type: str
    title: str
    content: Optional[str] = None
    status: str
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    metadata_json: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ConnectionCreate(BaseModel):
    source_id: str
    target_id: str
    connection_type: str

class ConnectionResponse(BaseModel):
    id: str
    source_id: str
    target_id: str
    connection_type: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ConnectionDetailResponse(BaseModel):
    id: str
    source_id: str
    target_id: str
    connection_type: str
    created_at: datetime
    source_title: str
    source_type: str
    target_title: str
    target_type: str
    model_config = ConfigDict(from_attributes=True)

class StudyReviewResponse(BaseModel):
    id: str
    user_id: str
    concept_id: str
    interval_days: int
    due_date: datetime
    last_reviewed_at: Optional[datetime] = None
    status: str
    created_at: datetime
    concept_title: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class StudyReviewSubmit(BaseModel):
    review_id: str
    score: int  # e.g., number of correct answers out of 3

class PracticeTestSubmit(BaseModel):
    material_id: str
    answers: List[Dict[str, Any]]  # [{"question": "...", "selected": "...", "correct": "...", "topic": "..."}]

class CommitmentInboxRequest(BaseModel):
    text: str

class CommitmentInboxConfirm(BaseModel):
    title: str
    content: Optional[str] = None
    priority: str
    due_date: Optional[datetime] = None
    category: Optional[str] = None

class DraftGenerateRequest(BaseModel):
    note_ids: List[str]
    format: str  # "essay", "plan", "email", "summary"

class PomodoroDebriefRequest(BaseModel):
    summary: str
    confusion: Optional[str] = ""

class WorkflowStartRequest(BaseModel):
    inputs: Optional[Dict[str, Any]] = None

class WorkflowDecisionRequest(BaseModel):
    run_id: str
    node_id: str
    approved: bool

class AssistantQueryRequest(BaseModel):
    query: str

class AssistantQueryResponse(BaseModel):
    intent: str
    integration: str
    execution_status: str
    response_message: str
    suggested_actions: Optional[List[Dict[str, Any]]] = None

# -- Chat / Conversations --

class ConversationCreate(BaseModel):
    title: Optional[str] = "New Chat"
    tag: Optional[str] = None

class ConversationUpdate(BaseModel):
    title: Optional[str] = None
    tag: Optional[str] = None

class ConversationResponse(BaseModel):
    id: Union[int, str]
    title: str
    tag: Optional[str] = None
    metadata_json: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class MessageResponse(BaseModel):
    id: Union[int, str]
    conversation_id: Union[int, str]
    role: str
    content: Optional[str] = None
    tool_calls_json: List[Dict[str, Any]] = []
    metadata_json: Dict[str, Any] = {}
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ChatSendRequest(BaseModel):
    message: str

class ChatSendResponse(BaseModel):
    conversation_id: Union[int, str]
    user_message: MessageResponse
    assistant_message: MessageResponse
    tools_used: List[str] = []


class AgentWorkflowCreateRequest(BaseModel):
    type: str
    name: str
    description: Optional[str] = ""
    instructions: Optional[str] = ""
    steps: List[str] = []
    trigger_type: str = "manual"
    cron: Optional[str] = None
    table_name: Optional[str] = None
    event: Optional[str] = None


class TemplateInstallRequest(BaseModel):
    template_id: str


class ScheduleCreateRequest(BaseModel):
    agent_name: Optional[str] = None
    workflow_name: Optional[str] = None
    schedule_type: str
    cron: Optional[str] = None
    table_name: Optional[str] = None
    event: Optional[str] = None
    name: Optional[str] = None


class WorkflowResumeRequest(BaseModel):
    node_id: str
    inputs: Dict[str, Any] = {}

# -- Settings --

class SettingsResponse(BaseModel):
    # Non-secret values returned verbatim; secrets returned as "" plus a *_set flag.
    values: Dict[str, Any]

class SettingsUpdate(BaseModel):
    values: Dict[str, Any]

# -- Web Search --

class WebSearchRequest(BaseModel):
    query: str
    max_results: Optional[int] = 6

class WebSearchResult(BaseModel):
    title: str
    url: str
    snippet: str

class WebSearchResponse(BaseModel):
    query: str
    provider: str
    answer: Optional[str] = None
    results: List[WebSearchResult] = []


class UserIntegrationResponse(BaseModel):
    name: str
    is_connected: bool
    scopes: List[str]
    metadata_json: Dict[str, Any]
    health_status: str
    error_message: Optional[str] = None
    last_sync_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)


