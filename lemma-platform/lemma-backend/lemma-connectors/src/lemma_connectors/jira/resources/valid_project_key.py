from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetValidProjectKeyToolInput, GetValidProjectKeyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetValidProjectKeyInput(GetValidProjectKeyToolInput):
    """Operation input for `get_valid_project_key`."""
    pass

class GetValidProjectKeyOutput(GetValidProjectKeyToolOutput):
    """Operation output for `get_valid_project_key`."""
    pass

class JiraValidProjectKeyResource(BaseResourceClient):
    """Operations for the `valid_project_key` resource."""

    @operation(
        name='get_valid_project_key',
        title='GetValidProjectKey',
        input_model=GetValidProjectKeyInput,
        output_model=GetValidProjectKeyOutput,
        tools_used=('get_valid_project_key',),
        tags=tuple(['Project key and name validation']),
    )
    async def get(self, data: GetValidProjectKeyInput) -> GetValidProjectKeyOutput:
        """Validates a project key and, if the key is invalid or in use, generates a valid random string for the project key. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_valid_project_key')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetValidProjectKeyOutput.model_validate(coerce_tool_result(result))
