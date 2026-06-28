from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AssignIssueToolInput, AssignIssueToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AssignIssueInput(AssignIssueToolInput):
    """Operation input for `assign_issue`."""
    pass

class AssignIssueOutput(AssignIssueToolOutput):
    """Operation output for `assign_issue`."""
    pass

class JiraAssignResource(BaseResourceClient):
    """Operations for the `assign` resource."""

    @operation(
        name='assign_issue',
        title='AssignIssue',
        input_model=AssignIssueInput,
        output_model=AssignIssueOutput,
        tools_used=('assign_issue',),
        tags=tuple(['Issues']),
    )
    async def issue(self, data: AssignIssueInput) -> AssignIssueOutput:
        """Assigns an issue to a user. Use this operation when the calling user does not have the *Edit Issues* permission but has the *Assign issue* permission for the project that the issue is in. If `name` or `accountId` is set to: * `"-1"`, the issue is assigned to the default assignee for the project. * `null`, the issue is set to unassigned. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse Projects* and *Assign Issues* [ project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, body"""
        tool = self._client.get_tool('assign_issue')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AssignIssueOutput.model_validate(coerce_tool_result(result))
