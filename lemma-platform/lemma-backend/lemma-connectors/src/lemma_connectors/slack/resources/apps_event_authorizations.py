from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import AppsEventAuthorizationsListToolInput, AppsEventAuthorizationsListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AppsEventAuthorizationsListInput(AppsEventAuthorizationsListToolInput):
    """Operation input for `apps_event_authorizations_list`."""
    pass

class AppsEventAuthorizationsListOutput(AppsEventAuthorizationsListToolOutput):
    """Operation output for `apps_event_authorizations_list`."""
    pass

class SlackAppsEventAuthorizationsResource(BaseResourceClient):
    """Operations for the `apps_event_authorizations` resource."""

    @operation(
        name='apps_event_authorizations_list',
        title='AppsEventAuthorizationsList',
        input_model=AppsEventAuthorizationsListInput,
        output_model=AppsEventAuthorizationsListOutput,
        tools_used=('apps_event_authorizations_list',),
        tags=tuple(['apps.event.authorizations', 'apps']),
    )
    async def list(self, data: AppsEventAuthorizationsListInput) -> AppsEventAuthorizationsListOutput:
        """Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

Important inputs: token, event_context, cursor, limit"""
        tool = self._client.get_tool('apps_event_authorizations_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppsEventAuthorizationsListOutput.model_validate(coerce_tool_result(result))
