from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="CustomFieldContextDefaultValueForgeMultiGroupField")



@_attrs_define
class CustomFieldContextDefaultValueForgeMultiGroupField:
    """ The default value for a Forge collection of groups custom field.

        Attributes:
            context_id (str): The ID of the context.
            group_ids (list[str]): The IDs of the default groups.
            type_ (str):
     """

    context_id: str
    group_ids: list[str]
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        group_ids = self.group_ids



        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "contextId": context_id,
            "groupIds": group_ids,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_id = d.pop("contextId")

        group_ids = cast(list[str], d.pop("groupIds"))


        type_ = d.pop("type")

        custom_field_context_default_value_forge_multi_group_field = cls(
            context_id=context_id,
            group_ids=group_ids,
            type_=type_,
        )


        custom_field_context_default_value_forge_multi_group_field.additional_properties = d
        return custom_field_context_default_value_forge_multi_group_field

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
