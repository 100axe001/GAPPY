from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetTaskToolInput, GetTaskToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetTaskInput(GetTaskToolInput):
    """Operation input for `get_task`."""
    pass

class GetTaskOutput(GetTaskToolOutput):
    """Operation output for `get_task`."""
    pass

class JiraTaskResource(BaseResourceClient):
    """Operations for the `task` resource."""

    @operation(
        name='get_task',
        title='GetTask',
        input_model=GetTaskInput,
        output_model=GetTaskOutput,
        tools_used=('get_task',),
        tags=tuple(['Tasks']),
    )
    async def get(self, data: GetTaskInput) -> GetTaskOutput:
        """Returns the status of a [long-running asynchronous task](#async). When a task has finished, this operation returns the JSON blob applicable to the task. See the documentation of the operation that created the task for details. Task details are not permanently retained. As of September 2019, details are retained for 14 days although this period may change without notice. **[Permissions](#permissions) required:** either of: * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). * Creator of the task.

Important inputs: task_id"""
        tool = self._client.get_tool('get_task')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetTaskOutput.model_validate(coerce_tool_result(result))
