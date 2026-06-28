from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_columns_request_delimiter_type import TextToColumnsRequestDelimiterType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="TextToColumnsRequest")



@_attrs_define
class TextToColumnsRequest:
    """ Splits a column of text into multiple columns, based on a delimiter in each cell.

        Attributes:
            delimiter (str | Unset): The delimiter to use. Used only if delimiterType is CUSTOM.
            delimiter_type (TextToColumnsRequestDelimiterType | Unset): The delimiter type to use.
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

    delimiter: str | Unset = UNSET
    delimiter_type: TextToColumnsRequestDelimiterType | Unset = UNSET
    source: GridRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_range import GridRange
        delimiter = self.delimiter

        delimiter_type: str | Unset = UNSET
        if not isinstance(self.delimiter_type, Unset):
            delimiter_type = self.delimiter_type.value


        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if delimiter is not UNSET:
            field_dict["delimiter"] = delimiter
        if delimiter_type is not UNSET:
            field_dict["delimiterType"] = delimiter_type
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        delimiter = d.pop("delimiter", UNSET)

        _delimiter_type = d.pop("delimiterType", UNSET)
        delimiter_type: TextToColumnsRequestDelimiterType | Unset
        if isinstance(_delimiter_type,  Unset):
            delimiter_type = UNSET
        else:
            delimiter_type = TextToColumnsRequestDelimiterType(_delimiter_type)




        _source = d.pop("source", UNSET)
        source: GridRange | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = GridRange.from_dict(_source)




        text_to_columns_request = cls(
            delimiter=delimiter,
            delimiter_type=delimiter_type,
            source=source,
        )


        text_to_columns_request.additional_properties = d
        return text_to_columns_request

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
