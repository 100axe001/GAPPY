from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DoTransitionToolInput, DoTransitionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DoTransitionInput(DoTransitionToolInput):
    """Operation input for `do_transition`."""
    pass

class DoTransitionOutput(DoTransitionToolOutput):
    """Operation output for `do_transition`."""
    pass

class JiraDoResource(BaseResourceClient):
    """Operations for the `do` resource."""

    @operation(
        name='do_transition',
        title='DoTransition',
        input_model=DoTransitionInput,
        output_model=DoTransitionOutput,
        tools_used=('do_transition',),
        tags=tuple(['Issues']),
    )
    async def transition(self, data: DoTransitionInput) -> DoTransitionOutput:
        """Performs an issue transition and, if the transition has a screen, updates the fields from the transition screen. sortByCategory To update the fields on the transition screen, specify the fields in the `fields` or `update` parameters in the request body. Get details about the fields using [ Get transitions](#api-rest-api-3-issue-issueIdOrKey-transitions-get) with the `transitions.fields` expand. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* and *Transition issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, body"""
        tool = self._client.get_tool('do_transition')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DoTransitionOutput.model_validate(coerce_tool_result(result))
