from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetCreateIssueMetaToolInput, GetCreateIssueMetaToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetCreateIssueMetaInput(GetCreateIssueMetaToolInput):
    """Operation input for `get_create_issue_meta`."""
    pass

class GetCreateIssueMetaOutput(GetCreateIssueMetaToolOutput):
    """Operation output for `get_create_issue_meta`."""
    pass

class JiraCreateIssueMetaResource(BaseResourceClient):
    """Operations for the `create_issue_meta` resource."""

    @operation(
        name='get_create_issue_meta',
        title='GetCreateIssueMeta',
        input_model=GetCreateIssueMetaInput,
        output_model=GetCreateIssueMetaOutput,
        tools_used=('get_create_issue_meta',),
        tags=tuple(['Issues']),
    )
    async def get(self, data: GetCreateIssueMetaInput) -> GetCreateIssueMetaOutput:
        """Returns details of projects, issue types within projects, and, when requested, the create screen fields for each issue type for the user. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post). The request can be restricted to specific projects or issue types using the query parameters. The response will contain information for the valid projects, issue types, or project and issue type combinations requested. Note that invalid project, issue type, or project and issue type combinations do not generate errors. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.

Important inputs: project_ids, project_keys, issuetype_ids, issuetype_names, expand"""
        tool = self._client.get_tool('get_create_issue_meta')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCreateIssueMetaOutput.model_validate(coerce_tool_result(result))
