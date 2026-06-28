from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetNotificationSchemeForProjectToolInput, GetNotificationSchemeForProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetNotificationSchemeForProjectInput(GetNotificationSchemeForProjectToolInput):
    """Operation input for `get_notification_scheme_for_project`."""
    pass

class GetNotificationSchemeForProjectOutput(GetNotificationSchemeForProjectToolOutput):
    """Operation output for `get_notification_scheme_for_project`."""
    pass

class JiraNotificationSchemeForProjectResource(BaseResourceClient):
    """Operations for the `notification_scheme_for_project` resource."""

    @operation(
        name='get_notification_scheme_for_project',
        title='GetNotificationSchemeForProject',
        input_model=GetNotificationSchemeForProjectInput,
        output_model=GetNotificationSchemeForProjectOutput,
        tools_used=('get_notification_scheme_for_project',),
        tags=tuple(['Projects']),
    )
    async def get(self, data: GetNotificationSchemeForProjectInput) -> GetNotificationSchemeForProjectOutput:
        """Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project. Deprecated, use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get) supporting search and pagination. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

Important inputs: project_key_or_id, expand"""
        tool = self._client.get_tool('get_notification_scheme_for_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetNotificationSchemeForProjectOutput.model_validate(coerce_tool_result(result))
