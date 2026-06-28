from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateOrUpdateRemoteIssueLinkToolInput, CreateOrUpdateRemoteIssueLinkToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateOrUpdateRemoteIssueLinkInput(CreateOrUpdateRemoteIssueLinkToolInput):
    """Operation input for `create_or_update_remote_issue_link`."""
    pass

class CreateOrUpdateRemoteIssueLinkOutput(CreateOrUpdateRemoteIssueLinkToolOutput):
    """Operation output for `create_or_update_remote_issue_link`."""
    pass

class JiraOrUpdateRemoteIssueLinkResource(BaseResourceClient):
    """Operations for the `or_update_remote_issue_link` resource."""

    @operation(
        name='create_or_update_remote_issue_link',
        title='CreateOrUpdateRemoteIssueLink',
        input_model=CreateOrUpdateRemoteIssueLinkInput,
        output_model=CreateOrUpdateRemoteIssueLinkOutput,
        tools_used=('create_or_update_remote_issue_link',),
        tags=tuple(['Issue remote links']),
    )
    async def create(self, data: CreateOrUpdateRemoteIssueLinkInput) -> CreateOrUpdateRemoteIssueLinkOutput:
        """Creates or updates a remote issue link for an issue. If a `globalId` is provided and a remote issue link with that global ID is found it is updated. Any fields without values in the request are set to null. Otherwise, the remote issue link is created. This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, body"""
        tool = self._client.get_tool('create_or_update_remote_issue_link')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateOrUpdateRemoteIssueLinkOutput.model_validate(coerce_tool_result(result))
