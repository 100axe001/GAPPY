from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueTypeScreenSchemeMappingsToolInput, GetIssueTypeScreenSchemeMappingsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueTypeScreenSchemeMappingsInput(GetIssueTypeScreenSchemeMappingsToolInput):
    """Operation input for `get_issue_type_screen_scheme_mappings`."""
    pass

class GetIssueTypeScreenSchemeMappingsOutput(GetIssueTypeScreenSchemeMappingsToolOutput):
    """Operation output for `get_issue_type_screen_scheme_mappings`."""
    pass

class JiraIssueTypeScreenSchemeMappingsResource(BaseResourceClient):
    """Operations for the `issue_type_screen_scheme_mappings` resource."""

    @operation(
        name='get_issue_type_screen_scheme_mappings',
        title='GetIssueTypeScreenSchemeMappings',
        input_model=GetIssueTypeScreenSchemeMappingsInput,
        output_model=GetIssueTypeScreenSchemeMappingsOutput,
        tools_used=('get_issue_type_screen_scheme_mappings',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def get(self, data: GetIssueTypeScreenSchemeMappingsInput) -> GetIssueTypeScreenSchemeMappingsOutput:
        """Returns a [paginated](#pagination) list of issue type screen scheme items. Only issue type screen schemes used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, issue_type_screen_scheme_id"""
        tool = self._client.get_tool('get_issue_type_screen_scheme_mappings')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypeScreenSchemeMappingsOutput.model_validate(coerce_tool_result(result))
