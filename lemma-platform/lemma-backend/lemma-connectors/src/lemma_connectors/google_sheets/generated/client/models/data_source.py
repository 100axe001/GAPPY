from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_column import DataSourceColumn
  from ..models.data_source_spec import DataSourceSpec





T = TypeVar("T", bound="DataSource")



@_attrs_define
class DataSource:
    """ Information about an external data source in the spreadsheet.

        Attributes:
            calculated_columns (list[DataSourceColumn] | Unset): All calculated columns in the data source.
            data_source_id (str | Unset): The spreadsheet-scoped unique ID that identifies the data source. Example:
                1080547365.
            sheet_id (int | Unset): The ID of the Sheet connected with the data source. The field cannot be changed once
                set. When creating a data source, an associated DATA_SOURCE sheet is also created, if the field is not
                specified, the ID of the created sheet will be randomly generated.
            spec (DataSourceSpec | Unset): This specifies the details of the data source. For example, for BigQuery, this
                specifies information about the BigQuery source.
     """

    calculated_columns: list[DataSourceColumn] | Unset = UNSET
    data_source_id: str | Unset = UNSET
    sheet_id: int | Unset = UNSET
    spec: DataSourceSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_column import DataSourceColumn
        from ..models.data_source_spec import DataSourceSpec
        calculated_columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.calculated_columns, Unset):
            calculated_columns = []
            for calculated_columns_item_data in self.calculated_columns:
                calculated_columns_item = calculated_columns_item_data.to_dict()
                calculated_columns.append(calculated_columns_item)



        data_source_id = self.data_source_id

        sheet_id = self.sheet_id

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if calculated_columns is not UNSET:
            field_dict["calculatedColumns"] = calculated_columns
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_column import DataSourceColumn
        from ..models.data_source_spec import DataSourceSpec
        d = dict(src_dict)
        _calculated_columns = d.pop("calculatedColumns", UNSET)
        calculated_columns: list[DataSourceColumn] | Unset = UNSET
        if _calculated_columns is not UNSET:
            calculated_columns = []
            for calculated_columns_item_data in _calculated_columns:
                calculated_columns_item = DataSourceColumn.from_dict(calculated_columns_item_data)



                calculated_columns.append(calculated_columns_item)


        data_source_id = d.pop("dataSourceId", UNSET)

        sheet_id = d.pop("sheetId", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: DataSourceSpec | Unset
        if isinstance(_spec,  Unset):
            spec = UNSET
        else:
            spec = DataSourceSpec.from_dict(_spec)




        data_source = cls(
            calculated_columns=calculated_columns,
            data_source_id=data_source_id,
            sheet_id=sheet_id,
            spec=spec,
        )


        data_source.additional_properties = d
        return data_source

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
