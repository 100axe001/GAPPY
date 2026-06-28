"""Authorization helpers for unit tests."""

from __future__ import annotations

from uuid import UUID, uuid4

from app.core.authorization.context import (
    ActorType,
    AuthorizationDecision,
    Context,
    ResourceRef,
    ResourceType,
)


class AllowAllAuthorizer:
    async def authorize(
        self,
        ctx: Context,
        permission_id: str,
        resource: ResourceRef | None = None,
    ) -> AuthorizationDecision:
        return AuthorizationDecision(True, "TEST_ALLOW", permission_id, resource)

    async def accessible_resource_ids(
        self,
        ctx: Context,
        permission_id: str,
        resource_type: ResourceType,
        pod_id: UUID,
    ) -> frozenset[UUID]:
        return frozenset()


class DenyAllAuthorizer:
    async def authorize(
        self,
        ctx: Context,
        permission_id: str,
        resource: ResourceRef | None = None,
    ) -> AuthorizationDecision:
        return AuthorizationDecision(False, "TEST_DENY", permission_id, resource)

    async def accessible_resource_ids(
        self,
        ctx: Context,
        permission_id: str,
        resource_type: ResourceType,
        pod_id: UUID,
    ) -> frozenset[UUID]:
        return frozenset()


def allow_all_context(
    *,
    user_id: UUID | None = None,
    pod_id: UUID | None = None,
) -> Context:
    """A user context whose authorizer allows every action. Unit tests only."""
    resolved_user_id = user_id or uuid4()
    return Context(
        actor_type=ActorType.USER,
        actor_id=str(resolved_user_id),
        user_id=resolved_user_id,
        pod_id=pod_id,
        authorizer=AllowAllAuthorizer(),
    )


def deny_all_context(
    *,
    user_id: UUID | None = None,
    pod_id: UUID | None = None,
) -> Context:
    """A user context whose authorizer denies every action. Unit tests only."""
    resolved_user_id = user_id or uuid4()
    return Context(
        actor_type=ActorType.USER,
        actor_id=str(resolved_user_id),
        user_id=resolved_user_id,
        pod_id=pod_id,
        authorizer=DenyAllAuthorizer(),
    )
