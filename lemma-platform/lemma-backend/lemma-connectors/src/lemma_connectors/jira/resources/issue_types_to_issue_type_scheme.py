from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddIssueTypesToIssueTypeSchemeToolInput, AddIssueTypesToIssueTypeSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddIssueTypesToIssueTypeSchemeInput(AddIssueTypesToIssueTypeSchemeToolInput):
    """Operation input for `add_issue_types_to_issue_type_scheme`."""
    pass

class AddIssueTypesToIssueTypeSchemeOutput(AddIssueTypesToIssueTypeSchemeToolOutput):
    """Operation output for `add_issue_types_to_issue_type_scheme`."""
    pass

class JiraIssueTypesToIssueTypeSchemeResource(BaseResourceClient):
    """Operations for the `issue_types_to_issue_type_scheme` resource."""

    @operation(
        name='add_issue_types_to_issue_type_scheme',
        title='AddIssueTypesToIssueTypeScheme',
        input_model=AddIssueTypesToIssueTypeSchemeInput,
        output_model=AddIssueTypesToIssueTypeSchemeOutput,
        tools_used=('add_issue_types_to_issue_type_scheme',),
        tags=tuple(['Issue type schemes']),
    )
    async def add(self, data: AddIssueTypesToIssueTypeSchemeInput) -> AddIssueTypesToIssueTypeSchemeOutput:
        """Adds issue types to an issue type scheme. The added issue types are appended to the issue types list. If any of the issue types exist in the issue type scheme, the operation fails and no issue types are added. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_scheme_id, body"""
        tool = self._client.get_tool('add_issue_types_to_issue_type_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddIssueTypesToIssueTypeSchemeOutput.model_validate(coerce_tool_result(result))
