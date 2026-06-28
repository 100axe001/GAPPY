from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetCommentsToolInput, GetCommentsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetCommentsInput(GetCommentsToolInput):
    """Operation input for `get_comments`."""
    pass

class GetCommentsOutput(GetCommentsToolOutput):
    """Operation output for `get_comments`."""
    pass

class JiraCommentsResource(BaseResourceClient):
    """Operations for the `comments` resource."""

    @operation(
        name='get_comments',
        title='GetComments',
        input_model=GetCommentsInput,
        output_model=GetCommentsOutput,
        tools_used=('get_comments',),
        tags=tuple(['Issue comments']),
    )
    async def get(self, data: GetCommentsInput) -> GetCommentsOutput:
        """Returns all comments for an issue. This operation can be accessed anonymously. **[Permissions](#permissions) required:** Comments are included in the response where the user has: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the comment has visibility restrictions, belongs to the group or has the role visibility is role visibility is restricted to.

Important inputs: issue_id_or_key, start_at, max_results, order_by, expand"""
        tool = self._client.get_tool('get_comments')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCommentsOutput.model_validate(coerce_tool_result(result))
