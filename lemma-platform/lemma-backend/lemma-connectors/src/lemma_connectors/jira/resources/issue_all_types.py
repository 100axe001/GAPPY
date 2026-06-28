from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueAllTypesToolInput, GetIssueAllTypesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueAllTypesInput(GetIssueAllTypesToolInput):
    """Operation input for `get_issue_all_types`."""
    pass

class GetIssueAllTypesOutput(GetIssueAllTypesToolOutput):
    """Operation output for `get_issue_all_types`."""
    pass

class JiraIssueAllTypesResource(BaseResourceClient):
    """Operations for the `issue_all_types` resource."""

    @operation(
        name='get_issue_all_types',
        title='GetIssueAllTypes',
        input_model=GetIssueAllTypesInput,
        output_model=GetIssueAllTypesOutput,
        tools_used=('get_issue_all_types',),
        tags=tuple(['Issue types']),
    )
    async def get(self, data: GetIssueAllTypesInput) -> GetIssueAllTypesOutput:
        """Returns all issue types. This operation can be accessed anonymously. **[Permissions](#permissions) required:** Issue types are only returned as follows: * if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned. * if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types associated with the projects the user has permission to browse are returned.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_issue_all_types')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueAllTypesOutput.model_validate(coerce_tool_result(result))
