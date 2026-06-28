from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsDelegatesCreateToolInput, GmailUsersSettingsDelegatesCreateToolOutput, GmailUsersSettingsDelegatesDeleteToolInput, GmailUsersSettingsDelegatesDeleteToolOutput, GmailUsersSettingsDelegatesGetToolInput, GmailUsersSettingsDelegatesGetToolOutput, GmailUsersSettingsDelegatesListToolInput, GmailUsersSettingsDelegatesListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SettingsDelegatesCreateInput(GmailUsersSettingsDelegatesCreateToolInput):
    """Operation input for `settings_delegates_create`."""
    pass

class SettingsDelegatesCreateOutput(GmailUsersSettingsDelegatesCreateToolOutput):
    """Operation output for `settings_delegates_create`."""
    pass

class SettingsDelegatesDeleteInput(GmailUsersSettingsDelegatesDeleteToolInput):
    """Operation input for `settings_delegates_delete`."""
    pass

class SettingsDelegatesDeleteOutput(GmailUsersSettingsDelegatesDeleteToolOutput):
    """Operation output for `settings_delegates_delete`."""
    pass

class SettingsDelegatesGetInput(GmailUsersSettingsDelegatesGetToolInput):
    """Operation input for `settings_delegates_get`."""
    pass

class SettingsDelegatesGetOutput(GmailUsersSettingsDelegatesGetToolOutput):
    """Operation output for `settings_delegates_get`."""
    pass

class SettingsDelegatesListInput(GmailUsersSettingsDelegatesListToolInput):
    """Operation input for `settings_delegates_list`."""
    pass

class SettingsDelegatesListOutput(GmailUsersSettingsDelegatesListToolOutput):
    """Operation output for `settings_delegates_list`."""
    pass

class GmailSettingsDelegatesResource(BaseResourceClient):
    """Operations for the `settings_delegates` resource."""

    @operation(
        name='settings_delegates_create',
        title='SettingsDelegatesCreate',
        input_model=SettingsDelegatesCreateInput,
        output_model=SettingsDelegatesCreateOutput,
        tools_used=('gmail_users_settings_delegates_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: SettingsDelegatesCreateInput) -> SettingsDelegatesCreateOutput:
        """Adds a delegate with its verification status set directly to `accepted`, without sending any verification email. The delegate user must be a member of the same Google Workspace organization as the delegator user. Gmail imposes limitations on the number of delegates and delegators each user in a Google Workspace organization can have. These limits depend on your organization, but in general each user can have up to 25 delegates and up to 10 delegators. Note that a delegate user must be referred to by their primary email address, and not an email alias. Also note that when a new delegate is created, there may be up to a one minute delay before the new delegate is available for use. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_delegates_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsDelegatesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_delegates_delete',
        title='SettingsDelegatesDelete',
        input_model=SettingsDelegatesDeleteInput,
        output_model=SettingsDelegatesDeleteOutput,
        tools_used=('gmail_users_settings_delegates_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: SettingsDelegatesDeleteInput) -> SettingsDelegatesDeleteOutput:
        """Removes the specified delegate (which can be of any verification status), and revokes any verification that may have been required for using it. Note that a delegate user must be referred to by their primary email address, and not an email alias. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, delegate_email"""
        tool = self._client.get_tool('gmail_users_settings_delegates_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsDelegatesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_delegates_get',
        title='SettingsDelegatesGet',
        input_model=SettingsDelegatesGetInput,
        output_model=SettingsDelegatesGetOutput,
        tools_used=('gmail_users_settings_delegates_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: SettingsDelegatesGetInput) -> SettingsDelegatesGetOutput:
        """Gets the specified delegate. Note that a delegate user must be referred to by their primary email address, and not an email alias. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, delegate_email"""
        tool = self._client.get_tool('gmail_users_settings_delegates_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsDelegatesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_delegates_list',
        title='SettingsDelegatesList',
        input_model=SettingsDelegatesListInput,
        output_model=SettingsDelegatesListOutput,
        tools_used=('gmail_users_settings_delegates_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: SettingsDelegatesListInput) -> SettingsDelegatesListOutput:
        """Lists the delegates for the specified account. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_settings_delegates_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsDelegatesListOutput.model_validate(coerce_tool_result(result))
