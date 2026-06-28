from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_field_context_default_value_cascading_option import CustomFieldContextDefaultValueCascadingOption
  from ..models.custom_field_context_default_value_date import CustomFieldContextDefaultValueDate
  from ..models.custom_field_context_default_value_date_time import CustomFieldContextDefaultValueDateTime
  from ..models.custom_field_context_default_value_float import CustomFieldContextDefaultValueFloat
  from ..models.custom_field_context_default_value_forge_date_time_field import CustomFieldContextDefaultValueForgeDateTimeField
  from ..models.custom_field_context_default_value_forge_group_field import CustomFieldContextDefaultValueForgeGroupField
  from ..models.custom_field_context_default_value_forge_multi_group_field import CustomFieldContextDefaultValueForgeMultiGroupField
  from ..models.custom_field_context_default_value_forge_multi_string_field import CustomFieldContextDefaultValueForgeMultiStringField
  from ..models.custom_field_context_default_value_forge_multi_user_field import CustomFieldContextDefaultValueForgeMultiUserField
  from ..models.custom_field_context_default_value_forge_number_field import CustomFieldContextDefaultValueForgeNumberField
  from ..models.custom_field_context_default_value_forge_object_field import CustomFieldContextDefaultValueForgeObjectField
  from ..models.custom_field_context_default_value_forge_string_field import CustomFieldContextDefaultValueForgeStringField
  from ..models.custom_field_context_default_value_forge_user_field import CustomFieldContextDefaultValueForgeUserField
  from ..models.custom_field_context_default_value_labels import CustomFieldContextDefaultValueLabels
  from ..models.custom_field_context_default_value_multi_user_picker import CustomFieldContextDefaultValueMultiUserPicker
  from ..models.custom_field_context_default_value_multiple_group_picker import CustomFieldContextDefaultValueMultipleGroupPicker
  from ..models.custom_field_context_default_value_multiple_option import CustomFieldContextDefaultValueMultipleOption
  from ..models.custom_field_context_default_value_multiple_version_picker import CustomFieldContextDefaultValueMultipleVersionPicker
  from ..models.custom_field_context_default_value_project import CustomFieldContextDefaultValueProject
  from ..models.custom_field_context_default_value_read_only import CustomFieldContextDefaultValueReadOnly
  from ..models.custom_field_context_default_value_single_group_picker import CustomFieldContextDefaultValueSingleGroupPicker
  from ..models.custom_field_context_default_value_single_option import CustomFieldContextDefaultValueSingleOption
  from ..models.custom_field_context_default_value_single_version_picker import CustomFieldContextDefaultValueSingleVersionPicker
  from ..models.custom_field_context_default_value_text_area import CustomFieldContextDefaultValueTextArea
  from ..models.custom_field_context_default_value_text_field import CustomFieldContextDefaultValueTextField
  from ..models.custom_field_context_default_value_url import CustomFieldContextDefaultValueURL
  from ..models.custom_field_context_single_user_picker_defaults import CustomFieldContextSingleUserPickerDefaults





T = TypeVar("T", bound="CustomFieldContextDefaultValueUpdate")



