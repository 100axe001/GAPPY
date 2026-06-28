from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetCommentPropertyKeysToolInput, GetCommentPropertyKeysToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetCommentPropertyKeysInput(GetCommentPropertyKeysToolInput):
    """Operation input for `get_comment_property_keys`."""
    pass

class GetCommentPropertyKeysOutput(GetCommentPropertyKeysToolOutput):
    """Operation output for `get_comment_property_keys`."""
    pass

class JiraCommentPropertyKeysResource(BaseResourceClient):
    """Operations for the `comment_property_keys` resource."""

    @operation(
        name='get_comment_property_keys',
        title='GetCommentPropertyKeys',
        input_model=GetCommentPropertyKeysInput,
        output_model=GetCommentPropertyKeysOutput,
        tools_used=('get_comment_property_keys',),
        tags=tuple(['Issue comment properties']),
    )
    async def get(self, data: GetCommentPropertyKeysInput) -> GetCommentPropertyKeysOutput:
        """Returns the keys of all the properties of a comment. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: comment_id"""
        tool = self._client.get_tool('get_comment_property_keys')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCommentPropertyKeysOutput.model_validate(coerce_tool_result(result))
