from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetWorkflowTransitionPropertiesToolInput, GetWorkflowTransitionPropertiesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetWorkflowTransitionPropertiesInput(GetWorkflowTransitionPropertiesToolInput):
    """Operation input for `get_workflow_transition_properties`."""
    pass

class GetWorkflowTransitionPropertiesOutput(GetWorkflowTransitionPropertiesToolOutput):
    """Operation output for `get_workflow_transition_properties`."""
    pass

class JiraWorkflowTransitionPropertiesResource(BaseResourceClient):
    """Operations for the `workflow_transition_properties` resource."""

    @operation(
        name='get_workflow_transition_properties',
        title='GetWorkflowTransitionProperties',
        input_model=GetWorkflowTransitionPropertiesInput,
        output_model=GetWorkflowTransitionPropertiesOutput,
        tools_used=('get_workflow_transition_properties',),
        tags=tuple(['Workflow transition properties']),
    )
    async def get(self, data: GetWorkflowTransitionPropertiesInput) -> GetWorkflowTransitionPropertiesOutput:
        """Returns the properties on a workflow transition. Transition properties are used to change the behavior of a transition. For more information, see [Transition properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: transition_id, include_reserved_keys, workflow_name, workflow_mode"""
        tool = self._client.get_tool('get_workflow_transition_properties')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorkflowTransitionPropertiesOutput.model_validate(coerce_tool_result(result))
