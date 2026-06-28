from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.global_scope_bean_attributes_item import GlobalScopeBeanAttributesItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GlobalScopeBean")



@_attrs_define
class GlobalScopeBean:
    """ 
        Attributes:
            attributes (list[GlobalScopeBeanAttributesItem] | Unset): Defines the behavior of the option in the global
                context.If notSelectable is set, the option cannot be set as the field's value. This is useful for archiving an
                option that has previously been selected but shouldn't be used anymore.If defaultValue is set, the option is
                selected by default.
     """

    attributes: list[GlobalScopeBeanAttributesItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        attributes: list[str] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.value
                attributes.append(attributes_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: list[GlobalScopeBeanAttributesItem] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = GlobalScopeBeanAttributesItem(attributes_item_data)



                attributes.append(attributes_item)


        global_scope_bean = cls(
            attributes=attributes,
        )

        return global_scope_bean

