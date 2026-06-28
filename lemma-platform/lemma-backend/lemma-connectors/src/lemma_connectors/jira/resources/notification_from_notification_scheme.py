from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import RemoveNotificationFromNotificationSchemeToolInput, RemoveNotificationFromNotificationSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RemoveNotificationFromNotificationSchemeInput(RemoveNotificationFromNotificationSchemeToolInput):
    """Operation input for `remove_notification_from_notification_scheme`."""
    pass

class RemoveNotificationFromNotificationSchemeOutput(RemoveNotificationFromNotificationSchemeToolOutput):
    """Operation output for `remove_notification_from_notification_scheme`."""
    pass

class JiraNotificationFromNotificationSchemeResource(BaseResourceClient):
    """Operations for the `notification_from_notification_scheme` resource."""

    @operation(
        name='remove_notification_from_notification_scheme',
        title='RemoveNotificationFromNotificationScheme',
        input_model=RemoveNotificationFromNotificationSchemeInput,
        output_model=RemoveNotificationFromNotificationSchemeOutput,
        tools_used=('remove_notification_from_notification_scheme',),
        tags=tuple(['Issue notification schemes']),
    )
    async def remove(self, data: RemoveNotificationFromNotificationSchemeInput) -> RemoveNotificationFromNotificationSchemeOutput:
        """Removes a notification from a notification scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: notification_scheme_id, notification_id"""
        tool = self._client.get_tool('remove_notification_from_notification_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveNotificationFromNotificationSchemeOutput.model_validate(coerce_tool_result(result))
