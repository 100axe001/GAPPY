from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CopyDashboardToolInput, CopyDashboardToolOutput, CreateDashboardToolInput, CreateDashboardToolOutput, DeleteDashboardToolInput, DeleteDashboardToolOutput, GetDashboardToolInput, GetDashboardToolOutput, UpdateDashboardToolInput, UpdateDashboardToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CopyDashboardInput(CopyDashboardToolInput):
    """Operation input for `copy_dashboard`."""
    pass

class CopyDashboardOutput(CopyDashboardToolOutput):
    """Operation output for `copy_dashboard`."""
    pass

class CreateDashboardInput(CreateDashboardToolInput):
    """Operation input for `create_dashboard`."""
    pass

class CreateDashboardOutput(CreateDashboardToolOutput):
    """Operation output for `create_dashboard`."""
    pass

class DeleteDashboardInput(DeleteDashboardToolInput):
    """Operation input for `delete_dashboard`."""
    pass

class DeleteDashboardOutput(DeleteDashboardToolOutput):
    """Operation output for `delete_dashboard`."""
    pass

class GetDashboardInput(GetDashboardToolInput):
    """Operation input for `get_dashboard`."""
    pass

class GetDashboardOutput(GetDashboardToolOutput):
    """Operation output for `get_dashboard`."""
    pass

class UpdateDashboardInput(UpdateDashboardToolInput):
    """Operation input for `update_dashboard`."""
    pass

class UpdateDashboardOutput(UpdateDashboardToolOutput):
    """Operation output for `update_dashboard`."""
    pass

class JiraDashboardResource(BaseResourceClient):
    """Operations for the `dashboard` resource."""

    @operation(
        name='copy_dashboard',
        title='CopyDashboard',
        input_model=CopyDashboardInput,
        output_model=CopyDashboardOutput,
        tools_used=('copy_dashboard',),
        tags=tuple(['Dashboards']),
    )
    async def copy(self, data: CopyDashboardInput) -> CopyDashboardOutput:
        """Copies a dashboard. Any values provided in the `dashboard` parameter replace those in the copied dashboard. **[Permissions](#permissions) required:** None The dashboard to be copied must be owned by or shared with the user.

Important inputs: id, body"""
        tool = self._client.get_tool('copy_dashboard')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CopyDashboardOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='create_dashboard',
        title='CreateDashboard',
        input_model=CreateDashboardInput,
        output_model=CreateDashboardOutput,
        tools_used=('create_dashboard',),
        tags=tuple(['Dashboards']),
    )
    async def create(self, data: CreateDashboardInput) -> CreateDashboardOutput:
        """Creates a dashboard. **[Permissions](#permissions) required:** None.

Important inputs: body"""
        tool = self._client.get_tool('create_dashboard')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateDashboardOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_dashboard',
        title='DeleteDashboard',
        input_model=DeleteDashboardInput,
        output_model=DeleteDashboardOutput,
        tools_used=('delete_dashboard',),
        tags=tuple(['Dashboards']),
    )
    async def delete(self, data: DeleteDashboardInput) -> DeleteDashboardOutput:
        """Deletes a dashboard. **[Permissions](#permissions) required:** None The dashboard to be deleted must be owned by the user.

Important inputs: id"""
        tool = self._client.get_tool('delete_dashboard')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteDashboardOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_dashboard',
        title='GetDashboard',
        input_model=GetDashboardInput,
        output_model=GetDashboardOutput,
        tools_used=('get_dashboard',),
        tags=tuple(['Dashboards']),
    )
    async def get(self, data: GetDashboardInput) -> GetDashboardOutput:
        """Returns a dashboard. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None. However, to get a dashboard, the dashboard must be shared with the user or the user must own it. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users.

Important inputs: id"""
        tool = self._client.get_tool('get_dashboard')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDashboardOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_dashboard',
        title='UpdateDashboard',
        input_model=UpdateDashboardInput,
        output_model=UpdateDashboardOutput,
        tools_used=('update_dashboard',),
        tags=tuple(['Dashboards']),
    )
    async def update(self, data: UpdateDashboardInput) -> UpdateDashboardOutput:
        """Updates a dashboard, replacing all the dashboard details with those provided. **[Permissions](#permissions) required:** None The dashboard to be updated must be owned by the user.

Important inputs: id, body"""
        tool = self._client.get_tool('update_dashboard')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateDashboardOutput.model_validate(coerce_tool_result(result))
