from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.copy_paste_request_paste_orientation import CopyPasteRequestPasteOrientation
from ..models.copy_paste_request_paste_type import CopyPasteRequestPasteType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="CopyPasteRequest")



@_attrs_define
class CopyPasteRequest:
    """ Copies data from the source to the destination.

        Attributes:
            destination (GridRange | Unset): A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the
                start index is inclusive and the end index is exclusive -- [start_index, end_index). Missing indexes indicate
                the range is unbounded on that side. For example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 ==
                sheet_id: 123456, start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index: 1`
                `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2, end_row_index: 4, start_column_index: 0,
                end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index: 0, end_column_index: 2` `Sheet1!A5:B
                == sheet_id: 123456, start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 == sheet_id:
                123456` The start index must always be less than or equal to the end index. If the start index equals the end
                index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as
                `#REF!`.
            paste_orientation (CopyPasteRequestPasteOrientation | Unset): How that data should be oriented when pasting.
            paste_type (CopyPasteRequestPasteType | Unset): What kind of data to paste.
            source (GridRange | Unset): A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the
                start index is inclusive and the end index is exclusive -- [start_index, end_index). Missing indexes indicate
                the range is unbounded on that side. For example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 ==
                sheet_id: 123456, start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index: 1`
                `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2, end_row_index: 4, start_column_index: 0,
                end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index: 0, end_column_index: 2` `Sheet1!A5:B
                == sheet_id: 123456, start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 == sheet_id:
                123456` The start index must always be less than or equal to the end index. If the start index equals the end
                index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as
                `#REF!`.
     """

    destination: GridRange | Unset = UNSET
    paste_orientation: CopyPasteRequestPasteOrientation | Unset = UNSET
    paste_type: CopyPasteRequestPasteType | Unset = UNSET
    source: GridRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_range import GridRange
        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        paste_orientation: str | Unset = UNSET
        if not isinstance(self.paste_orientation, Unset):
            paste_orientation = self.paste_orientation.value


        paste_type: str | Unset = UNSET
        if not isinstance(self.paste_type, Unset):
            paste_type = self.paste_type.value


        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if destination is not UNSET:
            field_dict["destination"] = destination
        if paste_orientation is not UNSET:
            field_dict["pasteOrientation"] = paste_orientation
        if paste_type is not UNSET:
            field_dict["pasteType"] = paste_type
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        _destination = d.pop("destination", UNSET)
        destination: GridRange | Unset
        if isinstance(_destination,  Unset):
            destination = UNSET
        else:
            destination = GridRange.from_dict(_destination)




        _paste_orientation = d.pop("pasteOrientation", UNSET)
        paste_orientation: CopyPasteRequestPasteOrientation | Unset
        if isinstance(_paste_orientation,  Unset):
            paste_orientation = UNSET
        else:
            paste_orientation = CopyPasteRequestPasteOrientation(_paste_orientation)




        _paste_type = d.pop("pasteType", UNSET)
        paste_type: CopyPasteRequestPasteType | Unset
        if isinstance(_paste_type,  Unset):
            paste_type = UNSET
        else:
            paste_type = CopyPasteRequestPasteType(_paste_type)




        _source = d.pop("source", UNSET)
        source: GridRange | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = GridRange.from_dict(_source)




        copy_paste_request = cls(
            destination=destination,
            paste_orientation=paste_orientation,
            paste_type=paste_type,
            source=source,
        )


        copy_paste_request.additional_properties = d
        return copy_paste_request

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
