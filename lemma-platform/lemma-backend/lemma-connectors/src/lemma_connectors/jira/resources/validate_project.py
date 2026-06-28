from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ValidateProjectKeyToolInput, ValidateProjectKeyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ValidateProjectKeyInput(ValidateProjectKeyToolInput):
    """Operation input for `validate_project_key`."""
    pass

class ValidateProjectKeyOutput(ValidateProjectKeyToolOutput):
    """Operation output for `validate_project_key`."""
    pass

class JiraValidateProjectResource(BaseResourceClient):
    """Operations for the `validate_project` resource."""

    @operation(
        name='validate_project_key',
        title='ValidateProjectKey',
        input_model=ValidateProjectKeyInput,
        output_model=ValidateProjectKeyOutput,
        tools_used=('validate_project_key',),
        tags=tuple(['Project key and name validation']),
    )
    async def key(self, data: ValidateProjectKeyInput) -> ValidateProjectKeyOutput:
        """Validates a project key by confirming the key is a valid string and not in use. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('validate_project_key')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ValidateProjectKeyOutput.model_validate(coerce_tool_result(result))
