from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import MigrationResourceUpdateEntityPropertiesValuePutToolInput, MigrationResourceUpdateEntityPropertiesValuePutToolOutput, MigrationResourceWorkflowRuleSearchPostToolInput, MigrationResourceWorkflowRuleSearchPostToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class MigrationResourceUpdateEntityPropertiesValuePutInput(MigrationResourceUpdateEntityPropertiesValuePutToolInput):
    """Operation input for `migration_resource_update_entity_properties_value_put`."""
    pass

class MigrationResourceUpdateEntityPropertiesValuePutOutput(MigrationResourceUpdateEntityPropertiesValuePutToolOutput):
    """Operation output for `migration_resource_update_entity_properties_value_put`."""
    pass

class MigrationResourceWorkflowRuleSearchPostInput(MigrationResourceWorkflowRuleSearchPostToolInput):
    """Operation input for `migration_resource_workflow_rule_search_post`."""
    pass

class MigrationResourceWorkflowRuleSearchPostOutput(MigrationResourceWorkflowRuleSearchPostToolOutput):
    """Operation output for `migration_resource_workflow_rule_search_post`."""
    pass

class JiraMigrationResourceResource(BaseResourceClient):
    """Operations for the `migration_resource` resource."""

    @operation(
        name='migration_resource_update_entity_properties_value_put',
        title='MigrationResourceUpdateEntityPropertiesValuePut',
        input_model=MigrationResourceUpdateEntityPropertiesValuePutInput,
        output_model=MigrationResourceUpdateEntityPropertiesValuePutOutput,
        tools_used=('migration_resource_update_entity_properties_value_put',),
        tags=tuple(['App migration']),
    )
    async def update_entity_properties_value_put(self, data: MigrationResourceUpdateEntityPropertiesValuePutInput) -> MigrationResourceUpdateEntityPropertiesValuePutOutput:
        """Updates the values of multiple entity properties for an object, up to 50 updates per request. This operation is for use by Connect apps during app migration.

Important inputs: atlassian_transfer_id, entity_type, body"""
        tool = self._client.get_tool('migration_resource_update_entity_properties_value_put')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MigrationResourceUpdateEntityPropertiesValuePutOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='migration_resource_workflow_rule_search_post',
        title='MigrationResourceWorkflowRuleSearchPost',
        input_model=MigrationResourceWorkflowRuleSearchPostInput,
        output_model=MigrationResourceWorkflowRuleSearchPostOutput,
        tools_used=('migration_resource_workflow_rule_search_post',),
        tags=tuple(['App migration']),
    )
    async def workflow_rule_search_post(self, data: MigrationResourceWorkflowRuleSearchPostInput) -> MigrationResourceWorkflowRuleSearchPostOutput:
        """Returns configurations for workflow transition rules migrated from server to cloud and owned by the calling Connect app.

Important inputs: atlassian_transfer_id, body"""
        tool = self._client.get_tool('migration_resource_workflow_rule_search_post')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MigrationResourceWorkflowRuleSearchPostOutput.model_validate(coerce_tool_result(result))
