from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFieldsToolInput, GetFieldsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFieldsInput(GetFieldsToolInput):
    """Operation input for `get_fields`."""
    pass

class GetFieldsOutput(GetFieldsToolOutput):
    """Operation output for `get_fields`."""
    pass

class JiraFieldsResource(BaseResourceClient):
    """Operations for the `fields` resource."""

    @operation(
        name='get_fields',
        title='GetFields',
        input_model=GetFieldsInput,
        output_model=GetFieldsOutput,
        tools_used=('get_fields',),
        tags=tuple(['Issue fields']),
    )
    async def get(self, data: GetFieldsInput) -> GetFieldsOutput:
        """Returns system and custom issue fields according to the following rules: * Fields that cannot be added to the issue navigator are always returned. * Fields that cannot be placed on an issue screen are always returned. * Fields that depend on global Jira settings are only returned if the setting is enabled. That is, timetracking fields, subtasks, votes, and watches. * For all other fields, this operation only returns the fields that the user has permission to view (that is, the field is used in at least one project that the user has *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.) This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_fields')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFieldsOutput.model_validate(coerce_tool_result(result))
