from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import EditIssueToolInput, EditIssueToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class EditIssueInput(EditIssueToolInput):
    """Operation input for `edit_issue`."""
    pass

class EditIssueOutput(EditIssueToolOutput):
    """Operation output for `edit_issue`."""
    pass

class JiraEditResource(BaseResourceClient):
    """Operations for the `edit` resource."""

    @operation(
        name='edit_issue',
        title='EditIssue',
        input_model=EditIssueInput,
        output_model=EditIssueOutput,
        tools_used=('edit_issue',),
        tags=tuple(['Issues']),
    )
    async def issue(self, data: EditIssueInput) -> EditIssueOutput:
        """Edits an issue. A transition may be applied and issue properties updated as part of the edit. The edits to the issue's fields are defined using `update` and `fields`. The fields that can be edited are determined using [ Get edit issue metadata](#api-rest-api-3-issue-issueIdOrKey-editmeta-get). The parent field may be set by key or ID. For standard issue types, the parent may be removed by setting `update.parent.set.none` to *true*. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content. Connect apps having an app user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can override the screen security configuration using `overrideScreenSecurity` and `overrideEditableFlag`. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, notify_users, override_screen_security, override_editable_flag, body"""
        tool = self._client.get_tool('edit_issue')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EditIssueOutput.model_validate(coerce_tool_result(result))
