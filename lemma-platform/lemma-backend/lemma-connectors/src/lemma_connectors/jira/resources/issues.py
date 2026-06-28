from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateIssuesToolInput, CreateIssuesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateIssuesInput(CreateIssuesToolInput):
    """Operation input for `create_issues`."""
    pass

class CreateIssuesOutput(CreateIssuesToolOutput):
    """Operation output for `create_issues`."""
    pass

class JiraIssuesResource(BaseResourceClient):
    """Operations for the `issues` resource."""

    @operation(
        name='create_issues',
        title='CreateIssues',
        input_model=CreateIssuesInput,
        output_model=CreateIssuesOutput,
        tools_used=('create_issues',),
        tags=tuple(['Issues']),
    )
    async def create(self, data: CreateIssuesInput) -> CreateIssuesOutput:
        """Creates upto **50** issues and, where the option to create subtasks is enabled in Jira, subtasks. Transitions may be applied, to move the issues or subtasks to a workflow step other than the default start step, and issue properties set. The content of each issue or subtask is defined using `update` and `fields`. The fields that can be set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get). These are the same fields that appear on the issues' create screens. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content. Creating a subtask differs from creating an issue as follows: * `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-api-3-issue-createmeta-get) to find subtask issue types). * `parent` the must contain the ID or key of the parent issue. **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which each issue or subtask is created.

Important inputs: body"""
        tool = self._client.get_tool('create_issues')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateIssuesOutput.model_validate(coerce_tool_result(result))
