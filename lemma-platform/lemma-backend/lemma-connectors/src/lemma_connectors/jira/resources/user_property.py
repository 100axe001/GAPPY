from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteUserPropertyToolInput, DeleteUserPropertyToolOutput, GetUserPropertyToolInput, GetUserPropertyToolOutput, SetUserPropertyToolInput, SetUserPropertyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteUserPropertyInput(DeleteUserPropertyToolInput):
    """Operation input for `delete_user_property`."""
    pass

class DeleteUserPropertyOutput(DeleteUserPropertyToolOutput):
    """Operation output for `delete_user_property`."""
    pass

class GetUserPropertyInput(GetUserPropertyToolInput):
    """Operation input for `get_user_property`."""
    pass

class GetUserPropertyOutput(GetUserPropertyToolOutput):
    """Operation output for `get_user_property`."""
    pass

class SetUserPropertyInput(SetUserPropertyToolInput):
    """Operation input for `set_user_property`."""
    pass

class SetUserPropertyOutput(SetUserPropertyToolOutput):
    """Operation output for `set_user_property`."""
    pass

class JiraUserPropertyResource(BaseResourceClient):
    """Operations for the `user_property` resource."""

    @operation(
        name='delete_user_property',
        title='DeleteUserProperty',
        input_model=DeleteUserPropertyInput,
        output_model=DeleteUserPropertyOutput,
        tools_used=('delete_user_property',),
        tags=tuple(['User properties']),
    )
    async def delete(self, data: DeleteUserPropertyInput) -> DeleteUserPropertyOutput:
        """Deletes a property from a user. Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to delete a property from any user. * Access to Jira, to delete a property from the calling user's record.

Important inputs: account_id, user_key, username, property_key"""
        tool = self._client.get_tool('delete_user_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteUserPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_user_property',
        title='GetUserProperty',
        input_model=GetUserPropertyInput,
        output_model=GetUserPropertyOutput,
        tools_used=('get_user_property',),
        tags=tuple(['User properties']),
    )
    async def get(self, data: GetUserPropertyInput) -> GetUserPropertyOutput:
        """Returns the value of a user's property. If no property key is provided [Get user property keys](#api-rest-api-3-user-properties-get) is called. Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get a property from any user. * Access to Jira, to get a property from the calling user's record.

Important inputs: account_id, user_key, username, property_key"""
        tool = self._client.get_tool('get_user_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetUserPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_user_property',
        title='SetUserProperty',
        input_model=SetUserPropertyInput,
        output_model=SetUserPropertyOutput,
        tools_used=('set_user_property',),
        tags=tuple(['User properties']),
    )
    async def set(self, data: SetUserPropertyInput) -> SetUserPropertyOutput:
        """Sets the value of a user's property. Use this resource to store custom data against a user. Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set a property on any user. * Access to Jira, to set a property on the calling user's record.

Important inputs: account_id, user_key, username, property_key, body"""
        tool = self._client.get_tool('set_user_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetUserPropertyOutput.model_validate(coerce_tool_result(result))
