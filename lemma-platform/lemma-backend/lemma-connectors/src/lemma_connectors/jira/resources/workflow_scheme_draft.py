from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteWorkflowSchemeDraftToolInput, DeleteWorkflowSchemeDraftToolOutput, GetWorkflowSchemeDraftToolInput, GetWorkflowSchemeDraftToolOutput, UpdateWorkflowSchemeDraftToolInput, UpdateWorkflowSchemeDraftToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteWorkflowSchemeDraftInput(DeleteWorkflowSchemeDraftToolInput):
    """Operation input for `delete_workflow_scheme_draft`."""
    pass

class DeleteWorkflowSchemeDraftOutput(DeleteWorkflowSchemeDraftToolOutput):
    """Operation output for `delete_workflow_scheme_draft`."""
    pass

class GetWorkflowSchemeDraftInput(GetWorkflowSchemeDraftToolInput):
    """Operation input for `get_workflow_scheme_draft`."""
    pass

class GetWorkflowSchemeDraftOutput(GetWorkflowSchemeDraftToolOutput):
    """Operation output for `get_workflow_scheme_draft`."""
    pass

class UpdateWorkflowSchemeDraftInput(UpdateWorkflowSchemeDraftToolInput):
    """Operation input for `update_workflow_scheme_draft`."""
    pass

class UpdateWorkflowSchemeDraftOutput(UpdateWorkflowSchemeDraftToolOutput):
    """Operation output for `update_workflow_scheme_draft`."""
    pass

class JiraWorkflowSchemeDraftResource(BaseResourceClient):
    """Operations for the `workflow_scheme_draft` resource."""

    @operation(
        name='delete_workflow_scheme_draft',
        title='DeleteWorkflowSchemeDraft',
        input_model=DeleteWorkflowSchemeDraftInput,
        output_model=DeleteWorkflowSchemeDraftOutput,
        tools_used=('delete_workflow_scheme_draft',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def delete(self, data: DeleteWorkflowSchemeDraftInput) -> DeleteWorkflowSchemeDraftOutput:
        """Deletes a draft workflow scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('delete_workflow_scheme_draft')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWorkflowSchemeDraftOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_workflow_scheme_draft',
        title='GetWorkflowSchemeDraft',
        input_model=GetWorkflowSchemeDraftInput,
        output_model=GetWorkflowSchemeDraftOutput,
        tools_used=('get_workflow_scheme_draft',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def get(self, data: GetWorkflowSchemeDraftInput) -> GetWorkflowSchemeDraftOutput:
        """Returns the draft workflow scheme for an active workflow scheme. Draft workflow schemes allow changes to be made to the active workflow schemes: When an active workflow scheme is updated, a draft copy is created. The draft is modified, then the changes in the draft are copied back to the active workflow scheme. See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information. Note that: * Only active workflow schemes can have draft workflow schemes. * An active workflow scheme can only have one draft workflow scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('get_workflow_scheme_draft')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorkflowSchemeDraftOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_workflow_scheme_draft',
        title='UpdateWorkflowSchemeDraft',
        input_model=UpdateWorkflowSchemeDraftInput,
        output_model=UpdateWorkflowSchemeDraftOutput,
        tools_used=('update_workflow_scheme_draft',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def update(self, data: UpdateWorkflowSchemeDraftInput) -> UpdateWorkflowSchemeDraftOutput:
        """Updates a draft workflow scheme. If a draft workflow scheme does not exist for the active workflow scheme, then a draft is created. Note that an active workflow scheme can only have one draft workflow scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_workflow_scheme_draft')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateWorkflowSchemeDraftOutput.model_validate(coerce_tool_result(result))
