from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetTransitionsToolInput, GetTransitionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetTransitionsInput(GetTransitionsToolInput):
    """Operation input for `get_transitions`."""
    pass

class GetTransitionsOutput(GetTransitionsToolOutput):
    """Operation output for `get_transitions`."""
    pass

class JiraTransitionsResource(BaseResourceClient):
    """Operations for the `transitions` resource."""

    @operation(
        name='get_transitions',
        title='GetTransitions',
        input_model=GetTransitionsInput,
        output_model=GetTransitionsOutput,
        tools_used=('get_transitions',),
        tags=tuple(['Issues']),
    )
    async def get(self, data: GetTransitionsInput) -> GetTransitionsOutput:
        """Returns either all transitions or a transition that can be performed by the user on an issue, based on the issue's status. Note, if a request is made for a transition that does not exist or cannot be performed on the issue, given its status, the response will return any empty transitions list. This operation can be accessed anonymously. **[Permissions](#permissions) required: A list or transition is returned only when the user has:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. However, if the user does not have the *Transition issues* [ project permission](https://confluence.atlassian.com/x/yodKLg) the response will not list any transitions.

Important inputs: issue_id_or_key, expand, transition_id, skip_remote_only_condition, include_unavailable_transitions, sort_by_ops_bar_and_status"""
        tool = self._client.get_tool('get_transitions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetTransitionsOutput.model_validate(coerce_tool_result(result))
