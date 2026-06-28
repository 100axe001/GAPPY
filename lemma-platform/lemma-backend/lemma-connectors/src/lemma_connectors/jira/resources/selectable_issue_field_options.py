from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetSelectableIssueFieldOptionsToolInput, GetSelectableIssueFieldOptionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetSelectableIssueFieldOptionsInput(GetSelectableIssueFieldOptionsToolInput):
    """Operation input for `get_selectable_issue_field_options`."""
    pass

class GetSelectableIssueFieldOptionsOutput(GetSelectableIssueFieldOptionsToolOutput):
    """Operation output for `get_selectable_issue_field_options`."""
    pass

class JiraSelectableIssueFieldOptionsResource(BaseResourceClient):
    """Operations for the `selectable_issue_field_options` resource."""

    @operation(
        name='get_selectable_issue_field_options',
        title='GetSelectableIssueFieldOptions',
        input_model=GetSelectableIssueFieldOptionsInput,
        output_model=GetSelectableIssueFieldOptionsOutput,
        tools_used=('get_selectable_issue_field_options',),
        tags=tuple(['Issue custom field options (apps)']),
    )
    async def get(self, data: GetSelectableIssueFieldOptionsInput) -> GetSelectableIssueFieldOptionsOutput:
        """Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed and selected by the user. Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: start_at, max_results, project_id, field_key"""
        tool = self._client.get_tool('get_selectable_issue_field_options')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetSelectableIssueFieldOptionsOutput.model_validate(coerce_tool_result(result))
