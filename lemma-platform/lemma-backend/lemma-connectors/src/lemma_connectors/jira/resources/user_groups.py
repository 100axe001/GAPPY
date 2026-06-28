from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetUserGroupsToolInput, GetUserGroupsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetUserGroupsInput(GetUserGroupsToolInput):
    """Operation input for `get_user_groups`."""
    pass

class GetUserGroupsOutput(GetUserGroupsToolOutput):
    """Operation output for `get_user_groups`."""
    pass

class JiraUserGroupsResource(BaseResourceClient):
    """Operations for the `user_groups` resource."""

    @operation(
        name='get_user_groups',
        title='GetUserGroups',
        input_model=GetUserGroupsInput,
        output_model=GetUserGroupsOutput,
        tools_used=('get_user_groups',),
        tags=tuple(['Users']),
    )
    async def get(self, data: GetUserGroupsInput) -> GetUserGroupsOutput:
        """Returns the groups to which a user belongs. **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: account_id, username"""
        tool = self._client.get_tool('get_user_groups')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetUserGroupsOutput.model_validate(coerce_tool_result(result))
