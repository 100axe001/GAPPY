from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteProjectPropertyToolInput, DeleteProjectPropertyToolOutput, GetProjectPropertyToolInput, GetProjectPropertyToolOutput, SetProjectPropertyToolInput, SetProjectPropertyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteProjectPropertyInput(DeleteProjectPropertyToolInput):
    """Operation input for `delete_project_property`."""
    pass

class DeleteProjectPropertyOutput(DeleteProjectPropertyToolOutput):
    """Operation output for `delete_project_property`."""
    pass

class GetProjectPropertyInput(GetProjectPropertyToolInput):
    """Operation input for `get_project_property`."""
    pass

class GetProjectPropertyOutput(GetProjectPropertyToolOutput):
    """Operation output for `get_project_property`."""
    pass

class SetProjectPropertyInput(SetProjectPropertyToolInput):
    """Operation input for `set_project_property`."""
    pass

class SetProjectPropertyOutput(SetProjectPropertyToolOutput):
    """Operation output for `set_project_property`."""
    pass

class JiraProjectPropertyResource(BaseResourceClient):
    """Operations for the `project_property` resource."""

    @operation(
        name='delete_project_property',
        title='DeleteProjectProperty',
        input_model=DeleteProjectPropertyInput,
        output_model=DeleteProjectPropertyOutput,
        tools_used=('delete_project_property',),
        tags=tuple(['Project properties']),
    )
    async def delete(self, data: DeleteProjectPropertyInput) -> DeleteProjectPropertyOutput:
        """Deletes the [property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) from a project. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.

Important inputs: project_id_or_key, property_key"""
        tool = self._client.get_tool('delete_project_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteProjectPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_project_property',
        title='GetProjectProperty',
        input_model=GetProjectPropertyInput,
        output_model=GetProjectPropertyOutput,
        tools_used=('get_project_property',),
        tags=tuple(['Project properties']),
    )
    async def get(self, data: GetProjectPropertyInput) -> GetProjectPropertyOutput:
        """Returns the value of a [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.

Important inputs: project_id_or_key, property_key"""
        tool = self._client.get_tool('get_project_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_project_property',
        title='SetProjectProperty',
        input_model=SetProjectPropertyInput,
        output_model=SetProjectPropertyOutput,
        tools_used=('set_project_property',),
        tags=tuple(['Project properties']),
    )
    async def set(self, data: SetProjectPropertyInput) -> SetProjectPropertyOutput:
        """Sets the value of the [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). You can use project properties to store custom data against the project. The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the property is created.

Important inputs: project_id_or_key, property_key, body"""
        tool = self._client.get_tool('set_project_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetProjectPropertyOutput.model_validate(coerce_tool_result(result))
