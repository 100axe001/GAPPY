from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetUserDefaultColumnsToolInput, GetUserDefaultColumnsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetUserDefaultColumnsInput(GetUserDefaultColumnsToolInput):
    """Operation input for `get_user_default_columns`."""
    pass

class GetUserDefaultColumnsOutput(GetUserDefaultColumnsToolOutput):
    """Operation output for `get_user_default_columns`."""
    pass

class JiraUserDefaultColumnsResource(BaseResourceClient):
    """Operations for the `user_default_columns` resource."""

    @operation(
        name='get_user_default_columns',
        title='GetUserDefaultColumns',
        input_model=GetUserDefaultColumnsInput,
        output_model=GetUserDefaultColumnsOutput,
        tools_used=('get_user_default_columns',),
        tags=tuple(['Users']),
    )
    async def get(self, data: GetUserDefaultColumnsInput) -> GetUserDefaultColumnsOutput:
        """Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If `accountId` is not passed in the request, the calling user's details are returned. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the column details for any user. * Permission to access Jira, to get the calling user's column details.

Important inputs: account_id, username"""
        tool = self._client.get_tool('get_user_default_columns')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetUserDefaultColumnsOutput.model_validate(coerce_tool_result(result))
