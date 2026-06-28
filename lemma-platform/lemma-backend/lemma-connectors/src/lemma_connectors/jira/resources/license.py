from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetLicenseToolInput, GetLicenseToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetLicenseInput(GetLicenseToolInput):
    """Operation input for `get_license`."""
    pass

class GetLicenseOutput(GetLicenseToolOutput):
    """Operation output for `get_license`."""
    pass

class JiraLicenseResource(BaseResourceClient):
    """Operations for the `license` resource."""

    @operation(
        name='get_license',
        title='GetLicense',
        input_model=GetLicenseInput,
        output_model=GetLicenseOutput,
        tools_used=('get_license',),
        tags=tuple(['Instance information']),
    )
    async def get(self, data: GetLicenseInput) -> GetLicenseOutput:
        """Returns licensing information about the Jira instance. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_license')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetLicenseOutput.model_validate(coerce_tool_result(result))
