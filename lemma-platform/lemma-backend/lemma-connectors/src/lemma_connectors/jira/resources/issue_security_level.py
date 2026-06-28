from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueSecurityLevelToolInput, GetIssueSecurityLevelToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueSecurityLevelInput(GetIssueSecurityLevelToolInput):
    """Operation input for `get_issue_security_level`."""
    pass

class GetIssueSecurityLevelOutput(GetIssueSecurityLevelToolOutput):
    """Operation output for `get_issue_security_level`."""
    pass

class JiraIssueSecurityLevelResource(BaseResourceClient):
    """Operations for the `issue_security_level` resource."""

    @operation(
        name='get_issue_security_level',
        title='GetIssueSecurityLevel',
        input_model=GetIssueSecurityLevelInput,
        output_model=GetIssueSecurityLevelOutput,
        tools_used=('get_issue_security_level',),
        tags=tuple(['Issue security level']),
    )
    async def get(self, data: GetIssueSecurityLevelInput) -> GetIssueSecurityLevelOutput:
        """Returns details of an issue security level. Use [Get issue security scheme](#api-rest-api-3-issuesecurityschemes-id-get) to obtain the IDs of issue security levels associated with the issue security scheme. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: id"""
        tool = self._client.get_tool('get_issue_security_level')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueSecurityLevelOutput.model_validate(coerce_tool_result(result))
