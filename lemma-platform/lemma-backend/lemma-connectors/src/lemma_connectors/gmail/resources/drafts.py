from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersDraftsCreateToolInput, GmailUsersDraftsCreateToolOutput, GmailUsersDraftsDeleteToolInput, GmailUsersDraftsDeleteToolOutput, GmailUsersDraftsGetToolInput, GmailUsersDraftsGetToolOutput, GmailUsersDraftsListToolInput, GmailUsersDraftsListToolOutput, GmailUsersDraftsSendToolInput, GmailUsersDraftsSendToolOutput, GmailUsersDraftsUpdateToolInput, GmailUsersDraftsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DraftsCreateInput(GmailUsersDraftsCreateToolInput):
    """Operation input for `drafts_create`."""
    pass

class DraftsCreateOutput(GmailUsersDraftsCreateToolOutput):
    """Operation output for `drafts_create`."""
    pass

class DraftsDeleteInput(GmailUsersDraftsDeleteToolInput):
    """Operation input for `drafts_delete`."""
    pass

class DraftsDeleteOutput(GmailUsersDraftsDeleteToolOutput):
    """Operation output for `drafts_delete`."""
    pass

class DraftsGetInput(GmailUsersDraftsGetToolInput):
    """Operation input for `drafts_get`."""
    pass

class DraftsGetOutput(GmailUsersDraftsGetToolOutput):
    """Operation output for `drafts_get`."""
    pass

class DraftsListInput(GmailUsersDraftsListToolInput):
    """Operation input for `drafts_list`."""
    pass

class DraftsListOutput(GmailUsersDraftsListToolOutput):
    """Operation output for `drafts_list`."""
    pass

class DraftsSendInput(GmailUsersDraftsSendToolInput):
    """Operation input for `drafts_send`."""
    pass

class DraftsSendOutput(GmailUsersDraftsSendToolOutput):
    """Operation output for `drafts_send`."""
    pass

class DraftsUpdateInput(GmailUsersDraftsUpdateToolInput):
    """Operation input for `drafts_update`."""
    pass

class DraftsUpdateOutput(GmailUsersDraftsUpdateToolOutput):
    """Operation output for `drafts_update`."""
    pass

class GmailDraftsResource(BaseResourceClient):
    """Operations for the `drafts` resource."""

    @operation(
        name='drafts_create',
        title='DraftsCreate',
        input_model=DraftsCreateInput,
        output_model=DraftsCreateOutput,
        tools_used=('gmail_users_drafts_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: DraftsCreateInput) -> DraftsCreateOutput:
        """Creates a new draft with the `DRAFT` label.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_drafts_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DraftsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drafts_delete',
        title='DraftsDelete',
        input_model=DraftsDeleteInput,
        output_model=DraftsDeleteOutput,
        tools_used=('gmail_users_drafts_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: DraftsDeleteInput) -> DraftsDeleteOutput:
        """Immediately and permanently deletes the specified draft. Does not simply trash it.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_drafts_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DraftsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drafts_get',
        title='DraftsGet',
        input_model=DraftsGetInput,
        output_model=DraftsGetOutput,
        tools_used=('gmail_users_drafts_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: DraftsGetInput) -> DraftsGetOutput:
        """Gets the specified draft.

Important inputs: fields, user_id, id, format"""
        tool = self._client.get_tool('gmail_users_drafts_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DraftsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drafts_list',
        title='DraftsList',
        input_model=DraftsListInput,
        output_model=DraftsListOutput,
        tools_used=('gmail_users_drafts_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: DraftsListInput) -> DraftsListOutput:
        """Lists the drafts in the user's mailbox.

Important inputs: fields, user_id, include_spam_trash, max_results, page_token, q"""
        tool = self._client.get_tool('gmail_users_drafts_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DraftsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drafts_send',
        title='DraftsSend',
        input_model=DraftsSendInput,
        output_model=DraftsSendOutput,
        tools_used=('gmail_users_drafts_send',),
        tags=tuple(['users']),
    )
    async def send(self, data: DraftsSendInput) -> DraftsSendOutput:
        """Sends the specified, existing draft to the recipients in the `To`, `Cc`, and `Bcc` headers.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_drafts_send')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DraftsSendOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drafts_update',
        title='DraftsUpdate',
        input_model=DraftsUpdateInput,
        output_model=DraftsUpdateOutput,
        tools_used=('gmail_users_drafts_update',),
        tags=tuple(['users']),
    )
    async def update(self, data: DraftsUpdateInput) -> DraftsUpdateOutput:
        """Replaces a draft's content.

Important inputs: fields, user_id, id, body"""
        tool = self._client.get_tool('gmail_users_drafts_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DraftsUpdateOutput.model_validate(coerce_tool_result(result))
