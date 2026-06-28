from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetValidProjectNameToolInput, GetValidProjectNameToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetValidProjectNameInput(GetValidProjectNameToolInput):
    """Operation input for `get_valid_project_name`."""
    pass

class GetValidProjectNameOutput(GetValidProjectNameToolOutput):
    """Operation output for `get_valid_project_name`."""
    pass

class JiraValidProjectNameResource(BaseResourceClient):
    """Operations for the `valid_project_name` resource."""

    @operation(
        name='get_valid_project_name',
        title='GetValidProjectName',
        input_model=GetValidProjectNameInput,
        output_model=GetValidProjectNameOutput,
        tools_used=('get_valid_project_name',),
        tags=tuple(['Project key and name validation']),
    )
    async def get(self, data: GetValidProjectNameInput) -> GetValidProjectNameOutput:
        """Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If the name is in use, this operation attempts to generate a valid project name based on the one supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404 response is returned. **[Permissions](#permissions) required:** None.

Important inputs: name"""
        tool = self._client.get_tool('get_valid_project_name')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetValidProjectNameOutput.model_validate(coerce_tool_result(result))
