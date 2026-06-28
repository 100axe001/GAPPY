from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.delete_range_request_shift_dimension import DeleteRangeRequestShiftDimension
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="DeleteRangeRequest")



@_attrs_define
class DeleteRangeRequest:
    """ Deletes a range of cells, shifting other cells into the deleted area.

        Attributes:
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
            shift_dimension (DeleteRangeRequestShiftDimension | Unset): The dimension from which deleted cells will be
                replaced with. If ROWS, existing cells will be shifted upward to replace the deleted cells. If COLUMNS, existing
                cells will be shifted left to replace the deleted cells.
     """

    range_: GridRange | Unset = UNSET
    shift_dimension: DeleteRangeRequestShiftDimension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_range import GridRange
        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        shift_dimension: str | Unset = UNSET
        if not isinstance(self.shift_dimension, Unset):
            shift_dimension = self.shift_dimension.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if range_ is not UNSET:
            field_dict["range"] = range_
        if shift_dimension is not UNSET:
            field_dict["shiftDimension"] = shift_dimension

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        _shift_dimension = d.pop("shiftDimension", UNSET)
        shift_dimension: DeleteRangeRequestShiftDimension | Unset
        if isinstance(_shift_dimension,  Unset):
            shift_dimension = UNSET
        else:
            shift_dimension = DeleteRangeRequestShiftDimension(_shift_dimension)




        delete_range_request = cls(
            range_=range_,
            shift_dimension=shift_dimension,
        )


        delete_range_request.additional_properties = d
        return delete_range_request

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
