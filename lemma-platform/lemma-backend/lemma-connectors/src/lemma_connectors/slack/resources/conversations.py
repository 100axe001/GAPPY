from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ConversationsArchiveToolInput, ConversationsArchiveToolOutput, ConversationsCloseToolInput, ConversationsCloseToolOutput, ConversationsCreateToolInput, ConversationsCreateToolOutput, ConversationsHistoryToolInput, ConversationsHistoryToolOutput, ConversationsInfoToolInput, ConversationsInfoToolOutput, ConversationsInviteToolInput, ConversationsInviteToolOutput, ConversationsJoinToolInput, ConversationsJoinToolOutput, ConversationsKickToolInput, ConversationsKickToolOutput, ConversationsLeaveToolInput, ConversationsLeaveToolOutput, ConversationsListToolInput, ConversationsListToolOutput, ConversationsMarkToolInput, ConversationsMarkToolOutput, ConversationsMembersToolInput, ConversationsMembersToolOutput, ConversationsOpenToolInput, ConversationsOpenToolOutput, ConversationsRenameToolInput, ConversationsRenameToolOutput, ConversationsRepliesToolInput, ConversationsRepliesToolOutput, ConversationsUnarchiveToolInput, ConversationsUnarchiveToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ConversationsArchiveInput(ConversationsArchiveToolInput):
    """Operation input for `conversations_archive`."""
    pass

class ConversationsArchiveOutput(ConversationsArchiveToolOutput):
    """Operation output for `conversations_archive`."""
    pass

class ConversationsCloseInput(ConversationsCloseToolInput):
    """Operation input for `conversations_close`."""
    pass

class ConversationsCloseOutput(ConversationsCloseToolOutput):
    """Operation output for `conversations_close`."""
    pass

class ConversationsCreateInput(ConversationsCreateToolInput):
    """Operation input for `conversations_create`."""
    pass

class ConversationsCreateOutput(ConversationsCreateToolOutput):
    """Operation output for `conversations_create`."""
    pass

class ConversationsHistoryInput(ConversationsHistoryToolInput):
    """Operation input for `conversations_history`."""
    pass

class ConversationsHistoryOutput(ConversationsHistoryToolOutput):
    """Operation output for `conversations_history`."""
    pass

class ConversationsInfoInput(ConversationsInfoToolInput):
    """Operation input for `conversations_info`."""
    pass

class ConversationsInfoOutput(ConversationsInfoToolOutput):
    """Operation output for `conversations_info`."""
    pass

class ConversationsInviteInput(ConversationsInviteToolInput):
    """Operation input for `conversations_invite`."""
    pass

class ConversationsInviteOutput(ConversationsInviteToolOutput):
    """Operation output for `conversations_invite`."""
    pass

class ConversationsJoinInput(ConversationsJoinToolInput):
    """Operation input for `conversations_join`."""
    pass

class ConversationsJoinOutput(ConversationsJoinToolOutput):
    """Operation output for `conversations_join`."""
    pass

class ConversationsKickInput(ConversationsKickToolInput):
    """Operation input for `conversations_kick`."""
    pass

class ConversationsKickOutput(ConversationsKickToolOutput):
    """Operation output for `conversations_kick`."""
    pass

class ConversationsLeaveInput(ConversationsLeaveToolInput):
    """Operation input for `conversations_leave`."""
    pass

class ConversationsLeaveOutput(ConversationsLeaveToolOutput):
    """Operation output for `conversations_leave`."""
    pass

class ConversationsListInput(ConversationsListToolInput):
    """Operation input for `conversations_list`."""
    pass

class ConversationsListOutput(ConversationsListToolOutput):
    """Operation output for `conversations_list`."""
    pass

class ConversationsMarkInput(ConversationsMarkToolInput):
    """Operation input for `conversations_mark`."""
    pass

class ConversationsMarkOutput(ConversationsMarkToolOutput):
    """Operation output for `conversations_mark`."""
    pass

