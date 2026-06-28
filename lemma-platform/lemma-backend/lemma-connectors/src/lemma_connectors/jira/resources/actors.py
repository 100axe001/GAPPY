from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SetActorsToolInput, SetActorsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SetActorsInput(SetActorsToolInput):
    """Operation input for `set_actors`."""
    pass

class SetActorsOutput(SetActorsToolOutput):
    """Operation output for `set_actors`."""
    pass

class JiraActorsResource(BaseResourceClient):
    """Operations for the `actors` resource."""

    @operation(
        name='set_actors',
        title='SetActors',
        input_model=SetActorsInput,
        output_model=SetActorsOutput,
        tools_used=('set_actors',),
        tags=tuple(['Project role actors']),
    )
    async def set(self, data: SetActorsInput) -> SetActorsOutput:
        """Sets the actors for a project role for a project, replacing all existing actors. To add actors to the project without overwriting the existing list, use [Add actors to project role](#api-rest-api-3-project-projectIdOrKey-role-id-post). **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key, id, body"""
        tool = self._client.get_tool('set_actors')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetActorsOutput.model_validate(coerce_tool_result(result))
