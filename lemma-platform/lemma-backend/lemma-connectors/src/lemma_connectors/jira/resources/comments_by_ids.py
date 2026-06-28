from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetCommentsByIdsToolInput, GetCommentsByIdsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetCommentsByIdsInput(GetCommentsByIdsToolInput):
    """Operation input for `get_comments_by_ids`."""
    pass

class GetCommentsByIdsOutput(GetCommentsByIdsToolOutput):
    """Operation output for `get_comments_by_ids`."""
    pass

class JiraCommentsByIdsResource(BaseResourceClient):
    """Operations for the `comments_by_ids` resource."""

    @operation(
        name='get_comments_by_ids',
        title='GetCommentsByIds',
        input_model=GetCommentsByIdsInput,
        output_model=GetCommentsByIdsOutput,
        tools_used=('get_comments_by_ids',),
        tags=tuple(['Issue comments']),
    )
    async def get(self, data: GetCommentsByIdsInput) -> GetCommentsByIdsOutput:
        """Returns a [paginated](#pagination) list of comments specified by a list of comment IDs. This operation can be accessed anonymously. **[Permissions](#permissions) required:** Comments are returned where the user: * has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: expand, body"""
        tool = self._client.get_tool('get_comments_by_ids')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCommentsByIdsOutput.model_validate(coerce_tool_result(result))
