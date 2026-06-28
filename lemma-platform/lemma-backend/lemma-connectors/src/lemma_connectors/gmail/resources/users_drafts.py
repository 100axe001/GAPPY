from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersDraftsCreateToolInput, GmailUsersDraftsCreateToolOutput, GmailUsersDraftsDeleteToolInput, GmailUsersDraftsDeleteToolOutput, GmailUsersDraftsGetToolInput, GmailUsersDraftsGetToolOutput, GmailUsersDraftsListToolInput, GmailUsersDraftsListToolOutput, GmailUsersDraftsSendToolInput, GmailUsersDraftsSendToolOutput, GmailUsersDraftsUpdateToolInput, GmailUsersDraftsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersDraftsCreateInput(GmailUsersDraftsCreateToolInput):
    """Operation input for `users_drafts_create`."""
    pass

class UsersDraftsCreateOutput(GmailUsersDraftsCreateToolOutput):
    """Operation output for `users_drafts_create`."""
    pass

class UsersDraftsDeleteInput(GmailUsersDraftsDeleteToolInput):
    """Operation input for `users_drafts_delete`."""
    pass

class UsersDraftsDeleteOutput(GmailUsersDraftsDeleteToolOutput):
    """Operation output for `users_drafts_delete`."""
    pass

class UsersDraftsGetInput(GmailUsersDraftsGetToolInput):
    """Operation input for `users_drafts_get`."""
    pass

class UsersDraftsGetOutput(GmailUsersDraftsGetToolOutput):
    """Operation output for `users_drafts_get`."""
    pass

class UsersDraftsListInput(GmailUsersDraftsListToolInput):
    """Operation input for `users_drafts_list`."""
    pass

class UsersDraftsListOutput(GmailUsersDraftsListToolOutput):
    """Operation output for `users_drafts_list`."""
    pass

class UsersDraftsSendInput(GmailUsersDraftsSendToolInput):
    """Operation input for `users_drafts_send`."""
    pass

class UsersDraftsSendOutput(GmailUsersDraftsSendToolOutput):
    """Operation output for `users_drafts_send`."""
    pass

class UsersDraftsUpdateInput(GmailUsersDraftsUpdateToolInput):
    """Operation input for `users_drafts_update`."""
    pass

class UsersDraftsUpdateOutput(GmailUsersDraftsUpdateToolOutput):
    """Operation output for `users_drafts_update`."""
    pass

class GmailUsersDraftsResource(BaseResourceClient):
    """Operations grouped around the `users_drafts` resource."""

    @operation(
        name='users_drafts_create',
        title='UsersDraftsCreate',
        input_model=UsersDraftsCreateInput,
        output_model=UsersDraftsCreateOutput,
        tools_used=('gmail_users_drafts_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: UsersDraftsCreateInput) -> UsersDraftsCreateOutput:
        """Creates a new draft with the `DRAFT` label.

Use this when you want to creates a new draft with the `DRAFT` label.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_drafts_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersDraftsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_drafts_delete',
        title='UsersDraftsDelete',
        input_model=UsersDraftsDeleteInput,
        output_model=UsersDraftsDeleteOutput,
        tools_used=('gmail_users_drafts_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersDraftsDeleteInput) -> UsersDraftsDeleteOutput:
        """Immediately and permanently deletes the specified draft. Does not simply trash it.

Use this when you want to immediately and permanently deletes the specified draft. Does not simply trash it.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_drafts_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersDraftsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_drafts_get',
        title='UsersDraftsGet',
        input_model=UsersDraftsGetInput,
        output_model=UsersDraftsGetOutput,
        tools_used=('gmail_users_drafts_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersDraftsGetInput) -> UsersDraftsGetOutput:
        """Gets the specified draft.

Use this when you want to gets the specified draft.
Key inputs: fields, user_id, id, format."""
        tool = self._client.get_tool('gmail_users_drafts_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersDraftsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_drafts_list',
        title='UsersDraftsList',
        input_model=UsersDraftsListInput,
        output_model=UsersDraftsListOutput,
        tools_used=('gmail_users_drafts_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersDraftsListInput) -> UsersDraftsListOutput:
        """Lists the drafts in the user's mailbox.

Use this when you want to lists the drafts in the user's mailbox.
Key inputs: fields, user_id, include_spam_trash, max_results, page_token, q."""
        tool = self._client.get_tool('gmail_users_drafts_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersDraftsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_drafts_send',
        title='UsersDraftsSend',
        input_model=UsersDraftsSendInput,
        output_model=UsersDraftsSendOutput,
        tools_used=('gmail_users_drafts_send',),
        tags=tuple(['users']),
    )
    async def send(self, data: UsersDraftsSendInput) -> UsersDraftsSendOutput:
        """Sends the specified, existing draft to the recipients in the `To`, `Cc`, and `Bcc` headers.

Use this when you want to sends the specified, existing draft to the recipients in the `To`, `Cc`, and `Bcc` headers.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_drafts_send')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersDraftsSendOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_drafts_update',
        title='UsersDraftsUpdate',
        input_model=UsersDraftsUpdateInput,
        output_model=UsersDraftsUpdateOutput,
        tools_used=('gmail_users_drafts_update',),
        tags=tuple(['users']),
    )
    async def update(self, data: UsersDraftsUpdateInput) -> UsersDraftsUpdateOutput:
        """Replaces a draft's content.

Use this when you want to replaces a draft's content.
Key inputs: fields, user_id, id, body."""
        tool = self._client.get_tool('gmail_users_drafts_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersDraftsUpdateOutput.model_validate(coerce_tool_result(result))
