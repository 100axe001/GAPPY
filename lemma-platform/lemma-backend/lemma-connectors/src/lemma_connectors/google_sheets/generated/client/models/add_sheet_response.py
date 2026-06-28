from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.sheet_properties import SheetProperties





T = TypeVar("T", bound="AddSheetResponse")



@_attrs_define
class AddSheetResponse:
    """ The result of adding a sheet.

        Attributes:
            properties (SheetProperties | Unset): Properties of a sheet.
     """

    properties: SheetProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sheet_properties import SheetProperties
        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sheet_properties import SheetProperties
        d = dict(src_dict)
        _properties = d.pop("properties", UNSET)
        properties: SheetProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = SheetProperties.from_dict(_properties)




        add_sheet_response = cls(
            properties=properties,
        )


        add_sheet_response.additional_properties = d
        return add_sheet_response

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
