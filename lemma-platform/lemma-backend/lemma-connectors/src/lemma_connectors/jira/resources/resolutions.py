from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetResolutionsToolInput, GetResolutionsToolOutput, MoveResolutionsToolInput, MoveResolutionsToolOutput, SearchResolutionsToolInput, SearchResolutionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetResolutionsInput(GetResolutionsToolInput):
    """Operation input for `get_resolutions`."""
    pass

class GetResolutionsOutput(GetResolutionsToolOutput):
    """Operation output for `get_resolutions`."""
    pass

class MoveResolutionsInput(MoveResolutionsToolInput):
    """Operation input for `move_resolutions`."""
    pass

class MoveResolutionsOutput(MoveResolutionsToolOutput):
    """Operation output for `move_resolutions`."""
    pass

class SearchResolutionsInput(SearchResolutionsToolInput):
    """Operation input for `search_resolutions`."""
    pass

class SearchResolutionsOutput(SearchResolutionsToolOutput):
    """Operation output for `search_resolutions`."""
    pass

class JiraResolutionsResource(BaseResourceClient):
    """Operations for the `resolutions` resource."""

    @operation(
        name='get_resolutions',
        title='GetResolutions',
        input_model=GetResolutionsInput,
        output_model=GetResolutionsOutput,
        tools_used=('get_resolutions',),
        tags=tuple(['Issue resolutions']),
    )
    async def get(self, data: GetResolutionsInput) -> GetResolutionsOutput:
        """Returns a list of all issue resolution values. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_resolutions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetResolutionsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='move_resolutions',
        title='MoveResolutions',
        input_model=MoveResolutionsInput,
        output_model=MoveResolutionsOutput,
        tools_used=('move_resolutions',),
        tags=tuple(['Issue resolutions']),
    )
    async def move(self, data: MoveResolutionsInput) -> MoveResolutionsOutput:
        """Changes the order of issue resolutions. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('move_resolutions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MoveResolutionsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='search_resolutions',
        title='SearchResolutions',
        input_model=SearchResolutionsInput,
        output_model=SearchResolutionsOutput,
        tools_used=('search_resolutions',),
        tags=tuple(['Issue resolutions']),
    )
    async def search(self, data: SearchResolutionsInput) -> SearchResolutionsOutput:
        """Returns a [paginated](#pagination) list of resolutions. The list can contain all resolutions or a subset determined by any combination of these criteria: * a list of resolutions IDs. * whether the field configuration is a default. This returns resolutions from company-managed (classic) projects only, as there is no concept of default resolutions in team-managed projects. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: start_at, max_results, id, only_default"""
        tool = self._client.get_tool('search_resolutions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SearchResolutionsOutput.model_validate(coerce_tool_result(result))
