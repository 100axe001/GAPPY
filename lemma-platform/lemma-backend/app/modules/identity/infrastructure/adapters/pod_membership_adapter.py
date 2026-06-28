from __future__ import annotations

from typing import Optional
from uuid import UUID

from app.core.domain.message_bus import MessageBus
from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.modules.identity.domain.ports import PodMembershipPort
from app.modules.pod.domain.pod_entities import PodMemberEntity
from app.modules.pod.domain.ports import PodMemberRepositoryPort, PodRepositoryPort
from app.modules.pod.infrastructure.pod_repositories import (
    PodMemberRepository,
    PodRepository,
)
from app.modules.pod.services.pod_role_service import PodRoleService
from app.modules.pod.domain.roles import PodRole
from app.core.log.log import get_logger

logger = get_logger(__name__)


class PodMembershipAdapter(PodMembershipPort):
    def __init__(
        self,
        uow: SqlAlchemyUnitOfWork,
        message_bus: MessageBus | None = None,
    ):
        self.uow = uow
        self.pod_repository: PodRepositoryPort = PodRepository(uow, message_bus=message_bus)
        self.pod_member_repository: PodMemberRepositoryPort = PodMemberRepository(
            uow, message_bus=message_bus
        )
        self.pod_role_service = PodRoleService(uow)

    async def get_pod_organization_id(self, pod_id: UUID) -> Optional[UUID]:
        pod = await self.pod_repository.get(pod_id)
        if pod is None:
            return None
        return pod.organization_id

    async def get_pod_invitation_details(
        self, pod_id: UUID
    ) -> Optional[tuple[str, str | None, UUID]]:
        pod = await self.pod_repository.get(pod_id)
        if pod is None:
            return None
        return pod.name, pod.description, pod.organization_id

    async def add_member_to_pod(
        self,
        *,
        pod_id: UUID,
        organization_member_id: UUID,
        user_id: UUID,
        user_email: str,
        user_name: Optional[str],
        pod_role: str,
    ) -> None:
        try:
            resolved_role = PodRole(pod_role)
        except ValueError:
            resolved_role = PodRole.USER

        entity = PodMemberEntity(
            pod_id=pod_id,
            organization_member_id=organization_member_id,
            roles=[resolved_role.value],
            user_id=user_id,
            user_email=user_email,
            user_name=user_name,
        )

        first_name: str | None = None
        last_name: str | None = None
        if user_name:
            parts = user_name.split(" ", 1)
            first_name = parts[0]
            last_name = parts[1] if len(parts) > 1 else None

        entity.mark_added(
            user_id=user_id,
            email=user_email,
            first_name=first_name,
            last_name=last_name,
        )

        created_member = await self.pod_member_repository.create(entity)
        await self.pod_role_service.sync_member_roles(
            pod_id=pod_id,
            pod_member_id=created_member.id,
            roles=[resolved_role],
            added_by_user_id=None,
        )
