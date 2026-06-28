from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import UpdateRemoteIssueLinkToolInput, UpdateRemoteIssueLinkToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UpdateRemoteIssueLinkInput(UpdateRemoteIssueLinkToolInput):
    """Operation input for `update_remote_issue_link`."""
    pass

class UpdateRemoteIssueLinkOutput(UpdateRemoteIssueLinkToolOutput):
    """Operation output for `update_remote_issue_link`."""
    pass

class JiraRemoteIssueLinkResource(BaseResourceClient):
    """Operations for the `remote_issue_link` resource."""

    @operation(
        name='update_remote_issue_link',
        title='UpdateRemoteIssueLink',
        input_model=UpdateRemoteIssueLinkInput,
        output_model=UpdateRemoteIssueLinkOutput,
        tools_used=('update_remote_issue_link',),
        tags=tuple(['Issue remote links']),
    )
    async def update(self, data: UpdateRemoteIssueLinkInput) -> UpdateRemoteIssueLinkOutput:
        """Updates a remote issue link for an issue. Note: Fields without values in the request are set to null. This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, link_id, body"""
        tool = self._client.get_tool('update_remote_issue_link')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateRemoteIssueLinkOutput.model_validate(coerce_tool_result(result))
