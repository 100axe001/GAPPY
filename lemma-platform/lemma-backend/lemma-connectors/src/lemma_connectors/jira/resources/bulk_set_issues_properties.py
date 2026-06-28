from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import BulkSetIssuesPropertiesListToolInput, BulkSetIssuesPropertiesListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class BulkSetIssuesPropertiesListInput(BulkSetIssuesPropertiesListToolInput):
    """Operation input for `bulk_set_issues_properties_list`."""
    pass

class BulkSetIssuesPropertiesListOutput(BulkSetIssuesPropertiesListToolOutput):
    """Operation output for `bulk_set_issues_properties_list`."""
    pass

class JiraBulkSetIssuesPropertiesResource(BaseResourceClient):
    """Operations for the `bulk_set_issues_properties` resource."""

    @operation(
        name='bulk_set_issues_properties_list',
        title='BulkSetIssuesPropertiesList',
        input_model=BulkSetIssuesPropertiesListInput,
        output_model=BulkSetIssuesPropertiesListOutput,
        tools_used=('bulk_set_issues_properties_list',),
        tags=tuple(['Issue properties']),
    )
    async def list(self, data: BulkSetIssuesPropertiesListInput) -> BulkSetIssuesPropertiesListOutput:
        """Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can be specified along with up to 10,000 issues on which to set or update that list of entity properties. The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON. The maximum length of single issue property value is 32768 characters. This operation can be accessed anonymously. This operation is: * transactional, either all properties are updated in all eligible issues or, when errors occur, no properties are updated. * [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates. **[Permissions](#permissions) required:** * *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: body"""
        tool = self._client.get_tool('bulk_set_issues_properties_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return BulkSetIssuesPropertiesListOutput.model_validate(coerce_tool_result(result))
