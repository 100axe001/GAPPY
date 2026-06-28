from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueTypesForProjectToolInput, GetIssueTypesForProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueTypesForProjectInput(GetIssueTypesForProjectToolInput):
    """Operation input for `get_issue_types_for_project`."""
    pass

class GetIssueTypesForProjectOutput(GetIssueTypesForProjectToolOutput):
    """Operation output for `get_issue_types_for_project`."""
    pass

class JiraIssueTypesForProjectResource(BaseResourceClient):
    """Operations for the `issue_types_for_project` resource."""

    @operation(
        name='get_issue_types_for_project',
        title='GetIssueTypesForProject',
        input_model=GetIssueTypesForProjectInput,
        output_model=GetIssueTypesForProjectOutput,
        tools_used=('get_issue_types_for_project',),
        tags=tuple(['Issue types']),
    )
    async def get(self, data: GetIssueTypesForProjectInput) -> GetIssueTypesForProjectOutput:
        """Returns issue types for a project. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id, level"""
        tool = self._client.get_tool('get_issue_types_for_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypesForProjectOutput.model_validate(coerce_tool_result(result))
