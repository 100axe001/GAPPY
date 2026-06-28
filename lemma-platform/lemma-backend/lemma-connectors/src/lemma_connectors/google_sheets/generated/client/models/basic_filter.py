from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.basic_filter_criteria import BasicFilterCriteria
  from ..models.filter_spec import FilterSpec
  from ..models.grid_range import GridRange
  from ..models.sort_spec import SortSpec





T = TypeVar("T", bound="BasicFilter")



@_attrs_define
class BasicFilter:
    """ The default filter associated with a sheet.

        Attributes:
            criteria (BasicFilterCriteria | Unset): The criteria for showing/hiding values per column. The map's key is the
                column index, and the value is the criteria for that column. This field is deprecated in favor of filter_specs.
            filter_specs (list[FilterSpec] | Unset): The filter criteria per column. Both criteria and filter_specs are
                populated in responses. If both fields are specified in an update request, this field takes precedence.
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

    criteria: BasicFilterCriteria | Unset = UNSET
    filter_specs: list[FilterSpec] | Unset = UNSET
    range_: GridRange | Unset = UNSET
    sort_specs: list[SortSpec] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.basic_filter_criteria import BasicFilterCriteria
        from ..models.filter_spec import FilterSpec
        from ..models.grid_range import GridRange
        from ..models.sort_spec import SortSpec
        criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        filter_specs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_specs, Unset):
            filter_specs = []
            for filter_specs_item_data in self.filter_specs:
                filter_specs_item = filter_specs_item_data.to_dict()
                filter_specs.append(filter_specs_item)



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
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if filter_specs is not UNSET:
            field_dict["filterSpecs"] = filter_specs
        if range_ is not UNSET:
            field_dict["range"] = range_
        if sort_specs is not UNSET:
            field_dict["sortSpecs"] = sort_specs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_filter_criteria import BasicFilterCriteria
        from ..models.filter_spec import FilterSpec
        from ..models.grid_range import GridRange
        from ..models.sort_spec import SortSpec
        d = dict(src_dict)
        _criteria = d.pop("criteria", UNSET)
        criteria: BasicFilterCriteria | Unset
        if isinstance(_criteria,  Unset):
            criteria = UNSET
        else:
            criteria = BasicFilterCriteria.from_dict(_criteria)




        _filter_specs = d.pop("filterSpecs", UNSET)
        filter_specs: list[FilterSpec] | Unset = UNSET
        if _filter_specs is not UNSET:
            filter_specs = []
            for filter_specs_item_data in _filter_specs:
                filter_specs_item = FilterSpec.from_dict(filter_specs_item_data)



                filter_specs.append(filter_specs_item)


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


        basic_filter = cls(
            criteria=criteria,
            filter_specs=filter_specs,
            range_=range_,
            sort_specs=sort_specs,
        )


        basic_filter.additional_properties = d
        return basic_filter

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
