from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import UpdateProjectTypeToolInput, UpdateProjectTypeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UpdateProjectTypeInput(UpdateProjectTypeToolInput):
    """Operation input for `update_project_type`."""
    pass

class UpdateProjectTypeOutput(UpdateProjectTypeToolOutput):
    """Operation output for `update_project_type`."""
    pass

class JiraProjectTypeResource(BaseResourceClient):
    """Operations for the `project_type` resource."""

    @operation(
        name='update_project_type',
        title='UpdateProjectType',
        input_model=UpdateProjectTypeInput,
        output_model=UpdateProjectTypeOutput,
        tools_used=('update_project_type',),
        tags=tuple(['Projects']),
    )
    async def update(self, data: UpdateProjectTypeInput) -> UpdateProjectTypeOutput:
        """Deprecated, this feature is no longer supported and no alternatives are available, see [Convert project to a different template or type](https://confluence.atlassian.com/x/yEKeOQ). Updates a [project type](https://confluence.atlassian.com/x/GwiiLQ). The project type can be updated for classic projects only, project type cannot be updated for next-gen projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key, new_project_type_key"""
        tool = self._client.get_tool('update_project_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateProjectTypeOutput.model_validate(coerce_tool_result(result))
