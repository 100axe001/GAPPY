"""End node executor."""

from app.modules.workflow.domain.nodes import EndNode
from app.modules.workflow.execution.outcome import Halt, NodeOutcome
from app.modules.workflow.execution.step_context import StepContext


class EndExecutor:
    async def execute(self, node: EndNode, step: StepContext) -> NodeOutcome:
        return Halt()
