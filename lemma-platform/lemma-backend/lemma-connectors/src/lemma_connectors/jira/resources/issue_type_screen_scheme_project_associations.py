from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueTypeScreenSchemeProjectAssociationsToolInput, GetIssueTypeScreenSchemeProjectAssociationsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueTypeScreenSchemeProjectAssociationsInput(GetIssueTypeScreenSchemeProjectAssociationsToolInput):
    """Operation input for `get_issue_type_screen_scheme_project_associations`."""
    pass

class GetIssueTypeScreenSchemeProjectAssociationsOutput(GetIssueTypeScreenSchemeProjectAssociationsToolOutput):
    """Operation output for `get_issue_type_screen_scheme_project_associations`."""
    pass

class JiraIssueTypeScreenSchemeProjectAssociationsResource(BaseResourceClient):
    """Operations for the `issue_type_screen_scheme_project_associations` resource."""

    @operation(
        name='get_issue_type_screen_scheme_project_associations',
        title='GetIssueTypeScreenSchemeProjectAssociations',
        input_model=GetIssueTypeScreenSchemeProjectAssociationsInput,
        output_model=GetIssueTypeScreenSchemeProjectAssociationsOutput,
        tools_used=('get_issue_type_screen_scheme_project_associations',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def get(self, data: GetIssueTypeScreenSchemeProjectAssociationsInput) -> GetIssueTypeScreenSchemeProjectAssociationsOutput:
        """Returns a [paginated](#pagination) list of issue type screen schemes and, for each issue type screen scheme, a list of the projects that use it. Only issue type screen schemes used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, project_id"""
        tool = self._client.get_tool('get_issue_type_screen_scheme_project_associations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypeScreenSchemeProjectAssociationsOutput.model_validate(coerce_tool_result(result))
