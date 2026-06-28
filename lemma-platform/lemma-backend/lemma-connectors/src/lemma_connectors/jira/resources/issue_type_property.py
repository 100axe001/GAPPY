from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteIssueTypePropertyToolInput, DeleteIssueTypePropertyToolOutput, GetIssueTypePropertyToolInput, GetIssueTypePropertyToolOutput, SetIssueTypePropertyToolInput, SetIssueTypePropertyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteIssueTypePropertyInput(DeleteIssueTypePropertyToolInput):
    """Operation input for `delete_issue_type_property`."""
    pass

class DeleteIssueTypePropertyOutput(DeleteIssueTypePropertyToolOutput):
    """Operation output for `delete_issue_type_property`."""
    pass

class GetIssueTypePropertyInput(GetIssueTypePropertyToolInput):
    """Operation input for `get_issue_type_property`."""
    pass

class GetIssueTypePropertyOutput(GetIssueTypePropertyToolOutput):
    """Operation output for `get_issue_type_property`."""
    pass

class SetIssueTypePropertyInput(SetIssueTypePropertyToolInput):
    """Operation input for `set_issue_type_property`."""
    pass

class SetIssueTypePropertyOutput(SetIssueTypePropertyToolOutput):
    """Operation output for `set_issue_type_property`."""
    pass

class JiraIssueTypePropertyResource(BaseResourceClient):
    """Operations for the `issue_type_property` resource."""

    @operation(
        name='delete_issue_type_property',
        title='DeleteIssueTypeProperty',
        input_model=DeleteIssueTypePropertyInput,
        output_model=DeleteIssueTypePropertyOutput,
        tools_used=('delete_issue_type_property',),
        tags=tuple(['Issue type properties']),
    )
    async def delete(self, data: DeleteIssueTypePropertyInput) -> DeleteIssueTypePropertyOutput:
        """Deletes the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_id, property_key"""
        tool = self._client.get_tool('delete_issue_type_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteIssueTypePropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_issue_type_property',
        title='GetIssueTypeProperty',
        input_model=GetIssueTypePropertyInput,
        output_model=GetIssueTypePropertyOutput,
        tools_used=('get_issue_type_property',),
        tags=tuple(['Issue type properties']),
    )
    async def get(self, data: GetIssueTypePropertyInput) -> GetIssueTypePropertyOutput:
        """Returns the key and value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the details of any issue type. * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the details of any issue types associated with the projects the user has permission to browse.

Important inputs: issue_type_id, property_key"""
        tool = self._client.get_tool('get_issue_type_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypePropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_issue_type_property',
        title='SetIssueTypeProperty',
        input_model=SetIssueTypePropertyInput,
        output_model=SetIssueTypePropertyOutput,
        tools_used=('set_issue_type_property',),
        tags=tuple(['Issue type properties']),
    )
    async def set(self, data: SetIssueTypePropertyInput) -> SetIssueTypePropertyOutput:
        """Creates or updates the value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). Use this resource to store and update data against an issue type. The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_id, property_key, body"""
        tool = self._client.get_tool('set_issue_type_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetIssueTypePropertyOutput.model_validate(coerce_tool_result(result))
