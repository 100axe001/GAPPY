from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateWorkflowTransitionPropertyToolInput, CreateWorkflowTransitionPropertyToolOutput, DeleteWorkflowTransitionPropertyToolInput, DeleteWorkflowTransitionPropertyToolOutput, UpdateWorkflowTransitionPropertyToolInput, UpdateWorkflowTransitionPropertyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateWorkflowTransitionPropertyInput(CreateWorkflowTransitionPropertyToolInput):
    """Operation input for `create_workflow_transition_property`."""
    pass

class CreateWorkflowTransitionPropertyOutput(CreateWorkflowTransitionPropertyToolOutput):
    """Operation output for `create_workflow_transition_property`."""
    pass

class DeleteWorkflowTransitionPropertyInput(DeleteWorkflowTransitionPropertyToolInput):
    """Operation input for `delete_workflow_transition_property`."""
    pass

class DeleteWorkflowTransitionPropertyOutput(DeleteWorkflowTransitionPropertyToolOutput):
    """Operation output for `delete_workflow_transition_property`."""
    pass

class UpdateWorkflowTransitionPropertyInput(UpdateWorkflowTransitionPropertyToolInput):
    """Operation input for `update_workflow_transition_property`."""
    pass

class UpdateWorkflowTransitionPropertyOutput(UpdateWorkflowTransitionPropertyToolOutput):
    """Operation output for `update_workflow_transition_property`."""
    pass

class JiraWorkflowTransitionPropertyResource(BaseResourceClient):
    """Operations for the `workflow_transition_property` resource."""

    @operation(
        name='create_workflow_transition_property',
        title='CreateWorkflowTransitionProperty',
        input_model=CreateWorkflowTransitionPropertyInput,
        output_model=CreateWorkflowTransitionPropertyOutput,
        tools_used=('create_workflow_transition_property',),
        tags=tuple(['Workflow transition properties']),
    )
    async def create(self, data: CreateWorkflowTransitionPropertyInput) -> CreateWorkflowTransitionPropertyOutput:
        """Adds a property to a workflow transition. Transition properties are used to change the behavior of a transition. For more information, see [Transition properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: transition_id, workflow_name, workflow_mode, body"""
        tool = self._client.get_tool('create_workflow_transition_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateWorkflowTransitionPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_workflow_transition_property',
        title='DeleteWorkflowTransitionProperty',
        input_model=DeleteWorkflowTransitionPropertyInput,
        output_model=DeleteWorkflowTransitionPropertyOutput,
        tools_used=('delete_workflow_transition_property',),
        tags=tuple(['Workflow transition properties']),
    )
    async def delete(self, data: DeleteWorkflowTransitionPropertyInput) -> DeleteWorkflowTransitionPropertyOutput:
        """Deletes a property from a workflow transition. Transition properties are used to change the behavior of a transition. For more information, see [Transition properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: transition_id, workflow_name, workflow_mode"""
        tool = self._client.get_tool('delete_workflow_transition_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWorkflowTransitionPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_workflow_transition_property',
        title='UpdateWorkflowTransitionProperty',
        input_model=UpdateWorkflowTransitionPropertyInput,
        output_model=UpdateWorkflowTransitionPropertyOutput,
        tools_used=('update_workflow_transition_property',),
        tags=tuple(['Workflow transition properties']),
    )
    async def update(self, data: UpdateWorkflowTransitionPropertyInput) -> UpdateWorkflowTransitionPropertyOutput:
        """Updates a workflow transition by changing the property value. Trying to update a property that does not exist results in a new property being added to the transition. Transition properties are used to change the behavior of a transition. For more information, see [Transition properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: transition_id, workflow_name, workflow_mode, body"""
        tool = self._client.get_tool('update_workflow_transition_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateWorkflowTransitionPropertyOutput.model_validate(coerce_tool_result(result))
