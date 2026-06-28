from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectPropertyKeysToolInput, GetProjectPropertyKeysToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectPropertyKeysInput(GetProjectPropertyKeysToolInput):
    """Operation input for `get_project_property_keys`."""
    pass

class GetProjectPropertyKeysOutput(GetProjectPropertyKeysToolOutput):
    """Operation output for `get_project_property_keys`."""
    pass

class JiraProjectPropertyKeysResource(BaseResourceClient):
    """Operations for the `project_property_keys` resource."""

    @operation(
        name='get_project_property_keys',
        title='GetProjectPropertyKeys',
        input_model=GetProjectPropertyKeysInput,
        output_model=GetProjectPropertyKeysOutput,
        tools_used=('get_project_property_keys',),
        tags=tuple(['Project properties']),
    )
    async def get(self, data: GetProjectPropertyKeysInput) -> GetProjectPropertyKeysOutput:
        """Returns all [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys for the project. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id_or_key"""
        tool = self._client.get_tool('get_project_property_keys')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectPropertyKeysOutput.model_validate(coerce_tool_result(result))
