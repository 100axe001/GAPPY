from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.field_configuration_item import FieldConfigurationItem





T = TypeVar("T", bound="FieldConfigurationItemsDetails")



@_attrs_define
class FieldConfigurationItemsDetails:
    """ Details of field configuration items.

        Attributes:
            field_configuration_items (list[FieldConfigurationItem]): Details of fields in a field configuration.
     """

    field_configuration_items: list[FieldConfigurationItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_configuration_item import FieldConfigurationItem
        field_configuration_items = []
        for field_configuration_items_item_data in self.field_configuration_items:
            field_configuration_items_item = field_configuration_items_item_data.to_dict()
            field_configuration_items.append(field_configuration_items_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fieldConfigurationItems": field_configuration_items,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_configuration_item import FieldConfigurationItem
        d = dict(src_dict)
        field_configuration_items = []
        _field_configuration_items = d.pop("fieldConfigurationItems")
        for field_configuration_items_item_data in (_field_configuration_items):
            field_configuration_items_item = FieldConfigurationItem.from_dict(field_configuration_items_item_data)



            field_configuration_items.append(field_configuration_items_item)


        field_configuration_items_details = cls(
            field_configuration_items=field_configuration_items,
        )

        return field_configuration_items_details

