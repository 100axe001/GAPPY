from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.banding_properties import BandingProperties
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="BandedRange")



@_attrs_define
class BandedRange:
    """ A banded (alternating colors) range in a sheet.

        Attributes:
            banded_range_id (int | Unset): The id of the banded range.
            column_properties (BandingProperties | Unset): Properties referring a single dimension (either row or column).
                If both BandedRange.row_properties and BandedRange.column_properties are set, the fill colors are applied to
                cells according to the following rules: * header_color and footer_color take priority over band colors. *
                first_band_color takes priority over second_band_color. * row_properties takes priority over column_properties.
                For example, the first row color takes priority over the first column color, but the first column color takes
                priority over the second row color. Similarly, the row header takes priority over the column header in the top
                left cell, but the column header takes priority over the first row color if the row header is not set.
            range_ (GridRange | Unset): A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the
                start index is inclusive and the end index is exclusive -- [start_index, end_index). Missing indexes indicate
                the range is unbounded on that side. For example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 ==
                sheet_id: 123456, start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index: 1`
                `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2, end_row_index: 4, start_column_index: 0,
                end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index: 0, end_column_index: 2` `Sheet1!A5:B
                == sheet_id: 123456, start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 == sheet_id:
                123456` The start index must always be less than or equal to the end index. If the start index equals the end
                index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as
                `#REF!`.
            row_properties (BandingProperties | Unset): Properties referring a single dimension (either row or column). If
                both BandedRange.row_properties and BandedRange.column_properties are set, the fill colors are applied to cells
                according to the following rules: * header_color and footer_color take priority over band colors. *
                first_band_color takes priority over second_band_color. * row_properties takes priority over column_properties.
                For example, the first row color takes priority over the first column color, but the first column color takes
                priority over the second row color. Similarly, the row header takes priority over the column header in the top
                left cell, but the column header takes priority over the first row color if the row header is not set.
     """

    banded_range_id: int | Unset = UNSET
    column_properties: BandingProperties | Unset = UNSET
    range_: GridRange | Unset = UNSET
    row_properties: BandingProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.banding_properties import BandingProperties
        from ..models.grid_range import GridRange
        banded_range_id = self.banded_range_id

        column_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.column_properties, Unset):
            column_properties = self.column_properties.to_dict()

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        row_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.row_properties, Unset):
            row_properties = self.row_properties.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if banded_range_id is not UNSET:
            field_dict["bandedRangeId"] = banded_range_id
        if column_properties is not UNSET:
            field_dict["columnProperties"] = column_properties
        if range_ is not UNSET:
            field_dict["range"] = range_
        if row_properties is not UNSET:
            field_dict["rowProperties"] = row_properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.banding_properties import BandingProperties
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        banded_range_id = d.pop("bandedRangeId", UNSET)

        _column_properties = d.pop("columnProperties", UNSET)
        column_properties: BandingProperties | Unset
        if isinstance(_column_properties,  Unset):
            column_properties = UNSET
        else:
            column_properties = BandingProperties.from_dict(_column_properties)




        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        _row_properties = d.pop("rowProperties", UNSET)
        row_properties: BandingProperties | Unset
        if isinstance(_row_properties,  Unset):
            row_properties = UNSET
        else:
            row_properties = BandingProperties.from_dict(_row_properties)




        banded_range = cls(
            banded_range_id=banded_range_id,
            column_properties=column_properties,
            range_=range_,
            row_properties=row_properties,
        )


        banded_range.additional_properties = d
        return banded_range

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
