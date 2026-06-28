from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteWorklogPropertyToolInput, DeleteWorklogPropertyToolOutput, GetWorklogPropertyToolInput, GetWorklogPropertyToolOutput, SetWorklogPropertyToolInput, SetWorklogPropertyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteWorklogPropertyInput(DeleteWorklogPropertyToolInput):
    """Operation input for `delete_worklog_property`."""
    pass

class DeleteWorklogPropertyOutput(DeleteWorklogPropertyToolOutput):
    """Operation output for `delete_worklog_property`."""
    pass

class GetWorklogPropertyInput(GetWorklogPropertyToolInput):
    """Operation input for `get_worklog_property`."""
    pass

class GetWorklogPropertyOutput(GetWorklogPropertyToolOutput):
    """Operation output for `get_worklog_property`."""
    pass

class SetWorklogPropertyInput(SetWorklogPropertyToolInput):
    """Operation input for `set_worklog_property`."""
    pass

class SetWorklogPropertyOutput(SetWorklogPropertyToolOutput):
    """Operation output for `set_worklog_property`."""
    pass

class JiraWorklogPropertyResource(BaseResourceClient):
    """Operations for the `worklog_property` resource."""

    @operation(
        name='delete_worklog_property',
        title='DeleteWorklogProperty',
        input_model=DeleteWorklogPropertyInput,
        output_model=DeleteWorklogPropertyOutput,
        tools_used=('delete_worklog_property',),
        tags=tuple(['Issue worklog properties']),
    )
    async def delete(self, data: DeleteWorklogPropertyInput) -> DeleteWorklogPropertyOutput:
        """Deletes a worklog property. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, worklog_id, property_key"""
        tool = self._client.get_tool('delete_worklog_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWorklogPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_worklog_property',
        title='GetWorklogProperty',
        input_model=GetWorklogPropertyInput,
        output_model=GetWorklogPropertyOutput,
        tools_used=('get_worklog_property',),
        tags=tuple(['Issue worklog properties']),
    )
    async def get(self, data: GetWorklogPropertyInput) -> GetWorklogPropertyOutput:
        """Returns the value of a worklog property. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, worklog_id, property_key"""
        tool = self._client.get_tool('get_worklog_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorklogPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_worklog_property',
        title='SetWorklogProperty',
        input_model=SetWorklogPropertyInput,
        output_model=SetWorklogPropertyOutput,
        tools_used=('set_worklog_property',),
        tags=tuple(['Issue worklog properties']),
    )
    async def set(self, data: SetWorklogPropertyInput) -> SetWorklogPropertyOutput:
        """Sets the value of a worklog property. Use this operation to store custom data against the worklog. The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user. * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, worklog_id, property_key, body"""
        tool = self._client.get_tool('set_worklog_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetWorklogPropertyOutput.model_validate(coerce_tool_result(result))
