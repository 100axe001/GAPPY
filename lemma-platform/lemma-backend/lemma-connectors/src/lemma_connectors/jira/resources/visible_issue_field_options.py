from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetVisibleIssueFieldOptionsToolInput, GetVisibleIssueFieldOptionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetVisibleIssueFieldOptionsInput(GetVisibleIssueFieldOptionsToolInput):
    """Operation input for `get_visible_issue_field_options`."""
    pass

class GetVisibleIssueFieldOptionsOutput(GetVisibleIssueFieldOptionsToolOutput):
    """Operation output for `get_visible_issue_field_options`."""
    pass

class JiraVisibleIssueFieldOptionsResource(BaseResourceClient):
    """Operations for the `visible_issue_field_options` resource."""

    @operation(
        name='get_visible_issue_field_options',
        title='GetVisibleIssueFieldOptions',
        input_model=GetVisibleIssueFieldOptionsInput,
        output_model=GetVisibleIssueFieldOptionsOutput,
        tools_used=('get_visible_issue_field_options',),
        tags=tuple(['Issue custom field options (apps)']),
    )
    async def get(self, data: GetVisibleIssueFieldOptionsInput) -> GetVisibleIssueFieldOptionsOutput:
        """Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed by the user. Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: start_at, max_results, project_id, field_key"""
        tool = self._client.get_tool('get_visible_issue_field_options')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetVisibleIssueFieldOptionsOutput.model_validate(coerce_tool_result(result))
