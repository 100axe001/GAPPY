from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetBannerToolInput, GetBannerToolOutput, SetBannerToolInput, SetBannerToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetBannerInput(GetBannerToolInput):
    """Operation input for `get_banner`."""
    pass

class GetBannerOutput(GetBannerToolOutput):
    """Operation output for `get_banner`."""
    pass

class SetBannerInput(SetBannerToolInput):
    """Operation input for `set_banner`."""
    pass

class SetBannerOutput(SetBannerToolOutput):
    """Operation output for `set_banner`."""
    pass

class JiraBannerResource(BaseResourceClient):
    """Operations for the `banner` resource."""

    @operation(
        name='get_banner',
        title='GetBanner',
        input_model=GetBannerInput,
        output_model=GetBannerOutput,
        tools_used=('get_banner',),
        tags=tuple(['Announcement banner']),
    )
    async def get(self, data: GetBannerInput) -> GetBannerOutput:
        """Returns the current announcement banner configuration. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_banner')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetBannerOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_banner',
        title='SetBanner',
        input_model=SetBannerInput,
        output_model=SetBannerOutput,
        tools_used=('set_banner',),
        tags=tuple(['Announcement banner']),
    )
    async def set(self, data: SetBannerInput) -> SetBannerOutput:
        """Updates the announcement banner configuration. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('set_banner')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetBannerOutput.model_validate(coerce_tool_result(result))
