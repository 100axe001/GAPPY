from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.extended_value import ExtendedValue





T = TypeVar("T", bound="ManualRuleGroup")



@_attrs_define
class ManualRuleGroup:
    """ A group name and a list of items from the source data that should be placed in the group with this name.

        Attributes:
            group_name (ExtendedValue | Unset): The kinds of value that a cell in a spreadsheet can have.
            items (list[ExtendedValue] | Unset): The items in the source data that should be placed into this group. Each
                item may be a string, number, or boolean. Items may appear in at most one group within a given ManualRule. Items
                that do not appear in any group will appear on their own.
     """

    group_name: ExtendedValue | Unset = UNSET
    items: list[ExtendedValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.extended_value import ExtendedValue
        group_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_name, Unset):
            group_name = self.group_name.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extended_value import ExtendedValue
        d = dict(src_dict)
        _group_name = d.pop("groupName", UNSET)
        group_name: ExtendedValue | Unset
        if isinstance(_group_name,  Unset):
            group_name = UNSET
        else:
            group_name = ExtendedValue.from_dict(_group_name)




        _items = d.pop("items", UNSET)
        items: list[ExtendedValue] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ExtendedValue.from_dict(items_item_data)



                items.append(items_item)


        manual_rule_group = cls(
            group_name=group_name,
            items=items,
        )


        manual_rule_group.additional_properties = d
        return manual_rule_group

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
