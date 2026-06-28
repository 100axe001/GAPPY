from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddUserToGroupToolInput, AddUserToGroupToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddUserToGroupInput(AddUserToGroupToolInput):
    """Operation input for `add_user_to_group`."""
    pass

class AddUserToGroupOutput(AddUserToGroupToolOutput):
    """Operation output for `add_user_to_group`."""
    pass

class JiraUserToGroupResource(BaseResourceClient):
    """Operations for the `user_to_group` resource."""

    @operation(
        name='add_user_to_group',
        title='AddUserToGroup',
        input_model=AddUserToGroupInput,
        output_model=AddUserToGroupOutput,
        tools_used=('add_user_to_group',),
        tags=tuple(['Groups']),
    )
    async def add(self, data: AddUserToGroupInput) -> AddUserToGroupOutput:
        """Adds a user to a group. **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).

Important inputs: groupname, group_id, body"""
        tool = self._client.get_tool('add_user_to_group')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddUserToGroupOutput.model_validate(coerce_tool_result(result))
