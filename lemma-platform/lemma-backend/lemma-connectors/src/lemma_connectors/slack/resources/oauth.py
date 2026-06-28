from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import OauthAccessToolInput, OauthAccessToolOutput, OauthTokenToolInput, OauthTokenToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class OauthAccessInput(OauthAccessToolInput):
    """Operation input for `oauth_access`."""
    pass

class OauthAccessOutput(OauthAccessToolOutput):
    """Operation output for `oauth_access`."""
    pass

class OauthTokenInput(OauthTokenToolInput):
    """Operation input for `oauth_token`."""
    pass

class OauthTokenOutput(OauthTokenToolOutput):
    """Operation output for `oauth_token`."""
    pass

class SlackOauthResource(BaseResourceClient):
    """Operations for the `oauth` resource."""

    @operation(
        name='oauth_access',
        title='OauthAccess',
        input_model=OauthAccessInput,
        output_model=OauthAccessOutput,
        tools_used=('oauth_access',),
        tags=tuple(['oauth']),
    )
    async def access(self, data: OauthAccessInput) -> OauthAccessOutput:
        """Exchanges a temporary OAuth verifier code for an access token.

Important inputs: client_id, client_secret, code, redirect_uri, single_channel"""
        tool = self._client.get_tool('oauth_access')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return OauthAccessOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='oauth_token',
        title='OauthToken',
        input_model=OauthTokenInput,
        output_model=OauthTokenOutput,
        tools_used=('oauth_token',),
        tags=tuple(['oauth']),
    )
    async def token(self, data: OauthTokenInput) -> OauthTokenOutput:
        """Exchanges a temporary OAuth verifier code for a workspace token.

Important inputs: client_id, client_secret, code, redirect_uri, single_channel"""
        tool = self._client.get_tool('oauth_token')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return OauthTokenOutput.model_validate(coerce_tool_result(result))
