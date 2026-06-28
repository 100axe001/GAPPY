from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddWorklogToolInput, AddWorklogToolOutput, DeleteWorklogToolInput, DeleteWorklogToolOutput, GetWorklogToolInput, GetWorklogToolOutput, UpdateWorklogToolInput, UpdateWorklogToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddWorklogInput(AddWorklogToolInput):
    """Operation input for `add_worklog`."""
    pass

class AddWorklogOutput(AddWorklogToolOutput):
    """Operation output for `add_worklog`."""
    pass

class DeleteWorklogInput(DeleteWorklogToolInput):
    """Operation input for `delete_worklog`."""
    pass

class DeleteWorklogOutput(DeleteWorklogToolOutput):
    """Operation output for `delete_worklog`."""
    pass

class GetWorklogInput(GetWorklogToolInput):
    """Operation input for `get_worklog`."""
    pass

class GetWorklogOutput(GetWorklogToolOutput):
    """Operation output for `get_worklog`."""
    pass

class UpdateWorklogInput(UpdateWorklogToolInput):
    """Operation input for `update_worklog`."""
    pass

class UpdateWorklogOutput(UpdateWorklogToolOutput):
    """Operation output for `update_worklog`."""
    pass

class JiraWorklogResource(BaseResourceClient):
    """Operations for the `worklog` resource."""

    @operation(
        name='add_worklog',
        title='AddWorklog',
        input_model=AddWorklogInput,
        output_model=AddWorklogOutput,
        tools_used=('add_worklog',),
        tags=tuple(['Issue worklogs']),
    )
    async def add(self, data: AddWorklogInput) -> AddWorklogOutput:
        """Adds a worklog to an issue. Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Work on issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, notify_users, adjust_estimate, new_estimate, reduce_by, expand, override_editable_flag, body"""
        tool = self._client.get_tool('add_worklog')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddWorklogOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_worklog',
        title='DeleteWorklog',
        input_model=DeleteWorklogInput,
        output_model=DeleteWorklogOutput,
        tools_used=('delete_worklog',),
        tags=tuple(['Issue worklogs']),
    )
    async def delete(self, data: DeleteWorklogInput) -> DeleteWorklogOutput:
        """Deletes a worklog from an issue. Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog or *Delete own worklogs* to delete worklogs created by the user, * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, id, notify_users, adjust_estimate, new_estimate, increase_by, override_editable_flag"""
        tool = self._client.get_tool('delete_worklog')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWorklogOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_worklog',
        title='GetWorklog',
        input_model=GetWorklogInput,
        output_model=GetWorklogOutput,
        tools_used=('get_worklog',),
        tags=tuple(['Issue worklogs']),
    )
    async def get(self, data: GetWorklogInput) -> GetWorklogOutput:
        """Returns a worklog. Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, id, expand"""
        tool = self._client.get_tool('get_worklog')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorklogOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_worklog',
        title='UpdateWorklog',
        input_model=UpdateWorklogInput,
        output_model=UpdateWorklogOutput,
        tools_used=('update_worklog',),
        tags=tuple(['Issue worklogs']),
    )
    async def update(self, data: UpdateWorklogInput) -> UpdateWorklogOutput:
        """Updates a worklog. Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user. * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, id, notify_users, adjust_estimate, new_estimate, expand, override_editable_flag, body"""
        tool = self._client.get_tool('update_worklog')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateWorklogOutput.model_validate(coerce_tool_result(result))
