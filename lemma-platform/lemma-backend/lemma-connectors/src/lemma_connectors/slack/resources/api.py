from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ApiTestToolInput, ApiTestToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ApiTestInput(ApiTestToolInput):
    """Operation input for `api_test`."""
    pass

class ApiTestOutput(ApiTestToolOutput):
    """Operation output for `api_test`."""
    pass

class SlackApiResource(BaseResourceClient):
    """Operations for the `api` resource."""

    @operation(
        name='api_test',
        title='ApiTest',
        input_model=ApiTestInput,
        output_model=ApiTestOutput,
        tools_used=('api_test',),
        tags=tuple(['api']),
    )
    async def test(self, data: ApiTestInput) -> ApiTestOutput:
        """Checks API calling code.

Important inputs: error, foo"""
        tool = self._client.get_tool('api_test')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ApiTestOutput.model_validate(coerce_tool_result(result))
