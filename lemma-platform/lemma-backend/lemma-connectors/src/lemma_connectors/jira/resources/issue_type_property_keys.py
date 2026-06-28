from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueTypePropertyKeysToolInput, GetIssueTypePropertyKeysToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueTypePropertyKeysInput(GetIssueTypePropertyKeysToolInput):
    """Operation input for `get_issue_type_property_keys`."""
    pass

class GetIssueTypePropertyKeysOutput(GetIssueTypePropertyKeysToolOutput):
    """Operation output for `get_issue_type_property_keys`."""
    pass

class JiraIssueTypePropertyKeysResource(BaseResourceClient):
    """Operations for the `issue_type_property_keys` resource."""

    @operation(
        name='get_issue_type_property_keys',
        title='GetIssueTypePropertyKeys',
        input_model=GetIssueTypePropertyKeysInput,
        output_model=GetIssueTypePropertyKeysOutput,
        tools_used=('get_issue_type_property_keys',),
        tags=tuple(['Issue type properties']),
    )
    async def get(self, data: GetIssueTypePropertyKeysInput) -> GetIssueTypePropertyKeysOutput:
        """Returns all the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys of the issue type. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the property keys of any issue type. * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the property keys of any issue types associated with the projects the user has permission to browse.

Important inputs: issue_type_id"""
        tool = self._client.get_tool('get_issue_type_property_keys')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypePropertyKeysOutput.model_validate(coerce_tool_result(result))
