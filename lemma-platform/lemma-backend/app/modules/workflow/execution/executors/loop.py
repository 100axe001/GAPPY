"""Loop node executor: resolve the items; the stepper drives iterations."""

from app.modules.workflow.domain.errors import NodeExecutionError
from app.modules.workflow.domain.nodes import LoopNode
from app.modules.workflow.execution.outcome import NodeOutcome, StartLoop
from app.modules.workflow.execution.step_context import StepContext


class LoopExecutor:
    async def execute(self, node: LoopNode, step: StepContext) -> NodeOutcome:
        items = step.context.resolve(node.config.items_path)
        if items is None:
            items = []
        if not isinstance(items, list):
            raise NodeExecutionError(
                node.id,
                f"items_path '{node.config.items_path}' resolved to "
                f"{type(items).__name__}, expected a list",
            )
        return StartLoop(
            items=items,
            body_node_id=node.config.child_node_id,
            item_var=node.config.item_var_name,
        )
