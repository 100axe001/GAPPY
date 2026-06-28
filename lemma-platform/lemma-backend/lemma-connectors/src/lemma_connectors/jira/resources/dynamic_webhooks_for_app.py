from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetDynamicWebhooksForAppToolInput, GetDynamicWebhooksForAppToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetDynamicWebhooksForAppInput(GetDynamicWebhooksForAppToolInput):
    """Operation input for `get_dynamic_webhooks_for_app`."""
    pass

class GetDynamicWebhooksForAppOutput(GetDynamicWebhooksForAppToolOutput):
    """Operation output for `get_dynamic_webhooks_for_app`."""
    pass

class JiraDynamicWebhooksForAppResource(BaseResourceClient):
    """Operations for the `dynamic_webhooks_for_app` resource."""

    @operation(
        name='get_dynamic_webhooks_for_app',
        title='GetDynamicWebhooksForApp',
        input_model=GetDynamicWebhooksForAppInput,
        output_model=GetDynamicWebhooksForAppOutput,
        tools_used=('get_dynamic_webhooks_for_app',),
        tags=tuple(['Webhooks']),
    )
    async def get(self, data: GetDynamicWebhooksForAppInput) -> GetDynamicWebhooksForAppOutput:
        """Returns a [paginated](#pagination) list of the webhooks registered by the calling app. **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

Important inputs: start_at, max_results"""
        tool = self._client.get_tool('get_dynamic_webhooks_for_app')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDynamicWebhooksForAppOutput.model_validate(coerce_tool_result(result))
