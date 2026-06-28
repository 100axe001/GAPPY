from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pivot_table_value_layout import PivotTableValueLayout
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_execution_status import DataExecutionStatus
  from ..models.grid_range import GridRange
  from ..models.pivot_filter_spec import PivotFilterSpec
  from ..models.pivot_group import PivotGroup
  from ..models.pivot_table_criteria import PivotTableCriteria
  from ..models.pivot_value import PivotValue





T = TypeVar("T", bound="PivotTable")



@_attrs_define
class PivotTable:
    """ A pivot table.

        Attributes:
            columns (list[PivotGroup] | Unset): Each column grouping in the pivot table.
            criteria (PivotTableCriteria | Unset): An optional mapping of filters per source column offset. The filters are
                applied before aggregating data into the pivot table. The map's key is the column offset of the source range
                that you want to filter, and the value is the criteria for that column. For example, if the source was
                `C10:E15`, a key of `0` will have the filter for column `C`, whereas the key `1` is for column `D`. This field
                is deprecated in favor of filter_specs.
            data_execution_status (DataExecutionStatus | Unset): The data execution status. A data execution is created to
                sync a data source object with the latest data from a DataSource. It is usually scheduled to run at background,
                you can check its state to tell if an execution completes There are several scenarios where a data execution is
                triggered to run: * Adding a data source creates an associated data source sheet as well as a data execution to
                sync the data from the data source to the sheet. * Updating a data source creates a data execution to refresh
                the associated data source sheet similarly. * You can send refresh request to explicitly refresh one or multiple
                data source objects.
            data_source_id (str | Unset): The ID of the data source the pivot table is reading data from.
            filter_specs (list[PivotFilterSpec] | Unset): The filters applied to the source columns before aggregating data
                for the pivot table. Both criteria and filter_specs are populated in responses. If both fields are specified in
                an update request, this field takes precedence.
            rows (list[PivotGroup] | Unset): Each row grouping in the pivot table.
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
            value_layout (PivotTableValueLayout | Unset): Whether values should be listed horizontally (as columns) or
                vertically (as rows).
            values (list[PivotValue] | Unset): A list of values to include in the pivot table.
     """

    columns: list[PivotGroup] | Unset = UNSET
    criteria: PivotTableCriteria | Unset = UNSET
    data_execution_status: DataExecutionStatus | Unset = UNSET
    data_source_id: str | Unset = UNSET
    filter_specs: list[PivotFilterSpec] | Unset = UNSET
    rows: list[PivotGroup] | Unset = UNSET
    source: GridRange | Unset = UNSET
    value_layout: PivotTableValueLayout | Unset = UNSET
    values: list[PivotValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_execution_status import DataExecutionStatus
        from ..models.grid_range import GridRange
        from ..models.pivot_filter_spec import PivotFilterSpec
        from ..models.pivot_group import PivotGroup
        from ..models.pivot_table_criteria import PivotTableCriteria
        from ..models.pivot_value import PivotValue
        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)



        criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        data_execution_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_execution_status, Unset):
            data_execution_status = self.data_execution_status.to_dict()

        data_source_id = self.data_source_id

        filter_specs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_specs, Unset):
            filter_specs = []
            for filter_specs_item_data in self.filter_specs:
                filter_specs_item = filter_specs_item_data.to_dict()
                filter_specs.append(filter_specs_item)



        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)



        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        value_layout: str | Unset = UNSET
        if not isinstance(self.value_layout, Unset):
            value_layout = self.value_layout.value


        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if columns is not UNSET:
            field_dict["columns"] = columns
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if data_execution_status is not UNSET:
            field_dict["dataExecutionStatus"] = data_execution_status
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if filter_specs is not UNSET:
            field_dict["filterSpecs"] = filter_specs
        if rows is not UNSET:
            field_dict["rows"] = rows
        if source is not UNSET:
            field_dict["source"] = source
        if value_layout is not UNSET:
            field_dict["valueLayout"] = value_layout
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_execution_status import DataExecutionStatus
        from ..models.grid_range import GridRange
        from ..models.pivot_filter_spec import PivotFilterSpec
        from ..models.pivot_group import PivotGroup
        from ..models.pivot_table_criteria import PivotTableCriteria
        from ..models.pivot_value import PivotValue
        d = dict(src_dict)
        _columns = d.pop("columns", UNSET)
        columns: list[PivotGroup] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = PivotGroup.from_dict(columns_item_data)



                columns.append(columns_item)


        _criteria = d.pop("criteria", UNSET)
        criteria: PivotTableCriteria | Unset
        if isinstance(_criteria,  Unset):
            criteria = UNSET
        else:
            criteria = PivotTableCriteria.from_dict(_criteria)




        _data_execution_status = d.pop("dataExecutionStatus", UNSET)
        data_execution_status: DataExecutionStatus | Unset
        if isinstance(_data_execution_status,  Unset):
            data_execution_status = UNSET
        else:
            data_execution_status = DataExecutionStatus.from_dict(_data_execution_status)




        data_source_id = d.pop("dataSourceId", UNSET)

        _filter_specs = d.pop("filterSpecs", UNSET)
        filter_specs: list[PivotFilterSpec] | Unset = UNSET
        if _filter_specs is not UNSET:
            filter_specs = []
            for filter_specs_item_data in _filter_specs:
                filter_specs_item = PivotFilterSpec.from_dict(filter_specs_item_data)



                filter_specs.append(filter_specs_item)


        _rows = d.pop("rows", UNSET)
        rows: list[PivotGroup] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = PivotGroup.from_dict(rows_item_data)



                rows.append(rows_item)


        _source = d.pop("source", UNSET)
        source: GridRange | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = GridRange.from_dict(_source)




        _value_layout = d.pop("valueLayout", UNSET)
        value_layout: PivotTableValueLayout | Unset
        if isinstance(_value_layout,  Unset):
            value_layout = UNSET
        else:
            value_layout = PivotTableValueLayout(_value_layout)




        _values = d.pop("values", UNSET)
        values: list[PivotValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = PivotValue.from_dict(values_item_data)



                values.append(values_item)


        pivot_table = cls(
            columns=columns,
            criteria=criteria,
            data_execution_status=data_execution_status,
            data_source_id=data_source_id,
            filter_specs=filter_specs,
            rows=rows,
            source=source,
            value_layout=value_layout,
            values=values,
        )


        pivot_table.additional_properties = d
        return pivot_table

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
