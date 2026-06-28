from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import RemoveIssueTypeFromIssueTypeSchemeToolInput, RemoveIssueTypeFromIssueTypeSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RemoveIssueTypeFromIssueTypeSchemeInput(RemoveIssueTypeFromIssueTypeSchemeToolInput):
    """Operation input for `remove_issue_type_from_issue_type_scheme`."""
    pass

class RemoveIssueTypeFromIssueTypeSchemeOutput(RemoveIssueTypeFromIssueTypeSchemeToolOutput):
    """Operation output for `remove_issue_type_from_issue_type_scheme`."""
    pass

class JiraIssueTypeFromIssueTypeSchemeResource(BaseResourceClient):
    """Operations for the `issue_type_from_issue_type_scheme` resource."""

    @operation(
        name='remove_issue_type_from_issue_type_scheme',
        title='RemoveIssueTypeFromIssueTypeScheme',
        input_model=RemoveIssueTypeFromIssueTypeSchemeInput,
        output_model=RemoveIssueTypeFromIssueTypeSchemeOutput,
        tools_used=('remove_issue_type_from_issue_type_scheme',),
        tags=tuple(['Issue type schemes']),
    )
    async def remove(self, data: RemoveIssueTypeFromIssueTypeSchemeInput) -> RemoveIssueTypeFromIssueTypeSchemeOutput:
        """Removes an issue type from an issue type scheme. This operation cannot remove: * any issue type used by issues. * any issue types from the default issue type scheme. * the last standard issue type from an issue type scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_scheme_id, issue_type_id"""
        tool = self._client.get_tool('remove_issue_type_from_issue_type_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveIssueTypeFromIssueTypeSchemeOutput.model_validate(coerce_tool_result(result))
