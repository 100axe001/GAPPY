from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetUserEmailToolInput, GetUserEmailToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetUserEmailInput(GetUserEmailToolInput):
    """Operation input for `get_user_email`."""
    pass

class GetUserEmailOutput(GetUserEmailToolOutput):
    """Operation output for `get_user_email`."""
    pass

class JiraUserEmailResource(BaseResourceClient):
    """Operations for the `user_email` resource."""

    @operation(
        name='get_user_email',
        title='GetUserEmail',
        input_model=GetUserEmailInput,
        output_model=GetUserEmailOutput,
        tools_used=('get_user_email',),
        tags=tuple(['Users']),
    )
    async def get(self, data: GetUserEmailInput) -> GetUserEmailOutput:
        """Returns a user's email address. This API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603).

Important inputs: account_id"""
        tool = self._client.get_tool('get_user_email')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetUserEmailOutput.model_validate(coerce_tool_result(result))
