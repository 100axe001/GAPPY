from pydantic import BaseModel, ConfigDict
from typing import Optional, Any, Dict, List
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
    id: int
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
    source_id: int
    target_id: int
    connection_type: str

class ConnectionResponse(BaseModel):
    id: int
    source_id: int
    target_id: int
    connection_type: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ConnectionDetailResponse(BaseModel):
    id: int
    source_id: int
    target_id: int
    connection_type: str
    created_at: datetime
    source_title: str
    source_type: str
    target_title: str
    target_type: str
    model_config = ConfigDict(from_attributes=True)

class StudyReviewResponse(BaseModel):
    id: int
    user_id: int
    concept_id: int
    interval_days: int
    due_date: datetime
    last_reviewed_at: Optional[datetime] = None
    status: str
    created_at: datetime
    concept_title: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class StudyReviewSubmit(BaseModel):
    review_id: int
    score: int  # e.g., number of correct answers out of 3

class PracticeTestSubmit(BaseModel):
    material_id: int
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
    note_ids: List[int]
    format: str  # "essay", "plan", "email", "summary"

class PomodoroDebriefRequest(BaseModel):
    summary: str
    confusion: Optional[str] = ""

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
    id: int
    title: str
    tag: Optional[str] = None
    metadata_json: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class MessageResponse(BaseModel):
    id: int
    conversation_id: int
    role: str
    content: Optional[str] = None
    tool_calls_json: List[Dict[str, Any]] = []
    metadata_json: Dict[str, Any] = {}
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ChatSendRequest(BaseModel):
    message: str

class ChatSendResponse(BaseModel):
    conversation_id: int
    user_message: MessageResponse
    assistant_message: MessageResponse
    tools_used: List[str] = []

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



