from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteSheetRequest")



@_attrs_define
class DeleteSheetRequest:
    """ Deletes the requested sheet.

        Attributes:
            sheet_id (int | Unset): The ID of the sheet to delete. If the sheet is of DATA_SOURCE type, the associated
                DataSource is also deleted.
     """

    sheet_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sheet_id = self.sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sheet_id = d.pop("sheetId", UNSET)

        delete_sheet_request = cls(
            sheet_id=sheet_id,
        )


        delete_sheet_request.additional_properties = d
        return delete_sheet_request

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
