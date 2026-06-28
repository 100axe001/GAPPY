from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetSecurityLevelsForProjectToolInput, GetSecurityLevelsForProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetSecurityLevelsForProjectInput(GetSecurityLevelsForProjectToolInput):
    """Operation input for `get_security_levels_for_project`."""
    pass

class GetSecurityLevelsForProjectOutput(GetSecurityLevelsForProjectToolOutput):
    """Operation output for `get_security_levels_for_project`."""
    pass

class JiraSecurityLevelsForProjectResource(BaseResourceClient):
    """Operations for the `security_levels_for_project` resource."""

    @operation(
        name='get_security_levels_for_project',
        title='GetSecurityLevelsForProject',
        input_model=GetSecurityLevelsForProjectInput,
        output_model=GetSecurityLevelsForProjectOutput,
        tools_used=('get_security_levels_for_project',),
        tags=tuple(['Project permission schemes']),
    )
    async def get(self, data: GetSecurityLevelsForProjectInput) -> GetSecurityLevelsForProjectOutput:
        """Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that the user has access to. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security levels are only returned for authenticated user with *Set Issue Security* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project.

Important inputs: project_key_or_id"""
        tool = self._client.get_tool('get_security_levels_for_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetSecurityLevelsForProjectOutput.model_validate(coerce_tool_result(result))
