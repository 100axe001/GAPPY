from datetime import datetime, timezone
from uuid import UUID, uuid7

from pydantic import BaseModel, ConfigDict, Field


class Entity(BaseModel):
    """Base Domain Entity."""

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: UUID = Field(default_factory=uuid7)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class CreatedEntity(BaseModel):
    """Base entity for append-only records."""

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: UUID = Field(default_factory=uuid7)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
