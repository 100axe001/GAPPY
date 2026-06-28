from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetTrashedFieldsPaginatedToolInput, GetTrashedFieldsPaginatedToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetTrashedFieldsPaginatedInput(GetTrashedFieldsPaginatedToolInput):
    """Operation input for `get_trashed_fields_paginated`."""
    pass

class GetTrashedFieldsPaginatedOutput(GetTrashedFieldsPaginatedToolOutput):
    """Operation output for `get_trashed_fields_paginated`."""
    pass

class JiraTrashedFieldsPaginatedResource(BaseResourceClient):
    """Operations for the `trashed_fields_paginated` resource."""

    @operation(
        name='get_trashed_fields_paginated',
        title='GetTrashedFieldsPaginated',
        input_model=GetTrashedFieldsPaginatedInput,
        output_model=GetTrashedFieldsPaginatedOutput,
        tools_used=('get_trashed_fields_paginated',),
        tags=tuple(['Issue fields']),
    )
    async def get(self, data: GetTrashedFieldsPaginatedInput) -> GetTrashedFieldsPaginatedOutput:
        """Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields whose field name or description partially match a string. Only custom fields can be queried, `type` must be set to `custom`. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, id, query, expand, order_by"""
        tool = self._client.get_tool('get_trashed_fields_paginated')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetTrashedFieldsPaginatedOutput.model_validate(coerce_tool_result(result))
