from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueNavigatorDefaultColumnsToolInput, GetIssueNavigatorDefaultColumnsToolOutput, SetIssueNavigatorDefaultColumnsToolInput, SetIssueNavigatorDefaultColumnsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueNavigatorDefaultColumnsInput(GetIssueNavigatorDefaultColumnsToolInput):
    """Operation input for `get_issue_navigator_default_columns`."""
    pass

class GetIssueNavigatorDefaultColumnsOutput(GetIssueNavigatorDefaultColumnsToolOutput):
    """Operation output for `get_issue_navigator_default_columns`."""
    pass

class SetIssueNavigatorDefaultColumnsInput(SetIssueNavigatorDefaultColumnsToolInput):
    """Operation input for `set_issue_navigator_default_columns`."""
    pass

class SetIssueNavigatorDefaultColumnsOutput(SetIssueNavigatorDefaultColumnsToolOutput):
    """Operation output for `set_issue_navigator_default_columns`."""
    pass

class JiraIssueNavigatorDefaultColumnsResource(BaseResourceClient):
    """Operations for the `issue_navigator_default_columns` resource."""

    @operation(
        name='get_issue_navigator_default_columns',
        title='GetIssueNavigatorDefaultColumns',
        input_model=GetIssueNavigatorDefaultColumnsInput,
        output_model=GetIssueNavigatorDefaultColumnsOutput,
        tools_used=('get_issue_navigator_default_columns',),
        tags=tuple(['Issue navigator settings']),
    )
    async def get(self, data: GetIssueNavigatorDefaultColumnsInput) -> GetIssueNavigatorDefaultColumnsOutput:
        """Returns the default issue navigator columns. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_issue_navigator_default_columns')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueNavigatorDefaultColumnsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_issue_navigator_default_columns',
        title='SetIssueNavigatorDefaultColumns',
        input_model=SetIssueNavigatorDefaultColumnsInput,
        output_model=SetIssueNavigatorDefaultColumnsOutput,
        tools_used=('set_issue_navigator_default_columns',),
        tags=tuple(['Issue navigator settings']),
    )
    async def set(self, data: SetIssueNavigatorDefaultColumnsInput) -> SetIssueNavigatorDefaultColumnsOutput:
        """Sets the default issue navigator columns. The `columns` parameter accepts a navigable field value and is expressed as HTML form data. To specify multiple columns, pass multiple `columns` parameters. For example, in curl: `curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/settings/columns` If no column details are sent, then all default columns are removed. A navigable field is one that can be used as a column on the issue navigator. Find details of navigable issue columns using [Get fields](#api-rest-api-3-field-get). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('set_issue_navigator_default_columns')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetIssueNavigatorDefaultColumnsOutput.model_validate(coerce_tool_result(result))
