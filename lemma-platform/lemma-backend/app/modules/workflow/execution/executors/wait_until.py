"""Wait-until node executor: schedule a wake and suspend on a TIME wait."""

from datetime import datetime, timedelta, timezone

from app.modules.workflow.domain.nodes import WaitUntilNode
from app.modules.workflow.domain.wait import WaitRequest, WorkflowRunWaitType
from app.modules.workflow.execution.outcome import NodeOutcome, Suspend
from app.modules.workflow.execution.step_context import StepContext


class WaitUntilExecutor:
    async def execute(self, node: WaitUntilNode, step: StepContext) -> NodeOutcome:
        scheduled_at = datetime.now(timezone.utc) + timedelta(
            seconds=node.config.timeout_seconds
        )

        timer_id = await step.schedule.schedule_workflow_wake(
            run_id=step.run_id,
            scheduled_at=scheduled_at.isoformat(),
            pod_id=step.pod_id,
            user_id=step.user_id,
        )

        return Suspend(
            wait=WaitRequest(
                wait_type=WorkflowRunWaitType.TIME,
                external_ref=str(timer_id),
                scheduled_at=scheduled_at,
                payload={"scheduled_at": scheduled_at.isoformat()},
            )
        )
