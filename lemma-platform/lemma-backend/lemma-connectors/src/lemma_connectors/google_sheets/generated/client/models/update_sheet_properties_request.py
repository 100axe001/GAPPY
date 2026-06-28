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





T = TypeVar("T", bound="UpdateSheetPropertiesRequest")



@_attrs_define
class UpdateSheetPropertiesRequest:
    """ Updates properties of the sheet with the specified sheetId.

        Attributes:
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `properties` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every
                field.
            properties (SheetProperties | Unset): Properties of a sheet.
     """

    fields: str | Unset = UNSET
    properties: SheetProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sheet_properties import SheetProperties
        fields = self.fields

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sheet_properties import SheetProperties
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: SheetProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = SheetProperties.from_dict(_properties)




        update_sheet_properties_request = cls(
            fields=fields,
            properties=properties,
        )


        update_sheet_properties_request.additional_properties = d
        return update_sheet_properties_request

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