class ConversationsMembersInput(ConversationsMembersToolInput):
    """Operation input for `conversations_members`."""
    pass

class ConversationsMembersOutput(ConversationsMembersToolOutput):
    """Operation output for `conversations_members`."""
    pass

class ConversationsOpenInput(ConversationsOpenToolInput):
    """Operation input for `conversations_open`."""
    pass

class ConversationsOpenOutput(ConversationsOpenToolOutput):
    """Operation output for `conversations_open`."""
    pass

class ConversationsRenameInput(ConversationsRenameToolInput):
    """Operation input for `conversations_rename`."""
    pass

class ConversationsRenameOutput(ConversationsRenameToolOutput):
    """Operation output for `conversations_rename`."""
    pass

class ConversationsRepliesInput(ConversationsRepliesToolInput):
    """Operation input for `conversations_replies`."""
    pass

class ConversationsRepliesOutput(ConversationsRepliesToolOutput):
    """Operation output for `conversations_replies`."""
    pass

class ConversationsUnarchiveInput(ConversationsUnarchiveToolInput):
    """Operation input for `conversations_unarchive`."""
    pass

class ConversationsUnarchiveOutput(ConversationsUnarchiveToolOutput):
    """Operation output for `conversations_unarchive`."""
    pass

class SlackConversationsResource(BaseResourceClient):
    """Operations for the `conversations` resource."""

    @operation(
        name='conversations_archive',
        title='ConversationsArchive',
        input_model=ConversationsArchiveInput,
        output_model=ConversationsArchiveOutput,
        tools_used=('conversations_archive',),
        tags=tuple(['conversations']),
    )
    async def archive(self, data: ConversationsArchiveInput) -> ConversationsArchiveOutput:
        """Archives a conversation.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_archive')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsArchiveOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_close',
        title='ConversationsClose',
        input_model=ConversationsCloseInput,
        output_model=ConversationsCloseOutput,
        tools_used=('conversations_close',),
        tags=tuple(['conversations']),
    )
    async def close(self, data: ConversationsCloseInput) -> ConversationsCloseOutput:
        """Closes a direct message or multi-person direct message.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_close')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsCloseOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_create',
        title='ConversationsCreate',
        input_model=ConversationsCreateInput,
        output_model=ConversationsCreateOutput,
        tools_used=('conversations_create',),
        tags=tuple(['conversations']),
    )
    async def create(self, data: ConversationsCreateInput) -> ConversationsCreateOutput:
        """Initiates a public or private channel-based conversation.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_history',
        title='ConversationsHistory',
        input_model=ConversationsHistoryInput,
        output_model=ConversationsHistoryOutput,
        tools_used=('conversations_history',),
        tags=tuple(['conversations']),
    )
    async def history(self, data: ConversationsHistoryInput) -> ConversationsHistoryOutput:
        """Fetches a conversation's history of messages and events.

Important inputs: token, channel, latest, oldest, inclusive, limit, cursor"""
        tool = self._client.get_tool('conversations_history')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsHistoryOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_info',
        title='ConversationsInfo',
        input_model=ConversationsInfoInput,
        output_model=ConversationsInfoOutput,
        tools_used=('conversations_info',),
        tags=tuple(['conversations']),
    )
    async def info(self, data: ConversationsInfoInput) -> ConversationsInfoOutput:
        """Retrieve information about a conversation.

