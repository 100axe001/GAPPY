from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetCustomFieldContextsForProjectsAndIssueTypesToolInput, GetCustomFieldContextsForProjectsAndIssueTypesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetCustomFieldContextsForProjectsAndIssueTypesInput(GetCustomFieldContextsForProjectsAndIssueTypesToolInput):
    """Operation input for `get_custom_field_contexts_for_projects_and_issue_types`."""
    pass

class GetCustomFieldContextsForProjectsAndIssueTypesOutput(GetCustomFieldContextsForProjectsAndIssueTypesToolOutput):
    """Operation output for `get_custom_field_contexts_for_projects_and_issue_types`."""
    pass

class JiraCustomFieldContextsForProjectsAndIssueTypesResource(BaseResourceClient):
    """Operations for the `custom_field_contexts_for_projects_and_issue_types` resource."""

    @operation(
        name='get_custom_field_contexts_for_projects_and_issue_types',
        title='GetCustomFieldContextsForProjectsAndIssueTypes',
        input_model=GetCustomFieldContextsForProjectsAndIssueTypesInput,
        output_model=GetCustomFieldContextsForProjectsAndIssueTypesOutput,
        tools_used=('get_custom_field_contexts_for_projects_and_issue_types',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def get(self, data: GetCustomFieldContextsForProjectsAndIssueTypesInput) -> GetCustomFieldContextsForProjectsAndIssueTypesOutput:
        """Returns a [paginated](#pagination) list of project and issue type mappings and, for each mapping, the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the project and issue type. If there is no custom field context assigned to the project then, if present, the custom field context that applies to all projects is returned if it also applies to the issue type or all issue types. If a custom field context is not found, the returned custom field context ID is `null`. Duplicate project and issue type mappings cannot be provided in the request. The order of the returned values is the same as provided in the request. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, start_at, max_results, body"""
        tool = self._client.get_tool('get_custom_field_contexts_for_projects_and_issue_types')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCustomFieldContextsForProjectsAndIssueTypesOutput.model_validate(coerce_tool_result(result))
