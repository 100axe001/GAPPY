from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ReorderIssueTypesInIssueTypeSchemeToolInput, ReorderIssueTypesInIssueTypeSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ReorderIssueTypesInIssueTypeSchemeInput(ReorderIssueTypesInIssueTypeSchemeToolInput):
    """Operation input for `reorder_issue_types_in_issue_type_scheme`."""
    pass

class ReorderIssueTypesInIssueTypeSchemeOutput(ReorderIssueTypesInIssueTypeSchemeToolOutput):
    """Operation output for `reorder_issue_types_in_issue_type_scheme`."""
    pass

class JiraReorderIssueTypesInIssueTypeResource(BaseResourceClient):
    """Operations for the `reorder_issue_types_in_issue_type` resource."""

    @operation(
        name='reorder_issue_types_in_issue_type_scheme',
        title='ReorderIssueTypesInIssueTypeScheme',
        input_model=ReorderIssueTypesInIssueTypeSchemeInput,
        output_model=ReorderIssueTypesInIssueTypeSchemeOutput,
        tools_used=('reorder_issue_types_in_issue_type_scheme',),
        tags=tuple(['Issue type schemes']),
    )
    async def scheme(self, data: ReorderIssueTypesInIssueTypeSchemeInput) -> ReorderIssueTypesInIssueTypeSchemeOutput:
        """Changes the order of issue types in an issue type scheme. The request body parameters must meet the following requirements: * all of the issue types must belong to the issue type scheme. * either `after` or `position` must be provided. * the issue type in `after` must not be in the issue type list. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_scheme_id, body"""
        tool = self._client.get_tool('reorder_issue_types_in_issue_type_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ReorderIssueTypesInIssueTypeSchemeOutput.model_validate(coerce_tool_result(result))
