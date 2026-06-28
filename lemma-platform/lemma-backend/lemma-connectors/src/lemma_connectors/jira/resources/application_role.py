from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetApplicationRoleToolInput, GetApplicationRoleToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetApplicationRoleInput(GetApplicationRoleToolInput):
    """Operation input for `get_application_role`."""
    pass

class GetApplicationRoleOutput(GetApplicationRoleToolOutput):
    """Operation output for `get_application_role`."""
    pass

class JiraApplicationRoleResource(BaseResourceClient):
    """Operations for the `application_role` resource."""

    @operation(
        name='get_application_role',
        title='GetApplicationRole',
        input_model=GetApplicationRoleInput,
        output_model=GetApplicationRoleOutput,
        tools_used=('get_application_role',),
        tags=tuple(['Application roles']),
    )
    async def get(self, data: GetApplicationRoleInput) -> GetApplicationRoleOutput:
        """Returns an application role. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_application_role')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetApplicationRoleOutput.model_validate(coerce_tool_result(result))
