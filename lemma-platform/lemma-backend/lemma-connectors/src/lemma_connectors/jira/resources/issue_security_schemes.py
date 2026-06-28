from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueSecuritySchemesToolInput, GetIssueSecuritySchemesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueSecuritySchemesInput(GetIssueSecuritySchemesToolInput):
    """Operation input for `get_issue_security_schemes`."""
    pass

class GetIssueSecuritySchemesOutput(GetIssueSecuritySchemesToolOutput):
    """Operation output for `get_issue_security_schemes`."""
    pass

class JiraIssueSecuritySchemesResource(BaseResourceClient):
    """Operations for the `issue_security_schemes` resource."""

    @operation(
        name='get_issue_security_schemes',
        title='GetIssueSecuritySchemes',
        input_model=GetIssueSecuritySchemesInput,
        output_model=GetIssueSecuritySchemesOutput,
        tools_used=('get_issue_security_schemes',),
        tags=tuple(['Issue security schemes']),
    )
    async def get(self, data: GetIssueSecuritySchemesInput) -> GetIssueSecuritySchemesOutput:
        """Returns all [issue security schemes](https://confluence.atlassian.com/x/J4lKLg). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_issue_security_schemes')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueSecuritySchemesOutput.model_validate(coerce_tool_result(result))
