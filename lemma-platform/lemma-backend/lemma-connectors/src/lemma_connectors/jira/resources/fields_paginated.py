from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFieldsPaginatedToolInput, GetFieldsPaginatedToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFieldsPaginatedInput(GetFieldsPaginatedToolInput):
    """Operation input for `get_fields_paginated`."""
    pass

class GetFieldsPaginatedOutput(GetFieldsPaginatedToolOutput):
    """Operation output for `get_fields_paginated`."""
    pass

class JiraFieldsPaginatedResource(BaseResourceClient):
    """Operations for the `fields_paginated` resource."""

    @operation(
        name='get_fields_paginated',
        title='GetFieldsPaginated',
        input_model=GetFieldsPaginatedInput,
        output_model=GetFieldsPaginatedOutput,
        tools_used=('get_fields_paginated',),
        tags=tuple(['Issue fields']),
    )
    async def get(self, data: GetFieldsPaginatedInput) -> GetFieldsPaginatedOutput:
        """Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include: * all fields * specific fields, by defining `id` * fields that contain a string in the field name or description, by defining `query` * specific fields that contain a string in the field name or description, by defining `id` and `query` Only custom fields can be queried, `type` must be set to `custom`. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, type, id, query, order_by, expand"""
        tool = self._client.get_tool('get_fields_paginated')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFieldsPaginatedOutput.model_validate(coerce_tool_result(result))
