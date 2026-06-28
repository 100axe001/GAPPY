from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateNotificationSchemeToolInput, CreateNotificationSchemeToolOutput, DeleteNotificationSchemeToolInput, DeleteNotificationSchemeToolOutput, GetNotificationSchemeToolInput, GetNotificationSchemeToolOutput, UpdateNotificationSchemeToolInput, UpdateNotificationSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateNotificationSchemeInput(CreateNotificationSchemeToolInput):
    """Operation input for `create_notification_scheme`."""
    pass

class CreateNotificationSchemeOutput(CreateNotificationSchemeToolOutput):
    """Operation output for `create_notification_scheme`."""
    pass

class DeleteNotificationSchemeInput(DeleteNotificationSchemeToolInput):
    """Operation input for `delete_notification_scheme`."""
    pass

class DeleteNotificationSchemeOutput(DeleteNotificationSchemeToolOutput):
    """Operation output for `delete_notification_scheme`."""
    pass

class GetNotificationSchemeInput(GetNotificationSchemeToolInput):
    """Operation input for `get_notification_scheme`."""
    pass

class GetNotificationSchemeOutput(GetNotificationSchemeToolOutput):
    """Operation output for `get_notification_scheme`."""
    pass

class UpdateNotificationSchemeInput(UpdateNotificationSchemeToolInput):
    """Operation input for `update_notification_scheme`."""
    pass

class UpdateNotificationSchemeOutput(UpdateNotificationSchemeToolOutput):
    """Operation output for `update_notification_scheme`."""
    pass

class JiraNotificationSchemeResource(BaseResourceClient):
    """Operations for the `notification_scheme` resource."""

    @operation(
        name='create_notification_scheme',
        title='CreateNotificationScheme',
        input_model=CreateNotificationSchemeInput,
        output_model=CreateNotificationSchemeOutput,
        tools_used=('create_notification_scheme',),
        tags=tuple(['Issue notification schemes']),
    )
    async def create(self, data: CreateNotificationSchemeInput) -> CreateNotificationSchemeOutput:
        """Creates a notification scheme with notifications. You can create up to 1000 notifications per request. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_notification_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateNotificationSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_notification_scheme',
        title='DeleteNotificationScheme',
        input_model=DeleteNotificationSchemeInput,
        output_model=DeleteNotificationSchemeOutput,
        tools_used=('delete_notification_scheme',),
        tags=tuple(['Issue notification schemes']),
    )
    async def delete(self, data: DeleteNotificationSchemeInput) -> DeleteNotificationSchemeOutput:
        """Deletes a notification scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: notification_scheme_id"""
        tool = self._client.get_tool('delete_notification_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteNotificationSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_notification_scheme',
        title='GetNotificationScheme',
        input_model=GetNotificationSchemeInput,
        output_model=GetNotificationSchemeOutput,
        tools_used=('get_notification_scheme',),
        tags=tuple(['Issue notification schemes']),
    )
    async def get(self, data: GetNotificationSchemeInput) -> GetNotificationSchemeOutput:
        """Returns a [notification scheme](https://confluence.atlassian.com/x/8YdKLg), including the list of events and the recipients who will receive notifications for those events. **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with the notification scheme.

Important inputs: id, expand"""
        tool = self._client.get_tool('get_notification_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetNotificationSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_notification_scheme',
        title='UpdateNotificationScheme',
        input_model=UpdateNotificationSchemeInput,
        output_model=UpdateNotificationSchemeOutput,
        tools_used=('update_notification_scheme',),
        tags=tuple(['Issue notification schemes']),
    )
    async def update(self, data: UpdateNotificationSchemeInput) -> UpdateNotificationSchemeOutput:
        """Updates a notification scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_notification_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateNotificationSchemeOutput.model_validate(coerce_tool_result(result))
