from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectTypeByKeyToolInput, GetProjectTypeByKeyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectTypeByKeyInput(GetProjectTypeByKeyToolInput):
    """Operation input for `get_project_type_by_key`."""
    pass

class GetProjectTypeByKeyOutput(GetProjectTypeByKeyToolOutput):
    """Operation output for `get_project_type_by_key`."""
    pass

class JiraProjectTypeByKeyResource(BaseResourceClient):
    """Operations for the `project_type_by_key` resource."""

    @operation(
        name='get_project_type_by_key',
        title='GetProjectTypeByKey',
        input_model=GetProjectTypeByKeyInput,
        output_model=GetProjectTypeByKeyOutput,
        tools_used=('get_project_type_by_key',),
        tags=tuple(['Project types']),
    )
    async def get(self, data: GetProjectTypeByKeyInput) -> GetProjectTypeByKeyOutput:
        """Returns a [project type](https://confluence.atlassian.com/x/Var1Nw). This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: project_type_key"""
        tool = self._client.get_tool('get_project_type_by_key')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectTypeByKeyOutput.model_validate(coerce_tool_result(result))
