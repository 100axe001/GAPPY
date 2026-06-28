from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectIssueSecuritySchemeToolInput, GetProjectIssueSecuritySchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectIssueSecuritySchemeInput(GetProjectIssueSecuritySchemeToolInput):
    """Operation input for `get_project_issue_security_scheme`."""
    pass

class GetProjectIssueSecuritySchemeOutput(GetProjectIssueSecuritySchemeToolOutput):
    """Operation output for `get_project_issue_security_scheme`."""
    pass

class JiraProjectIssueSecuritySchemeResource(BaseResourceClient):
    """Operations for the `project_issue_security_scheme` resource."""

    @operation(
        name='get_project_issue_security_scheme',
        title='GetProjectIssueSecurityScheme',
        input_model=GetProjectIssueSecuritySchemeInput,
        output_model=GetProjectIssueSecuritySchemeOutput,
        tools_used=('get_project_issue_security_scheme',),
        tags=tuple(['Project permission schemes']),
    )
    async def get(self, data: GetProjectIssueSecuritySchemeInput) -> GetProjectIssueSecuritySchemeOutput:
        """Returns the [issue security scheme](https://confluence.atlassian.com/x/J4lKLg) associated with the project. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or the *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

Important inputs: project_key_or_id"""
        tool = self._client.get_tool('get_project_issue_security_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectIssueSecuritySchemeOutput.model_validate(coerce_tool_result(result))
