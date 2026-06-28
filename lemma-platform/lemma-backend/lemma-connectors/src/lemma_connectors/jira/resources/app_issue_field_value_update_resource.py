from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutToolInput, AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutInput(AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutToolInput):
    """Operation input for `app_issue_field_value_update_resource_update_issue_fields_put`."""
    pass

class AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutOutput(AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutToolOutput):
    """Operation output for `app_issue_field_value_update_resource_update_issue_fields_put`."""
    pass

class JiraAppIssueFieldValueUpdateResourceResource(BaseResourceClient):
    """Operations for the `app_issue_field_value_update_resource` resource."""

    @operation(
        name='app_issue_field_value_update_resource_update_issue_fields_put',
        title='AppIssueFieldValueUpdateResourceUpdateIssueFieldsPut',
        input_model=AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutInput,
        output_model=AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutOutput,
        tools_used=('app_issue_field_value_update_resource_update_issue_fields_put',),
        tags=tuple(['App migration']),
    )
    async def update_issue_fields_put(self, data: AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutInput) -> AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutOutput:
        """Updates the value of a custom field added by Connect apps on one or more issues. The values of up to 200 custom fields can be updated. **[Permissions](#permissions) required:** Only Connect apps can make this request.

Important inputs: atlassian_transfer_id, body"""
        tool = self._client.get_tool('app_issue_field_value_update_resource_update_issue_fields_put')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutOutput.model_validate(coerce_tool_result(result))
