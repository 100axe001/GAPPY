from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.border import Border
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="UpdateBordersRequest")



@_attrs_define
class UpdateBordersRequest:
    """ Updates the borders of a range. If a field is not set in the request, that means the border remains as-is. For
    example, with two subsequent UpdateBordersRequest: 1. range: A1:A5 `{ top: RED, bottom: WHITE }` 2. range: A1:A5 `{
    left: BLUE }` That would result in A1:A5 having a borders of `{ top: RED, bottom: WHITE, left: BLUE }`. If you want
    to clear a border, explicitly set the style to NONE.

        Attributes:
            bottom (Border | Unset): A border along a cell.
            inner_horizontal (Border | Unset): A border along a cell.
            inner_vertical (Border | Unset): A border along a cell.
            left (Border | Unset): A border along a cell.
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
            right (Border | Unset): A border along a cell.
            top (Border | Unset): A border along a cell.
     """

    bottom: Border | Unset = UNSET
    inner_horizontal: Border | Unset = UNSET
    inner_vertical: Border | Unset = UNSET
    left: Border | Unset = UNSET
    range_: GridRange | Unset = UNSET
    right: Border | Unset = UNSET
    top: Border | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.border import Border
        from ..models.grid_range import GridRange
        bottom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bottom, Unset):
            bottom = self.bottom.to_dict()

        inner_horizontal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inner_horizontal, Unset):
            inner_horizontal = self.inner_horizontal.to_dict()

        inner_vertical: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inner_vertical, Unset):
            inner_vertical = self.inner_vertical.to_dict()

        left: dict[str, Any] | Unset = UNSET
        if not isinstance(self.left, Unset):
            left = self.left.to_dict()

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        right: dict[str, Any] | Unset = UNSET
        if not isinstance(self.right, Unset):
            right = self.right.to_dict()

        top: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top, Unset):
            top = self.top.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bottom is not UNSET:
            field_dict["bottom"] = bottom
        if inner_horizontal is not UNSET:
            field_dict["innerHorizontal"] = inner_horizontal
        if inner_vertical is not UNSET:
            field_dict["innerVertical"] = inner_vertical
        if left is not UNSET:
            field_dict["left"] = left
        if range_ is not UNSET:
            field_dict["range"] = range_
        if right is not UNSET:
            field_dict["right"] = right
        if top is not UNSET:
            field_dict["top"] = top

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.border import Border
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        _bottom = d.pop("bottom", UNSET)
        bottom: Border | Unset
        if isinstance(_bottom,  Unset):
            bottom = UNSET
        else:
            bottom = Border.from_dict(_bottom)




        _inner_horizontal = d.pop("innerHorizontal", UNSET)
        inner_horizontal: Border | Unset
        if isinstance(_inner_horizontal,  Unset):
            inner_horizontal = UNSET
        else:
            inner_horizontal = Border.from_dict(_inner_horizontal)




        _inner_vertical = d.pop("innerVertical", UNSET)
        inner_vertical: Border | Unset
        if isinstance(_inner_vertical,  Unset):
            inner_vertical = UNSET
        else:
            inner_vertical = Border.from_dict(_inner_vertical)




        _left = d.pop("left", UNSET)
        left: Border | Unset
        if isinstance(_left,  Unset):
            left = UNSET
        else:
            left = Border.from_dict(_left)




        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        _right = d.pop("right", UNSET)
        right: Border | Unset
        if isinstance(_right,  Unset):
            right = UNSET
        else:
            right = Border.from_dict(_right)




        _top = d.pop("top", UNSET)
        top: Border | Unset
        if isinstance(_top,  Unset):
            top = UNSET
        else:
            top = Border.from_dict(_top)




        update_borders_request = cls(
            bottom=bottom,
            inner_horizontal=inner_horizontal,
            inner_vertical=inner_vertical,
            left=left,
            range_=range_,
            right=right,
            top=top,
        )


        update_borders_request.additional_properties = d
        return update_borders_request

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
