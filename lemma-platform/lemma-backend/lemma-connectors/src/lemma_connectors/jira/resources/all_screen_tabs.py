from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllScreenTabsToolInput, GetAllScreenTabsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllScreenTabsInput(GetAllScreenTabsToolInput):
    """Operation input for `get_all_screen_tabs`."""
    pass

class GetAllScreenTabsOutput(GetAllScreenTabsToolOutput):
    """Operation output for `get_all_screen_tabs`."""
    pass

class JiraAllScreenTabsResource(BaseResourceClient):
    """Operations for the `all_screen_tabs` resource."""

    @operation(
        name='get_all_screen_tabs',
        title='GetAllScreenTabs',
        input_model=GetAllScreenTabsInput,
        output_model=GetAllScreenTabsOutput,
        tools_used=('get_all_screen_tabs',),
        tags=tuple(['Screen tabs']),
    )
    async def get(self, data: GetAllScreenTabsInput) -> GetAllScreenTabsOutput:
        """Returns the list of tabs for a screen. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). * *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.

Important inputs: screen_id, project_key"""
        tool = self._client.get_tool('get_all_screen_tabs')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllScreenTabsOutput.model_validate(coerce_tool_result(result))
