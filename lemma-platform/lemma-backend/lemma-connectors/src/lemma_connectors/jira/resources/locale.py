from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteLocaleToolInput, DeleteLocaleToolOutput, GetLocaleToolInput, GetLocaleToolOutput, SetLocaleToolInput, SetLocaleToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteLocaleInput(DeleteLocaleToolInput):
    """Operation input for `delete_locale`."""
    pass

class DeleteLocaleOutput(DeleteLocaleToolOutput):
    """Operation output for `delete_locale`."""
    pass

class GetLocaleInput(GetLocaleToolInput):
    """Operation input for `get_locale`."""
    pass

class GetLocaleOutput(GetLocaleToolOutput):
    """Operation output for `get_locale`."""
    pass

class SetLocaleInput(SetLocaleToolInput):
    """Operation input for `set_locale`."""
    pass

class SetLocaleOutput(SetLocaleToolOutput):
    """Operation output for `set_locale`."""
    pass

class JiraLocaleResource(BaseResourceClient):
    """Operations for the `locale` resource."""

    @operation(
        name='delete_locale',
        title='DeleteLocale',
        input_model=DeleteLocaleInput,
        output_model=DeleteLocaleOutput,
        tools_used=('delete_locale',),
        tags=tuple(['Myself']),
    )
    async def delete(self, data: DeleteLocaleInput) -> DeleteLocaleOutput:
        """Deprecated, use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API instead. Deletes the locale of the user, which restores the default setting. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('delete_locale')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteLocaleOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_locale',
        title='GetLocale',
        input_model=GetLocaleInput,
        output_model=GetLocaleOutput,
        tools_used=('get_locale',),
        tags=tuple(['Myself']),
    )
    async def get(self, data: GetLocaleInput) -> GetLocaleOutput:
        """Returns the locale for the user. If the user has no language preference set (which is the default setting) or this resource is accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale using the *Accept-Language* header in the request. However, if this doesn't match a locale available Jira, the site default locale is returned. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_locale')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetLocaleOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_locale',
        title='SetLocale',
        input_model=SetLocaleInput,
        output_model=SetLocaleOutput,
        tools_used=('set_locale',),
        tags=tuple(['Myself']),
    )
    async def set(self, data: SetLocaleInput) -> SetLocaleOutput:
        """Deprecated, use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API instead. Sets the locale of the user. The locale must be one supported by the instance of Jira. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: body"""
        tool = self._client.get_tool('set_locale')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetLocaleOutput.model_validate(coerce_tool_result(result))
