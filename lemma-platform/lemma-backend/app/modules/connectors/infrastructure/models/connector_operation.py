from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.infrastructure.db.base import StringAuditBase
from app.modules.connectors.domain.connector_operation import (
    ConnectorOperationEntity,
)

if TYPE_CHECKING:
    from .connector import Connector


class ConnectorOperation(StringAuditBase):
    """Stored catalog entry for connector operations."""

    __tablename__ = "connector_operations"

    connector_id: Mapped[str] = mapped_column(
        String(255),
        ForeignKey("connectors.id", ondelete="CASCADE"),
        nullable=False,
    )
    provider: Mapped[str] = mapped_column(String(50), default="LEMMA", nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    provider_operation_name: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )
    display_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    search_document: Mapped[str | None] = mapped_column(Text, nullable=True)
    input_schema: Mapped[dict | None] = mapped_column(
        JSONB,
        default=None,
        nullable=True,
    )
    output_schema: Mapped[dict | None] = mapped_column(
        JSONB,
        default=None,
        nullable=True,
    )

    connector: Mapped["Connector"] = relationship("Connector")

    __table_args__ = (
        Index(
            "ix_connector_operations_app_provider_name",
            "connector_id",
            "provider",
            "name",
            unique=True,
        ),
        Index(
            "ix_connector_operations_app_provider_operation",
            "connector_id",
            "provider",
            "provider_operation_name",
        ),
    )

    def to_entity(self) -> ConnectorOperationEntity:
        return ConnectorOperationEntity.model_validate(self)

    def __repr__(self) -> str:
        return (
            f"<ConnectorOperation(connector_id={self.connector_id}, name={self.name})>"
        )
