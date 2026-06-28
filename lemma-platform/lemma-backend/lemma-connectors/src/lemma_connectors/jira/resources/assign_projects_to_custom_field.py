from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AssignProjectsToCustomFieldContextToolInput, AssignProjectsToCustomFieldContextToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AssignProjectsToCustomFieldContextInput(AssignProjectsToCustomFieldContextToolInput):
    """Operation input for `assign_projects_to_custom_field_context`."""
    pass

class AssignProjectsToCustomFieldContextOutput(AssignProjectsToCustomFieldContextToolOutput):
    """Operation output for `assign_projects_to_custom_field_context`."""
    pass

class JiraAssignProjectsToCustomFieldResource(BaseResourceClient):
    """Operations for the `assign_projects_to_custom_field` resource."""

    @operation(
        name='assign_projects_to_custom_field_context',
        title='AssignProjectsToCustomFieldContext',
        input_model=AssignProjectsToCustomFieldContextInput,
        output_model=AssignProjectsToCustomFieldContextOutput,
        tools_used=('assign_projects_to_custom_field_context',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def context(self, data: AssignProjectsToCustomFieldContextInput) -> AssignProjectsToCustomFieldContextOutput:
        """Assigns a custom field context to projects. If any project in the request is assigned to any context of the custom field, the operation fails. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, body"""
        tool = self._client.get_tool('assign_projects_to_custom_field_context')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AssignProjectsToCustomFieldContextOutput.model_validate(coerce_tool_result(result))
