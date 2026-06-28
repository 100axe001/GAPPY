"""Flow run repository."""

from uuid import UUID
from typing import List, Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import load_only

from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.modules.workflow.domain.ports import FlowRunRepository
from app.modules.workflow.domain.run import (
    FlowRunEntity,
    FlowRunStatus,
)
from app.modules.workflow.infrastructure.models import FlowRunModel


class SqlAlchemyFlowRunRepository(FlowRunRepository):
    def __init__(self, uow: SqlAlchemyUnitOfWork):
        self.session: AsyncSession = uow.session

    def _to_entity(self, model: FlowRunModel) -> FlowRunEntity:
        return model.to_entity()

    def _to_summary_entity(self, model: FlowRunModel) -> FlowRunEntity:
        return FlowRunEntity(
            id=model.id,
            created_at=model.created_at,
            updated_at=model.updated_at,
            flow_id=model.flow_id,
            pod_id=model.pod_id,
            user_id=model.user_id,
            start_type=model.start_type,
            schedule_event_id=model.schedule_event_id,
            status=FlowRunStatus(model.status),
            current_node_id=model.current_node_id,
            error=model.error,
            failed_node_id=model.failed_node_id,
            started_at=model.started_at,
            completed_at=model.completed_at,
        )

    def _to_dict(self, entity: FlowRunEntity) -> dict:
        return {
            "flow_id": entity.flow_id,
            "pod_id": entity.pod_id,
            "user_id": entity.user_id,
            "start_type": entity.start_type,
            "schedule_event_id": entity.schedule_event_id,
            "start_payload": entity.start_payload,
            "status": entity.status.value,
            "current_node_id": entity.current_node_id,
            "execution_context": entity.execution_context.model_dump(mode="json"),
            "execution_stack": [
                f.model_dump(mode="json") for f in entity.execution_stack
            ],
            "step_history": [s.model_dump(mode="json") for s in entity.step_history],
            "error": entity.error,
            "failed_node_id": entity.failed_node_id,
            "started_at": (
                entity.started_at.replace(tzinfo=None) if entity.started_at else None
            ),
            "completed_at": (
                entity.completed_at.replace(tzinfo=None)
                if entity.completed_at
                else None
            ),
        }

    async def create(self, run: FlowRunEntity) -> FlowRunEntity:
        data = self._to_dict(run)
        if run.id:
            data["id"] = run.id
        model = FlowRunModel(**data)
        self.session.add(model)
        await self.session.flush()
        run.id = model.id
        return self._to_entity(model)

    async def get(self, run_id: UUID) -> Optional[FlowRunEntity]:
        stmt = select(FlowRunModel).where(FlowRunModel.id == run_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def get_for_update(self, run_id: UUID) -> Optional[FlowRunEntity]:
        """Row-locked read — serializes concurrent resumes/cancels."""
        stmt = (
            select(FlowRunModel)
            .where(FlowRunModel.id == run_id)
            .with_for_update()
        )
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def update(self, run: FlowRunEntity) -> FlowRunEntity:
        stmt = (
            update(FlowRunModel)
            .where(FlowRunModel.id == run.id)
            .values(**self._to_dict(run))
        )
        await self.session.execute(stmt)
        return await self.get(run.id)

    async def list_by_flow(
        self,
        flow_id: UUID,
        *,
        limit: int = 100,
        cursor: UUID | None = None,
    ) -> tuple[List[FlowRunEntity], UUID | None]:
        stmt = (
            select(FlowRunModel)
            .options(
                load_only(
                    FlowRunModel.id,
                    FlowRunModel.flow_id,
                    FlowRunModel.pod_id,
                    FlowRunModel.user_id,
                    FlowRunModel.start_type,
                    FlowRunModel.schedule_event_id,
                    FlowRunModel.status,
                    FlowRunModel.current_node_id,
                    FlowRunModel.error,
                    FlowRunModel.failed_node_id,
                    FlowRunModel.started_at,
                    FlowRunModel.completed_at,
                    FlowRunModel.created_at,
                    FlowRunModel.updated_at,
                )
            )
            .where(FlowRunModel.flow_id == flow_id)
            .order_by(FlowRunModel.id.desc())
            .limit(limit + 1)
        )
        if cursor is not None:
            stmt = stmt.where(FlowRunModel.id < cursor)
        result = await self.session.execute(stmt)
        models = list(result.scalars().all())

        next_cursor = None
        if len(models) > limit:
            next_cursor = models[limit - 1].id
            models = models[:limit]

        return [self._to_summary_entity(m) for m in models], next_cursor

    async def find_by_schedule_event(
        self,
        *,
        flow_id: UUID,
        user_id: UUID,
        schedule_event_id: str,
    ) -> FlowRunEntity | None:
        stmt = select(FlowRunModel).where(
            FlowRunModel.flow_id == flow_id,
            FlowRunModel.user_id == user_id,
            FlowRunModel.schedule_event_id == schedule_event_id,
        )
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None
