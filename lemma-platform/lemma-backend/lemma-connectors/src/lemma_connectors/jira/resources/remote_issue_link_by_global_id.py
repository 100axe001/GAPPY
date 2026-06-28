from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteRemoteIssueLinkByGlobalIdToolInput, DeleteRemoteIssueLinkByGlobalIdToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteRemoteIssueLinkByGlobalIdInput(DeleteRemoteIssueLinkByGlobalIdToolInput):
    """Operation input for `delete_remote_issue_link_by_global_id`."""
    pass

class DeleteRemoteIssueLinkByGlobalIdOutput(DeleteRemoteIssueLinkByGlobalIdToolOutput):
    """Operation output for `delete_remote_issue_link_by_global_id`."""
    pass

class JiraRemoteIssueLinkByGlobalIdResource(BaseResourceClient):
    """Operations for the `remote_issue_link_by_global_id` resource."""

    @operation(
        name='delete_remote_issue_link_by_global_id',
        title='DeleteRemoteIssueLinkByGlobalId',
        input_model=DeleteRemoteIssueLinkByGlobalIdInput,
        output_model=DeleteRemoteIssueLinkByGlobalIdOutput,
        tools_used=('delete_remote_issue_link_by_global_id',),
        tags=tuple(['Issue remote links']),
    )
    async def delete(self, data: DeleteRemoteIssueLinkByGlobalIdInput) -> DeleteRemoteIssueLinkByGlobalIdOutput:
        """Deletes the remote issue link from the issue using the link's global ID. Where the global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`. This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is implemented, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, global_id"""
        tool = self._client.get_tool('delete_remote_issue_link_by_global_id')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteRemoteIssueLinkByGlobalIdOutput.model_validate(coerce_tool_result(result))
