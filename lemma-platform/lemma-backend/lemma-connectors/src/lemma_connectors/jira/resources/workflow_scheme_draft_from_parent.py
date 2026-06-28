from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateWorkflowSchemeDraftFromParentToolInput, CreateWorkflowSchemeDraftFromParentToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateWorkflowSchemeDraftFromParentInput(CreateWorkflowSchemeDraftFromParentToolInput):
    """Operation input for `create_workflow_scheme_draft_from_parent`."""
    pass

class CreateWorkflowSchemeDraftFromParentOutput(CreateWorkflowSchemeDraftFromParentToolOutput):
    """Operation output for `create_workflow_scheme_draft_from_parent`."""
    pass

class JiraWorkflowSchemeDraftFromParentResource(BaseResourceClient):
    """Operations for the `workflow_scheme_draft_from_parent` resource."""

    @operation(
        name='create_workflow_scheme_draft_from_parent',
        title='CreateWorkflowSchemeDraftFromParent',
        input_model=CreateWorkflowSchemeDraftFromParentInput,
        output_model=CreateWorkflowSchemeDraftFromParentOutput,
        tools_used=('create_workflow_scheme_draft_from_parent',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def create(self, data: CreateWorkflowSchemeDraftFromParentInput) -> CreateWorkflowSchemeDraftFromParentOutput:
        """Create a draft workflow scheme from an active workflow scheme, by copying the active workflow scheme. Note that an active workflow scheme can only have one draft workflow scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('create_workflow_scheme_draft_from_parent')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateWorkflowSchemeDraftFromParentOutput.model_validate(coerce_tool_result(result))
