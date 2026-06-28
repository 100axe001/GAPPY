"""Schedule adapter for the workflow module."""

from datetime import datetime
from uuid import UUID

from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.modules.workflow.domain.ports import SchedulePort


class ScheduleControlAdapter(SchedulePort):
    def __init__(self, uow: SqlAlchemyUnitOfWork):
        _ = uow
        from app.modules.schedule.scheduler.api_client import SchedulerAPIClient

        self.scheduler = SchedulerAPIClient()

    async def schedule_workflow_wake(
        self, run_id: UUID, scheduled_at: str, pod_id: UUID, user_id: UUID
    ) -> UUID:
        """Ask the scheduler to wake this workflow run at a specific time."""
        _ = (pod_id, user_id)
        await self.scheduler.schedule_once_job(
            schedule_id=run_id,
            run_date=datetime.fromisoformat(scheduled_at),
            payload={
                "workflow_run_id": str(run_id),
                "scheduled_at": scheduled_at,
                "source": "workflow_wait_until",
            },
            replace_existing=True,
        )
        return run_id
