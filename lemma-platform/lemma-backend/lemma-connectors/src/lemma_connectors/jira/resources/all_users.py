from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllUsersToolInput, GetAllUsersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllUsersInput(GetAllUsersToolInput):
    """Operation input for `get_all_users`."""
    pass

class GetAllUsersOutput(GetAllUsersToolOutput):
    """Operation output for `get_all_users`."""
    pass

class JiraAllUsersResource(BaseResourceClient):
    """Operations for the `all_users` resource."""

    @operation(
        name='get_all_users',
        title='GetAllUsers',
        input_model=GetAllUsersInput,
        output_model=GetAllUsersOutput,
        tools_used=('get_all_users',),
        tags=tuple(['Users']),
    )
    async def get(self, data: GetAllUsersInput) -> GetAllUsersOutput:
        """Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account. Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details. **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results"""
        tool = self._client.get_tool('get_all_users')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllUsersOutput.model_validate(coerce_tool_result(result))
