from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AssociatedItemBean")



@_attrs_define
class AssociatedItemBean:
    """ Details of an item associated with the changed record.

        Attributes:
            id (str | Unset): The ID of the associated record.
            name (str | Unset): The name of the associated record.
            parent_id (str | Unset): The ID of the associated parent record.
            parent_name (str | Unset): The name of the associated parent record.
            type_name (str | Unset): The type of the associated record.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    parent_name: str | Unset = UNSET
    type_name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        parent_id = self.parent_id

        parent_name = self.parent_name

        type_name = self.type_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_name is not UNSET:
            field_dict["parentName"] = parent_name
        if type_name is not UNSET:
            field_dict["typeName"] = type_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        parent_id = d.pop("parentId", UNSET)

        parent_name = d.pop("parentName", UNSET)

        type_name = d.pop("typeName", UNSET)

        associated_item_bean = cls(
            id=id,
            name=name,
            parent_id=parent_id,
            parent_name=parent_name,
            type_name=type_name,
        )

        return associated_item_bean

