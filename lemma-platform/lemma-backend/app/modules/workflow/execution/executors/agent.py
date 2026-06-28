"""Agent node executor: start the conversation and suspend on an AGENT wait."""

from app.modules.workflow.domain.nodes import AgentNode
from app.modules.workflow.domain.wait import WaitRequest, WorkflowRunWaitType
from app.modules.workflow.execution.outcome import NodeOutcome, Suspend
from app.modules.workflow.execution.step_context import StepContext


class AgentExecutor:
    async def execute(self, node: AgentNode, step: StepContext) -> NodeOutcome:
        input_data = step.context.resolve_inputs(node.config.input_mapping)

        conversation_id = await step.agent.run_agent(
            agent_name=node.config.agent_name,
            input_data=input_data,
            pod_id=step.pod_id,
            user_id=step.user_id,
            workflow_run_id=step.run_id,
        )

        return Suspend(
            wait=WaitRequest(
                wait_type=WorkflowRunWaitType.AGENT,
                external_ref=str(conversation_id),
                payload={"agent_name": node.config.agent_name},
            )
        )
