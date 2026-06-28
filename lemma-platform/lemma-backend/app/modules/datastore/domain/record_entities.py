from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class RecordEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: Any
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    pod_id: UUID
    table_name: str
    data: Dict[str, Any]
    user_id: Optional[UUID] = None
