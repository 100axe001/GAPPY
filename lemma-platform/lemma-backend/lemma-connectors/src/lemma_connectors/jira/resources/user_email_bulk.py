from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetUserEmailBulkToolInput, GetUserEmailBulkToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetUserEmailBulkInput(GetUserEmailBulkToolInput):
    """Operation input for `get_user_email_bulk`."""
    pass

class GetUserEmailBulkOutput(GetUserEmailBulkToolOutput):
    """Operation output for `get_user_email_bulk`."""
    pass

class JiraUserEmailBulkResource(BaseResourceClient):
    """Operations for the `user_email_bulk` resource."""

    @operation(
        name='get_user_email_bulk',
        title='GetUserEmailBulk',
        input_model=GetUserEmailBulkInput,
        output_model=GetUserEmailBulkOutput,
        tools_used=('get_user_email_bulk',),
        tags=tuple(['Users']),
    )
    async def get(self, data: GetUserEmailBulkInput) -> GetUserEmailBulkOutput:
        """Returns a user's email address. This API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603).

Important inputs: account_id"""
        tool = self._client.get_tool('get_user_email_bulk')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetUserEmailBulkOutput.model_validate(coerce_tool_result(result))
