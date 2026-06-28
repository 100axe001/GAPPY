from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AssignIssueTypeSchemeToProjectToolInput, AssignIssueTypeSchemeToProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AssignIssueTypeSchemeToProjectInput(AssignIssueTypeSchemeToProjectToolInput):
    """Operation input for `assign_issue_type_scheme_to_project`."""
    pass

class AssignIssueTypeSchemeToProjectOutput(AssignIssueTypeSchemeToProjectToolOutput):
    """Operation output for `assign_issue_type_scheme_to_project`."""
    pass

class JiraAssignIssueTypeSchemeToResource(BaseResourceClient):
    """Operations for the `assign_issue_type_scheme_to` resource."""

    @operation(
        name='assign_issue_type_scheme_to_project',
        title='AssignIssueTypeSchemeToProject',
        input_model=AssignIssueTypeSchemeToProjectInput,
        output_model=AssignIssueTypeSchemeToProjectOutput,
        tools_used=('assign_issue_type_scheme_to_project',),
        tags=tuple(['Issue type schemes']),
    )
    async def project(self, data: AssignIssueTypeSchemeToProjectInput) -> AssignIssueTypeSchemeToProjectOutput:
        """Assigns an issue type scheme to a project. If any issues in the project are assigned issue types not present in the new scheme, the operation will fail. To complete the assignment those issues must be updated to use issue types in the new scheme. Issue type schemes can only be assigned to classic projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('assign_issue_type_scheme_to_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AssignIssueTypeSchemeToProjectOutput.model_validate(coerce_tool_result(result))
