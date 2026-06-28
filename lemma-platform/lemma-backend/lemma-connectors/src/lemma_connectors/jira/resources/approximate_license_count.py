from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetApproximateLicenseCountToolInput, GetApproximateLicenseCountToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetApproximateLicenseCountInput(GetApproximateLicenseCountToolInput):
    """Operation input for `get_approximate_license_count`."""
    pass

class GetApproximateLicenseCountOutput(GetApproximateLicenseCountToolOutput):
    """Operation output for `get_approximate_license_count`."""
    pass

class JiraApproximateLicenseCountResource(BaseResourceClient):
    """Operations for the `approximate_license_count` resource."""

    @operation(
        name='get_approximate_license_count',
        title='GetApproximateLicenseCount',
        input_model=GetApproximateLicenseCountInput,
        output_model=GetApproximateLicenseCountOutput,
        tools_used=('get_approximate_license_count',),
        tags=tuple(['License metrics']),
    )
    async def get(self, data: GetApproximateLicenseCountInput) -> GetApproximateLicenseCountOutput:
        """Returns the total approximate user account across all jira licenced application keys. Please note this information is cached with a 7-day lifecycle and could be stale at the time of call. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_approximate_license_count')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetApproximateLicenseCountOutput.model_validate(coerce_tool_result(result))
