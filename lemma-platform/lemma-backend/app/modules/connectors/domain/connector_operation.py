from datetime import datetime, timezone
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field

from app.modules.connectors.domain.connector import AuthProvider


class ConnectorOperationEntity(BaseModel):
    """Catalog entry for a connector's operation."""

    id: str = Field(..., description="Unique catalog ID for the operation")
    connector_id: str = Field(..., description="Connector ID")
    provider: AuthProvider = Field(
        default=AuthProvider.LEMMA,
        description="Backend provider that owns this operation",
    )
    name: str = Field(..., description="Public operation name, normalized to lowercase")
    provider_operation_name: Optional[str] = Field(
        default=None,
        description="Provider-specific operation name used during execution",
    )
    display_name: Optional[str] = Field(
        default=None,
        description="Optional human-friendly operation name",
    )
    description: Optional[str] = Field(default=None, description="Operation description")
    search_document: Optional[str] = Field(
        default=None,
        description="Searchable text used for discovery and ranking.",
    )
    input_schema: Optional[dict[str, Any]] = Field(
        default=None,
        description="JSON schema describing the operation input",
    )
    output_schema: Optional[dict[str, Any]] = Field(
        default=None,
        description="JSON schema describing the operation output",
    )
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def execution_name(self) -> str:
        return self.provider_operation_name or self.name
