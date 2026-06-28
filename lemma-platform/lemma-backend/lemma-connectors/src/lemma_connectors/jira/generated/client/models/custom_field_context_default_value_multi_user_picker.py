from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="CustomFieldContextDefaultValueMultiUserPicker")



@_attrs_define
class CustomFieldContextDefaultValueMultiUserPicker:
    """ The default value for a User Picker (multiple) custom field.

        Attributes:
            account_ids (list[str]): The IDs of the default users.
            context_id (str): The ID of the context.
            type_ (str):
     """

    account_ids: list[str]
    context_id: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_ids = self.account_ids



        context_id = self.context_id

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "accountIds": account_ids,
            "contextId": context_id,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_ids = cast(list[str], d.pop("accountIds"))


        context_id = d.pop("contextId")

        type_ = d.pop("type")

        custom_field_context_default_value_multi_user_picker = cls(
            account_ids=account_ids,
            context_id=context_id,
            type_=type_,
        )


        custom_field_context_default_value_multi_user_picker.additional_properties = d
        return custom_field_context_default_value_multi_user_picker

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
