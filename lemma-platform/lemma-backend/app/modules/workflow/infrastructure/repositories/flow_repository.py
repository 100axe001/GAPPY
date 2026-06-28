"""Flow (workflow definition) repository."""

from uuid import UUID
from typing import List, Optional

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.authorization.context import Context, ResourceType, ResourceVisibility
from app.core.authorization.grants import delete_resource_sharing_grants
from app.core.authorization.permissions import Permissions
from app.core.authorization.sql_actions import (
    allowed_actions_contains,
    allowed_actions_expr,
)
from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.modules.workflow.domain.flow import FlowEntity, FlowSummaryEntity, WorkflowMode
from app.modules.workflow.domain.graph import WorkflowEdge
from app.modules.workflow.domain.nodes import WORKFLOW_NODE_ADAPTER
from app.modules.workflow.domain.ports import FlowRepository
from app.modules.workflow.infrastructure.models import FlowModel


class SqlAlchemyFlowRepository(FlowRepository):
    def __init__(self, uow: SqlAlchemyUnitOfWork):
        self.session: AsyncSession = uow.session

    def _to_entity(
        self,
        model: FlowModel,
        allowed_actions: list[str] | tuple[str, ...] | None = None,
    ) -> FlowEntity:
        nodes = [WORKFLOW_NODE_ADAPTER.validate_python(n) for n in model.nodes]
        edges = [WorkflowEdge(**e) for e in model.edges]
        entity = FlowEntity(
            id=model.id,
            pod_id=model.pod_id,
            user_id=model.user_id,
            name=model.name,
            description=model.description,
            icon_url=model.icon_url,
            nodes=nodes,
            edges=edges,
            entry_node_id=model.entry_node_id,
            start=model.start,
            mode=WorkflowMode(model.mode),
            is_active=model.is_active,
            visibility=model.visibility,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
        if allowed_actions is not None:
            entity.allowed_actions = list(allowed_actions)
        return entity

    def _to_dict(self, entity: FlowEntity) -> dict:
        return {
            "id": entity.id,
            "pod_id": entity.pod_id,
            "user_id": entity.user_id,
            "name": entity.name,
            "description": entity.description,
            "icon_url": entity.icon_url,
            "nodes": [n.model_dump(mode="json") for n in entity.nodes],
            "edges": [e.model_dump(mode="json") for e in entity.edges],
            "entry_node_id": entity.entry_node_id,
            "start": entity.start.model_dump(mode="json") if entity.start else None,
            "mode": entity.mode.value,
            "is_active": entity.is_active,
            "visibility": entity.visibility,
        }

    async def create(self, flow: FlowEntity) -> FlowEntity:
        data = self._to_dict(flow)
        if flow.id:
            data["id"] = flow.id

        model = FlowModel(**data)
        self.session.add(model)
        await self.session.flush()
        flow.id = model.id
        return self._to_entity(model)

    async def get(self, flow_id: UUID, ctx: Context | None = None) -> Optional[FlowEntity]:
        if ctx is None:
            stmt = select(FlowModel).where(FlowModel.id == flow_id)
            result = await self.session.execute(stmt)
            model = result.scalar_one_or_none()
            return self._to_entity(model) if model else None
        actions = allowed_actions_expr(
            ctx=ctx,
            resource_type=ResourceType.WORKFLOW,
            resource_id_col=FlowModel.id,
            pod_id_col=FlowModel.pod_id,
            owner_user_id_col=FlowModel.user_id,
            visibility_col=FlowModel.visibility,
        )
        stmt = select(FlowModel, actions).where(FlowModel.id == flow_id)
        result = await self.session.execute(stmt)
        row = result.one_or_none()
        return self._to_entity(row[0], row[1]) if row else None

    async def get_for_update(self, flow_id: UUID) -> Optional[FlowEntity]:
        stmt = select(FlowModel).where(FlowModel.id == flow_id).with_for_update()
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def get_by_name(
        self,
        pod_id: UUID,
        name: str,
        ctx: Context | None = None,
    ) -> Optional[FlowEntity]:
        if ctx is None:
            stmt = select(FlowModel).where(
                FlowModel.pod_id == pod_id,
                FlowModel.name == name,
            )
            result = await self.session.execute(stmt)
            model = result.scalar_one_or_none()
            return self._to_entity(model) if model else None
        actions = allowed_actions_expr(
            ctx=ctx,
            resource_type=ResourceType.WORKFLOW,
            resource_id_col=FlowModel.id,
            pod_id_col=FlowModel.pod_id,
            owner_user_id_col=FlowModel.user_id,
            visibility_col=FlowModel.visibility,
        )
        stmt = select(FlowModel, actions).where(
            FlowModel.pod_id == pod_id,
            FlowModel.name == name,
        )
        result = await self.session.execute(stmt)
        row = result.one_or_none()
        return self._to_entity(row[0], row[1]) if row else None

    async def update(self, flow: FlowEntity) -> FlowEntity:
        payload = self._to_dict(flow)
        for field in {"id", "pod_id", "name"}:
            payload.pop(field, None)
        previous_visibility = (
            await self.session.execute(
                select(FlowModel.visibility).where(FlowModel.id == flow.id)
            )
        ).scalar_one_or_none()
        if (
            previous_visibility == ResourceVisibility.RESTRICTED.value
            and flow.visibility != ResourceVisibility.RESTRICTED.value
        ):
            await delete_resource_sharing_grants(
                self.session,
                pod_id=flow.pod_id,
                resource_type=ResourceType.WORKFLOW,
                resource_id=flow.id,
            )
        stmt = update(FlowModel).where(FlowModel.id == flow.id).values(**payload)
        await self.session.execute(stmt)
        return await self.get(flow.id)

    async def delete(self, flow_id: UUID) -> None:
        stmt = delete(FlowModel).where(FlowModel.id == flow_id)
        await self.session.execute(stmt)

    async def list_by_pod(
        self,
        pod_id: UUID,
        *,
        limit: int = 100,
        cursor: UUID | None = None,
    ) -> tuple[List[FlowEntity], UUID | None]:
        stmt = select(FlowModel).where(FlowModel.pod_id == pod_id)
        if cursor is not None:
            stmt = stmt.where(FlowModel.id < cursor)
        stmt = stmt.order_by(FlowModel.id.desc()).limit(limit + 1)
        result = await self.session.execute(stmt)
        models = list(result.scalars().all())

        next_cursor = None
        if len(models) > limit:
            next_cursor = models[limit - 1].id
            models = models[:limit]

        return [self._to_entity(m) for m in models], next_cursor

    def _to_summary(
        self,
        model: FlowModel,
        allowed_actions: list[str] | tuple[str, ...],
    ) -> FlowSummaryEntity:
        # Derive graph stats from the raw JSONB without validating every node
        # through WORKFLOW_NODE_ADAPTER (that per-node validation is a large part
        # of the list serialization cost we are removing here).
        raw_nodes = model.nodes or []
        node_types = sorted(
            {n.get("type") for n in raw_nodes if isinstance(n, dict) and n.get("type")}
        )
        return FlowSummaryEntity(
            id=model.id,
            pod_id=model.pod_id,
            user_id=model.user_id,
            name=model.name,
            description=model.description,
            icon_url=model.icon_url,
            is_active=model.is_active,
            mode=WorkflowMode(model.mode),
            visibility=model.visibility,
            node_count=len(raw_nodes),
            node_types=node_types,
            allowed_actions=list(allowed_actions),
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    async def list_summaries_visible_by_pod(
        self,
        pod_id: UUID,
        *,
        ctx: Context,
        limit: int = 100,
        cursor: UUID | None = None,
    ) -> tuple[List[FlowSummaryEntity], UUID | None]:
        actions = allowed_actions_expr(
            ctx=ctx,
            resource_type=ResourceType.WORKFLOW,
            resource_id_col=FlowModel.id,
            pod_id_col=FlowModel.pod_id,
            owner_user_id_col=FlowModel.user_id,
            visibility_col=FlowModel.visibility,
        )
        stmt = select(FlowModel, actions).where(
            FlowModel.pod_id == pod_id,
            allowed_actions_contains(actions, Permissions.WORKFLOW_READ),
        )
        if cursor is not None:
            stmt = stmt.where(FlowModel.id < cursor)
        stmt = stmt.order_by(FlowModel.id.desc()).limit(limit + 1)
        result = await self.session.execute(stmt)
        rows = list(result.all())

        next_cursor = None
        if len(rows) > limit:
            next_cursor = rows[limit - 1][0].id
            rows = rows[:limit]

        return [self._to_summary(model, actions) for model, actions in rows], next_cursor

    async def list_visible_by_pod(
        self,
        pod_id: UUID,
        *,
        ctx: Context,
        limit: int = 100,
        cursor: UUID | None = None,
    ) -> tuple[List[FlowEntity], UUID | None]:
        actions = allowed_actions_expr(
            ctx=ctx,
            resource_type=ResourceType.WORKFLOW,
            resource_id_col=FlowModel.id,
            pod_id_col=FlowModel.pod_id,
            owner_user_id_col=FlowModel.user_id,
            visibility_col=FlowModel.visibility,
        )
        stmt = select(FlowModel, actions).where(
            FlowModel.pod_id == pod_id,
            allowed_actions_contains(actions, Permissions.WORKFLOW_READ),
        )
        if cursor is not None:
            stmt = stmt.where(FlowModel.id < cursor)
        stmt = stmt.order_by(FlowModel.id.desc()).limit(limit + 1)
        result = await self.session.execute(stmt)
        rows = list(result.all())

        next_cursor = None
        if len(rows) > limit:
            next_cursor = rows[limit - 1][0].id
            rows = rows[:limit]

        return [self._to_entity(model, actions) for model, actions in rows], next_cursor
