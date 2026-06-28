from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import RemoveCustomFieldContextFromProjectsToolInput, RemoveCustomFieldContextFromProjectsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RemoveCustomFieldContextFromProjectsInput(RemoveCustomFieldContextFromProjectsToolInput):
    """Operation input for `remove_custom_field_context_from_projects`."""
    pass

class RemoveCustomFieldContextFromProjectsOutput(RemoveCustomFieldContextFromProjectsToolOutput):
    """Operation output for `remove_custom_field_context_from_projects`."""
    pass

class JiraCustomFieldContextFromProjectsResource(BaseResourceClient):
    """Operations for the `custom_field_context_from_projects` resource."""

    @operation(
        name='remove_custom_field_context_from_projects',
        title='RemoveCustomFieldContextFromProjects',
        input_model=RemoveCustomFieldContextFromProjectsInput,
        output_model=RemoveCustomFieldContextFromProjectsOutput,
        tools_used=('remove_custom_field_context_from_projects',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def remove(self, data: RemoveCustomFieldContextFromProjectsInput) -> RemoveCustomFieldContextFromProjectsOutput:
        """Removes a custom field context from projects. A custom field context without any projects applies to all projects. Removing all projects from a custom field context would result in it applying to all projects. If any project in the request is not assigned to the context, or the operation would result in two global contexts for the field, the operation fails. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, body"""
        tool = self._client.get_tool('remove_custom_field_context_from_projects')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveCustomFieldContextFromProjectsOutput.model_validate(coerce_tool_result(result))
