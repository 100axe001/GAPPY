from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetUserPropertyKeysToolInput, GetUserPropertyKeysToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetUserPropertyKeysInput(GetUserPropertyKeysToolInput):
    """Operation input for `get_user_property_keys`."""
    pass

class GetUserPropertyKeysOutput(GetUserPropertyKeysToolOutput):
    """Operation output for `get_user_property_keys`."""
    pass

class JiraUserPropertyKeysResource(BaseResourceClient):
    """Operations for the `user_property_keys` resource."""

    @operation(
        name='get_user_property_keys',
        title='GetUserPropertyKeys',
        input_model=GetUserPropertyKeysInput,
        output_model=GetUserPropertyKeysOutput,
        tools_used=('get_user_property_keys',),
        tags=tuple(['User properties']),
    )
    async def get(self, data: GetUserPropertyKeysInput) -> GetUserPropertyKeysOutput:
        """Returns the keys of all properties for a user. Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the property keys on any user. * Access to Jira, to access the calling user's property keys.

Important inputs: account_id, user_key, username"""
        tool = self._client.get_tool('get_user_property_keys')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetUserPropertyKeysOutput.model_validate(coerce_tool_result(result))