Important inputs: token, channel, include_locale, include_num_members"""
        tool = self._client.get_tool('conversations_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsInfoOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_invite',
        title='ConversationsInvite',
        input_model=ConversationsInviteInput,
        output_model=ConversationsInviteOutput,
        tools_used=('conversations_invite',),
        tags=tuple(['conversations']),
    )
    async def invite(self, data: ConversationsInviteInput) -> ConversationsInviteOutput:
        """Invites users to a channel.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_invite')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsInviteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_join',
        title='ConversationsJoin',
        input_model=ConversationsJoinInput,
        output_model=ConversationsJoinOutput,
        tools_used=('conversations_join',),
        tags=tuple(['conversations']),
    )
    async def join(self, data: ConversationsJoinInput) -> ConversationsJoinOutput:
        """Joins an existing conversation.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_join')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsJoinOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_kick',
        title='ConversationsKick',
        input_model=ConversationsKickInput,
        output_model=ConversationsKickOutput,
        tools_used=('conversations_kick',),
        tags=tuple(['conversations']),
    )
    async def kick(self, data: ConversationsKickInput) -> ConversationsKickOutput:
        """Removes a user from a conversation.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_kick')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsKickOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_leave',
        title='ConversationsLeave',
        input_model=ConversationsLeaveInput,
        output_model=ConversationsLeaveOutput,
        tools_used=('conversations_leave',),
        tags=tuple(['conversations']),
    )
    async def leave(self, data: ConversationsLeaveInput) -> ConversationsLeaveOutput:
        """Leaves a conversation.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_leave')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsLeaveOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_list',
        title='ConversationsList',
        input_model=ConversationsListInput,
        output_model=ConversationsListOutput,
        tools_used=('conversations_list',),
        tags=tuple(['conversations']),
    )
    async def list(self, data: ConversationsListInput) -> ConversationsListOutput:
        """Lists all channels in a Slack team.

Important inputs: token, exclude_archived, types, limit, cursor"""
        tool = self._client.get_tool('conversations_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_mark',
        title='ConversationsMark',
        input_model=ConversationsMarkInput,
        output_model=ConversationsMarkOutput,
        tools_used=('conversations_mark',),
        tags=tuple(['conversations']),
    )
    async def mark(self, data: ConversationsMarkInput) -> ConversationsMarkOutput:
        """Sets the read cursor in a channel.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_mark')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsMarkOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_members',
        title='ConversationsMembers',
        input_model=ConversationsMembersInput,
        output_model=ConversationsMembersOutput,
        tools_used=('conversations_members',),
        tags=tuple(['conversations']),
    )
    async def members(self, data: ConversationsMembersInput) -> ConversationsMembersOutput:
        """Retrieve members of a conversation.

Important inputs: token, channel, limit, cursor"""
        tool = self._client.get_tool('conversations_members')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsMembersOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_open',
        title='ConversationsOpen',
        input_model=ConversationsOpenInput,
        output_model=ConversationsOpenOutput,
        tools_used=('conversations_open',),
        tags=tuple(['conversations']),
    )
    async def open(self, data: ConversationsOpenInput) -> ConversationsOpenOutput:
        """Opens or resumes a direct message or multi-person direct message.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_open')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsOpenOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_rename',
        title='ConversationsRename',
        input_model=ConversationsRenameInput,
        output_model=ConversationsRenameOutput,
        tools_used=('conversations_rename',),
        tags=tuple(['conversations']),
    )
    async def rename(self, data: ConversationsRenameInput) -> ConversationsRenameOutput:
        """Renames a conversation.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_rename')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsRenameOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_replies',
        title='ConversationsReplies',
        input_model=ConversationsRepliesInput,
        output_model=ConversationsRepliesOutput,
        tools_used=('conversations_replies',),
        tags=tuple(['conversations']),
    )
    async def replies(self, data: ConversationsRepliesInput) -> ConversationsRepliesOutput:
        """Retrieve a thread of messages posted to a conversation.

Important inputs: token, channel, ts, latest, oldest, inclusive, limit, cursor"""
        tool = self._client.get_tool('conversations_replies')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsRepliesOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_unarchive',
        title='ConversationsUnarchive',
        input_model=ConversationsUnarchiveInput,
        output_model=ConversationsUnarchiveOutput,
        tools_used=('conversations_unarchive',),
        tags=tuple(['conversations']),
    )
    async def unarchive(self, data: ConversationsUnarchiveInput) -> ConversationsUnarchiveOutput:
        """Reverses conversation archival.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_unarchive')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsUnarchiveOutput.model_validate(coerce_tool_result(result))
