from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import RegisterDynamicWebhooksToolInput, RegisterDynamicWebhooksToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RegisterDynamicWebhooksInput(RegisterDynamicWebhooksToolInput):
    """Operation input for `register_dynamic_webhooks`."""
    pass

class RegisterDynamicWebhooksOutput(RegisterDynamicWebhooksToolOutput):
    """Operation output for `register_dynamic_webhooks`."""
    pass

class JiraRegisterDynamicResource(BaseResourceClient):
    """Operations for the `register_dynamic` resource."""

    @operation(
        name='register_dynamic_webhooks',
        title='RegisterDynamicWebhooks',
        input_model=RegisterDynamicWebhooksInput,
        output_model=RegisterDynamicWebhooksOutput,
        tools_used=('register_dynamic_webhooks',),
        tags=tuple(['Webhooks']),
    )
    async def webhooks(self, data: RegisterDynamicWebhooksInput) -> RegisterDynamicWebhooksOutput:
        """Registers webhooks. **NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app owner and the user who registered a dynamic webhook. **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

Important inputs: body"""
        tool = self._client.get_tool('register_dynamic_webhooks')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RegisterDynamicWebhooksOutput.model_validate(coerce_tool_result(result))
