from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoopNodeConfig")


@_attrs_define
class LoopNodeConfig:
    """Configuration for Loop node.

    Attributes:
        child_node_id (str): Id of the first node of the loop body executed per item.
        items_path (str): JMESPath to an array in the run context to iterate over.
        item_var_name (str | Unset): Alias for the current item inside the loop body, available as
            `loop.<item_var_name>` (the item is always available as `loop.item`). Default: 'item'.
    """

    child_node_id: str
    items_path: str
    item_var_name: str | Unset = "item"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        child_node_id = self.child_node_id

        items_path = self.items_path

        item_var_name = self.item_var_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "child_node_id": child_node_id,
                "items_path": items_path,
            }
        )
        if item_var_name is not UNSET:
            field_dict["item_var_name"] = item_var_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        child_node_id = d.pop("child_node_id")

        items_path = d.pop("items_path")

        item_var_name = d.pop("item_var_name", UNSET)

        loop_node_config = cls(
            child_node_id=child_node_id,
            items_path=items_path,
            item_var_name=item_var_name,
        )

        loop_node_config.additional_properties = d
        return loop_node_config

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
