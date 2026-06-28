from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import RemoveIssueTypesFromContextToolInput, RemoveIssueTypesFromContextToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RemoveIssueTypesFromContextInput(RemoveIssueTypesFromContextToolInput):
    """Operation input for `remove_issue_types_from_context`."""
    pass

class RemoveIssueTypesFromContextOutput(RemoveIssueTypesFromContextToolOutput):
    """Operation output for `remove_issue_types_from_context`."""
    pass

class JiraIssueTypesFromContextResource(BaseResourceClient):
    """Operations for the `issue_types_from_context` resource."""

    @operation(
        name='remove_issue_types_from_context',
        title='RemoveIssueTypesFromContext',
        input_model=RemoveIssueTypesFromContextInput,
        output_model=RemoveIssueTypesFromContextOutput,
        tools_used=('remove_issue_types_from_context',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def remove(self, data: RemoveIssueTypesFromContextInput) -> RemoveIssueTypesFromContextOutput:
        """Removes issue types from a custom field context. A custom field context without any issue types applies to all issue types. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, body"""
        tool = self._client.get_tool('remove_issue_types_from_context')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveIssueTypesFromContextOutput.model_validate(coerce_tool_result(result))
