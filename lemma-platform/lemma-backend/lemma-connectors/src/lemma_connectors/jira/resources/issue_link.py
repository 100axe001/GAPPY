from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteIssueLinkToolInput, DeleteIssueLinkToolOutput, GetIssueLinkToolInput, GetIssueLinkToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteIssueLinkInput(DeleteIssueLinkToolInput):
    """Operation input for `delete_issue_link`."""
    pass

class DeleteIssueLinkOutput(DeleteIssueLinkToolOutput):
    """Operation output for `delete_issue_link`."""
    pass

class GetIssueLinkInput(GetIssueLinkToolInput):
    """Operation input for `get_issue_link`."""
    pass

class GetIssueLinkOutput(GetIssueLinkToolOutput):
    """Operation output for `get_issue_link`."""
    pass

class JiraIssueLinkResource(BaseResourceClient):
    """Operations for the `issue_link` resource."""

    @operation(
        name='delete_issue_link',
        title='DeleteIssueLink',
        input_model=DeleteIssueLinkInput,
        output_model=DeleteIssueLinkOutput,
        tools_used=('delete_issue_link',),
        tags=tuple(['Issue links']),
    )
    async def delete(self, data: DeleteIssueLinkInput) -> DeleteIssueLinkOutput:
        """Deletes an issue link. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * Browse project [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues in the link. * *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one of the projects containing issues in the link. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.

Important inputs: link_id"""
        tool = self._client.get_tool('delete_issue_link')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteIssueLinkOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_issue_link',
        title='GetIssueLink',
        input_model=GetIssueLinkInput,
        output_model=GetIssueLinkOutput,
        tools_used=('get_issue_link',),
        tags=tuple(['Issue links']),
    )
    async def get(self, data: GetIssueLinkInput) -> GetIssueLinkOutput:
        """Returns an issue link. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the linked issues. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.

Important inputs: link_id"""
        tool = self._client.get_tool('get_issue_link')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueLinkOutput.model_validate(coerce_tool_result(result))
