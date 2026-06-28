from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectsForIssueTypeScreenSchemeToolInput, GetProjectsForIssueTypeScreenSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectsForIssueTypeScreenSchemeInput(GetProjectsForIssueTypeScreenSchemeToolInput):
    """Operation input for `get_projects_for_issue_type_screen_scheme`."""
    pass

class GetProjectsForIssueTypeScreenSchemeOutput(GetProjectsForIssueTypeScreenSchemeToolOutput):
    """Operation output for `get_projects_for_issue_type_screen_scheme`."""
    pass

class JiraProjectsForIssueTypeScreenSchemeResource(BaseResourceClient):
    """Operations for the `projects_for_issue_type_screen_scheme` resource."""

    @operation(
        name='get_projects_for_issue_type_screen_scheme',
        title='GetProjectsForIssueTypeScreenScheme',
        input_model=GetProjectsForIssueTypeScreenSchemeInput,
        output_model=GetProjectsForIssueTypeScreenSchemeOutput,
        tools_used=('get_projects_for_issue_type_screen_scheme',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def get(self, data: GetProjectsForIssueTypeScreenSchemeInput) -> GetProjectsForIssueTypeScreenSchemeOutput:
        """Returns a [paginated](#pagination) list of projects associated with an issue type screen scheme. Only company-managed projects associated with an issue type screen scheme are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_screen_scheme_id, start_at, max_results, query"""
        tool = self._client.get_tool('get_projects_for_issue_type_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectsForIssueTypeScreenSchemeOutput.model_validate(coerce_tool_result(result))
