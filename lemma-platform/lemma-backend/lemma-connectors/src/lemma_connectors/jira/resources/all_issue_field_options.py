from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllIssueFieldOptionsToolInput, GetAllIssueFieldOptionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllIssueFieldOptionsInput(GetAllIssueFieldOptionsToolInput):
    """Operation input for `get_all_issue_field_options`."""
    pass

class GetAllIssueFieldOptionsOutput(GetAllIssueFieldOptionsToolOutput):
    """Operation output for `get_all_issue_field_options`."""
    pass

class JiraAllIssueFieldOptionsResource(BaseResourceClient):
    """Operations for the `all_issue_field_options` resource."""

    @operation(
        name='get_all_issue_field_options',
        title='GetAllIssueFieldOptions',
        input_model=GetAllIssueFieldOptionsInput,
        output_model=GetAllIssueFieldOptionsOutput,
        tools_used=('get_all_issue_field_options',),
        tags=tuple(['Issue custom field options (apps)']),
    )
    async def get(self, data: GetAllIssueFieldOptionsInput) -> GetAllIssueFieldOptionsOutput:
        """Returns a [paginated](#pagination) list of all the options of a select list issue field. A select list issue field is a type of [issue field](https://developer.atlassian.com/cloud/jira/platform/modules/issue-field/) that enables a user to select a value from a list of options. Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.

Important inputs: start_at, max_results, field_key"""
        tool = self._client.get_tool('get_all_issue_field_options')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllIssueFieldOptionsOutput.model_validate(coerce_tool_result(result))
