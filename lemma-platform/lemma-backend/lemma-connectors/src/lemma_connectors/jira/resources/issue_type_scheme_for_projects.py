from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueTypeSchemeForProjectsToolInput, GetIssueTypeSchemeForProjectsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueTypeSchemeForProjectsInput(GetIssueTypeSchemeForProjectsToolInput):
    """Operation input for `get_issue_type_scheme_for_projects`."""
    pass

class GetIssueTypeSchemeForProjectsOutput(GetIssueTypeSchemeForProjectsToolOutput):
    """Operation output for `get_issue_type_scheme_for_projects`."""
    pass

class JiraIssueTypeSchemeForProjectsResource(BaseResourceClient):
    """Operations for the `issue_type_scheme_for_projects` resource."""

    @operation(
        name='get_issue_type_scheme_for_projects',
        title='GetIssueTypeSchemeForProjects',
        input_model=GetIssueTypeSchemeForProjectsInput,
        output_model=GetIssueTypeSchemeForProjectsOutput,
        tools_used=('get_issue_type_scheme_for_projects',),
        tags=tuple(['Issue type schemes']),
    )
    async def get(self, data: GetIssueTypeSchemeForProjectsInput) -> GetIssueTypeSchemeForProjectsOutput:
        """Returns a [paginated](#pagination) list of issue type schemes and, for each issue type scheme, a list of the projects that use it. Only issue type schemes used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, project_id"""
        tool = self._client.get_tool('get_issue_type_scheme_for_projects')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypeSchemeForProjectsOutput.model_validate(coerce_tool_result(result))
