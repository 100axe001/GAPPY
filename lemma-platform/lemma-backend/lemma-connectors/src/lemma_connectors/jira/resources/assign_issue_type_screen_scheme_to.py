from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AssignIssueTypeScreenSchemeToProjectToolInput, AssignIssueTypeScreenSchemeToProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AssignIssueTypeScreenSchemeToProjectInput(AssignIssueTypeScreenSchemeToProjectToolInput):
    """Operation input for `assign_issue_type_screen_scheme_to_project`."""
    pass

class AssignIssueTypeScreenSchemeToProjectOutput(AssignIssueTypeScreenSchemeToProjectToolOutput):
    """Operation output for `assign_issue_type_screen_scheme_to_project`."""
    pass

class JiraAssignIssueTypeScreenSchemeToResource(BaseResourceClient):
    """Operations for the `assign_issue_type_screen_scheme_to` resource."""

    @operation(
        name='assign_issue_type_screen_scheme_to_project',
        title='AssignIssueTypeScreenSchemeToProject',
        input_model=AssignIssueTypeScreenSchemeToProjectInput,
        output_model=AssignIssueTypeScreenSchemeToProjectOutput,
        tools_used=('assign_issue_type_screen_scheme_to_project',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def project(self, data: AssignIssueTypeScreenSchemeToProjectInput) -> AssignIssueTypeScreenSchemeToProjectOutput:
        """Assigns an issue type screen scheme to a project. Issue type screen schemes can only be assigned to classic projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('assign_issue_type_screen_scheme_to_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AssignIssueTypeScreenSchemeToProjectOutput.model_validate(coerce_tool_result(result))
