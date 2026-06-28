from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteCommentPropertyToolInput, DeleteCommentPropertyToolOutput, GetCommentPropertyToolInput, GetCommentPropertyToolOutput, SetCommentPropertyToolInput, SetCommentPropertyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteCommentPropertyInput(DeleteCommentPropertyToolInput):
    """Operation input for `delete_comment_property`."""
    pass

class DeleteCommentPropertyOutput(DeleteCommentPropertyToolOutput):
    """Operation output for `delete_comment_property`."""
    pass

class GetCommentPropertyInput(GetCommentPropertyToolInput):
    """Operation input for `get_comment_property`."""
    pass

class GetCommentPropertyOutput(GetCommentPropertyToolOutput):
    """Operation output for `get_comment_property`."""
    pass

class SetCommentPropertyInput(SetCommentPropertyToolInput):
    """Operation input for `set_comment_property`."""
    pass

class SetCommentPropertyOutput(SetCommentPropertyToolOutput):
    """Operation output for `set_comment_property`."""
    pass

class JiraCommentPropertyResource(BaseResourceClient):
    """Operations for the `comment_property` resource."""

    @operation(
        name='delete_comment_property',
        title='DeleteCommentProperty',
        input_model=DeleteCommentPropertyInput,
        output_model=DeleteCommentPropertyOutput,
        tools_used=('delete_comment_property',),
        tags=tuple(['Issue comment properties']),
    )
    async def delete(self, data: DeleteCommentPropertyInput) -> DeleteCommentPropertyOutput:
        """Deletes a comment property. **[Permissions](#permissions) required:** either of: * *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from any comment. * *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from a comment created by the user. Also, when the visibility of a comment is restricted to a role or group the user must be a member of that role or group.

Important inputs: comment_id, property_key"""
        tool = self._client.get_tool('delete_comment_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteCommentPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_comment_property',
        title='GetCommentProperty',
        input_model=GetCommentPropertyInput,
        output_model=GetCommentPropertyOutput,
        tools_used=('get_comment_property',),
        tags=tuple(['Issue comment properties']),
    )
    async def get(self, data: GetCommentPropertyInput) -> GetCommentPropertyOutput:
        """Returns the value of a comment property. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: comment_id, property_key"""
        tool = self._client.get_tool('get_comment_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCommentPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_comment_property',
        title='SetCommentProperty',
        input_model=SetCommentPropertyInput,
        output_model=SetCommentPropertyOutput,
        tools_used=('set_comment_property',),
        tags=tuple(['Issue comment properties']),
    )
    async def set(self, data: SetCommentPropertyInput) -> SetCommentPropertyOutput:
        """Creates or updates the value of a property for a comment. Use this resource to store custom data against a comment. The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters. **[Permissions](#permissions) required:** either of: * *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on any comment. * *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on a comment created by the user. Also, when the visibility of a comment is restricted to a role or group the user must be a member of that role or group.

Important inputs: comment_id, property_key, body"""
        tool = self._client.get_tool('set_comment_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetCommentPropertyOutput.model_validate(coerce_tool_result(result))
