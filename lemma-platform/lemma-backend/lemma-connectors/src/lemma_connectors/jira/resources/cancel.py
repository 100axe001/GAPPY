from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CancelTaskToolInput, CancelTaskToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CancelTaskInput(CancelTaskToolInput):
    """Operation input for `cancel_task`."""
    pass

class CancelTaskOutput(CancelTaskToolOutput):
    """Operation output for `cancel_task`."""
    pass

class JiraCancelResource(BaseResourceClient):
    """Operations for the `cancel` resource."""

    @operation(
        name='cancel_task',
        title='CancelTask',
        input_model=CancelTaskInput,
        output_model=CancelTaskOutput,
        tools_used=('cancel_task',),
        tags=tuple(['Tasks']),
    )
    async def task(self, data: CancelTaskInput) -> CancelTaskOutput:
        """Cancels a task. **[Permissions](#permissions) required:** either of: * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). * Creator of the task.

Important inputs: task_id"""
        tool = self._client.get_tool('cancel_task')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CancelTaskOutput.model_validate(coerce_tool_result(result))
