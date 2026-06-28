from __future__ import annotations

from uuid import UUID

from sqlalchemy import select

from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.modules.identity.infrastructure.models.organization_models import (
    Organization,
    OrganizationMember,
)
from app.modules.connectors.domain.ports import OrganizationAccessPort


class SqlAlchemyOrganizationAccessAdapter(OrganizationAccessPort):
    def __init__(self, uow: SqlAlchemyUnitOfWork):
        self.session = uow.session

    async def organization_exists(self, organization_id: UUID) -> bool:
        stmt = select(Organization.id).where(Organization.id == organization_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none() is not None

    async def user_has_organization_role(
        self,
        user_id: UUID,
        organization_id: UUID,
        allowed_roles: list[str] | None = None,
    ) -> bool:
        stmt = select(OrganizationMember.id).where(
            OrganizationMember.user_id == user_id,
            OrganizationMember.organization_id == organization_id,
        )
        if allowed_roles:
            stmt = stmt.where(OrganizationMember.role.in_(allowed_roles))
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none() is not None
