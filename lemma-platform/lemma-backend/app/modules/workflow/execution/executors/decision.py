"""Decision node executor: first truthy rule wins."""

from app.modules.workflow.domain.nodes import DecisionNode
from app.modules.workflow.execution.outcome import Branch, NodeOutcome
from app.modules.workflow.execution.step_context import StepContext


class DecisionExecutor:
    async def execute(self, node: DecisionNode, step: StepContext) -> NodeOutcome:
        for rule in node.config.rules:
            # Evaluation errors propagate and fail the run loudly; conditions
            # were compile-checked at save time, so a failure here is a
            # genuine runtime problem worth surfacing.
            if step.context.resolve_condition(rule.condition):
                return Branch(
                    next_node_id=rule.next_node_id,
                    output={"matched_condition": rule.condition},
                )
        # No rule matched: fall through to the default outgoing edge.
        return Branch(next_node_id=None, output={"matched_condition": None})
