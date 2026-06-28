from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsFiltersCreateToolInput, GmailUsersSettingsFiltersCreateToolOutput, GmailUsersSettingsFiltersDeleteToolInput, GmailUsersSettingsFiltersDeleteToolOutput, GmailUsersSettingsFiltersGetToolInput, GmailUsersSettingsFiltersGetToolOutput, GmailUsersSettingsFiltersListToolInput, GmailUsersSettingsFiltersListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersSettingsFiltersCreateInput(GmailUsersSettingsFiltersCreateToolInput):
    """Operation input for `users_settings_filters_create`."""
    pass

class UsersSettingsFiltersCreateOutput(GmailUsersSettingsFiltersCreateToolOutput):
    """Operation output for `users_settings_filters_create`."""
    pass

class UsersSettingsFiltersDeleteInput(GmailUsersSettingsFiltersDeleteToolInput):
    """Operation input for `users_settings_filters_delete`."""
    pass

class UsersSettingsFiltersDeleteOutput(GmailUsersSettingsFiltersDeleteToolOutput):
    """Operation output for `users_settings_filters_delete`."""
    pass

class UsersSettingsFiltersGetInput(GmailUsersSettingsFiltersGetToolInput):
    """Operation input for `users_settings_filters_get`."""
    pass

class UsersSettingsFiltersGetOutput(GmailUsersSettingsFiltersGetToolOutput):
    """Operation output for `users_settings_filters_get`."""
    pass

class UsersSettingsFiltersListInput(GmailUsersSettingsFiltersListToolInput):
    """Operation input for `users_settings_filters_list`."""
    pass

class UsersSettingsFiltersListOutput(GmailUsersSettingsFiltersListToolOutput):
    """Operation output for `users_settings_filters_list`."""
    pass

class GmailUsersSettingsFiltersResource(BaseResourceClient):
    """Operations grouped around the `users_settings_filters` resource."""

    @operation(
        name='users_settings_filters_create',
        title='UsersSettingsFiltersCreate',
        input_model=UsersSettingsFiltersCreateInput,
        output_model=UsersSettingsFiltersCreateOutput,
        tools_used=('gmail_users_settings_filters_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: UsersSettingsFiltersCreateInput) -> UsersSettingsFiltersCreateOutput:
        """Creates a filter. Note: you can only create a maximum of 1,000 filters.

Use this when you want to creates a filter. Note: you can only create a maximum of 1,000 filters.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_filters_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsFiltersCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_filters_delete',
        title='UsersSettingsFiltersDelete',
        input_model=UsersSettingsFiltersDeleteInput,
        output_model=UsersSettingsFiltersDeleteOutput,
        tools_used=('gmail_users_settings_filters_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersSettingsFiltersDeleteInput) -> UsersSettingsFiltersDeleteOutput:
        """Immediately and permanently deletes the specified filter.

Use this when you want to immediately and permanently deletes the specified filter.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_settings_filters_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsFiltersDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_filters_get',
        title='UsersSettingsFiltersGet',
        input_model=UsersSettingsFiltersGetInput,
        output_model=UsersSettingsFiltersGetOutput,
        tools_used=('gmail_users_settings_filters_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersSettingsFiltersGetInput) -> UsersSettingsFiltersGetOutput:
        """Gets a filter.

Use this when you want to gets a filter.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_settings_filters_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsFiltersGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_filters_list',
        title='UsersSettingsFiltersList',
        input_model=UsersSettingsFiltersListInput,
        output_model=UsersSettingsFiltersListOutput,
        tools_used=('gmail_users_settings_filters_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersSettingsFiltersListInput) -> UsersSettingsFiltersListOutput:
        """Lists the message filters of a Gmail user.

Use this when you want to lists the message filters of a Gmail user.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_settings_filters_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsFiltersListOutput.model_validate(coerce_tool_result(result))
