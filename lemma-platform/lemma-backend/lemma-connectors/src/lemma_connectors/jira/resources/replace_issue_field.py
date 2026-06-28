from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ReplaceIssueFieldOptionToolInput, ReplaceIssueFieldOptionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ReplaceIssueFieldOptionInput(ReplaceIssueFieldOptionToolInput):
    """Operation input for `replace_issue_field_option`."""
    pass

class ReplaceIssueFieldOptionOutput(ReplaceIssueFieldOptionToolOutput):
    """Operation output for `replace_issue_field_option`."""
    pass

class JiraReplaceIssueFieldResource(BaseResourceClient):
    """Operations for the `replace_issue_field` resource."""

    @operation(
        name='replace_issue_field_option',
        title='ReplaceIssueFieldOption',
        input_model=ReplaceIssueFieldOptionInput,
        output_model=ReplaceIssueFieldOptionOutput,
        tools_used=('replace_issue_field_option',),
        tags=tuple(['Issue custom field options (apps)']),
    )
    async def option(self, data: ReplaceIssueFieldOptionInput) -> ReplaceIssueFieldOptionOutput:
        """Deselects an issue-field select-list option from all issues where it is selected. A different option can be selected to replace the deselected option. The update can also be limited to a smaller set of issues by using a JQL query. Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can override the screen security configuration using `overrideScreenSecurity` and `overrideEditableFlag`. This is an [asynchronous operation](#async). The response object contains a link to the long-running task. Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.

Important inputs: replace_with, jql, override_screen_security, override_editable_flag, field_key, option_id"""
        tool = self._client.get_tool('replace_issue_field_option')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ReplaceIssueFieldOptionOutput.model_validate(coerce_tool_result(result))
