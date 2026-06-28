from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersLabelsCreateToolInput, GmailUsersLabelsCreateToolOutput, GmailUsersLabelsDeleteToolInput, GmailUsersLabelsDeleteToolOutput, GmailUsersLabelsGetToolInput, GmailUsersLabelsGetToolOutput, GmailUsersLabelsListToolInput, GmailUsersLabelsListToolOutput, GmailUsersLabelsPatchToolInput, GmailUsersLabelsPatchToolOutput, GmailUsersLabelsUpdateToolInput, GmailUsersLabelsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersLabelsCreateInput(GmailUsersLabelsCreateToolInput):
    """Operation input for `users_labels_create`."""
    pass

class UsersLabelsCreateOutput(GmailUsersLabelsCreateToolOutput):
    """Operation output for `users_labels_create`."""
    pass

class UsersLabelsDeleteInput(GmailUsersLabelsDeleteToolInput):
    """Operation input for `users_labels_delete`."""
    pass

class UsersLabelsDeleteOutput(GmailUsersLabelsDeleteToolOutput):
    """Operation output for `users_labels_delete`."""
    pass

class UsersLabelsGetInput(GmailUsersLabelsGetToolInput):
    """Operation input for `users_labels_get`."""
    pass

class UsersLabelsGetOutput(GmailUsersLabelsGetToolOutput):
    """Operation output for `users_labels_get`."""
    pass

class UsersLabelsListInput(GmailUsersLabelsListToolInput):
    """Operation input for `users_labels_list`."""
    pass

class UsersLabelsListOutput(GmailUsersLabelsListToolOutput):
    """Operation output for `users_labels_list`."""
    pass

class UsersLabelsPatchInput(GmailUsersLabelsPatchToolInput):
    """Operation input for `users_labels_patch`."""
    pass

class UsersLabelsPatchOutput(GmailUsersLabelsPatchToolOutput):
    """Operation output for `users_labels_patch`."""
    pass

class UsersLabelsUpdateInput(GmailUsersLabelsUpdateToolInput):
    """Operation input for `users_labels_update`."""
    pass

class UsersLabelsUpdateOutput(GmailUsersLabelsUpdateToolOutput):
    """Operation output for `users_labels_update`."""
    pass

class GmailUsersLabelsResource(BaseResourceClient):
    """Operations grouped around the `users_labels` resource."""

    @operation(
        name='users_labels_create',
        title='UsersLabelsCreate',
        input_model=UsersLabelsCreateInput,
        output_model=UsersLabelsCreateOutput,
        tools_used=('gmail_users_labels_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: UsersLabelsCreateInput) -> UsersLabelsCreateOutput:
        """Creates a new label.

Use this when you want to creates a new label.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_labels_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersLabelsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_labels_delete',
        title='UsersLabelsDelete',
        input_model=UsersLabelsDeleteInput,
        output_model=UsersLabelsDeleteOutput,
        tools_used=('gmail_users_labels_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersLabelsDeleteInput) -> UsersLabelsDeleteOutput:
        """Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to.

Use this when you want to immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_labels_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersLabelsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_labels_get',
        title='UsersLabelsGet',
        input_model=UsersLabelsGetInput,
        output_model=UsersLabelsGetOutput,
        tools_used=('gmail_users_labels_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersLabelsGetInput) -> UsersLabelsGetOutput:
        """Gets the specified label.

Use this when you want to gets the specified label.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_labels_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersLabelsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_labels_list',
        title='UsersLabelsList',
        input_model=UsersLabelsListInput,
        output_model=UsersLabelsListOutput,
        tools_used=('gmail_users_labels_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersLabelsListInput) -> UsersLabelsListOutput:
        """Lists all labels in the user's mailbox.

Use this when you want to lists all labels in the user's mailbox.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_labels_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersLabelsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_labels_patch',
        title='UsersLabelsPatch',
        input_model=UsersLabelsPatchInput,
        output_model=UsersLabelsPatchOutput,
        tools_used=('gmail_users_labels_patch',),
        tags=tuple(['users']),
    )
    async def patch(self, data: UsersLabelsPatchInput) -> UsersLabelsPatchOutput:
        """Patch the specified label.

Use this when you want to patch the specified label.
Key inputs: fields, user_id, id, body."""
        tool = self._client.get_tool('gmail_users_labels_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersLabelsPatchOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_labels_update',
        title='UsersLabelsUpdate',
        input_model=UsersLabelsUpdateInput,
        output_model=UsersLabelsUpdateOutput,
        tools_used=('gmail_users_labels_update',),
        tags=tuple(['users']),
    )
    async def update(self, data: UsersLabelsUpdateInput) -> UsersLabelsUpdateOutput:
        """Updates the specified label.

Use this when you want to updates the specified label.
Key inputs: fields, user_id, id, body."""
        tool = self._client.get_tool('gmail_users_labels_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersLabelsUpdateOutput.model_validate(coerce_tool_result(result))
