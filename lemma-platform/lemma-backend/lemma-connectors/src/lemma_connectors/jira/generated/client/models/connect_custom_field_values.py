from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.connect_custom_field_value import ConnectCustomFieldValue





T = TypeVar("T", bound="ConnectCustomFieldValues")



@_attrs_define
class ConnectCustomFieldValues:
    """ Details of updates for a custom field.

        Attributes:
            update_value_list (list[ConnectCustomFieldValue] | Unset): The list of custom field update details.
     """

    update_value_list: list[ConnectCustomFieldValue] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.connect_custom_field_value import ConnectCustomFieldValue
        update_value_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.update_value_list, Unset):
            update_value_list = []
            for update_value_list_item_data in self.update_value_list:
                update_value_list_item = update_value_list_item_data.to_dict()
                update_value_list.append(update_value_list_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if update_value_list is not UNSET:
            field_dict["updateValueList"] = update_value_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connect_custom_field_value import ConnectCustomFieldValue
        d = dict(src_dict)
        _update_value_list = d.pop("updateValueList", UNSET)
        update_value_list: list[ConnectCustomFieldValue] | Unset = UNSET
        if _update_value_list is not UNSET:
            update_value_list = []
            for update_value_list_item_data in _update_value_list:
                update_value_list_item = ConnectCustomFieldValue.from_dict(update_value_list_item_data)



                update_value_list.append(update_value_list_item)


        connect_custom_field_values = cls(
            update_value_list=update_value_list,
        )

        return connect_custom_field_values

