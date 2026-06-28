from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteWorkflowTransitionRuleConfigurationsToolInput, DeleteWorkflowTransitionRuleConfigurationsToolOutput, GetWorkflowTransitionRuleConfigurationsToolInput, GetWorkflowTransitionRuleConfigurationsToolOutput, UpdateWorkflowTransitionRuleConfigurationsToolInput, UpdateWorkflowTransitionRuleConfigurationsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteWorkflowTransitionRuleConfigurationsInput(DeleteWorkflowTransitionRuleConfigurationsToolInput):
    """Operation input for `delete_workflow_transition_rule_configurations`."""
    pass

class DeleteWorkflowTransitionRuleConfigurationsOutput(DeleteWorkflowTransitionRuleConfigurationsToolOutput):
    """Operation output for `delete_workflow_transition_rule_configurations`."""
    pass

class GetWorkflowTransitionRuleConfigurationsInput(GetWorkflowTransitionRuleConfigurationsToolInput):
    """Operation input for `get_workflow_transition_rule_configurations`."""
    pass

class GetWorkflowTransitionRuleConfigurationsOutput(GetWorkflowTransitionRuleConfigurationsToolOutput):
    """Operation output for `get_workflow_transition_rule_configurations`."""
    pass

class UpdateWorkflowTransitionRuleConfigurationsInput(UpdateWorkflowTransitionRuleConfigurationsToolInput):
    """Operation input for `update_workflow_transition_rule_configurations`."""
    pass

class UpdateWorkflowTransitionRuleConfigurationsOutput(UpdateWorkflowTransitionRuleConfigurationsToolOutput):
    """Operation output for `update_workflow_transition_rule_configurations`."""
    pass

class JiraWorkflowTransitionRuleConfigurationsResource(BaseResourceClient):
    """Operations for the `workflow_transition_rule_configurations` resource."""

    @operation(
        name='delete_workflow_transition_rule_configurations',
        title='DeleteWorkflowTransitionRuleConfigurations',
        input_model=DeleteWorkflowTransitionRuleConfigurationsInput,
        output_model=DeleteWorkflowTransitionRuleConfigurationsOutput,
        tools_used=('delete_workflow_transition_rule_configurations',),
        tags=tuple(['Workflow transition rules']),
    )
    async def delete(self, data: DeleteWorkflowTransitionRuleConfigurationsInput) -> DeleteWorkflowTransitionRuleConfigurationsOutput:
        """Deletes workflow transition rules from one or more workflows. These rule types are supported: * [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/) * [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/) * [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/) Only rules created by the calling Connect app can be deleted. **[Permissions](#permissions) required:** Only Connect apps can use this operation.

Important inputs: body"""
        tool = self._client.get_tool('delete_workflow_transition_rule_configurations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWorkflowTransitionRuleConfigurationsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_workflow_transition_rule_configurations',
        title='GetWorkflowTransitionRuleConfigurations',
        input_model=GetWorkflowTransitionRuleConfigurationsInput,
        output_model=GetWorkflowTransitionRuleConfigurationsOutput,
        tools_used=('get_workflow_transition_rule_configurations',),
        tags=tuple(['Workflow transition rules']),
    )
    async def get(self, data: GetWorkflowTransitionRuleConfigurationsInput) -> GetWorkflowTransitionRuleConfigurationsOutput:
        """Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules: * of one or more transition rule types, such as [workflow post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/). * matching one or more transition rule keys. Only workflows containing transition rules created by the calling Connect app are returned. Due to server-side optimizations, workflows with an empty list of rules may be returned; these workflows can be ignored. **[Permissions](#permissions) required:** Only Connect apps can use this operation.

Important inputs: start_at, max_results, types, keys, workflow_names, with_tags, draft, expand"""
        tool = self._client.get_tool('get_workflow_transition_rule_configurations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorkflowTransitionRuleConfigurationsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_workflow_transition_rule_configurations',
        title='UpdateWorkflowTransitionRuleConfigurations',
        input_model=UpdateWorkflowTransitionRuleConfigurationsInput,
        output_model=UpdateWorkflowTransitionRuleConfigurationsOutput,
        tools_used=('update_workflow_transition_rule_configurations',),
        tags=tuple(['Workflow transition rules']),
    )
    async def update(self, data: UpdateWorkflowTransitionRuleConfigurationsInput) -> UpdateWorkflowTransitionRuleConfigurationsOutput:
        """Updates configuration of workflow transition rules. The following rule types are supported: * [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/) * [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/) * [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/) Only rules created by the calling Connect app can be updated. To assist with app migration, this operation can be used to: * Disable a rule. * Add a `tag`. Use this to filter rules in the [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get). Rules are enabled if the `disabled` parameter is not provided. **[Permissions](#permissions) required:** Only Connect apps can use this operation.

Important inputs: body"""
        tool = self._client.get_tool('update_workflow_transition_rule_configurations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateWorkflowTransitionRuleConfigurationsOutput.model_validate(coerce_tool_result(result))
