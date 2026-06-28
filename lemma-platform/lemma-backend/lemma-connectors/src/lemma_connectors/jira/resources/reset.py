from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ResetColumnsToolInput, ResetColumnsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ResetColumnsInput(ResetColumnsToolInput):
    """Operation input for `reset_columns`."""
    pass

class ResetColumnsOutput(ResetColumnsToolOutput):
    """Operation output for `reset_columns`."""
    pass

class JiraResetResource(BaseResourceClient):
    """Operations for the `reset` resource."""

    @operation(
        name='reset_columns',
        title='ResetColumns',
        input_model=ResetColumnsInput,
        output_model=ResetColumnsOutput,
        tools_used=('reset_columns',),
        tags=tuple(['Filters']),
    )
    async def columns(self, data: ResetColumnsInput) -> ResetColumnsOutput:
        """Reset the user's column configuration for the filter to the default. **[Permissions](#permissions) required:** Permission to access Jira, however, columns are only reset for: * filters owned by the user. * filters shared with a group that the user is a member of. * filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * filters shared with a public project. * filters shared with the public.

Important inputs: id"""
        tool = self._client.get_tool('reset_columns')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ResetColumnsOutput.model_validate(coerce_tool_result(result))
