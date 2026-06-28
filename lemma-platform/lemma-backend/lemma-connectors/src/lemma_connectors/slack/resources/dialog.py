from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import DialogOpenToolInput, DialogOpenToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DialogOpenInput(DialogOpenToolInput):
    """Operation input for `dialog_open`."""
    pass

class DialogOpenOutput(DialogOpenToolOutput):
    """Operation output for `dialog_open`."""
    pass

class SlackDialogResource(BaseResourceClient):
    """Operations for the `dialog` resource."""

    @operation(
        name='dialog_open',
        title='DialogOpen',
        input_model=DialogOpenInput,
        output_model=DialogOpenOutput,
        tools_used=('dialog_open',),
        tags=tuple(['dialog']),
    )
    async def open(self, data: DialogOpenInput) -> DialogOpenOutput:
        """Open a dialog with a user.

Important inputs: token, dialog, trigger_id"""
        tool = self._client.get_tool('dialog_open')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DialogOpenOutput.model_validate(coerce_tool_result(result))
