from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import AuthRevokeToolInput, AuthRevokeToolOutput, AuthTestToolInput, AuthTestToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AuthRevokeInput(AuthRevokeToolInput):
    """Operation input for `auth_revoke`."""
    pass

class AuthRevokeOutput(AuthRevokeToolOutput):
    """Operation output for `auth_revoke`."""
    pass

class AuthTestInput(AuthTestToolInput):
    """Operation input for `auth_test`."""
    pass

class AuthTestOutput(AuthTestToolOutput):
    """Operation output for `auth_test`."""
    pass

class SlackAuthResource(BaseResourceClient):
    """Operations for the `auth` resource."""

    @operation(
        name='auth_revoke',
        title='AuthRevoke',
        input_model=AuthRevokeInput,
        output_model=AuthRevokeOutput,
        tools_used=('auth_revoke',),
        tags=tuple(['auth']),
    )
    async def revoke(self, data: AuthRevokeInput) -> AuthRevokeOutput:
        """Revokes a token.

Important inputs: token, test"""
        tool = self._client.get_tool('auth_revoke')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AuthRevokeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='auth_test',
        title='AuthTest',
        input_model=AuthTestInput,
        output_model=AuthTestOutput,
        tools_used=('auth_test',),
        tags=tuple(['auth']),
    )
    async def test(self, data: AuthTestInput) -> AuthTestOutput:
        """Checks authentication & identity.

Important inputs: token"""
        tool = self._client.get_tool('auth_test')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AuthTestOutput.model_validate(coerce_tool_result(result))