@_attrs_define
class CustomFieldContextDefaultValueUpdate:
    """ Default values to update.

        Attributes:
            default_values (list[CustomFieldContextDefaultValueCascadingOption | CustomFieldContextDefaultValueDate |
                CustomFieldContextDefaultValueDateTime | CustomFieldContextDefaultValueFloat |
                CustomFieldContextDefaultValueForgeDateTimeField | CustomFieldContextDefaultValueForgeGroupField |
                CustomFieldContextDefaultValueForgeMultiGroupField | CustomFieldContextDefaultValueForgeMultiStringField |
                CustomFieldContextDefaultValueForgeMultiUserField | CustomFieldContextDefaultValueForgeNumberField |
                CustomFieldContextDefaultValueForgeObjectField | CustomFieldContextDefaultValueForgeStringField |
                CustomFieldContextDefaultValueForgeUserField | CustomFieldContextDefaultValueLabels |
                CustomFieldContextDefaultValueMultipleGroupPicker | CustomFieldContextDefaultValueMultipleOption |
                CustomFieldContextDefaultValueMultipleVersionPicker | CustomFieldContextDefaultValueMultiUserPicker |
                CustomFieldContextDefaultValueProject | CustomFieldContextDefaultValueReadOnly |
                CustomFieldContextDefaultValueSingleGroupPicker | CustomFieldContextDefaultValueSingleOption |
                CustomFieldContextDefaultValueSingleVersionPicker | CustomFieldContextDefaultValueTextArea |
                CustomFieldContextDefaultValueTextField | CustomFieldContextDefaultValueURL |
                CustomFieldContextSingleUserPickerDefaults] | Unset):
     """

    default_values: list[CustomFieldContextDefaultValueCascadingOption | CustomFieldContextDefaultValueDate | CustomFieldContextDefaultValueDateTime | CustomFieldContextDefaultValueFloat | CustomFieldContextDefaultValueForgeDateTimeField | CustomFieldContextDefaultValueForgeGroupField | CustomFieldContextDefaultValueForgeMultiGroupField | CustomFieldContextDefaultValueForgeMultiStringField | CustomFieldContextDefaultValueForgeMultiUserField | CustomFieldContextDefaultValueForgeNumberField | CustomFieldContextDefaultValueForgeObjectField | CustomFieldContextDefaultValueForgeStringField | CustomFieldContextDefaultValueForgeUserField | CustomFieldContextDefaultValueLabels | CustomFieldContextDefaultValueMultipleGroupPicker | CustomFieldContextDefaultValueMultipleOption | CustomFieldContextDefaultValueMultipleVersionPicker | CustomFieldContextDefaultValueMultiUserPicker | CustomFieldContextDefaultValueProject | CustomFieldContextDefaultValueReadOnly | CustomFieldContextDefaultValueSingleGroupPicker | CustomFieldContextDefaultValueSingleOption | CustomFieldContextDefaultValueSingleVersionPicker | CustomFieldContextDefaultValueTextArea | CustomFieldContextDefaultValueTextField | CustomFieldContextDefaultValueURL | CustomFieldContextSingleUserPickerDefaults] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_field_context_default_value_cascading_option import CustomFieldContextDefaultValueCascadingOption
        from ..models.custom_field_context_default_value_date import CustomFieldContextDefaultValueDate
        from ..models.custom_field_context_default_value_date_time import CustomFieldContextDefaultValueDateTime
        from ..models.custom_field_context_default_value_float import CustomFieldContextDefaultValueFloat
        from ..models.custom_field_context_default_value_forge_date_time_field import CustomFieldContextDefaultValueForgeDateTimeField
        from ..models.custom_field_context_default_value_forge_group_field import CustomFieldContextDefaultValueForgeGroupField
        from ..models.custom_field_context_default_value_forge_multi_group_field import CustomFieldContextDefaultValueForgeMultiGroupField
        from ..models.custom_field_context_default_value_forge_multi_string_field import CustomFieldContextDefaultValueForgeMultiStringField
        from ..models.custom_field_context_default_value_forge_multi_user_field import CustomFieldContextDefaultValueForgeMultiUserField
        from ..models.custom_field_context_default_value_forge_number_field import CustomFieldContextDefaultValueForgeNumberField
        from ..models.custom_field_context_default_value_forge_object_field import CustomFieldContextDefaultValueForgeObjectField
        from ..models.custom_field_context_default_value_forge_string_field import CustomFieldContextDefaultValueForgeStringField
        from ..models.custom_field_context_default_value_forge_user_field import CustomFieldContextDefaultValueForgeUserField
        from ..models.custom_field_context_default_value_labels import CustomFieldContextDefaultValueLabels
        from ..models.custom_field_context_default_value_multi_user_picker import CustomFieldContextDefaultValueMultiUserPicker
        from ..models.custom_field_context_default_value_multiple_group_picker import CustomFieldContextDefaultValueMultipleGroupPicker
        from ..models.custom_field_context_default_value_multiple_option import CustomFieldContextDefaultValueMultipleOption
        from ..models.custom_field_context_default_value_multiple_version_picker import CustomFieldContextDefaultValueMultipleVersionPicker
        from ..models.custom_field_context_default_value_project import CustomFieldContextDefaultValueProject
        from ..models.custom_field_context_default_value_read_only import CustomFieldContextDefaultValueReadOnly
        from ..models.custom_field_context_default_value_single_group_picker import CustomFieldContextDefaultValueSingleGroupPicker
        from ..models.custom_field_context_default_value_single_option import CustomFieldContextDefaultValueSingleOption
        from ..models.custom_field_context_default_value_single_version_picker import CustomFieldContextDefaultValueSingleVersionPicker
        from ..models.custom_field_context_default_value_text_area import CustomFieldContextDefaultValueTextArea
        from ..models.custom_field_context_default_value_text_field import CustomFieldContextDefaultValueTextField
        from ..models.custom_field_context_default_value_url import CustomFieldContextDefaultValueURL
        from ..models.custom_field_context_single_user_picker_defaults import CustomFieldContextSingleUserPickerDefaults
        default_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_values, Unset):
            default_values = []
            for default_values_item_data in self.default_values:
                default_values_item: dict[str, Any]
                if isinstance(default_values_item_data, CustomFieldContextDefaultValueCascadingOption):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueMultipleOption):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueSingleOption):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextSingleUserPickerDefaults):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueMultiUserPicker):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueSingleGroupPicker):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueMultipleGroupPicker):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueDate):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueDateTime):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueURL):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueProject):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueFloat):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueLabels):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueTextField):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueTextArea):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueReadOnly):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueSingleVersionPicker):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueMultipleVersionPicker):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueForgeStringField):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueForgeMultiStringField):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueForgeObjectField):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueForgeDateTimeField):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueForgeGroupField):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueForgeMultiGroupField):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueForgeNumberField):
                    default_values_item = default_values_item_data.to_dict()
                elif isinstance(default_values_item_data, CustomFieldContextDefaultValueForgeUserField):
                    default_values_item = default_values_item_data.to_dict()
                else:
                    default_values_item = default_values_item_data.to_dict()

                default_values.append(default_values_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if default_values is not UNSET:
            field_dict["defaultValues"] = default_values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_context_default_value_cascading_option import CustomFieldContextDefaultValueCascadingOption
        from ..models.custom_field_context_default_value_date import CustomFieldContextDefaultValueDate
        from ..models.custom_field_context_default_value_date_time import CustomFieldContextDefaultValueDateTime
        from ..models.custom_field_context_default_value_float import CustomFieldContextDefaultValueFloat
        from ..models.custom_field_context_default_value_forge_date_time_field import CustomFieldContextDefaultValueForgeDateTimeField
        from ..models.custom_field_context_default_value_forge_group_field import CustomFieldContextDefaultValueForgeGroupField
        from ..models.custom_field_context_default_value_forge_multi_group_field import CustomFieldContextDefaultValueForgeMultiGroupField
        from ..models.custom_field_context_default_value_forge_multi_string_field import CustomFieldContextDefaultValueForgeMultiStringField
        from ..models.custom_field_context_default_value_forge_multi_user_field import CustomFieldContextDefaultValueForgeMultiUserField
        from ..models.custom_field_context_default_value_forge_number_field import CustomFieldContextDefaultValueForgeNumberField
        from ..models.custom_field_context_default_value_forge_object_field import CustomFieldContextDefaultValueForgeObjectField
        from ..models.custom_field_context_default_value_forge_string_field import CustomFieldContextDefaultValueForgeStringField
        from ..models.custom_field_context_default_value_forge_user_field import CustomFieldContextDefaultValueForgeUserField
        from ..models.custom_field_context_default_value_labels import CustomFieldContextDefaultValueLabels
        from ..models.custom_field_context_default_value_multi_user_picker import CustomFieldContextDefaultValueMultiUserPicker
        from ..models.custom_field_context_default_value_multiple_group_picker import CustomFieldContextDefaultValueMultipleGroupPicker
        from ..models.custom_field_context_default_value_multiple_option import CustomFieldContextDefaultValueMultipleOption
        from ..models.custom_field_context_default_value_multiple_version_picker import CustomFieldContextDefaultValueMultipleVersionPicker
        from ..models.custom_field_context_default_value_project import CustomFieldContextDefaultValueProject
        from ..models.custom_field_context_default_value_read_only import CustomFieldContextDefaultValueReadOnly
        from ..models.custom_field_context_default_value_single_group_picker import CustomFieldContextDefaultValueSingleGroupPicker
        from ..models.custom_field_context_default_value_single_option import CustomFieldContextDefaultValueSingleOption
        from ..models.custom_field_context_default_value_single_version_picker import CustomFieldContextDefaultValueSingleVersionPicker
        from ..models.custom_field_context_default_value_text_area import CustomFieldContextDefaultValueTextArea
        from ..models.custom_field_context_default_value_text_field import CustomFieldContextDefaultValueTextField
        from ..models.custom_field_context_default_value_url import CustomFieldContextDefaultValueURL
        from ..models.custom_field_context_single_user_picker_defaults import CustomFieldContextSingleUserPickerDefaults
        d = dict(src_dict)
        _default_values = d.pop("defaultValues", UNSET)
        default_values: list[CustomFieldContextDefaultValueCascadingOption | CustomFieldContextDefaultValueDate | CustomFieldContextDefaultValueDateTime | CustomFieldContextDefaultValueFloat | CustomFieldContextDefaultValueForgeDateTimeField | CustomFieldContextDefaultValueForgeGroupField | CustomFieldContextDefaultValueForgeMultiGroupField | CustomFieldContextDefaultValueForgeMultiStringField | CustomFieldContextDefaultValueForgeMultiUserField | CustomFieldContextDefaultValueForgeNumberField | CustomFieldContextDefaultValueForgeObjectField | CustomFieldContextDefaultValueForgeStringField | CustomFieldContextDefaultValueForgeUserField | CustomFieldContextDefaultValueLabels | CustomFieldContextDefaultValueMultipleGroupPicker | CustomFieldContextDefaultValueMultipleOption | CustomFieldContextDefaultValueMultipleVersionPicker | CustomFieldContextDefaultValueMultiUserPicker | CustomFieldContextDefaultValueProject | CustomFieldContextDefaultValueReadOnly | CustomFieldContextDefaultValueSingleGroupPicker | CustomFieldContextDefaultValueSingleOption | CustomFieldContextDefaultValueSingleVersionPicker | CustomFieldContextDefaultValueTextArea | CustomFieldContextDefaultValueTextField | CustomFieldContextDefaultValueURL | CustomFieldContextSingleUserPickerDefaults] | Unset = UNSET
        if _default_values is not UNSET:
            default_values = []
            for default_values_item_data in _default_values:
                def _parse_default_values_item(data: object) -> CustomFieldContextDefaultValueCascadingOption | CustomFieldContextDefaultValueDate | CustomFieldContextDefaultValueDateTime | CustomFieldContextDefaultValueFloat | CustomFieldContextDefaultValueForgeDateTimeField | CustomFieldContextDefaultValueForgeGroupField | CustomFieldContextDefaultValueForgeMultiGroupField | CustomFieldContextDefaultValueForgeMultiStringField | CustomFieldContextDefaultValueForgeMultiUserField | CustomFieldContextDefaultValueForgeNumberField | CustomFieldContextDefaultValueForgeObjectField | CustomFieldContextDefaultValueForgeStringField | CustomFieldContextDefaultValueForgeUserField | CustomFieldContextDefaultValueLabels | CustomFieldContextDefaultValueMultipleGroupPicker | CustomFieldContextDefaultValueMultipleOption | CustomFieldContextDefaultValueMultipleVersionPicker | CustomFieldContextDefaultValueMultiUserPicker | CustomFieldContextDefaultValueProject | CustomFieldContextDefaultValueReadOnly | CustomFieldContextDefaultValueSingleGroupPicker | CustomFieldContextDefaultValueSingleOption | CustomFieldContextDefaultValueSingleVersionPicker | CustomFieldContextDefaultValueTextArea | CustomFieldContextDefaultValueTextField | CustomFieldContextDefaultValueURL | CustomFieldContextSingleUserPickerDefaults:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_0 = CustomFieldContextDefaultValueCascadingOption.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_1 = CustomFieldContextDefaultValueMultipleOption.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_2 = CustomFieldContextDefaultValueSingleOption.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_3 = CustomFieldContextSingleUserPickerDefaults.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_4 = CustomFieldContextDefaultValueMultiUserPicker.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_5 = CustomFieldContextDefaultValueSingleGroupPicker.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_6 = CustomFieldContextDefaultValueMultipleGroupPicker.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_7 = CustomFieldContextDefaultValueDate.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_7
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_8 = CustomFieldContextDefaultValueDateTime.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_8
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_9 = CustomFieldContextDefaultValueURL.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_9
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_10 = CustomFieldContextDefaultValueProject.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_10
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_11 = CustomFieldContextDefaultValueFloat.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_11
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_12 = CustomFieldContextDefaultValueLabels.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_12
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_13 = CustomFieldContextDefaultValueTextField.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_13
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_14 = CustomFieldContextDefaultValueTextArea.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_14
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_15 = CustomFieldContextDefaultValueReadOnly.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_15
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_16 = CustomFieldContextDefaultValueSingleVersionPicker.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_16
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_17 = CustomFieldContextDefaultValueMultipleVersionPicker.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_17
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_18 = CustomFieldContextDefaultValueForgeStringField.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_18
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_19 = CustomFieldContextDefaultValueForgeMultiStringField.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_19
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_20 = CustomFieldContextDefaultValueForgeObjectField.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_20
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_21 = CustomFieldContextDefaultValueForgeDateTimeField.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_21
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_22 = CustomFieldContextDefaultValueForgeGroupField.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_22
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_23 = CustomFieldContextDefaultValueForgeMultiGroupField.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_23
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_24 = CustomFieldContextDefaultValueForgeNumberField.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_24
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_field_context_default_value_type_25 = CustomFieldContextDefaultValueForgeUserField.from_dict(data)



                        return componentsschemas_custom_field_context_default_value_type_25
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_custom_field_context_default_value_type_26 = CustomFieldContextDefaultValueForgeMultiUserField.from_dict(data)



                    return componentsschemas_custom_field_context_default_value_type_26

                default_values_item = _parse_default_values_item(default_values_item_data)

                default_values.append(default_values_item)


        custom_field_context_default_value_update = cls(
            default_values=default_values,
        )

        return custom_field_context_default_value_update

