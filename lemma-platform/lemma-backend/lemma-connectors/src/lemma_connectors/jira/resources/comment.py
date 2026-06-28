from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddCommentToolInput, AddCommentToolOutput, DeleteCommentToolInput, DeleteCommentToolOutput, GetCommentToolInput, GetCommentToolOutput, UpdateCommentToolInput, UpdateCommentToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddCommentInput(AddCommentToolInput):
    """Operation input for `add_comment`."""
    pass

class AddCommentOutput(AddCommentToolOutput):
    """Operation output for `add_comment`."""
    pass

class DeleteCommentInput(DeleteCommentToolInput):
    """Operation input for `delete_comment`."""
    pass

class DeleteCommentOutput(DeleteCommentToolOutput):
    """Operation output for `delete_comment`."""
    pass

class GetCommentInput(GetCommentToolInput):
    """Operation input for `get_comment`."""
    pass

class GetCommentOutput(GetCommentToolOutput):
    """Operation output for `get_comment`."""
    pass

class UpdateCommentInput(UpdateCommentToolInput):
    """Operation input for `update_comment`."""
    pass

class UpdateCommentOutput(UpdateCommentToolOutput):
    """Operation output for `update_comment`."""
    pass

class JiraCommentResource(BaseResourceClient):
    """Operations for the `comment` resource."""

    @operation(
        name='add_comment',
        title='AddComment',
        input_model=AddCommentInput,
        output_model=AddCommentOutput,
        tools_used=('add_comment',),
        tags=tuple(['Issue comments']),
    )
    async def add(self, data: AddCommentInput) -> AddCommentOutput:
        """Adds a comment to an issue. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Add comments* [ project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, expand, body"""
        tool = self._client.get_tool('add_comment')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddCommentOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_comment',
        title='DeleteComment',
        input_model=DeleteCommentInput,
        output_model=DeleteCommentOutput,
        tools_used=('delete_comment',),
        tags=tuple(['Issue comments']),
    )
    async def delete(self, data: DeleteCommentInput) -> DeleteCommentOutput:
        """Deletes a comment. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * *Delete all comments*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any comment or *Delete own comments* to delete comment created by the user, * If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, id"""
        tool = self._client.get_tool('delete_comment')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteCommentOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_comment',
        title='GetComment',
        input_model=GetCommentInput,
        output_model=GetCommentOutput,
        tools_used=('get_comment',),
        tags=tuple(['Issue comments']),
    )
    async def get(self, data: GetCommentInput) -> GetCommentOutput:
        """Returns a comment. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, id, expand"""
        tool = self._client.get_tool('get_comment')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCommentOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_comment',
        title='UpdateComment',
        input_model=UpdateCommentInput,
        output_model=UpdateCommentOutput,
        tools_used=('update_comment',),
        tags=tuple(['Issue comments']),
    )
    async def update(self, data: UpdateCommentInput) -> UpdateCommentOutput:
        """Updates a comment. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * *Edit all comments*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any comment or *Edit own comments* to update comment created by the user. * If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, id, notify_users, override_editable_flag, expand, body"""
        tool = self._client.get_tool('update_comment')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateCommentOutput.model_validate(coerce_tool_result(result))
