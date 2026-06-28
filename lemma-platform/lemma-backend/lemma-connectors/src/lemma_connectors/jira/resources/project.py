from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ArchiveProjectToolInput, ArchiveProjectToolOutput, CreateProjectToolInput, CreateProjectToolOutput, DeleteProjectToolInput, DeleteProjectToolOutput, GetProjectToolInput, GetProjectToolOutput, UpdateProjectToolInput, UpdateProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ArchiveProjectInput(ArchiveProjectToolInput):
    """Operation input for `archive_project`."""
    pass

class ArchiveProjectOutput(ArchiveProjectToolOutput):
    """Operation output for `archive_project`."""
    pass

class CreateProjectInput(CreateProjectToolInput):
    """Operation input for `create_project`."""
    pass

class CreateProjectOutput(CreateProjectToolOutput):
    """Operation output for `create_project`."""
    pass

class DeleteProjectInput(DeleteProjectToolInput):
    """Operation input for `delete_project`."""
    pass

class DeleteProjectOutput(DeleteProjectToolOutput):
    """Operation output for `delete_project`."""
    pass

class GetProjectInput(GetProjectToolInput):
    """Operation input for `get_project`."""
    pass

class GetProjectOutput(GetProjectToolOutput):
    """Operation output for `get_project`."""
    pass

class UpdateProjectInput(UpdateProjectToolInput):
    """Operation input for `update_project`."""
    pass

class UpdateProjectOutput(UpdateProjectToolOutput):
    """Operation output for `update_project`."""
    pass

class JiraProjectResource(BaseResourceClient):
    """Operations for the `project` resource."""

    @operation(
        name='archive_project',
        title='ArchiveProject',
        input_model=ArchiveProjectInput,
        output_model=ArchiveProjectOutput,
        tools_used=('archive_project',),
        tags=tuple(['Projects']),
    )
    async def archive(self, data: ArchiveProjectInput) -> ArchiveProjectOutput:
        """Archives a project. You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key"""
        tool = self._client.get_tool('archive_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ArchiveProjectOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='create_project',
        title='CreateProject',
        input_model=CreateProjectInput,
        output_model=CreateProjectOutput,
        tools_used=('create_project',),
        tags=tuple(['Projects']),
    )
    async def create(self, data: CreateProjectInput) -> CreateProjectOutput:
        """Creates a project based on a project type template, as shown in the following table: | Project Type Key | Project Template Key | |--|--| | `business` | `com.atlassian.jira-core-project-templates:jira-core-simplified-content-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval`, `com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking`, `com.atlassian.jira-core-project-templates:jira-core-simplified-process-control`, `com.atlassian.jira-core-project-templates:jira-core-simplified-procurement`, `com.atlassian.jira-core-project-templates:jira-core-simplified-project-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment`, `com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking` | | `service_desk` | `com.atlassian.servicedesk:simplified-it-service-management`, `com.atlassian.servicedesk:simplified-general-service-desk-it`, `com.atlassian.servicedesk:simplified-general-service-desk-business`, `com.atlassian.servicedesk:simplified-internal-service-desk`, `com.atlassian.servicedesk:simplified-external-service-desk`, `com.atlassian.servicedesk:simplified-hr-service-desk`, `com.atlassian.servicedesk:simplified-facilities-service-desk`, `com.atlassian.servicedesk:simplified-legal-service-desk`, `com.atlassian.servicedesk:simplified-analytics-service-desk`, `com.atlassian.servicedesk:simplified-marketing-service-desk`, `com.atlassian.servicedesk:simplified-finance-service-desk` | | `software` | `com.pyxis.greenhopper.jira:gh-simplified-agility-kanban`, `com.pyxis.greenhopper.jira:gh-simplified-agility-scrum`, `com.pyxis.greenhopper.jira:gh-simplified-basic`, `com.pyxis.greenhopper.jira:gh-simplified-kanban-classic`, `com.pyxis.greenhopper.jira:gh-simplified-scrum-classic` | The project types are available according to the installed Jira features as follows: * Jira Core, the default, enables `business` projects. * Jira Service Management enables `service_desk` projects. * Jira Software enables `software` projects. To determine which features are installed, go to **Jira settings** > **Apps** > **Manage apps** and review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance, use **Jira settings** > **Apps** > **Finding new apps**. For more information, see [ Managing add-ons](https://confluence.atlassian.com/x/S31NLg). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateProjectOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_project',
        title='DeleteProject',
        input_model=DeleteProjectInput,
        output_model=DeleteProjectOutput,
        tools_used=('delete_project',),
        tags=tuple(['Projects']),
    )
    async def delete(self, data: DeleteProjectInput) -> DeleteProjectOutput:
        """Deletes a project. You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key, enable_undo"""
        tool = self._client.get_tool('delete_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteProjectOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_project',
        title='GetProject',
        input_model=GetProjectInput,
        output_model=GetProjectOutput,
        tools_used=('get_project',),
        tags=tuple(['Projects']),
    )
    async def get(self, data: GetProjectInput) -> GetProjectOutput:
        """Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id_or_key, expand, properties"""
        tool = self._client.get_tool('get_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_project',
        title='UpdateProject',
        input_model=UpdateProjectInput,
        output_model=UpdateProjectOutput,
        tools_used=('update_project',),
        tags=tuple(['Projects']),
    )
    async def update(self, data: UpdateProjectInput) -> UpdateProjectOutput:
        """Updates the [project details](https://confluence.atlassian.com/x/ahLpNw) of a project. All parameters are optional in the body of the request. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key, expand, body"""
        tool = self._client.get_tool('update_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateProjectOutput.model_validate(coerce_tool_result(result))
