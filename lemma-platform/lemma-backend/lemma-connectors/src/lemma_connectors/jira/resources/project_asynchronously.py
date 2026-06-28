from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteProjectAsynchronouslyToolInput, DeleteProjectAsynchronouslyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteProjectAsynchronouslyInput(DeleteProjectAsynchronouslyToolInput):
    """Operation input for `delete_project_asynchronously`."""
    pass

class DeleteProjectAsynchronouslyOutput(DeleteProjectAsynchronouslyToolOutput):
    """Operation output for `delete_project_asynchronously`."""
    pass

class JiraProjectAsynchronouslyResource(BaseResourceClient):
    """Operations for the `project_asynchronously` resource."""

    @operation(
        name='delete_project_asynchronously',
        title='DeleteProjectAsynchronously',
        input_model=DeleteProjectAsynchronouslyInput,
        output_model=DeleteProjectAsynchronouslyOutput,
        tools_used=('delete_project_asynchronously',),
        tags=tuple(['Projects']),
    )
    async def delete(self, data: DeleteProjectAsynchronouslyInput) -> DeleteProjectAsynchronouslyOutput:
        """Deletes a project asynchronously. This operation is: * transactional, that is, if part of the delete fails the project is not deleted. * [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key"""
        tool = self._client.get_tool('delete_project_asynchronously')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteProjectAsynchronouslyOutput.model_validate(coerce_tool_result(result))
