from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFailedWebhooksToolInput, GetFailedWebhooksToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFailedWebhooksInput(GetFailedWebhooksToolInput):
    """Operation input for `get_failed_webhooks`."""
    pass

class GetFailedWebhooksOutput(GetFailedWebhooksToolOutput):
    """Operation output for `get_failed_webhooks`."""
    pass

class JiraFailedWebhooksResource(BaseResourceClient):
    """Operations for the `failed_webhooks` resource."""

    @operation(
        name='get_failed_webhooks',
        title='GetFailedWebhooks',
        input_model=GetFailedWebhooksInput,
        output_model=GetFailedWebhooksOutput,
        tools_used=('get_failed_webhooks',),
        tags=tuple(['Webhooks']),
    )
    async def get(self, data: GetFailedWebhooksInput) -> GetFailedWebhooksOutput:
        """Returns webhooks that have recently failed to be delivered to the requesting app after the maximum number of retries. After 72 hours the failure may no longer be returned by this operation. The oldest failure is returned first. This method uses a cursor-based pagination. To request the next page use the failure time of the last webhook on the list as the `failedAfter` value or use the URL provided in `next`. **[Permissions](#permissions) required:** Only [Connect apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this operation.

Important inputs: max_results, after"""
        tool = self._client.get_tool('get_failed_webhooks')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFailedWebhooksOutput.model_validate(coerce_tool_result(result))
