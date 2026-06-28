from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueSecurityLevelMembersToolInput, GetIssueSecurityLevelMembersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueSecurityLevelMembersInput(GetIssueSecurityLevelMembersToolInput):
    """Operation input for `get_issue_security_level_members`."""
    pass

class GetIssueSecurityLevelMembersOutput(GetIssueSecurityLevelMembersToolOutput):
    """Operation output for `get_issue_security_level_members`."""
    pass

class JiraIssueSecurityLevelMembersResource(BaseResourceClient):
    """Operations for the `issue_security_level_members` resource."""

    @operation(
        name='get_issue_security_level_members',
        title='GetIssueSecurityLevelMembers',
        input_model=GetIssueSecurityLevelMembersInput,
        output_model=GetIssueSecurityLevelMembersOutput,
        tools_used=('get_issue_security_level_members',),
        tags=tuple(['Issue security level']),
    )
    async def get(self, data: GetIssueSecurityLevelMembersInput) -> GetIssueSecurityLevelMembersOutput:
        """Returns issue security level members. Only issue security level members in context of classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_security_scheme_id, start_at, max_results, issue_security_level_id, expand"""
        tool = self._client.get_tool('get_issue_security_level_members')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueSecurityLevelMembersOutput.model_validate(coerce_tool_result(result))
