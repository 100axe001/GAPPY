from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateStatusesToolInput, CreateStatusesToolOutput, GetStatusesToolInput, GetStatusesToolOutput, UpdateStatusesToolInput, UpdateStatusesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateStatusesInput(CreateStatusesToolInput):
    """Operation input for `create_statuses`."""
    pass

class CreateStatusesOutput(CreateStatusesToolOutput):
    """Operation output for `create_statuses`."""
    pass

class GetStatusesInput(GetStatusesToolInput):
    """Operation input for `get_statuses`."""
    pass

class GetStatusesOutput(GetStatusesToolOutput):
    """Operation output for `get_statuses`."""
    pass

class UpdateStatusesInput(UpdateStatusesToolInput):
    """Operation input for `update_statuses`."""
    pass

class UpdateStatusesOutput(UpdateStatusesToolOutput):
    """Operation output for `update_statuses`."""
    pass

class JiraStatusesResource(BaseResourceClient):
    """Operations for the `statuses` resource."""

    @operation(
        name='create_statuses',
        title='CreateStatuses',
        input_model=CreateStatusesInput,
        output_model=CreateStatusesOutput,
        tools_used=('create_statuses',),
        tags=tuple(['Status']),
    )
    async def create(self, data: CreateStatusesInput) -> CreateStatusesOutput:
        """Creates statuses for a global or project scope. **[Permissions](#permissions) required:** * *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg) * *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_statuses')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateStatusesOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_statuses',
        title='GetStatuses',
        input_model=GetStatusesInput,
        output_model=GetStatusesOutput,
        tools_used=('get_statuses',),
        tags=tuple(['Workflow statuses']),
    )
    async def get(self, data: GetStatusesInput) -> GetStatusesOutput:
        """Returns a list of all statuses associated with active workflows. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_statuses')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetStatusesOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_statuses',
        title='UpdateStatuses',
        input_model=UpdateStatusesInput,
        output_model=UpdateStatusesOutput,
        tools_used=('update_statuses',),
        tags=tuple(['Status']),
    )
    async def update(self, data: UpdateStatusesInput) -> UpdateStatusesOutput:
        """Updates statuses by ID. **[Permissions](#permissions) required:** * *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg) * *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg).

Important inputs: body"""
        tool = self._client.get_tool('update_statuses')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateStatusesOutput.model_validate(coerce_tool_result(result))
