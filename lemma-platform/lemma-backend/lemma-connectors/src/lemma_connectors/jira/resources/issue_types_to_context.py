from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddIssueTypesToContextToolInput, AddIssueTypesToContextToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddIssueTypesToContextInput(AddIssueTypesToContextToolInput):
    """Operation input for `add_issue_types_to_context`."""
    pass

class AddIssueTypesToContextOutput(AddIssueTypesToContextToolOutput):
    """Operation output for `add_issue_types_to_context`."""
    pass

class JiraIssueTypesToContextResource(BaseResourceClient):
    """Operations for the `issue_types_to_context` resource."""

    @operation(
        name='add_issue_types_to_context',
        title='AddIssueTypesToContext',
        input_model=AddIssueTypesToContextInput,
        output_model=AddIssueTypesToContextOutput,
        tools_used=('add_issue_types_to_context',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def add(self, data: AddIssueTypesToContextInput) -> AddIssueTypesToContextOutput:
        """Adds issue types to a custom field context, appending the issue types to the issue types list. A custom field context without any issue types applies to all issue types. Adding issue types to such a custom field context would result in it applying to only the listed issue types. If any of the issue types exists in the custom field context, the operation fails and no issue types are added. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, body"""
        tool = self._client.get_tool('add_issue_types_to_context')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddIssueTypesToContextOutput.model_validate(coerce_tool_result(result))
