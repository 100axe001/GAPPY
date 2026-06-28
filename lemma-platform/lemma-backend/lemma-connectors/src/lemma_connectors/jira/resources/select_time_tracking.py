from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SelectTimeTrackingImplementationToolInput, SelectTimeTrackingImplementationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SelectTimeTrackingImplementationInput(SelectTimeTrackingImplementationToolInput):
    """Operation input for `select_time_tracking_implementation`."""
    pass

class SelectTimeTrackingImplementationOutput(SelectTimeTrackingImplementationToolOutput):
    """Operation output for `select_time_tracking_implementation`."""
    pass

class JiraSelectTimeTrackingResource(BaseResourceClient):
    """Operations for the `select_time_tracking` resource."""

    @operation(
        name='select_time_tracking_implementation',
        title='SelectTimeTrackingImplementation',
        input_model=SelectTimeTrackingImplementationInput,
        output_model=SelectTimeTrackingImplementationOutput,
        tools_used=('select_time_tracking_implementation',),
        tags=tuple(['Time tracking']),
    )
    async def implementation(self, data: SelectTimeTrackingImplementationInput) -> SelectTimeTrackingImplementationOutput:
        """Selects a time tracking provider. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('select_time_tracking_implementation')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SelectTimeTrackingImplementationOutput.model_validate(coerce_tool_result(result))
