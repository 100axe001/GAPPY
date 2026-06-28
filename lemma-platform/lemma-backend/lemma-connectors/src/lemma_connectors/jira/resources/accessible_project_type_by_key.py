from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAccessibleProjectTypeByKeyToolInput, GetAccessibleProjectTypeByKeyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAccessibleProjectTypeByKeyInput(GetAccessibleProjectTypeByKeyToolInput):
    """Operation input for `get_accessible_project_type_by_key`."""
    pass

class GetAccessibleProjectTypeByKeyOutput(GetAccessibleProjectTypeByKeyToolOutput):
    """Operation output for `get_accessible_project_type_by_key`."""
    pass

class JiraAccessibleProjectTypeByKeyResource(BaseResourceClient):
    """Operations for the `accessible_project_type_by_key` resource."""

    @operation(
        name='get_accessible_project_type_by_key',
        title='GetAccessibleProjectTypeByKey',
        input_model=GetAccessibleProjectTypeByKeyInput,
        output_model=GetAccessibleProjectTypeByKeyOutput,
        tools_used=('get_accessible_project_type_by_key',),
        tags=tuple(['Project types']),
    )
    async def get(self, data: GetAccessibleProjectTypeByKeyInput) -> GetAccessibleProjectTypeByKeyOutput:
        """Returns a [project type](https://confluence.atlassian.com/x/Var1Nw) if it is accessible to the user. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: project_type_key"""
        tool = self._client.get_tool('get_accessible_project_type_by_key')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAccessibleProjectTypeByKeyOutput.model_validate(coerce_tool_result(result))
