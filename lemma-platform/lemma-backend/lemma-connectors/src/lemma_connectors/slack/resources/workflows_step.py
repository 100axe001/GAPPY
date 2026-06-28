from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import WorkflowsStepCompletedToolInput, WorkflowsStepCompletedToolOutput, WorkflowsStepFailedToolInput, WorkflowsStepFailedToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class WorkflowsStepCompletedInput(WorkflowsStepCompletedToolInput):
    """Operation input for `workflows_step_completed`."""
    pass

class WorkflowsStepCompletedOutput(WorkflowsStepCompletedToolOutput):
    """Operation output for `workflows_step_completed`."""
    pass

class WorkflowsStepFailedInput(WorkflowsStepFailedToolInput):
    """Operation input for `workflows_step_failed`."""
    pass

class WorkflowsStepFailedOutput(WorkflowsStepFailedToolOutput):
    """Operation output for `workflows_step_failed`."""
    pass

class SlackWorkflowsStepResource(BaseResourceClient):
    """Operations for the `workflows_step` resource."""

    @operation(
        name='workflows_step_completed',
        title='WorkflowsStepCompleted',
        input_model=WorkflowsStepCompletedInput,
        output_model=WorkflowsStepCompletedOutput,
        tools_used=('workflows_step_completed',),
        tags=tuple(['workflows']),
    )
    async def completed(self, data: WorkflowsStepCompletedInput) -> WorkflowsStepCompletedOutput:
        """Indicate that an app's step in a workflow completed execution.

Important inputs: token, workflow_step_execute_id, outputs"""
        tool = self._client.get_tool('workflows_step_completed')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return WorkflowsStepCompletedOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='workflows_step_failed',
        title='WorkflowsStepFailed',
        input_model=WorkflowsStepFailedInput,
        output_model=WorkflowsStepFailedOutput,
        tools_used=('workflows_step_failed',),
        tags=tuple(['workflows']),
    )
    async def failed(self, data: WorkflowsStepFailedInput) -> WorkflowsStepFailedOutput:
        """Indicate that an app's step in a workflow failed to execute.

Important inputs: token, workflow_step_execute_id, error"""
        tool = self._client.get_tool('workflows_step_failed')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return WorkflowsStepFailedOutput.model_validate(coerce_tool_result(result))
