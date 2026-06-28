from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import BulkSetIssuePropertiesByIssueToolInput, BulkSetIssuePropertiesByIssueToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class BulkSetIssuePropertiesByIssueInput(BulkSetIssuePropertiesByIssueToolInput):
    """Operation input for `bulk_set_issue_properties_by_issue`."""
    pass

class BulkSetIssuePropertiesByIssueOutput(BulkSetIssuePropertiesByIssueToolOutput):
    """Operation output for `bulk_set_issue_properties_by_issue`."""
    pass

class JiraBulkSetIssuePropertiesByResource(BaseResourceClient):
    """Operations for the `bulk_set_issue_properties_by` resource."""

    @operation(
        name='bulk_set_issue_properties_by_issue',
        title='BulkSetIssuePropertiesByIssue',
        input_model=BulkSetIssuePropertiesByIssueInput,
        output_model=BulkSetIssuePropertiesByIssueOutput,
        tools_used=('bulk_set_issue_properties_by_issue',),
        tags=tuple(['Issue properties']),
    )
    async def issue(self, data: BulkSetIssuePropertiesByIssueInput) -> BulkSetIssuePropertiesByIssueOutput:
        """Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request. The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON. This operation is: * [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates. * non-transactional. Updating some entities may fail. Such information will available in the task result. **[Permissions](#permissions) required:** * *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: body"""
        tool = self._client.get_tool('bulk_set_issue_properties_by_issue')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return BulkSetIssuePropertiesByIssueOutput.model_validate(coerce_tool_result(result))
