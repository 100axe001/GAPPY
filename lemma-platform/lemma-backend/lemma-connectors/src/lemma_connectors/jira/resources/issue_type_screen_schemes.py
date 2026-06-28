from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueTypeScreenSchemesToolInput, GetIssueTypeScreenSchemesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueTypeScreenSchemesInput(GetIssueTypeScreenSchemesToolInput):
    """Operation input for `get_issue_type_screen_schemes`."""
    pass

class GetIssueTypeScreenSchemesOutput(GetIssueTypeScreenSchemesToolOutput):
    """Operation output for `get_issue_type_screen_schemes`."""
    pass

class JiraIssueTypeScreenSchemesResource(BaseResourceClient):
    """Operations for the `issue_type_screen_schemes` resource."""

    @operation(
        name='get_issue_type_screen_schemes',
        title='GetIssueTypeScreenSchemes',
        input_model=GetIssueTypeScreenSchemesInput,
        output_model=GetIssueTypeScreenSchemesOutput,
        tools_used=('get_issue_type_screen_schemes',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def get(self, data: GetIssueTypeScreenSchemesInput) -> GetIssueTypeScreenSchemesOutput:
        """Returns a [paginated](#pagination) list of issue type screen schemes. Only issue type screen schemes used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, id, query_string, order_by, expand"""
        tool = self._client.get_tool('get_issue_type_screen_schemes')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypeScreenSchemesOutput.model_validate(coerce_tool_result(result))
