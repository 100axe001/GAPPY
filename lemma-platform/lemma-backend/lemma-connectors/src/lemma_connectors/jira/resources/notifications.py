from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddNotificationsToolInput, AddNotificationsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddNotificationsInput(AddNotificationsToolInput):
    """Operation input for `add_notifications`."""
    pass

class AddNotificationsOutput(AddNotificationsToolOutput):
    """Operation output for `add_notifications`."""
    pass

class JiraNotificationsResource(BaseResourceClient):
    """Operations for the `notifications` resource."""

    @operation(
        name='add_notifications',
        title='AddNotifications',
        input_model=AddNotificationsInput,
        output_model=AddNotificationsOutput,
        tools_used=('add_notifications',),
        tags=tuple(['Issue notification schemes']),
    )
    async def add(self, data: AddNotificationsInput) -> AddNotificationsOutput:
        """Adds notifications to a notification scheme. You can add up to 1000 notifications per request. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('add_notifications')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddNotificationsOutput.model_validate(coerce_tool_result(result))
