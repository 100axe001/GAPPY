from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetEditIssueMetaToolInput, GetEditIssueMetaToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetEditIssueMetaInput(GetEditIssueMetaToolInput):
    """Operation input for `get_edit_issue_meta`."""
    pass

class GetEditIssueMetaOutput(GetEditIssueMetaToolOutput):
    """Operation output for `get_edit_issue_meta`."""
    pass

class JiraEditIssueMetaResource(BaseResourceClient):
    """Operations for the `edit_issue_meta` resource."""

    @operation(
        name='get_edit_issue_meta',
        title='GetEditIssueMeta',
        input_model=GetEditIssueMetaInput,
        output_model=GetEditIssueMetaOutput,
        tools_used=('get_edit_issue_meta',),
        tags=tuple(['Issues']),
    )
    async def get(self, data: GetEditIssueMetaInput) -> GetEditIssueMetaOutput:
        """Returns the edit screen fields for an issue that are visible to and editable by the user. Use the information to populate the requests in [Edit issue](#api-rest-api-3-issue-issueIdOrKey-put). This endpoint will check for these conditions: 1. Field is available on a field screen - through screen, screen scheme, issue type screen scheme, and issue type scheme configuration. `overrideScreenSecurity=true` skips this condition. 2. Field is visible in the [field configuration](https://support.atlassian.com/jira-cloud-administration/docs/change-a-field-configuration/). `overrideScreenSecurity=true` skips this condition. 3. Field is shown on the issue: each field has different conditions here. For example: Attachment field only shows if attachments are enabled. Assignee only shows if user has permissions to assign the issue. 4. If a field is custom then it must have valid custom field context, applicable for its project and issue type. All system fields are assumed to have context in all projects and all issue types. 5. Issue has a project, issue type, and status defined. 6. Issue is assigned to a valid workflow, and the current status has assigned a workflow step. `overrideEditableFlag=true` skips this condition. 7. The current workflow step is editable. This is true by default, but [can be disabled by setting](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) the `jira.issue.editable` property to `false`. `overrideEditableFlag=true` skips this condition. 8. User has [Edit issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/). 9. Workflow permissions allow editing a field. This is true by default but [can be modified](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) using `jira.permission.*` workflow properties. Fields hidden using [Issue layout settings page](https://support.atlassian.com/jira-software-cloud/docs/configure-field-layout-in-the-issue-view/) remain editable. Connect apps having an app user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can return additional details using: * `overrideScreenSecurity` When this flag is `true`, then this endpoint skips checking if fields are available through screens, and field configuration (conditions 1. and 2. from the list above). * `overrideEditableFlag` When this flag is `true`, then this endpoint skips checking if workflow is present and if the current step is editable (conditions 6. and 7. from the list above). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. Note: For any fields to be editable the user must have the *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the issue.

Important inputs: issue_id_or_key, override_screen_security, override_editable_flag"""
        tool = self._client.get_tool('get_edit_issue_meta')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetEditIssueMetaOutput.model_validate(coerce_tool_result(result))
