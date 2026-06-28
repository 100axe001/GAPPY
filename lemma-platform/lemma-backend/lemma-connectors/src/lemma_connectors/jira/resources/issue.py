from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateIssueToolInput, CreateIssueToolOutput, DeleteIssueToolInput, DeleteIssueToolOutput, GetIssueToolInput, GetIssueToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateIssueInput(CreateIssueToolInput):
    """Operation input for `create_issue`."""
    pass

class CreateIssueOutput(CreateIssueToolOutput):
    """Operation output for `create_issue`."""
    pass

class DeleteIssueInput(DeleteIssueToolInput):
    """Operation input for `delete_issue`."""
    pass

class DeleteIssueOutput(DeleteIssueToolOutput):
    """Operation output for `delete_issue`."""
    pass

class GetIssueInput(GetIssueToolInput):
    """Operation input for `get_issue`."""
    pass

class GetIssueOutput(GetIssueToolOutput):
    """Operation output for `get_issue`."""
    pass

class JiraIssueResource(BaseResourceClient):
    """Operations for the `issue` resource."""

    @operation(
        name='create_issue',
        title='CreateIssue',
        input_model=CreateIssueInput,
        output_model=CreateIssueOutput,
        tools_used=('create_issue',),
        tags=tuple(['Issues']),
    )
    async def create(self, data: CreateIssueInput) -> CreateIssueOutput:
        """Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask. A transition may be applied, to move the issue or subtask to a workflow step other than the default start step, and issue properties set. The content of the issue or subtask is defined using `update` and `fields`. The fields that can be set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get). These are the same fields that appear on the issue's create screen. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content. Creating a subtask differs from creating an issue as follows: * `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get) to find subtask issue types). * `parent` must contain the ID or key of the parent issue. In a next-gen project any issue may be made a child providing that the parent and child are members of the same project. **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which the issue or subtask is created.

Important inputs: update_history, body"""
        tool = self._client.get_tool('create_issue')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateIssueOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_issue',
        title='DeleteIssue',
        input_model=DeleteIssueInput,
        output_model=DeleteIssueOutput,
        tools_used=('delete_issue',),
        tags=tuple(['Issues']),
    )
    async def delete(self, data: DeleteIssueInput) -> DeleteIssueOutput:
        """Deletes an issue. An issue cannot be deleted if it has one or more subtasks. To delete an issue with subtasks, set `deleteSubtasks`. This causes the issue's subtasks to be deleted with the issue. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Delete issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, delete_subtasks"""
        tool = self._client.get_tool('delete_issue')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteIssueOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_issue',
        title='GetIssue',
        input_model=GetIssueInput,
        output_model=GetIssueOutput,
        tools_used=('get_issue',),
        tags=tuple(['Issues']),
    )
    async def get(self, data: GetIssueInput) -> GetIssueOutput:
        """Returns the details for an issue. The issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-insensitive search and check for moved issues is performed. If a matching issue is found its details are returned, a 302 or other redirect is **not** returned. The issue key returned in the response is the key of the issue found. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, fields, fields_by_keys, expand, properties, update_history"""
        tool = self._client.get_tool('get_issue')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueOutput.model_validate(coerce_tool_result(result))
