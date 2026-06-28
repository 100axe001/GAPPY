from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AnalyseExpressionToolInput, AnalyseExpressionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AnalyseExpressionInput(AnalyseExpressionToolInput):
    """Operation input for `analyse_expression`."""
    pass

class AnalyseExpressionOutput(AnalyseExpressionToolOutput):
    """Operation output for `analyse_expression`."""
    pass

class JiraAnalyseResource(BaseResourceClient):
    """Operations for the `analyse` resource."""

    @operation(
        name='analyse_expression',
        title='AnalyseExpression',
        input_model=AnalyseExpressionInput,
        output_model=AnalyseExpressionOutput,
        tools_used=('analyse_expression',),
        tags=tuple(['Jira expressions']),
    )
    async def expression(self, data: AnalyseExpressionInput) -> AnalyseExpressionOutput:
        """Analyses and validates Jira expressions. As an experimental feature, this operation can also attempt to type-check the expressions. Learn more about Jira expressions in the [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/). **[Permissions](#permissions) required**: None.

Important inputs: check, body"""
        tool = self._client.get_tool('analyse_expression')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AnalyseExpressionOutput.model_validate(coerce_tool_result(result))
