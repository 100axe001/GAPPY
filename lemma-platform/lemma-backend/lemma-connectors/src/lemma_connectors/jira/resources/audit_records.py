from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAuditRecordsToolInput, GetAuditRecordsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAuditRecordsInput(GetAuditRecordsToolInput):
    """Operation input for `get_audit_records`."""
    pass

class GetAuditRecordsOutput(GetAuditRecordsToolOutput):
    """Operation output for `get_audit_records`."""
    pass

class JiraAuditRecordsResource(BaseResourceClient):
    """Operations for the `audit_records` resource."""

    @operation(
        name='get_audit_records',
        title='GetAuditRecords',
        input_model=GetAuditRecordsInput,
        output_model=GetAuditRecordsOutput,
        tools_used=('get_audit_records',),
        tags=tuple(['Audit records']),
    )
    async def get(self, data: GetAuditRecordsInput) -> GetAuditRecordsOutput:
        """Returns a list of audit records. The list can be filtered to include items: * where each item in `filter` has at least one match in any of these fields: * `summary` * `category` * `eventSource` * `objectItem.name` If the object is a user, account ID is available to filter. * `objectItem.parentName` * `objectItem.typeName` * `changedValues.changedFrom` * `changedValues.changedTo` * `remoteAddress` For example, if `filter` contains *man ed*, an audit record containing `summary": "User added to group"` and `"category": "group management"` is returned. * created on or after a date and time. * created or or before a date and time. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: offset, limit, filter, from_, to"""
        tool = self._client.get_tool('get_audit_records')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAuditRecordsOutput.model_validate(coerce_tool_result(result))
