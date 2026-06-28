from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetNotificationSchemeToProjectMappingsToolInput, GetNotificationSchemeToProjectMappingsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetNotificationSchemeToProjectMappingsInput(GetNotificationSchemeToProjectMappingsToolInput):
    """Operation input for `get_notification_scheme_to_project_mappings`."""
    pass

class GetNotificationSchemeToProjectMappingsOutput(GetNotificationSchemeToProjectMappingsToolOutput):
    """Operation output for `get_notification_scheme_to_project_mappings`."""
    pass

class JiraNotificationSchemeToProjectMappingsResource(BaseResourceClient):
    """Operations for the `notification_scheme_to_project_mappings` resource."""

    @operation(
        name='get_notification_scheme_to_project_mappings',
        title='GetNotificationSchemeToProjectMappings',
        input_model=GetNotificationSchemeToProjectMappingsInput,
        output_model=GetNotificationSchemeToProjectMappingsOutput,
        tools_used=('get_notification_scheme_to_project_mappings',),
        tags=tuple(['Issue notification schemes']),
    )
    async def get(self, data: GetNotificationSchemeToProjectMappingsInput) -> GetNotificationSchemeToProjectMappingsOutput:
        """Returns a [paginated](#pagination) mapping of project that have notification scheme assigned. You can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Note that only company-managed (classic) projects are supported. This is because team-managed projects don't have a concept of a default notification scheme. The mappings are ordered by projectId. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: start_at, max_results, notification_scheme_id, project_id"""
        tool = self._client.get_tool('get_notification_scheme_to_project_mappings')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetNotificationSchemeToProjectMappingsOutput.model_validate(coerce_tool_result(result))
