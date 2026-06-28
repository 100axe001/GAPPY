from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllScreenTabFieldsToolInput, GetAllScreenTabFieldsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllScreenTabFieldsInput(GetAllScreenTabFieldsToolInput):
    """Operation input for `get_all_screen_tab_fields`."""
    pass

class GetAllScreenTabFieldsOutput(GetAllScreenTabFieldsToolOutput):
    """Operation output for `get_all_screen_tab_fields`."""
    pass

class JiraAllScreenTabFieldsResource(BaseResourceClient):
    """Operations for the `all_screen_tab_fields` resource."""

    @operation(
        name='get_all_screen_tab_fields',
        title='GetAllScreenTabFields',
        input_model=GetAllScreenTabFieldsInput,
        output_model=GetAllScreenTabFieldsOutput,
        tools_used=('get_all_screen_tab_fields',),
        tags=tuple(['Screen tab fields']),
    )
    async def get(self, data: GetAllScreenTabFieldsInput) -> GetAllScreenTabFieldsOutput:
        """Returns all fields for a screen tab. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). * *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.

Important inputs: screen_id, tab_id, project_key"""
        tool = self._client.get_tool('get_all_screen_tab_fields')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllScreenTabFieldsOutput.model_validate(coerce_tool_result(result))
