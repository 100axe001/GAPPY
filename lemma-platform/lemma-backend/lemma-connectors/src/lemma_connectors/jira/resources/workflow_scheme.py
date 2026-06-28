from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateWorkflowSchemeToolInput, CreateWorkflowSchemeToolOutput, DeleteWorkflowSchemeToolInput, DeleteWorkflowSchemeToolOutput, GetWorkflowSchemeToolInput, GetWorkflowSchemeToolOutput, UpdateWorkflowSchemeToolInput, UpdateWorkflowSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateWorkflowSchemeInput(CreateWorkflowSchemeToolInput):
    """Operation input for `create_workflow_scheme`."""
    pass

class CreateWorkflowSchemeOutput(CreateWorkflowSchemeToolOutput):
    """Operation output for `create_workflow_scheme`."""
    pass

class DeleteWorkflowSchemeInput(DeleteWorkflowSchemeToolInput):
    """Operation input for `delete_workflow_scheme`."""
    pass

class DeleteWorkflowSchemeOutput(DeleteWorkflowSchemeToolOutput):
    """Operation output for `delete_workflow_scheme`."""
    pass

class GetWorkflowSchemeInput(GetWorkflowSchemeToolInput):
    """Operation input for `get_workflow_scheme`."""
    pass

class GetWorkflowSchemeOutput(GetWorkflowSchemeToolOutput):
    """Operation output for `get_workflow_scheme`."""
    pass

class UpdateWorkflowSchemeInput(UpdateWorkflowSchemeToolInput):
    """Operation input for `update_workflow_scheme`."""
    pass

class UpdateWorkflowSchemeOutput(UpdateWorkflowSchemeToolOutput):
    """Operation output for `update_workflow_scheme`."""
    pass

class JiraWorkflowSchemeResource(BaseResourceClient):
    """Operations for the `workflow_scheme` resource."""

    @operation(
        name='create_workflow_scheme',
        title='CreateWorkflowScheme',
        input_model=CreateWorkflowSchemeInput,
        output_model=CreateWorkflowSchemeOutput,
        tools_used=('create_workflow_scheme',),
        tags=tuple(['Workflow schemes']),
    )
    async def create(self, data: CreateWorkflowSchemeInput) -> CreateWorkflowSchemeOutput:
        """Creates a workflow scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_workflow_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateWorkflowSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_workflow_scheme',
        title='DeleteWorkflowScheme',
        input_model=DeleteWorkflowSchemeInput,
        output_model=DeleteWorkflowSchemeOutput,
        tools_used=('delete_workflow_scheme',),
        tags=tuple(['Workflow schemes']),
    )
    async def delete(self, data: DeleteWorkflowSchemeInput) -> DeleteWorkflowSchemeOutput:
        """Deletes a workflow scheme. Note that a workflow scheme cannot be deleted if it is active (that is, being used by at least one project). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('delete_workflow_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWorkflowSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_workflow_scheme',
        title='GetWorkflowScheme',
        input_model=GetWorkflowSchemeInput,
        output_model=GetWorkflowSchemeOutput,
        tools_used=('get_workflow_scheme',),
        tags=tuple(['Workflow schemes']),
    )
    async def get(self, data: GetWorkflowSchemeInput) -> GetWorkflowSchemeOutput:
        """Returns a workflow scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, return_draft_if_exists"""
        tool = self._client.get_tool('get_workflow_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorkflowSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_workflow_scheme',
        title='UpdateWorkflowScheme',
        input_model=UpdateWorkflowSchemeInput,
        output_model=UpdateWorkflowSchemeOutput,
        tools_used=('update_workflow_scheme',),
        tags=tuple(['Workflow schemes']),
    )
    async def update(self, data: UpdateWorkflowSchemeInput) -> UpdateWorkflowSchemeOutput:
        """Updates a workflow scheme, including the name, default workflow, issue type to project mappings, and more. If the workflow scheme is active (that is, being used by at least one project), then a draft workflow scheme is created or updated instead, provided that `updateDraftIfNeeded` is set to `true`. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_workflow_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateWorkflowSchemeOutput.model_validate(coerce_tool_result(result))
