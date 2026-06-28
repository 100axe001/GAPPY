from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueSecuritySchemeToolInput, GetIssueSecuritySchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueSecuritySchemeInput(GetIssueSecuritySchemeToolInput):
    """Operation input for `get_issue_security_scheme`."""
    pass

class GetIssueSecuritySchemeOutput(GetIssueSecuritySchemeToolOutput):
    """Operation output for `get_issue_security_scheme`."""
    pass

class JiraIssueSecuritySchemeResource(BaseResourceClient):
    """Operations for the `issue_security_scheme` resource."""

    @operation(
        name='get_issue_security_scheme',
        title='GetIssueSecurityScheme',
        input_model=GetIssueSecuritySchemeInput,
        output_model=GetIssueSecuritySchemeOutput,
        tools_used=('get_issue_security_scheme',),
        tags=tuple(['Issue security schemes']),
    )
    async def get(self, data: GetIssueSecuritySchemeInput) -> GetIssueSecuritySchemeOutput:
        """Returns an issue security scheme along with its security levels. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). * *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project that uses the requested issue security scheme.

Important inputs: id"""
        tool = self._client.get_tool('get_issue_security_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueSecuritySchemeOutput.model_validate(coerce_tool_result(result))
