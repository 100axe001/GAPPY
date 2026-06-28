from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pivot_group_sort_order import PivotGroupSortOrder
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_column_reference import DataSourceColumnReference
  from ..models.pivot_group_limit import PivotGroupLimit
  from ..models.pivot_group_rule import PivotGroupRule
  from ..models.pivot_group_sort_value_bucket import PivotGroupSortValueBucket
  from ..models.pivot_group_value_metadata import PivotGroupValueMetadata





T = TypeVar("T", bound="PivotGroup")



@_attrs_define
class PivotGroup:
    """ A single grouping (either row or column) in a pivot table.

        Attributes:
            data_source_column_reference (DataSourceColumnReference | Unset): An unique identifier that references a data
                source column.
            group_limit (PivotGroupLimit | Unset): The count limit on rows or columns in the pivot group.
            group_rule (PivotGroupRule | Unset): An optional setting on a PivotGroup that defines buckets for the values in
                the source data column rather than breaking out each individual value. Only one PivotGroup with a group rule may
                be added for each column in the source data, though on any given column you may add both a PivotGroup that has a
                rule and a PivotGroup that does not.
            label (str | Unset): The labels to use for the row/column groups which can be customized. For example, in the
                following pivot table, the row label is `Region` (which could be renamed to `State`) and the column label is
                `Product` (which could be renamed `Item`). Pivot tables created before December 2017 do not have header labels.
                If you'd like to add header labels to an existing pivot table, please delete the existing pivot table and then
                create a new pivot table with same parameters. +--------------+---------+-------+ | SUM of Units | Product | | |
                Region | Pen | Paper | +--------------+---------+-------+ | New York | 345 | 98 | | Oregon | 234 | 123 | |
                Tennessee | 531 | 415 | +--------------+---------+-------+ | Grand Total | 1110 | 636 |
                +--------------+---------+-------+
            repeat_headings (bool | Unset): True if the headings in this pivot group should be repeated. This is only valid
                for row groupings and is ignored by columns. By default, we minimize repetition of headings by not showing
                higher level headings where they are the same. For example, even though the third row below corresponds to "Q1
                Mar", "Q1" is not shown because it is redundant with previous rows. Setting repeat_headings to true would cause
                "Q1" to be repeated for "Feb" and "Mar". +--------------+ | Q1 | Jan | | | Feb | | | Mar | +--------+-----+ | Q1
                Total | +--------------+
            show_totals (bool | Unset): True if the pivot table should include the totals for this grouping.
            sort_order (PivotGroupSortOrder | Unset): The order the values in this group should be sorted.
            source_column_offset (int | Unset): The column offset of the source range that this grouping is based on. For
                example, if the source was `C10:E15`, a `sourceColumnOffset` of `0` means this group refers to column `C`,
                whereas the offset `1` would refer to column `D`.
            value_bucket (PivotGroupSortValueBucket | Unset): Information about which values in a pivot group should be used
                for sorting.
            value_metadata (list[PivotGroupValueMetadata] | Unset): Metadata about values in the grouping.
     """

    data_source_column_reference: DataSourceColumnReference | Unset = UNSET
    group_limit: PivotGroupLimit | Unset = UNSET
    group_rule: PivotGroupRule | Unset = UNSET
    label: str | Unset = UNSET
    repeat_headings: bool | Unset = UNSET
    show_totals: bool | Unset = UNSET
    sort_order: PivotGroupSortOrder | Unset = UNSET
    source_column_offset: int | Unset = UNSET
    value_bucket: PivotGroupSortValueBucket | Unset = UNSET
    value_metadata: list[PivotGroupValueMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.pivot_group_limit import PivotGroupLimit
        from ..models.pivot_group_rule import PivotGroupRule
        from ..models.pivot_group_sort_value_bucket import PivotGroupSortValueBucket
        from ..models.pivot_group_value_metadata import PivotGroupValueMetadata
        data_source_column_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_column_reference, Unset):
            data_source_column_reference = self.data_source_column_reference.to_dict()

        group_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_limit, Unset):
            group_limit = self.group_limit.to_dict()

        group_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_rule, Unset):
            group_rule = self.group_rule.to_dict()

        label = self.label

        repeat_headings = self.repeat_headings

        show_totals = self.show_totals

        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value


        source_column_offset = self.source_column_offset

        value_bucket: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_bucket, Unset):
            value_bucket = self.value_bucket.to_dict()

        value_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value_metadata, Unset):
            value_metadata = []
            for value_metadata_item_data in self.value_metadata:
                value_metadata_item = value_metadata_item_data.to_dict()
                value_metadata.append(value_metadata_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_source_column_reference is not UNSET:
            field_dict["dataSourceColumnReference"] = data_source_column_reference
        if group_limit is not UNSET:
            field_dict["groupLimit"] = group_limit
        if group_rule is not UNSET:
            field_dict["groupRule"] = group_rule
        if label is not UNSET:
            field_dict["label"] = label
        if repeat_headings is not UNSET:
            field_dict["repeatHeadings"] = repeat_headings
        if show_totals is not UNSET:
            field_dict["showTotals"] = show_totals
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if source_column_offset is not UNSET:
            field_dict["sourceColumnOffset"] = source_column_offset
        if value_bucket is not UNSET:
            field_dict["valueBucket"] = value_bucket
        if value_metadata is not UNSET:
            field_dict["valueMetadata"] = value_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.pivot_group_limit import PivotGroupLimit
        from ..models.pivot_group_rule import PivotGroupRule
        from ..models.pivot_group_sort_value_bucket import PivotGroupSortValueBucket
        from ..models.pivot_group_value_metadata import PivotGroupValueMetadata
        d = dict(src_dict)
        _data_source_column_reference = d.pop("dataSourceColumnReference", UNSET)
        data_source_column_reference: DataSourceColumnReference | Unset
        if isinstance(_data_source_column_reference,  Unset):
            data_source_column_reference = UNSET
        else:
            data_source_column_reference = DataSourceColumnReference.from_dict(_data_source_column_reference)




        _group_limit = d.pop("groupLimit", UNSET)
        group_limit: PivotGroupLimit | Unset
        if isinstance(_group_limit,  Unset):
            group_limit = UNSET
        else:
            group_limit = PivotGroupLimit.from_dict(_group_limit)




        _group_rule = d.pop("groupRule", UNSET)
        group_rule: PivotGroupRule | Unset
        if isinstance(_group_rule,  Unset):
            group_rule = UNSET
        else:
            group_rule = PivotGroupRule.from_dict(_group_rule)




        label = d.pop("label", UNSET)

        repeat_headings = d.pop("repeatHeadings", UNSET)

        show_totals = d.pop("showTotals", UNSET)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: PivotGroupSortOrder | Unset
        if isinstance(_sort_order,  Unset):
            sort_order = UNSET
        else:
            sort_order = PivotGroupSortOrder(_sort_order)




        source_column_offset = d.pop("sourceColumnOffset", UNSET)

        _value_bucket = d.pop("valueBucket", UNSET)
        value_bucket: PivotGroupSortValueBucket | Unset
        if isinstance(_value_bucket,  Unset):
            value_bucket = UNSET
        else:
            value_bucket = PivotGroupSortValueBucket.from_dict(_value_bucket)




        _value_metadata = d.pop("valueMetadata", UNSET)
        value_metadata: list[PivotGroupValueMetadata] | Unset = UNSET
        if _value_metadata is not UNSET:
            value_metadata = []
            for value_metadata_item_data in _value_metadata:
                value_metadata_item = PivotGroupValueMetadata.from_dict(value_metadata_item_data)



                value_metadata.append(value_metadata_item)


        pivot_group = cls(
            data_source_column_reference=data_source_column_reference,
            group_limit=group_limit,
            group_rule=group_rule,
            label=label,
            repeat_headings=repeat_headings,
            show_totals=show_totals,
            sort_order=sort_order,
            source_column_offset=source_column_offset,
            value_bucket=value_bucket,
            value_metadata=value_metadata,
        )


        pivot_group.additional_properties = d
        return pivot_group

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
