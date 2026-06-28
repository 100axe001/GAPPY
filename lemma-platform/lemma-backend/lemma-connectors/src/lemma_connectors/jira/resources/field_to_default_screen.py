from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddFieldToDefaultScreenToolInput, AddFieldToDefaultScreenToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddFieldToDefaultScreenInput(AddFieldToDefaultScreenToolInput):
    """Operation input for `add_field_to_default_screen`."""
    pass

class AddFieldToDefaultScreenOutput(AddFieldToDefaultScreenToolOutput):
    """Operation output for `add_field_to_default_screen`."""
    pass

class JiraFieldToDefaultScreenResource(BaseResourceClient):
    """Operations for the `field_to_default_screen` resource."""

    @operation(
        name='add_field_to_default_screen',
        title='AddFieldToDefaultScreen',
        input_model=AddFieldToDefaultScreenInput,
        output_model=AddFieldToDefaultScreenOutput,
        tools_used=('add_field_to_default_screen',),
        tags=tuple(['Screens']),
    )
    async def add(self, data: AddFieldToDefaultScreenInput) -> AddFieldToDefaultScreenOutput:
        """Adds a field to the default tab of the default screen. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id"""
        tool = self._client.get_tool('add_field_to_default_screen')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddFieldToDefaultScreenOutput.model_validate(coerce_tool_result(result))
