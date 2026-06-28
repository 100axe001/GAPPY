from __future__ import annotations

from uuid import UUID

from sqlalchemy import String, ForeignKey, Index, Text
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.infrastructure.db.base import UUIDAuditBase
from app.modules.connectors.domain.account import AccountEntity

from app.modules.identity.infrastructure.models.user_models import User
from app.modules.connectors.infrastructure.models.connector import Connector


class Account(UUIDAuditBase):
    """User account for third-party connectors."""

    __tablename__ = "accounts"

    # User and connector references
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False
    )
    auth_config_id: Mapped[UUID] = mapped_column(
        ForeignKey("auth_configs.id", ondelete="CASCADE"), nullable=False
    )
    connector_id: Mapped[str] = mapped_column(
        String(255), ForeignKey("connectors.id", ondelete="CASCADE")
    )
    status: Mapped[str] = mapped_column(
        String(50), default="CONNECTED", nullable=False
    )
    provider_account_id: Mapped[str | None] = mapped_column(
        String(255), default=None, nullable=True, index=True
    )

    # Account details
    email: Mapped[str | None] = mapped_column(String(255), default=None, nullable=True)

    # JSON configuration fields
    credentials: Mapped[dict | None] = mapped_column(
        JSONB, default=None, nullable=True
    )
    preferences: Mapped[dict | None] = mapped_column(
        JSONB, default=None, nullable=True
    )
    # Scopes
    allowed_scopes: Mapped[list[str] | None] = mapped_column(
        ARRAY(Text), default=None, nullable=True
    )

    # Relationships
    connector: Mapped["Connector"] = relationship(Connector)
    auth_config: Mapped["AuthConfig"] = relationship("AuthConfig")
    user: Mapped["User"] = relationship(User, foreign_keys=[user_id])
    __table_args__ = (
        Index(
            "ix_unique_user_auth_config_account",
            "user_id",
            "auth_config_id",
            unique=True,
        ),
    )

    def to_entity(self) -> AccountEntity:
        return AccountEntity.model_validate(self)

    def __repr__(self) -> str:
        return f"<Account(id={self.id}, user_id={self.user_id}, connector_id={self.connector_id})>"
