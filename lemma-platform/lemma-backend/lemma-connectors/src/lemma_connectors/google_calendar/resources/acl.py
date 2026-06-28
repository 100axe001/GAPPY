from __future__ import annotations

from lemma_connectors.google_calendar.generated.tool_types import CalendarAclDeleteToolInput, CalendarAclDeleteToolOutput, CalendarAclGetToolInput, CalendarAclGetToolOutput, CalendarAclInsertToolInput, CalendarAclInsertToolOutput, CalendarAclListToolInput, CalendarAclListToolOutput, CalendarAclPatchToolInput, CalendarAclPatchToolOutput, CalendarAclUpdateToolInput, CalendarAclUpdateToolOutput, CalendarAclWatchToolInput, CalendarAclWatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AclDeleteInput(CalendarAclDeleteToolInput):
    """Operation input for `acl_delete`."""
    pass

class AclDeleteOutput(CalendarAclDeleteToolOutput):
    """Operation output for `acl_delete`."""
    pass

class AclGetInput(CalendarAclGetToolInput):
    """Operation input for `acl_get`."""
    pass

class AclGetOutput(CalendarAclGetToolOutput):
    """Operation output for `acl_get`."""
    pass

class AclInsertInput(CalendarAclInsertToolInput):
    """Operation input for `acl_insert`."""
    pass

class AclInsertOutput(CalendarAclInsertToolOutput):
    """Operation output for `acl_insert`."""
    pass

class AclListInput(CalendarAclListToolInput):
    """Operation input for `acl_list`."""
    pass

class AclListOutput(CalendarAclListToolOutput):
    """Operation output for `acl_list`."""
    pass

class AclPatchInput(CalendarAclPatchToolInput):
    """Operation input for `acl_patch`."""
    pass

class AclPatchOutput(CalendarAclPatchToolOutput):
    """Operation output for `acl_patch`."""
    pass

class AclUpdateInput(CalendarAclUpdateToolInput):
    """Operation input for `acl_update`."""
    pass

class AclUpdateOutput(CalendarAclUpdateToolOutput):
    """Operation output for `acl_update`."""
    pass

class AclWatchInput(CalendarAclWatchToolInput):
    """Operation input for `acl_watch`."""
    pass

class AclWatchOutput(CalendarAclWatchToolOutput):
    """Operation output for `acl_watch`."""
    pass

class GoogleCalendarAclResource(BaseResourceClient):
    """Operations for the `acl` resource."""

    @operation(
        name='acl_delete',
        title='AclDelete',
        input_model=AclDeleteInput,
        output_model=AclDeleteOutput,
        tools_used=('calendar_acl_delete',),
        tags=tuple(['acl']),
    )
    async def delete(self, data: AclDeleteInput) -> AclDeleteOutput:
        """Deletes an access control rule.

Important inputs: fields, calendar_id, rule_id"""
        tool = self._client.get_tool('calendar_acl_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AclDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='acl_get',
        title='AclGet',
        input_model=AclGetInput,
        output_model=AclGetOutput,
        tools_used=('calendar_acl_get',),
        tags=tuple(['acl']),
    )
    async def get(self, data: AclGetInput) -> AclGetOutput:
        """Returns an access control rule.

Important inputs: fields, calendar_id, rule_id"""
        tool = self._client.get_tool('calendar_acl_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AclGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='acl_insert',
        title='AclInsert',
        input_model=AclInsertInput,
        output_model=AclInsertOutput,
        tools_used=('calendar_acl_insert',),
        tags=tuple(['acl']),
    )
    async def insert(self, data: AclInsertInput) -> AclInsertOutput:
        """Creates an access control rule.

Important inputs: fields, calendar_id, send_notifications, body"""
        tool = self._client.get_tool('calendar_acl_insert')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AclInsertOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='acl_list',
        title='AclList',
        input_model=AclListInput,
        output_model=AclListOutput,
        tools_used=('calendar_acl_list',),
        tags=tuple(['acl']),
    )
    async def list(self, data: AclListInput) -> AclListOutput:
        """Returns the rules in the access control list for the calendar.

Important inputs: fields, calendar_id, max_results, page_token, show_deleted, sync_token"""
        tool = self._client.get_tool('calendar_acl_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AclListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='acl_patch',
        title='AclPatch',
        input_model=AclPatchInput,
        output_model=AclPatchOutput,
        tools_used=('calendar_acl_patch',),
        tags=tuple(['acl']),
    )
    async def patch(self, data: AclPatchInput) -> AclPatchOutput:
        """Updates an access control rule. This method supports patch semantics.

Important inputs: fields, calendar_id, rule_id, send_notifications, body"""
        tool = self._client.get_tool('calendar_acl_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AclPatchOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='acl_update',
        title='AclUpdate',
        input_model=AclUpdateInput,
        output_model=AclUpdateOutput,
        tools_used=('calendar_acl_update',),
        tags=tuple(['acl']),
    )
    async def update(self, data: AclUpdateInput) -> AclUpdateOutput:
        """Updates an access control rule.

Important inputs: fields, calendar_id, rule_id, send_notifications, body"""
        tool = self._client.get_tool('calendar_acl_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AclUpdateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='acl_watch',
        title='AclWatch',
        input_model=AclWatchInput,
        output_model=AclWatchOutput,
        tools_used=('calendar_acl_watch',),
        tags=tuple(['acl']),
    )
    async def watch(self, data: AclWatchInput) -> AclWatchOutput:
        """Watch for changes to ACL resources.

Important inputs: fields, calendar_id, max_results, page_token, show_deleted, sync_token, body"""
        tool = self._client.get_tool('calendar_acl_watch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AclWatchOutput.model_validate(coerce_tool_result(result))
