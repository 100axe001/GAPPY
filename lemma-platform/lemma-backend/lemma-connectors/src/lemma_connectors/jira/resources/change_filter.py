from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ChangeFilterOwnerToolInput, ChangeFilterOwnerToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChangeFilterOwnerInput(ChangeFilterOwnerToolInput):
    """Operation input for `change_filter_owner`."""
    pass

class ChangeFilterOwnerOutput(ChangeFilterOwnerToolOutput):
    """Operation output for `change_filter_owner`."""
    pass

class JiraChangeFilterResource(BaseResourceClient):
    """Operations for the `change_filter` resource."""

    @operation(
        name='change_filter_owner',
        title='ChangeFilterOwner',
        input_model=ChangeFilterOwnerInput,
        output_model=ChangeFilterOwnerOutput,
        tools_used=('change_filter_owner',),
        tags=tuple(['Filters']),
    )
    async def owner(self, data: ChangeFilterOwnerInput) -> ChangeFilterOwnerOutput:
        """Changes the owner of the filter. **[Permissions](#permissions) required:** Permission to access Jira. However, the user must own the filter or have the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('change_filter_owner')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChangeFilterOwnerOutput.model_validate(coerce_tool_result(result))
