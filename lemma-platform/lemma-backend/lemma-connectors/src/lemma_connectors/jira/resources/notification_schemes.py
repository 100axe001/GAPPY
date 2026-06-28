from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetNotificationSchemesToolInput, GetNotificationSchemesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetNotificationSchemesInput(GetNotificationSchemesToolInput):
    """Operation input for `get_notification_schemes`."""
    pass

class GetNotificationSchemesOutput(GetNotificationSchemesToolOutput):
    """Operation output for `get_notification_schemes`."""
    pass

class JiraNotificationSchemesResource(BaseResourceClient):
    """Operations for the `notification_schemes` resource."""

    @operation(
        name='get_notification_schemes',
        title='GetNotificationSchemes',
        input_model=GetNotificationSchemesInput,
        output_model=GetNotificationSchemesOutput,
        tools_used=('get_notification_schemes',),
        tags=tuple(['Issue notification schemes']),
    )
    async def get(self, data: GetNotificationSchemesInput) -> GetNotificationSchemesOutput:
        """Returns a [paginated](#pagination) list of [notification schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name. *Note that you should allow for events without recipients to appear in responses.* **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with a notification scheme for it to be returned.

Important inputs: start_at, max_results, id, project_id, only_default, expand"""
        tool = self._client.get_tool('get_notification_schemes')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetNotificationSchemesOutput.model_validate(coerce_tool_result(result))
