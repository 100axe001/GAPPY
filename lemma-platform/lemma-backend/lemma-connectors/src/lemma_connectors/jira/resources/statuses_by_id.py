from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteStatusesByIdToolInput, DeleteStatusesByIdToolOutput, GetStatusesByIdToolInput, GetStatusesByIdToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteStatusesByIdInput(DeleteStatusesByIdToolInput):
    """Operation input for `delete_statuses_by_id`."""
    pass

class DeleteStatusesByIdOutput(DeleteStatusesByIdToolOutput):
    """Operation output for `delete_statuses_by_id`."""
    pass

class GetStatusesByIdInput(GetStatusesByIdToolInput):
    """Operation input for `get_statuses_by_id`."""
    pass

class GetStatusesByIdOutput(GetStatusesByIdToolOutput):
    """Operation output for `get_statuses_by_id`."""
    pass

class JiraStatusesByIdResource(BaseResourceClient):
    """Operations for the `statuses_by_id` resource."""

    @operation(
        name='delete_statuses_by_id',
        title='DeleteStatusesById',
        input_model=DeleteStatusesByIdInput,
        output_model=DeleteStatusesByIdOutput,
        tools_used=('delete_statuses_by_id',),
        tags=tuple(['Status']),
    )
    async def delete(self, data: DeleteStatusesByIdInput) -> DeleteStatusesByIdOutput:
        """Deletes statuses by ID. **[Permissions](#permissions) required:** * *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg) * *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg).

Important inputs: id"""
        tool = self._client.get_tool('delete_statuses_by_id')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteStatusesByIdOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_statuses_by_id',
        title='GetStatusesById',
        input_model=GetStatusesByIdInput,
        output_model=GetStatusesByIdOutput,
        tools_used=('get_statuses_by_id',),
        tags=tuple(['Status']),
    )
    async def get(self, data: GetStatusesByIdInput) -> GetStatusesByIdOutput:
        """Returns a list of the statuses specified by one or more status IDs. **[Permissions](#permissions) required:** * *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg) * *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg).

Important inputs: expand, id"""
        tool = self._client.get_tool('get_statuses_by_id')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetStatusesByIdOutput.model_validate(coerce_tool_result(result))
