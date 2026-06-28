from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SetDefaultResolutionToolInput, SetDefaultResolutionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SetDefaultResolutionInput(SetDefaultResolutionToolInput):
    """Operation input for `set_default_resolution`."""
    pass

class SetDefaultResolutionOutput(SetDefaultResolutionToolOutput):
    """Operation output for `set_default_resolution`."""
    pass

class JiraDefaultResolutionResource(BaseResourceClient):
    """Operations for the `default_resolution` resource."""

    @operation(
        name='set_default_resolution',
        title='SetDefaultResolution',
        input_model=SetDefaultResolutionInput,
        output_model=SetDefaultResolutionOutput,
        tools_used=('set_default_resolution',),
        tags=tuple(['Issue resolutions']),
    )
    async def set(self, data: SetDefaultResolutionInput) -> SetDefaultResolutionOutput:
        """Sets default issue resolution. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('set_default_resolution')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetDefaultResolutionOutput.model_validate(coerce_tool_result(result))
