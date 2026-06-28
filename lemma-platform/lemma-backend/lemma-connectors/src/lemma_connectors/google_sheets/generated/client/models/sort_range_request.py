from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.grid_range import GridRange
  from ..models.sort_spec import SortSpec





T = TypeVar("T", bound="SortRangeRequest")



@_attrs_define
class SortRangeRequest:
    """ Sorts data in rows based on a sort order per column.

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
            sort_specs (list[SortSpec] | Unset): The sort order per column. Later specifications are used when values are
                equal in the earlier specifications.
     """

    range_: GridRange | Unset = UNSET
    sort_specs: list[SortSpec] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_range import GridRange
        from ..models.sort_spec import SortSpec
        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        sort_specs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sort_specs, Unset):
            sort_specs = []
            for sort_specs_item_data in self.sort_specs:
                sort_specs_item = sort_specs_item_data.to_dict()
                sort_specs.append(sort_specs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if range_ is not UNSET:
            field_dict["range"] = range_
        if sort_specs is not UNSET:
            field_dict["sortSpecs"] = sort_specs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_range import GridRange
        from ..models.sort_spec import SortSpec
        d = dict(src_dict)
        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        _sort_specs = d.pop("sortSpecs", UNSET)
        sort_specs: list[SortSpec] | Unset = UNSET
        if _sort_specs is not UNSET:
            sort_specs = []
            for sort_specs_item_data in _sort_specs:
                sort_specs_item = SortSpec.from_dict(sort_specs_item_data)



                sort_specs.append(sort_specs_item)


        sort_range_request = cls(
            range_=range_,
            sort_specs=sort_specs,
        )


        sort_range_request.additional_properties = d
        return sort_range_request

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
