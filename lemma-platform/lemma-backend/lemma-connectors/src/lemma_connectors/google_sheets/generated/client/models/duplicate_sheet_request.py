from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DuplicateSheetRequest")



@_attrs_define
class DuplicateSheetRequest:
    """ Duplicates the contents of a sheet.

        Attributes:
            insert_sheet_index (int | Unset): The zero-based index where the new sheet should be inserted. The index of all
                sheets after this are incremented.
            new_sheet_id (int | Unset): If set, the ID of the new sheet. If not set, an ID is chosen. If set, the ID must
                not conflict with any existing sheet ID. If set, it must be non-negative.
            new_sheet_name (str | Unset): The name of the new sheet. If empty, a new name is chosen for you.
            source_sheet_id (int | Unset): The sheet to duplicate. If the source sheet is of DATA_SOURCE type, its backing
                DataSource is also duplicated and associated with the new copy of the sheet. No data execution is triggered, the
                grid data of this sheet is also copied over but only available after the batch request completes.
     """

    insert_sheet_index: int | Unset = UNSET
    new_sheet_id: int | Unset = UNSET
    new_sheet_name: str | Unset = UNSET
    source_sheet_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        insert_sheet_index = self.insert_sheet_index

        new_sheet_id = self.new_sheet_id

        new_sheet_name = self.new_sheet_name

        source_sheet_id = self.source_sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if insert_sheet_index is not UNSET:
            field_dict["insertSheetIndex"] = insert_sheet_index
        if new_sheet_id is not UNSET:
            field_dict["newSheetId"] = new_sheet_id
        if new_sheet_name is not UNSET:
            field_dict["newSheetName"] = new_sheet_name
        if source_sheet_id is not UNSET:
            field_dict["sourceSheetId"] = source_sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        insert_sheet_index = d.pop("insertSheetIndex", UNSET)

        new_sheet_id = d.pop("newSheetId", UNSET)

        new_sheet_name = d.pop("newSheetName", UNSET)

        source_sheet_id = d.pop("sourceSheetId", UNSET)

        duplicate_sheet_request = cls(
            insert_sheet_index=insert_sheet_index,
            new_sheet_id=new_sheet_id,
            new_sheet_name=new_sheet_name,
            source_sheet_id=source_sheet_id,
        )


        duplicate_sheet_request.additional_properties = d
        return duplicate_sheet_request

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
