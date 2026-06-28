from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersLabelsCreateToolInput, GmailUsersLabelsCreateToolOutput, GmailUsersLabelsDeleteToolInput, GmailUsersLabelsDeleteToolOutput, GmailUsersLabelsGetToolInput, GmailUsersLabelsGetToolOutput, GmailUsersLabelsListToolInput, GmailUsersLabelsListToolOutput, GmailUsersLabelsPatchToolInput, GmailUsersLabelsPatchToolOutput, GmailUsersLabelsUpdateToolInput, GmailUsersLabelsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class LabelsCreateInput(GmailUsersLabelsCreateToolInput):
    """Operation input for `labels_create`."""
    pass

class LabelsCreateOutput(GmailUsersLabelsCreateToolOutput):
    """Operation output for `labels_create`."""
    pass

class LabelsDeleteInput(GmailUsersLabelsDeleteToolInput):
    """Operation input for `labels_delete`."""
    pass

class LabelsDeleteOutput(GmailUsersLabelsDeleteToolOutput):
    """Operation output for `labels_delete`."""
    pass

class LabelsGetInput(GmailUsersLabelsGetToolInput):
    """Operation input for `labels_get`."""
    pass

class LabelsGetOutput(GmailUsersLabelsGetToolOutput):
    """Operation output for `labels_get`."""
    pass

class LabelsListInput(GmailUsersLabelsListToolInput):
    """Operation input for `labels_list`."""
    pass

class LabelsListOutput(GmailUsersLabelsListToolOutput):
    """Operation output for `labels_list`."""
    pass

class LabelsPatchInput(GmailUsersLabelsPatchToolInput):
    """Operation input for `labels_patch`."""
    pass

class LabelsPatchOutput(GmailUsersLabelsPatchToolOutput):
    """Operation output for `labels_patch`."""
    pass

class LabelsUpdateInput(GmailUsersLabelsUpdateToolInput):
    """Operation input for `labels_update`."""
    pass

class LabelsUpdateOutput(GmailUsersLabelsUpdateToolOutput):
    """Operation output for `labels_update`."""
    pass

class GmailLabelsResource(BaseResourceClient):
    """Operations for the `labels` resource."""

    @operation(
        name='labels_create',
        title='LabelsCreate',
        input_model=LabelsCreateInput,
        output_model=LabelsCreateOutput,
        tools_used=('gmail_users_labels_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: LabelsCreateInput) -> LabelsCreateOutput:
        """Creates a new label.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_labels_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return LabelsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='labels_delete',
        title='LabelsDelete',
        input_model=LabelsDeleteInput,
        output_model=LabelsDeleteOutput,
        tools_used=('gmail_users_labels_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: LabelsDeleteInput) -> LabelsDeleteOutput:
        """Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_labels_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return LabelsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='labels_get',
        title='LabelsGet',
        input_model=LabelsGetInput,
        output_model=LabelsGetOutput,
        tools_used=('gmail_users_labels_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: LabelsGetInput) -> LabelsGetOutput:
        """Gets the specified label.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_labels_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return LabelsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='labels_list',
        title='LabelsList',
        input_model=LabelsListInput,
        output_model=LabelsListOutput,
        tools_used=('gmail_users_labels_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: LabelsListInput) -> LabelsListOutput:
        """Lists all labels in the user's mailbox.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_labels_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return LabelsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='labels_patch',
        title='LabelsPatch',
        input_model=LabelsPatchInput,
        output_model=LabelsPatchOutput,
        tools_used=('gmail_users_labels_patch',),
        tags=tuple(['users']),
    )
    async def patch(self, data: LabelsPatchInput) -> LabelsPatchOutput:
        """Patch the specified label.

Important inputs: fields, user_id, id, body"""
        tool = self._client.get_tool('gmail_users_labels_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return LabelsPatchOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='labels_update',
        title='LabelsUpdate',
        input_model=LabelsUpdateInput,
        output_model=LabelsUpdateOutput,
        tools_used=('gmail_users_labels_update',),
        tags=tuple(['users']),
    )
    async def update(self, data: LabelsUpdateInput) -> LabelsUpdateOutput:
        """Updates the specified label.

Important inputs: fields, user_id, id, body"""
        tool = self._client.get_tool('gmail_users_labels_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return LabelsUpdateOutput.model_validate(coerce_tool_result(result))
