from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteRemoteIssueLinkByIdToolInput, DeleteRemoteIssueLinkByIdToolOutput, GetRemoteIssueLinkByIdToolInput, GetRemoteIssueLinkByIdToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteRemoteIssueLinkByIdInput(DeleteRemoteIssueLinkByIdToolInput):
    """Operation input for `delete_remote_issue_link_by_id`."""
    pass

class DeleteRemoteIssueLinkByIdOutput(DeleteRemoteIssueLinkByIdToolOutput):
    """Operation output for `delete_remote_issue_link_by_id`."""
    pass

class GetRemoteIssueLinkByIdInput(GetRemoteIssueLinkByIdToolInput):
    """Operation input for `get_remote_issue_link_by_id`."""
    pass

class GetRemoteIssueLinkByIdOutput(GetRemoteIssueLinkByIdToolOutput):
    """Operation output for `get_remote_issue_link_by_id`."""
    pass

class JiraRemoteIssueLinkByIdResource(BaseResourceClient):
    """Operations for the `remote_issue_link_by_id` resource."""

    @operation(
        name='delete_remote_issue_link_by_id',
        title='DeleteRemoteIssueLinkById',
        input_model=DeleteRemoteIssueLinkByIdInput,
        output_model=DeleteRemoteIssueLinkByIdOutput,
        tools_used=('delete_remote_issue_link_by_id',),
        tags=tuple(['Issue remote links']),
    )
    async def delete(self, data: DeleteRemoteIssueLinkByIdInput) -> DeleteRemoteIssueLinkByIdOutput:
        """Deletes a remote issue link from an issue. This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects*, *Edit issues*, and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, link_id"""
        tool = self._client.get_tool('delete_remote_issue_link_by_id')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteRemoteIssueLinkByIdOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_remote_issue_link_by_id',
        title='GetRemoteIssueLinkById',
        input_model=GetRemoteIssueLinkByIdInput,
        output_model=GetRemoteIssueLinkByIdOutput,
        tools_used=('get_remote_issue_link_by_id',),
        tags=tuple(['Issue remote links']),
    )
    async def get(self, data: GetRemoteIssueLinkByIdInput) -> GetRemoteIssueLinkByIdOutput:
        """Returns a remote issue link for an issue. This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, link_id"""
        tool = self._client.get_tool('get_remote_issue_link_by_id')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetRemoteIssueLinkByIdOutput.model_validate(coerce_tool_result(result))
