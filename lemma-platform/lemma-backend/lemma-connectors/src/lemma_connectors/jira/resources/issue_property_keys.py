from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssuePropertyKeysToolInput, GetIssuePropertyKeysToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssuePropertyKeysInput(GetIssuePropertyKeysToolInput):
    """Operation input for `get_issue_property_keys`."""
    pass

class GetIssuePropertyKeysOutput(GetIssuePropertyKeysToolOutput):
    """Operation output for `get_issue_property_keys`."""
    pass

class JiraIssuePropertyKeysResource(BaseResourceClient):
    """Operations for the `issue_property_keys` resource."""

    @operation(
        name='get_issue_property_keys',
        title='GetIssuePropertyKeys',
        input_model=GetIssuePropertyKeysInput,
        output_model=GetIssuePropertyKeysOutput,
        tools_used=('get_issue_property_keys',),
        tags=tuple(['Issue properties']),
    )
    async def get(self, data: GetIssuePropertyKeysInput) -> GetIssuePropertyKeysOutput:
        """Returns the URLs and keys of an issue's properties. This operation can be accessed anonymously. **[Permissions](#permissions) required:** Property details are only returned where the user has: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key"""
        tool = self._client.get_tool('get_issue_property_keys')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssuePropertyKeysOutput.model_validate(coerce_tool_result(result))
