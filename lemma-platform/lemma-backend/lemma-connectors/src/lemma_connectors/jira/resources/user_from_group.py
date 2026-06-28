from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import RemoveUserFromGroupToolInput, RemoveUserFromGroupToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RemoveUserFromGroupInput(RemoveUserFromGroupToolInput):
    """Operation input for `remove_user_from_group`."""
    pass

class RemoveUserFromGroupOutput(RemoveUserFromGroupToolOutput):
    """Operation output for `remove_user_from_group`."""
    pass

class JiraUserFromGroupResource(BaseResourceClient):
    """Operations for the `user_from_group` resource."""

    @operation(
        name='remove_user_from_group',
        title='RemoveUserFromGroup',
        input_model=RemoveUserFromGroupInput,
        output_model=RemoveUserFromGroupOutput,
        tools_used=('remove_user_from_group',),
        tags=tuple(['Groups']),
    )
    async def remove(self, data: RemoveUserFromGroupInput) -> RemoveUserFromGroupOutput:
        """Removes a user from a group. **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).

Important inputs: groupname, group_id, username, account_id"""
        tool = self._client.get_tool('remove_user_from_group')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveUserFromGroupOutput.model_validate(coerce_tool_result(result))
