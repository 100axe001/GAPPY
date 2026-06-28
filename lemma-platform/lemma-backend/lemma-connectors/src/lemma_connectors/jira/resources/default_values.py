from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetDefaultValuesToolInput, GetDefaultValuesToolOutput, SetDefaultValuesToolInput, SetDefaultValuesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetDefaultValuesInput(GetDefaultValuesToolInput):
    """Operation input for `get_default_values`."""
    pass

class GetDefaultValuesOutput(GetDefaultValuesToolOutput):
    """Operation output for `get_default_values`."""
    pass

class SetDefaultValuesInput(SetDefaultValuesToolInput):
    """Operation input for `set_default_values`."""
    pass

class SetDefaultValuesOutput(SetDefaultValuesToolOutput):
    """Operation output for `set_default_values`."""
    pass

class JiraDefaultValuesResource(BaseResourceClient):
    """Operations for the `default_values` resource."""

    @operation(
        name='get_default_values',
        title='GetDefaultValues',
        input_model=GetDefaultValuesInput,
        output_model=GetDefaultValuesOutput,
        tools_used=('get_default_values',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def get(self, data: GetDefaultValuesInput) -> GetDefaultValuesOutput:
        """Returns a [paginated](#pagination) list of defaults for a custom field. The results can be filtered by `contextId`, otherwise all values are returned. If no defaults are set for a context, nothing is returned. The returned object depends on type of the custom field: * `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields. * `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields. * `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select lists and radio buttons. * `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice select lists and checkboxes. * `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select lists. * `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users. * `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists. * `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice group pickers. * `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple choice group pickers. * `CustomFieldContextDefaultValueURL` (type `url`) for URLs. * `CustomFieldContextDefaultValueProject` (type `project`) for project pickers. * `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers). * `CustomFieldContextDefaultValueLabels` (type `labels`) for labels. * `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields. * `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields. * `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields. * `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice version pickers. * `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice version pickers. Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning: * `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string fields. * `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge string collection fields. * `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object fields. * `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-time fields. * `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields. * `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge group collection fields. * `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number fields. * `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields. * `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user collection fields. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, start_at, max_results"""
        tool = self._client.get_tool('get_default_values')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDefaultValuesOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_default_values',
        title='SetDefaultValues',
        input_model=SetDefaultValuesInput,
        output_model=SetDefaultValuesOutput,
        tools_used=('set_default_values',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def set(self, data: SetDefaultValuesInput) -> SetDefaultValuesOutput:
        """Sets default for contexts of a custom field. Default are defined using these objects: * `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields. * `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields. * `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select lists and radio buttons. * `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice select lists and checkboxes. * `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select lists. * `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users. * `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists. * `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice group pickers. * `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple choice group pickers. * `CustomFieldContextDefaultValueURL` (type `url`) for URLs. * `CustomFieldContextDefaultValueProject` (type `project`) for project pickers. * `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers). * `CustomFieldContextDefaultValueLabels` (type `labels`) for labels. * `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields. * `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields. * `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields. * `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice version pickers. * `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice version pickers. Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning: * `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string fields. * `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge string collection fields. * `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object fields. * `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-time fields. * `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields. * `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge group collection fields. * `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number fields. * `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields. * `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user collection fields. Only one type of default object can be included in a request. To remove a default for a context, set the default parameter to `null`. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, body"""
        tool = self._client.get_tool('set_default_values')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetDefaultValuesOutput.model_validate(coerce_tool_result(result))
