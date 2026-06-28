from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import OauthV2AccessToolInput, OauthV2AccessToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class OauthV2AccessInput(OauthV2AccessToolInput):
    """Operation input for `oauth_v2_access`."""
    pass

class OauthV2AccessOutput(OauthV2AccessToolOutput):
    """Operation output for `oauth_v2_access`."""
    pass

class SlackOauthV2Resource(BaseResourceClient):
    """Operations for the `oauth_v2` resource."""

    @operation(
        name='oauth_v2_access',
        title='OauthV2Access',
        input_model=OauthV2AccessInput,
        output_model=OauthV2AccessOutput,
        tools_used=('oauth_v2_access',),
        tags=tuple(['oauth.v2', 'oauth']),
    )
    async def access(self, data: OauthV2AccessInput) -> OauthV2AccessOutput:
        """Exchanges a temporary OAuth verifier code for an access token.

Important inputs: client_id, client_secret, code, redirect_uri"""
        tool = self._client.get_tool('oauth_v2_access')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return OauthV2AccessOutput.model_validate(coerce_tool_result(result))
