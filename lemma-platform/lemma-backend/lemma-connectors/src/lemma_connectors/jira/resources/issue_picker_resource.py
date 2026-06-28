from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssuePickerResourceToolInput, GetIssuePickerResourceToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssuePickerResourceInput(GetIssuePickerResourceToolInput):
    """Operation input for `get_issue_picker_resource`."""
    pass

class GetIssuePickerResourceOutput(GetIssuePickerResourceToolOutput):
    """Operation output for `get_issue_picker_resource`."""
    pass

class JiraIssuePickerResourceResource(BaseResourceClient):
    """Operations for the `issue_picker_resource` resource."""

    @operation(
        name='get_issue_picker_resource',
        title='GetIssuePickerResource',
        input_model=GetIssuePickerResourceInput,
        output_model=GetIssuePickerResourceOutput,
        tools_used=('get_issue_picker_resource',),
        tags=tuple(['Issue search']),
    )
    async def get(self, data: GetIssuePickerResourceInput) -> GetIssuePickerResourceOutput:
        """Returns lists of issues matching a query string. Use this resource to provide auto-completion suggestions when the user is looking for an issue using a word or string. This operation returns two lists: * `History Search` which includes issues from the user's history of created, edited, or viewed issues that contain the string in the `query` parameter. * `Current Search` which includes issues that match the JQL expression in `currentJQL` and contain the string in the `query` parameter. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: query, current_jql, current_issue_key, current_project_id, show_sub_tasks, show_sub_task_parent"""
        tool = self._client.get_tool('get_issue_picker_resource')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssuePickerResourceOutput.model_validate(coerce_tool_result(result))
