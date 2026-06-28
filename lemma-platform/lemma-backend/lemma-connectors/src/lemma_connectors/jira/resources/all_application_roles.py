from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllApplicationRolesToolInput, GetAllApplicationRolesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllApplicationRolesInput(GetAllApplicationRolesToolInput):
    """Operation input for `get_all_application_roles`."""
    pass

class GetAllApplicationRolesOutput(GetAllApplicationRolesToolOutput):
    """Operation output for `get_all_application_roles`."""
    pass

class JiraAllApplicationRolesResource(BaseResourceClient):
    """Operations for the `all_application_roles` resource."""

    @operation(
        name='get_all_application_roles',
        title='GetAllApplicationRoles',
        input_model=GetAllApplicationRolesInput,
        output_model=GetAllApplicationRolesOutput,
        tools_used=('get_all_application_roles',),
        tags=tuple(['Application roles']),
    )
    async def get(self, data: GetAllApplicationRolesInput) -> GetAllApplicationRolesOutput:
        """Returns all application roles. In Jira, application roles are managed using the [Application access configuration](https://confluence.atlassian.com/x/3YxjL) page. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_all_application_roles')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllApplicationRolesOutput.model_validate(coerce_tool_result(result))
