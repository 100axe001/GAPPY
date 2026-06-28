from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteWebhookByIdToolInput, DeleteWebhookByIdToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteWebhookByIdInput(DeleteWebhookByIdToolInput):
    """Operation input for `delete_webhook_by_id`."""
    pass

class DeleteWebhookByIdOutput(DeleteWebhookByIdToolOutput):
    """Operation output for `delete_webhook_by_id`."""
    pass

class JiraWebhookByIdResource(BaseResourceClient):
    """Operations for the `webhook_by_id` resource."""

    @operation(
        name='delete_webhook_by_id',
        title='DeleteWebhookById',
        input_model=DeleteWebhookByIdInput,
        output_model=DeleteWebhookByIdOutput,
        tools_used=('delete_webhook_by_id',),
        tags=tuple(['Webhooks']),
    )
    async def delete(self, data: DeleteWebhookByIdInput) -> DeleteWebhookByIdOutput:
        """Removes webhooks by ID. Only webhooks registered by the calling app are removed. If webhooks created by other apps are specified, they are ignored. **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

Important inputs: body"""
        tool = self._client.get_tool('delete_webhook_by_id')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWebhookByIdOutput.model_validate(coerce_tool_result(result))
