"""Standalone pod reads for callers that have no UnitOfWork in scope.

Schedule filtering and workspace env setup resolve a pod's organization id
outside any request/UoW boundary. They used to open their own SQLAlchemy
session inline; this keeps that raw access inside the pod infrastructure layer
so those services stay ORM-free.
"""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select

from app.core.infrastructure.db.session import async_session_maker
from app.modules.pod.infrastructure.models.pod_models import Pod


async def resolve_pod_organization_id(pod_id: UUID) -> UUID | None:
    """Look up a pod's organization id via a short-lived session."""
    async with async_session_maker() as session:
        result = await session.execute(
            select(Pod.organization_id).where(Pod.id == pod_id)
        )
        return result.scalar_one_or_none()
