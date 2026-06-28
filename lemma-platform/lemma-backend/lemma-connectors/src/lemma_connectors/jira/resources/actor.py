from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteActorToolInput, DeleteActorToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteActorInput(DeleteActorToolInput):
    """Operation input for `delete_actor`."""
    pass

class DeleteActorOutput(DeleteActorToolOutput):
    """Operation output for `delete_actor`."""
    pass

class JiraActorResource(BaseResourceClient):
    """Operations for the `actor` resource."""

    @operation(
        name='delete_actor',
        title='DeleteActor',
        input_model=DeleteActorInput,
        output_model=DeleteActorOutput,
        tools_used=('delete_actor',),
        tags=tuple(['Project role actors']),
    )
    async def delete(self, data: DeleteActorInput) -> DeleteActorOutput:
        """Deletes actors from a project role for the project. To remove default actors from the project role, use [Delete default actors from project role](#api-rest-api-3-role-id-actors-delete). This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key, id, user, group, group_id"""
        tool = self._client.get_tool('delete_actor')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteActorOutput.model_validate(coerce_tool_result(result))
