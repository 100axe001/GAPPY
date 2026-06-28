from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SetDefaultPriorityToolInput, SetDefaultPriorityToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SetDefaultPriorityInput(SetDefaultPriorityToolInput):
    """Operation input for `set_default_priority`."""
    pass

class SetDefaultPriorityOutput(SetDefaultPriorityToolOutput):
    """Operation output for `set_default_priority`."""
    pass

class JiraDefaultPriorityResource(BaseResourceClient):
    """Operations for the `default_priority` resource."""

    @operation(
        name='set_default_priority',
        title='SetDefaultPriority',
        input_model=SetDefaultPriorityInput,
        output_model=SetDefaultPriorityOutput,
        tools_used=('set_default_priority',),
        tags=tuple(['Issue priorities']),
    )
    async def set(self, data: SetDefaultPriorityInput) -> SetDefaultPriorityOutput:
        """Sets default issue priority. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('set_default_priority')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetDefaultPriorityOutput.model_validate(coerce_tool_result(result))
