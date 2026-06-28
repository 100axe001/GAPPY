from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import WorkflowsUpdateStepToolInput, WorkflowsUpdateStepToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class WorkflowsUpdateStepInput(WorkflowsUpdateStepToolInput):
    """Operation input for `workflows_update_step`."""
    pass

class WorkflowsUpdateStepOutput(WorkflowsUpdateStepToolOutput):
    """Operation output for `workflows_update_step`."""
    pass

class SlackWorkflowsUpdateResource(BaseResourceClient):
    """Operations for the `workflows_update` resource."""

    @operation(
        name='workflows_update_step',
        title='WorkflowsUpdateStep',
        input_model=WorkflowsUpdateStepInput,
        output_model=WorkflowsUpdateStepOutput,
        tools_used=('workflows_update_step',),
        tags=tuple(['workflows']),
    )
    async def step(self, data: WorkflowsUpdateStepInput) -> WorkflowsUpdateStepOutput:
        """Update the configuration for a workflow extension step.

Important inputs: token, workflow_step_edit_id, inputs, outputs, step_name, step_image_url"""
        tool = self._client.get_tool('workflows_update_step')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return WorkflowsUpdateStepOutput.model_validate(coerce_tool_result(result))
