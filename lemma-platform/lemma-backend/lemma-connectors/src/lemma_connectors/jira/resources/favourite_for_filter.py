from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteFavouriteForFilterToolInput, DeleteFavouriteForFilterToolOutput, SetFavouriteForFilterToolInput, SetFavouriteForFilterToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteFavouriteForFilterInput(DeleteFavouriteForFilterToolInput):
    """Operation input for `delete_favourite_for_filter`."""
    pass

class DeleteFavouriteForFilterOutput(DeleteFavouriteForFilterToolOutput):
    """Operation output for `delete_favourite_for_filter`."""
    pass

class SetFavouriteForFilterInput(SetFavouriteForFilterToolInput):
    """Operation input for `set_favourite_for_filter`."""
    pass

class SetFavouriteForFilterOutput(SetFavouriteForFilterToolOutput):
    """Operation output for `set_favourite_for_filter`."""
    pass

class JiraFavouriteForFilterResource(BaseResourceClient):
    """Operations for the `favourite_for_filter` resource."""

    @operation(
        name='delete_favourite_for_filter',
        title='DeleteFavouriteForFilter',
        input_model=DeleteFavouriteForFilterInput,
        output_model=DeleteFavouriteForFilterOutput,
        tools_used=('delete_favourite_for_filter',),
        tags=tuple(['Filters']),
    )
    async def delete(self, data: DeleteFavouriteForFilterInput) -> DeleteFavouriteForFilterOutput:
        """Removes a filter as a favorite for the user. Note that this operation only removes filters visible to the user from the user's favorites list. For example, if the user favorites a public filter that is subsequently made private (and is therefore no longer visible on their favorites list) they cannot remove it from their favorites list. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: id, expand"""
        tool = self._client.get_tool('delete_favourite_for_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteFavouriteForFilterOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_favourite_for_filter',
        title='SetFavouriteForFilter',
        input_model=SetFavouriteForFilterInput,
        output_model=SetFavouriteForFilterOutput,
        tools_used=('set_favourite_for_filter',),
        tags=tuple(['Filters']),
    )
    async def set(self, data: SetFavouriteForFilterInput) -> SetFavouriteForFilterOutput:
        """Add a filter as a favorite for the user. **[Permissions](#permissions) required:** Permission to access Jira, however, the user can only favorite: * filters owned by the user. * filters shared with a group that the user is a member of. * filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * filters shared with a public project. * filters shared with the public.

Important inputs: id, expand"""
        tool = self._client.get_tool('set_favourite_for_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetFavouriteForFilterOutput.model_validate(coerce_tool_result(result))
