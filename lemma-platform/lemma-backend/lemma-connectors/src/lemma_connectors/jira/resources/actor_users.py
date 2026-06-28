from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddActorUsersToolInput, AddActorUsersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddActorUsersInput(AddActorUsersToolInput):
    """Operation input for `add_actor_users`."""
    pass

class AddActorUsersOutput(AddActorUsersToolOutput):
    """Operation output for `add_actor_users`."""
    pass

class JiraActorUsersResource(BaseResourceClient):
    """Operations for the `actor_users` resource."""

    @operation(
        name='add_actor_users',
        title='AddActorUsers',
        input_model=AddActorUsersInput,
        output_model=AddActorUsersOutput,
        tools_used=('add_actor_users',),
        tags=tuple(['Project role actors']),
    )
    async def add(self, data: AddActorUsersInput) -> AddActorUsersOutput:
        """Adds actors to a project role for the project. To replace all actors for the project, use [Set actors for project role](#api-rest-api-3-project-projectIdOrKey-role-id-put). This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key, id, body"""
        tool = self._client.get_tool('add_actor_users')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddActorUsersOutput.model_validate(coerce_tool_result(result))
