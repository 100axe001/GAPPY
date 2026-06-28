from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetWorkflowSchemeProjectAssociationsToolInput, GetWorkflowSchemeProjectAssociationsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetWorkflowSchemeProjectAssociationsInput(GetWorkflowSchemeProjectAssociationsToolInput):
    """Operation input for `get_workflow_scheme_project_associations`."""
    pass

class GetWorkflowSchemeProjectAssociationsOutput(GetWorkflowSchemeProjectAssociationsToolOutput):
    """Operation output for `get_workflow_scheme_project_associations`."""
    pass

class JiraWorkflowSchemeProjectAssociationsResource(BaseResourceClient):
    """Operations for the `workflow_scheme_project_associations` resource."""

    @operation(
        name='get_workflow_scheme_project_associations',
        title='GetWorkflowSchemeProjectAssociations',
        input_model=GetWorkflowSchemeProjectAssociationsInput,
        output_model=GetWorkflowSchemeProjectAssociationsOutput,
        tools_used=('get_workflow_scheme_project_associations',),
        tags=tuple(['Workflow scheme project associations']),
    )
    async def get(self, data: GetWorkflowSchemeProjectAssociationsInput) -> GetWorkflowSchemeProjectAssociationsOutput:
        """Returns a list of the workflow schemes associated with a list of projects. Each returned workflow scheme includes a list of the requested projects associated with it. Any team-managed or non-existent projects in the request are ignored and no errors are returned. If the project is associated with the `Default Workflow Scheme` no ID is returned. This is because the way the `Default Workflow Scheme` is stored means it has no ID. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id"""
        tool = self._client.get_tool('get_workflow_scheme_project_associations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorkflowSchemeProjectAssociationsOutput.model_validate(coerce_tool_result(result))
