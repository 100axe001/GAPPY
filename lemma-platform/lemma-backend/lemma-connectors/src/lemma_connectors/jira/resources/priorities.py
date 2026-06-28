from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetPrioritiesToolInput, GetPrioritiesToolOutput, MovePrioritiesToolInput, MovePrioritiesToolOutput, SearchPrioritiesToolInput, SearchPrioritiesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetPrioritiesInput(GetPrioritiesToolInput):
    """Operation input for `get_priorities`."""
    pass

class GetPrioritiesOutput(GetPrioritiesToolOutput):
    """Operation output for `get_priorities`."""
    pass

class MovePrioritiesInput(MovePrioritiesToolInput):
    """Operation input for `move_priorities`."""
    pass

class MovePrioritiesOutput(MovePrioritiesToolOutput):
    """Operation output for `move_priorities`."""
    pass

class SearchPrioritiesInput(SearchPrioritiesToolInput):
    """Operation input for `search_priorities`."""
    pass

class SearchPrioritiesOutput(SearchPrioritiesToolOutput):
    """Operation output for `search_priorities`."""
    pass

class JiraPrioritiesResource(BaseResourceClient):
    """Operations for the `priorities` resource."""

    @operation(
        name='get_priorities',
        title='GetPriorities',
        input_model=GetPrioritiesInput,
        output_model=GetPrioritiesOutput,
        tools_used=('get_priorities',),
        tags=tuple(['Issue priorities']),
    )
    async def get(self, data: GetPrioritiesInput) -> GetPrioritiesOutput:
        """Returns the list of all issue priorities. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_priorities')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetPrioritiesOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='move_priorities',
        title='MovePriorities',
        input_model=MovePrioritiesInput,
        output_model=MovePrioritiesOutput,
        tools_used=('move_priorities',),
        tags=tuple(['Issue priorities']),
    )
    async def move(self, data: MovePrioritiesInput) -> MovePrioritiesOutput:
        """Changes the order of issue priorities. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('move_priorities')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MovePrioritiesOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='search_priorities',
        title='SearchPriorities',
        input_model=SearchPrioritiesInput,
        output_model=SearchPrioritiesOutput,
        tools_used=('search_priorities',),
        tags=tuple(['Issue priorities']),
    )
    async def search(self, data: SearchPrioritiesInput) -> SearchPrioritiesOutput:
        """Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a subset determined by any combination of these criteria: * a list of priority IDs. Any invalid priority IDs are ignored. * whether the field configuration is a default. This returns priorities from company-managed (classic) projects only, as there is no concept of default priorities in team-managed projects. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: start_at, max_results, id, only_default"""
        tool = self._client.get_tool('search_priorities')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SearchPrioritiesOutput.model_validate(coerce_tool_result(result))
