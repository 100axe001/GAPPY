from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SetUserColumnsToolInput, SetUserColumnsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SetUserColumnsInput(SetUserColumnsToolInput):
    """Operation input for `set_user_columns`."""
    pass

class SetUserColumnsOutput(SetUserColumnsToolOutput):
    """Operation output for `set_user_columns`."""
    pass

class JiraUserColumnsResource(BaseResourceClient):
    """Operations for the `user_columns` resource."""

    @operation(
        name='set_user_columns',
        title='SetUserColumns',
        input_model=SetUserColumnsInput,
        output_model=SetUserColumnsOutput,
        tools_used=('set_user_columns',),
        tags=tuple(['Users']),
    )
    async def set(self, data: SetUserColumnsInput) -> SetUserColumnsOutput:
        """Sets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If an account ID is not passed, the calling user's default columns are set. If no column details are sent, then all default columns are removed. The parameters for this resource are expressed as HTML form data. For example, in curl: `curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/user/columns?accountId=5b10ac8d82e05b22cc7d4ef5'` **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user. * Permission to access Jira, to set the calling user's columns.

Important inputs: account_id, body"""
        tool = self._client.get_tool('set_user_columns')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetUserColumnsOutput.model_validate(coerce_tool_result(result))
