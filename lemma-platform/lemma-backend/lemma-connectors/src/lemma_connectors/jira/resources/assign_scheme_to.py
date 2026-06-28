from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AssignSchemeToProjectToolInput, AssignSchemeToProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AssignSchemeToProjectInput(AssignSchemeToProjectToolInput):
    """Operation input for `assign_scheme_to_project`."""
    pass

class AssignSchemeToProjectOutput(AssignSchemeToProjectToolOutput):
    """Operation output for `assign_scheme_to_project`."""
    pass

class JiraAssignSchemeToResource(BaseResourceClient):
    """Operations for the `assign_scheme_to` resource."""

    @operation(
        name='assign_scheme_to_project',
        title='AssignSchemeToProject',
        input_model=AssignSchemeToProjectInput,
        output_model=AssignSchemeToProjectOutput,
        tools_used=('assign_scheme_to_project',),
        tags=tuple(['Workflow scheme project associations']),
    )
    async def project(self, data: AssignSchemeToProjectInput) -> AssignSchemeToProjectOutput:
        """Assigns a workflow scheme to a project. This operation is performed only when there are no issues in the project. Workflow schemes can only be assigned to classic projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('assign_scheme_to_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AssignSchemeToProjectOutput.model_validate(coerce_tool_result(result))
