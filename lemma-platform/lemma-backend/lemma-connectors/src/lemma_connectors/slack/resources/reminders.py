from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import RemindersAddToolInput, RemindersAddToolOutput, RemindersCompleteToolInput, RemindersCompleteToolOutput, RemindersDeleteToolInput, RemindersDeleteToolOutput, RemindersInfoToolInput, RemindersInfoToolOutput, RemindersListToolInput, RemindersListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RemindersAddInput(RemindersAddToolInput):
    """Operation input for `reminders_add`."""
    pass

class RemindersAddOutput(RemindersAddToolOutput):
    """Operation output for `reminders_add`."""
    pass

class RemindersCompleteInput(RemindersCompleteToolInput):
    """Operation input for `reminders_complete`."""
    pass

class RemindersCompleteOutput(RemindersCompleteToolOutput):
    """Operation output for `reminders_complete`."""
    pass

class RemindersDeleteInput(RemindersDeleteToolInput):
    """Operation input for `reminders_delete`."""
    pass

class RemindersDeleteOutput(RemindersDeleteToolOutput):
    """Operation output for `reminders_delete`."""
    pass

class RemindersInfoInput(RemindersInfoToolInput):
    """Operation input for `reminders_info`."""
    pass

class RemindersInfoOutput(RemindersInfoToolOutput):
    """Operation output for `reminders_info`."""
    pass

class RemindersListInput(RemindersListToolInput):
    """Operation input for `reminders_list`."""
    pass

class RemindersListOutput(RemindersListToolOutput):
    """Operation output for `reminders_list`."""
    pass

class SlackRemindersResource(BaseResourceClient):
    """Operations for the `reminders` resource."""

    @operation(
        name='reminders_add',
        title='RemindersAdd',
        input_model=RemindersAddInput,
        output_model=RemindersAddOutput,
        tools_used=('reminders_add',),
        tags=tuple(['reminders']),
    )
    async def add(self, data: RemindersAddInput) -> RemindersAddOutput:
        """Creates a reminder.

Important inputs: token, body"""
        tool = self._client.get_tool('reminders_add')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemindersAddOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='reminders_complete',
        title='RemindersComplete',
        input_model=RemindersCompleteInput,
        output_model=RemindersCompleteOutput,
        tools_used=('reminders_complete',),
        tags=tuple(['reminders']),
    )
    async def complete(self, data: RemindersCompleteInput) -> RemindersCompleteOutput:
        """Marks a reminder as complete.

Important inputs: token, body"""
        tool = self._client.get_tool('reminders_complete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemindersCompleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='reminders_delete',
        title='RemindersDelete',
        input_model=RemindersDeleteInput,
        output_model=RemindersDeleteOutput,
        tools_used=('reminders_delete',),
        tags=tuple(['reminders']),
    )
    async def delete(self, data: RemindersDeleteInput) -> RemindersDeleteOutput:
        """Deletes a reminder.

Important inputs: token, body"""
        tool = self._client.get_tool('reminders_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemindersDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='reminders_info',
        title='RemindersInfo',
        input_model=RemindersInfoInput,
        output_model=RemindersInfoOutput,
        tools_used=('reminders_info',),
        tags=tuple(['reminders']),
    )
    async def info(self, data: RemindersInfoInput) -> RemindersInfoOutput:
        """Gets information about a reminder.

Important inputs: token, reminder"""
        tool = self._client.get_tool('reminders_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemindersInfoOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='reminders_list',
        title='RemindersList',
        input_model=RemindersListInput,
        output_model=RemindersListOutput,
        tools_used=('reminders_list',),
        tags=tuple(['reminders']),
    )
    async def list(self, data: RemindersListInput) -> RemindersListOutput:
        """Lists all reminders created by or for a given user.

Important inputs: token"""
        tool = self._client.get_tool('reminders_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemindersListOutput.model_validate(coerce_tool_result(result))
