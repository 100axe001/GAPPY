from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateFilterToolInput, CreateFilterToolOutput, DeleteFilterToolInput, DeleteFilterToolOutput, GetFilterToolInput, GetFilterToolOutput, UpdateFilterToolInput, UpdateFilterToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateFilterInput(CreateFilterToolInput):
    """Operation input for `create_filter`."""
    pass

class CreateFilterOutput(CreateFilterToolOutput):
    """Operation output for `create_filter`."""
    pass

class DeleteFilterInput(DeleteFilterToolInput):
    """Operation input for `delete_filter`."""
    pass

class DeleteFilterOutput(DeleteFilterToolOutput):
    """Operation output for `delete_filter`."""
    pass

class GetFilterInput(GetFilterToolInput):
    """Operation input for `get_filter`."""
    pass

class GetFilterOutput(GetFilterToolOutput):
    """Operation output for `get_filter`."""
    pass

class UpdateFilterInput(UpdateFilterToolInput):
    """Operation input for `update_filter`."""
    pass

class UpdateFilterOutput(UpdateFilterToolOutput):
    """Operation output for `update_filter`."""
    pass

class JiraFilterResource(BaseResourceClient):
    """Operations for the `filter` resource."""

    @operation(
        name='create_filter',
        title='CreateFilter',
        input_model=CreateFilterInput,
        output_model=CreateFilterOutput,
        tools_used=('create_filter',),
        tags=tuple(['Filters']),
    )
    async def create(self, data: CreateFilterInput) -> CreateFilterOutput:
        """Creates a filter. The filter is shared according to the [default share scope](#api-rest-api-3-filter-post). The filter is not selected as a favorite. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: expand, override_share_permissions, body"""
        tool = self._client.get_tool('create_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateFilterOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_filter',
        title='DeleteFilter',
        input_model=DeleteFilterInput,
        output_model=DeleteFilterOutput,
        tools_used=('delete_filter',),
        tags=tuple(['Filters']),
    )
    async def delete(self, data: DeleteFilterInput) -> DeleteFilterOutput:
        """Delete a filter. **[Permissions](#permissions) required:** Permission to access Jira, however filters can only be deleted by the creator of the filter or a user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('delete_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteFilterOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_filter',
        title='GetFilter',
        input_model=GetFilterInput,
        output_model=GetFilterOutput,
        tools_used=('get_filter',),
        tags=tuple(['Filters']),
    )
    async def get(self, data: GetFilterInput) -> GetFilterOutput:
        """Returns a filter. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None, however, the filter is only returned where it is: * owned by the user. * shared with a group that the user is a member of. * shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * shared with a public project. * shared with the public.

Important inputs: id, expand, override_share_permissions"""
        tool = self._client.get_tool('get_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFilterOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_filter',
        title='UpdateFilter',
        input_model=UpdateFilterInput,
        output_model=UpdateFilterOutput,
        tools_used=('update_filter',),
        tags=tuple(['Filters']),
    )
    async def update(self, data: UpdateFilterInput) -> UpdateFilterOutput:
        """Updates a filter. Use this operation to update a filter's name, description, JQL, or sharing. **[Permissions](#permissions) required:** Permission to access Jira, however the user must own the filter.

Important inputs: id, expand, override_share_permissions, body"""
        tool = self._client.get_tool('update_filter')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateFilterOutput.model_validate(coerce_tool_result(result))
