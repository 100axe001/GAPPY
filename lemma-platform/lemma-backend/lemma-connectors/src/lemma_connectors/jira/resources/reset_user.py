from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ResetUserColumnsToolInput, ResetUserColumnsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ResetUserColumnsInput(ResetUserColumnsToolInput):
    """Operation input for `reset_user_columns`."""
    pass

class ResetUserColumnsOutput(ResetUserColumnsToolOutput):
    """Operation output for `reset_user_columns`."""
    pass

class JiraResetUserResource(BaseResourceClient):
    """Operations for the `reset_user` resource."""

    @operation(
        name='reset_user_columns',
        title='ResetUserColumns',
        input_model=ResetUserColumnsInput,
        output_model=ResetUserColumnsOutput,
        tools_used=('reset_user_columns',),
        tags=tuple(['Users']),
    )
    async def columns(self, data: ResetUserColumnsInput) -> ResetUserColumnsOutput:
        """Resets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user to the system default. If `accountId` is not passed, the calling user's default columns are reset. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user. * Permission to access Jira, to set the calling user's columns.

Important inputs: account_id, username"""
        tool = self._client.get_tool('reset_user_columns')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ResetUserColumnsOutput.model_validate(coerce_tool_result(result))
