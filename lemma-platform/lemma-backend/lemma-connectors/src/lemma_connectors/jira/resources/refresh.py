from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import RefreshWebhooksToolInput, RefreshWebhooksToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RefreshWebhooksInput(RefreshWebhooksToolInput):
    """Operation input for `refresh_webhooks`."""
    pass

class RefreshWebhooksOutput(RefreshWebhooksToolOutput):
    """Operation output for `refresh_webhooks`."""
    pass

class JiraRefreshResource(BaseResourceClient):
    """Operations for the `refresh` resource."""

    @operation(
        name='refresh_webhooks',
        title='RefreshWebhooks',
        input_model=RefreshWebhooksInput,
        output_model=RefreshWebhooksOutput,
        tools_used=('refresh_webhooks',),
        tags=tuple(['Webhooks']),
    )
    async def webhooks(self, data: RefreshWebhooksInput) -> RefreshWebhooksOutput:
        """Extends the life of webhook. Webhooks registered through the REST API expire after 30 days. Call this operation to keep them alive. Unrecognized webhook IDs (those that are not found or belong to other apps) are ignored. **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

Important inputs: body"""
        tool = self._client.get_tool('refresh_webhooks')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RefreshWebhooksOutput.model_validate(coerce_tool_result(result))
