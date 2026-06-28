from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddonPropertiesResourceDeleteAddonPropertyDeleteToolInput, AddonPropertiesResourceDeleteAddonPropertyDeleteToolOutput, AddonPropertiesResourceGetAddonPropertiesGetToolInput, AddonPropertiesResourceGetAddonPropertiesGetToolOutput, AddonPropertiesResourceGetAddonPropertyGetToolInput, AddonPropertiesResourceGetAddonPropertyGetToolOutput, AddonPropertiesResourcePutAddonPropertyPutToolInput, AddonPropertiesResourcePutAddonPropertyPutToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddonPropertiesResourceDeleteAddonPropertyDeleteInput(AddonPropertiesResourceDeleteAddonPropertyDeleteToolInput):
    """Operation input for `addon_properties_resource_delete_addon_property_delete`."""
    pass

class AddonPropertiesResourceDeleteAddonPropertyDeleteOutput(AddonPropertiesResourceDeleteAddonPropertyDeleteToolOutput):
    """Operation output for `addon_properties_resource_delete_addon_property_delete`."""
    pass

class AddonPropertiesResourceGetAddonPropertiesGetInput(AddonPropertiesResourceGetAddonPropertiesGetToolInput):
    """Operation input for `addon_properties_resource_get_addon_properties_get`."""
    pass

class AddonPropertiesResourceGetAddonPropertiesGetOutput(AddonPropertiesResourceGetAddonPropertiesGetToolOutput):
    """Operation output for `addon_properties_resource_get_addon_properties_get`."""
    pass

class AddonPropertiesResourceGetAddonPropertyGetInput(AddonPropertiesResourceGetAddonPropertyGetToolInput):
    """Operation input for `addon_properties_resource_get_addon_property_get`."""
    pass

class AddonPropertiesResourceGetAddonPropertyGetOutput(AddonPropertiesResourceGetAddonPropertyGetToolOutput):
    """Operation output for `addon_properties_resource_get_addon_property_get`."""
    pass

class AddonPropertiesResourcePutAddonPropertyPutInput(AddonPropertiesResourcePutAddonPropertyPutToolInput):
    """Operation input for `addon_properties_resource_put_addon_property_put`."""
    pass

class AddonPropertiesResourcePutAddonPropertyPutOutput(AddonPropertiesResourcePutAddonPropertyPutToolOutput):
    """Operation output for `addon_properties_resource_put_addon_property_put`."""
    pass

class JiraAddonPropertiesResourceResource(BaseResourceClient):
    """Operations for the `addon_properties_resource` resource."""

    @operation(
        name='addon_properties_resource_delete_addon_property_delete',
        title='AddonPropertiesResourceDeleteAddonPropertyDelete',
        input_model=AddonPropertiesResourceDeleteAddonPropertyDeleteInput,
        output_model=AddonPropertiesResourceDeleteAddonPropertyDeleteOutput,
        tools_used=('addon_properties_resource_delete_addon_property_delete',),
        tags=tuple(['App properties']),
    )
    async def delete_addon_property_delete(self, data: AddonPropertiesResourceDeleteAddonPropertyDeleteInput) -> AddonPropertiesResourceDeleteAddonPropertyDeleteOutput:
        """Deletes an app's property. **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.

Important inputs: addon_key, property_key"""
        tool = self._client.get_tool('addon_properties_resource_delete_addon_property_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddonPropertiesResourceDeleteAddonPropertyDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='addon_properties_resource_get_addon_properties_get',
        title='AddonPropertiesResourceGetAddonPropertiesGet',
        input_model=AddonPropertiesResourceGetAddonPropertiesGetInput,
        output_model=AddonPropertiesResourceGetAddonPropertiesGetOutput,
        tools_used=('addon_properties_resource_get_addon_properties_get',),
        tags=tuple(['App properties']),
    )
    async def get_addon_properties_get(self, data: AddonPropertiesResourceGetAddonPropertiesGetInput) -> AddonPropertiesResourceGetAddonPropertiesGetOutput:
        """Gets all the properties of an app. **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request. Additionally, Forge apps published on the Marketplace can access properties of Connect apps they were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

Important inputs: addon_key"""
        tool = self._client.get_tool('addon_properties_resource_get_addon_properties_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddonPropertiesResourceGetAddonPropertiesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='addon_properties_resource_get_addon_property_get',
        title='AddonPropertiesResourceGetAddonPropertyGet',
        input_model=AddonPropertiesResourceGetAddonPropertyGetInput,
        output_model=AddonPropertiesResourceGetAddonPropertyGetOutput,
        tools_used=('addon_properties_resource_get_addon_property_get',),
        tags=tuple(['App properties']),
    )
    async def get_addon_property_get(self, data: AddonPropertiesResourceGetAddonPropertyGetInput) -> AddonPropertiesResourceGetAddonPropertyGetOutput:
        """Returns the key and value of an app's property. **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request. Additionally, Forge apps published on the Marketplace can access properties of Connect apps they were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

Important inputs: addon_key, property_key"""
        tool = self._client.get_tool('addon_properties_resource_get_addon_property_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddonPropertiesResourceGetAddonPropertyGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='addon_properties_resource_put_addon_property_put',
        title='AddonPropertiesResourcePutAddonPropertyPut',
        input_model=AddonPropertiesResourcePutAddonPropertyPutInput,
        output_model=AddonPropertiesResourcePutAddonPropertyPutOutput,
        tools_used=('addon_properties_resource_put_addon_property_put',),
        tags=tuple(['App properties']),
    )
    async def put_addon_property_put(self, data: AddonPropertiesResourcePutAddonPropertyPutInput) -> AddonPropertiesResourcePutAddonPropertyPutOutput:
        """Sets the value of an app's property. Use this resource to store custom data for your app. The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters. **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.

Important inputs: addon_key, property_key, body"""
        tool = self._client.get_tool('addon_properties_resource_put_addon_property_put')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddonPropertiesResourcePutAddonPropertyPutOutput.model_validate(coerce_tool_result(result))
