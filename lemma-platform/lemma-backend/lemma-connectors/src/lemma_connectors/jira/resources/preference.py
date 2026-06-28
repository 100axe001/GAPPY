from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetPreferenceToolInput, GetPreferenceToolOutput, RemovePreferenceToolInput, RemovePreferenceToolOutput, SetPreferenceToolInput, SetPreferenceToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetPreferenceInput(GetPreferenceToolInput):
    """Operation input for `get_preference`."""
    pass

class GetPreferenceOutput(GetPreferenceToolOutput):
    """Operation output for `get_preference`."""
    pass

class RemovePreferenceInput(RemovePreferenceToolInput):
    """Operation input for `remove_preference`."""
    pass

class RemovePreferenceOutput(RemovePreferenceToolOutput):
    """Operation output for `remove_preference`."""
    pass

class SetPreferenceInput(SetPreferenceToolInput):
    """Operation input for `set_preference`."""
    pass

class SetPreferenceOutput(SetPreferenceToolOutput):
    """Operation output for `set_preference`."""
    pass

class JiraPreferenceResource(BaseResourceClient):
    """Operations for the `preference` resource."""

    @operation(
        name='get_preference',
        title='GetPreference',
        input_model=GetPreferenceInput,
        output_model=GetPreferenceOutput,
        tools_used=('get_preference',),
        tags=tuple(['Myself']),
    )
    async def get(self, data: GetPreferenceInput) -> GetPreferenceOutput:
        """Returns the value of a preference of the current user. Note that these keys are deprecated: * *jira.user.locale* The locale of the user. By default this is not set and the user takes the locale of the instance. * *jira.user.timezone* The time zone of the user. By default this is not set and the user takes the timezone of the instance. Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_preference')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetPreferenceOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='remove_preference',
        title='RemovePreference',
        input_model=RemovePreferenceInput,
        output_model=RemovePreferenceOutput,
        tools_used=('remove_preference',),
        tags=tuple(['Myself']),
    )
    async def remove(self, data: RemovePreferenceInput) -> RemovePreferenceOutput:
        """Deletes a preference of the user, which restores the default value of system defined settings. Note that these keys are deprecated: * *jira.user.locale* The locale of the user. By default, not set. The user takes the instance locale. * *jira.user.timezone* The time zone of the user. By default, not set. The user takes the instance timezone. Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('remove_preference')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemovePreferenceOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_preference',
        title='SetPreference',
        input_model=SetPreferenceInput,
        output_model=SetPreferenceOutput,
        tools_used=('set_preference',),
        tags=tuple(['Myself']),
    )
    async def set(self, data: SetPreferenceInput) -> SetPreferenceOutput:
        """Creates a preference for the user or updates a preference's value by sending a plain text string. For example, `false`. An arbitrary preference can be created with the value containing up to 255 characters. In addition, the following keys define system preferences that can be set or created: * *user.notifications.mimetype* The mime type used in notifications sent to the user. Defaults to `html`. * *user.notify.own.changes* Whether the user gets notified of their own changes. Defaults to `false`. * *user.default.share.private* Whether new [ filters](https://confluence.atlassian.com/x/eQiiLQ) are set to private. Defaults to `true`. * *user.keyboard.shortcuts.disabled* Whether keyboard shortcuts are disabled. Defaults to `false`. * *user.autowatch.disabled* Whether the user automatically watches issues they create or add a comment to. By default, not set: the user takes the instance autowatch setting. Note that these keys are deprecated: * *jira.user.locale* The locale of the user. By default, not set. The user takes the instance locale. * *jira.user.timezone* The time zone of the user. By default, not set. The user takes the instance timezone. Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: body"""
        tool = self._client.get_tool('set_preference')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetPreferenceOutput.model_validate(coerce_tool_result(result))
