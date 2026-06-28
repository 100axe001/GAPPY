from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsDelegatesCreateToolInput, GmailUsersSettingsDelegatesCreateToolOutput, GmailUsersSettingsDelegatesDeleteToolInput, GmailUsersSettingsDelegatesDeleteToolOutput, GmailUsersSettingsDelegatesGetToolInput, GmailUsersSettingsDelegatesGetToolOutput, GmailUsersSettingsDelegatesListToolInput, GmailUsersSettingsDelegatesListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersSettingsDelegatesCreateInput(GmailUsersSettingsDelegatesCreateToolInput):
    """Operation input for `users_settings_delegates_create`."""
    pass

class UsersSettingsDelegatesCreateOutput(GmailUsersSettingsDelegatesCreateToolOutput):
    """Operation output for `users_settings_delegates_create`."""
    pass

class UsersSettingsDelegatesDeleteInput(GmailUsersSettingsDelegatesDeleteToolInput):
    """Operation input for `users_settings_delegates_delete`."""
    pass

class UsersSettingsDelegatesDeleteOutput(GmailUsersSettingsDelegatesDeleteToolOutput):
    """Operation output for `users_settings_delegates_delete`."""
    pass

class UsersSettingsDelegatesGetInput(GmailUsersSettingsDelegatesGetToolInput):
    """Operation input for `users_settings_delegates_get`."""
    pass

class UsersSettingsDelegatesGetOutput(GmailUsersSettingsDelegatesGetToolOutput):
    """Operation output for `users_settings_delegates_get`."""
    pass

class UsersSettingsDelegatesListInput(GmailUsersSettingsDelegatesListToolInput):
    """Operation input for `users_settings_delegates_list`."""
    pass

class UsersSettingsDelegatesListOutput(GmailUsersSettingsDelegatesListToolOutput):
    """Operation output for `users_settings_delegates_list`."""
    pass

class GmailUsersSettingsDelegatesResource(BaseResourceClient):
    """Operations grouped around the `users_settings_delegates` resource."""

    @operation(
        name='users_settings_delegates_create',
        title='UsersSettingsDelegatesCreate',
        input_model=UsersSettingsDelegatesCreateInput,
        output_model=UsersSettingsDelegatesCreateOutput,
        tools_used=('gmail_users_settings_delegates_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: UsersSettingsDelegatesCreateInput) -> UsersSettingsDelegatesCreateOutput:
        """Adds a delegate with its verification status set directly to `accepted`, without sending any verification email. The delegate user must be a member of the same Google Workspace organization as the delegator user. Gmail imposes limitations on the number of delegates and delegators each user in a Google Workspace organization can have. These limits depend on your organization, but in general each user can have up to 25 delegates and up to 10 delegators. Note that a delegate user must be referred to by their primary email address, and not an email alias. Also note that when a new delegate is created, there may be up to a one minute delay before the new delegate is available for use. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to adds a delegate with its verification status set directly to `accepted`, without sending any verification email. The delegate user must be a member of the same Google Workspace organization as the delegator user. Gmail imposes limitations on the number of delegates and delegators each user in a Google Workspace organization can have. These limits depend on your organization, but in general each user can have up to 25 delegates and up to 10 delegators. Note that a delegate user must be referred to by their primary email address, and not an email alias. Also note that when a new delegate is created, there may be up to a one minute delay before the new delegate is available for use. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_delegates_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsDelegatesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_delegates_delete',
        title='UsersSettingsDelegatesDelete',
        input_model=UsersSettingsDelegatesDeleteInput,
        output_model=UsersSettingsDelegatesDeleteOutput,
        tools_used=('gmail_users_settings_delegates_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersSettingsDelegatesDeleteInput) -> UsersSettingsDelegatesDeleteOutput:
        """Removes the specified delegate (which can be of any verification status), and revokes any verification that may have been required for using it. Note that a delegate user must be referred to by their primary email address, and not an email alias. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to removes the specified delegate (which can be of any verification status), and revokes any verification that may have been required for using it. Note that a delegate user must be referred to by their primary email address, and not an email alias. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, delegate_email."""
        tool = self._client.get_tool('gmail_users_settings_delegates_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsDelegatesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_delegates_get',
        title='UsersSettingsDelegatesGet',
        input_model=UsersSettingsDelegatesGetInput,
        output_model=UsersSettingsDelegatesGetOutput,
        tools_used=('gmail_users_settings_delegates_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersSettingsDelegatesGetInput) -> UsersSettingsDelegatesGetOutput:
        """Gets the specified delegate. Note that a delegate user must be referred to by their primary email address, and not an email alias. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to gets the specified delegate. Note that a delegate user must be referred to by their primary email address, and not an email alias. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, delegate_email."""
        tool = self._client.get_tool('gmail_users_settings_delegates_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsDelegatesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_delegates_list',
        title='UsersSettingsDelegatesList',
        input_model=UsersSettingsDelegatesListInput,
        output_model=UsersSettingsDelegatesListOutput,
        tools_used=('gmail_users_settings_delegates_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersSettingsDelegatesListInput) -> UsersSettingsDelegatesListOutput:
        """Lists the delegates for the specified account. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to lists the delegates for the specified account. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_settings_delegates_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsDelegatesListOutput.model_validate(coerce_tool_result(result))
