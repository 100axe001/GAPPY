from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DynamicModulesResourceGetModulesGetToolInput, DynamicModulesResourceGetModulesGetToolOutput, DynamicModulesResourceRegisterModulesPostToolInput, DynamicModulesResourceRegisterModulesPostToolOutput, DynamicModulesResourceRemoveModulesDeleteToolInput, DynamicModulesResourceRemoveModulesDeleteToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DynamicModulesResourceGetModulesGetInput(DynamicModulesResourceGetModulesGetToolInput):
    """Operation input for `dynamic_modules_resource_get_modules_get`."""
    pass

class DynamicModulesResourceGetModulesGetOutput(DynamicModulesResourceGetModulesGetToolOutput):
    """Operation output for `dynamic_modules_resource_get_modules_get`."""
    pass

class DynamicModulesResourceRegisterModulesPostInput(DynamicModulesResourceRegisterModulesPostToolInput):
    """Operation input for `dynamic_modules_resource_register_modules_post`."""
    pass

class DynamicModulesResourceRegisterModulesPostOutput(DynamicModulesResourceRegisterModulesPostToolOutput):
    """Operation output for `dynamic_modules_resource_register_modules_post`."""
    pass

class DynamicModulesResourceRemoveModulesDeleteInput(DynamicModulesResourceRemoveModulesDeleteToolInput):
    """Operation input for `dynamic_modules_resource_remove_modules_delete`."""
    pass

class DynamicModulesResourceRemoveModulesDeleteOutput(DynamicModulesResourceRemoveModulesDeleteToolOutput):
    """Operation output for `dynamic_modules_resource_remove_modules_delete`."""
    pass

class JiraDynamicModulesResourceResource(BaseResourceClient):
    """Operations for the `dynamic_modules_resource` resource."""

    @operation(
        name='dynamic_modules_resource_get_modules_get',
        title='DynamicModulesResourceGetModulesGet',
        input_model=DynamicModulesResourceGetModulesGetInput,
        output_model=DynamicModulesResourceGetModulesGetOutput,
        tools_used=('dynamic_modules_resource_get_modules_get',),
        tags=tuple(['Dynamic modules']),
    )
    async def get_modules_get(self, data: DynamicModulesResourceGetModulesGetInput) -> DynamicModulesResourceGetModulesGetOutput:
        """Returns all modules registered dynamically by the calling app. **[Permissions](#permissions) required:** Only Connect apps can make this request.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('dynamic_modules_resource_get_modules_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DynamicModulesResourceGetModulesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='dynamic_modules_resource_register_modules_post',
        title='DynamicModulesResourceRegisterModulesPost',
        input_model=DynamicModulesResourceRegisterModulesPostInput,
        output_model=DynamicModulesResourceRegisterModulesPostOutput,
        tools_used=('dynamic_modules_resource_register_modules_post',),
        tags=tuple(['Dynamic modules']),
    )
    async def register_modules_post(self, data: DynamicModulesResourceRegisterModulesPostInput) -> DynamicModulesResourceRegisterModulesPostOutput:
        """Registers a list of modules. **[Permissions](#permissions) required:** Only Connect apps can make this request.

Important inputs: body"""
        tool = self._client.get_tool('dynamic_modules_resource_register_modules_post')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DynamicModulesResourceRegisterModulesPostOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='dynamic_modules_resource_remove_modules_delete',
        title='DynamicModulesResourceRemoveModulesDelete',
        input_model=DynamicModulesResourceRemoveModulesDeleteInput,
        output_model=DynamicModulesResourceRemoveModulesDeleteOutput,
        tools_used=('dynamic_modules_resource_remove_modules_delete',),
        tags=tuple(['Dynamic modules']),
    )
    async def remove_modules_delete(self, data: DynamicModulesResourceRemoveModulesDeleteInput) -> DynamicModulesResourceRemoveModulesDeleteOutput:
        """Remove all or a list of modules registered by the calling app. **[Permissions](#permissions) required:** Only Connect apps can make this request.

Important inputs: module_key"""
        tool = self._client.get_tool('dynamic_modules_resource_remove_modules_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DynamicModulesResourceRemoveModulesDeleteOutput.model_validate(coerce_tool_result(result))
