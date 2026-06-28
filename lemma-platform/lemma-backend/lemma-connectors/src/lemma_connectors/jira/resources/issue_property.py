from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteIssuePropertyToolInput, DeleteIssuePropertyToolOutput, GetIssuePropertyToolInput, GetIssuePropertyToolOutput, SetIssuePropertyToolInput, SetIssuePropertyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteIssuePropertyInput(DeleteIssuePropertyToolInput):
    """Operation input for `delete_issue_property`."""
    pass

class DeleteIssuePropertyOutput(DeleteIssuePropertyToolOutput):
    """Operation output for `delete_issue_property`."""
    pass

class GetIssuePropertyInput(GetIssuePropertyToolInput):
    """Operation input for `get_issue_property`."""
    pass

class GetIssuePropertyOutput(GetIssuePropertyToolOutput):
    """Operation output for `get_issue_property`."""
    pass

class SetIssuePropertyInput(SetIssuePropertyToolInput):
    """Operation input for `set_issue_property`."""
    pass

class SetIssuePropertyOutput(SetIssuePropertyToolOutput):
    """Operation output for `set_issue_property`."""
    pass

class JiraIssuePropertyResource(BaseResourceClient):
    """Operations for the `issue_property` resource."""

    @operation(
        name='delete_issue_property',
        title='DeleteIssueProperty',
        input_model=DeleteIssuePropertyInput,
        output_model=DeleteIssuePropertyOutput,
        tools_used=('delete_issue_property',),
        tags=tuple(['Issue properties']),
    )
    async def delete(self, data: DeleteIssuePropertyInput) -> DeleteIssuePropertyOutput:
        """Deletes an issue's property. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, property_key"""
        tool = self._client.get_tool('delete_issue_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteIssuePropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_issue_property',
        title='GetIssueProperty',
        input_model=GetIssuePropertyInput,
        output_model=GetIssuePropertyOutput,
        tools_used=('get_issue_property',),
        tags=tuple(['Issue properties']),
    )
    async def get(self, data: GetIssuePropertyInput) -> GetIssuePropertyOutput:
        """Returns the key and value of an issue's property. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, property_key"""
        tool = self._client.get_tool('get_issue_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssuePropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_issue_property',
        title='SetIssueProperty',
        input_model=SetIssuePropertyInput,
        output_model=SetIssuePropertyOutput,
        tools_used=('set_issue_property',),
        tags=tuple(['Issue properties']),
    )
    async def set(self, data: SetIssuePropertyInput) -> SetIssuePropertyOutput:
        """Sets the value of an issue's property. Use this resource to store custom data against an issue. The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, property_key, body"""
        tool = self._client.get_tool('set_issue_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetIssuePropertyOutput.model_validate(coerce_tool_result(result))
