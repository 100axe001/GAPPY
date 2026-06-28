from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.big_query_query_spec import BigQueryQuerySpec
  from ..models.big_query_table_spec import BigQueryTableSpec





T = TypeVar("T", bound="BigQueryDataSourceSpec")



@_attrs_define
class BigQueryDataSourceSpec:
    """ The specification of a BigQuery data source that's connected to a sheet.

        Attributes:
            project_id (str | Unset): The ID of a BigQuery enabled GCP project with a billing account attached. For any
                queries executed against the data source, the project is charged.
            query_spec (BigQueryQuerySpec | Unset): Specifies a custom BigQuery query.
            table_spec (BigQueryTableSpec | Unset): Specifies a BigQuery table definition. Only [native
                tables](https://cloud.google.com/bigquery/docs/tables-intro) is allowed.
     """

    project_id: str | Unset = UNSET
    query_spec: BigQueryQuerySpec | Unset = UNSET
    table_spec: BigQueryTableSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.big_query_query_spec import BigQueryQuerySpec
        from ..models.big_query_table_spec import BigQueryTableSpec
        project_id = self.project_id

        query_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_spec, Unset):
            query_spec = self.query_spec.to_dict()

        table_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_spec, Unset):
            table_spec = self.table_spec.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if query_spec is not UNSET:
            field_dict["querySpec"] = query_spec
        if table_spec is not UNSET:
            field_dict["tableSpec"] = table_spec

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.big_query_query_spec import BigQueryQuerySpec
        from ..models.big_query_table_spec import BigQueryTableSpec
        d = dict(src_dict)
        project_id = d.pop("projectId", UNSET)

        _query_spec = d.pop("querySpec", UNSET)
        query_spec: BigQueryQuerySpec | Unset
        if isinstance(_query_spec,  Unset):
            query_spec = UNSET
        else:
            query_spec = BigQueryQuerySpec.from_dict(_query_spec)




        _table_spec = d.pop("tableSpec", UNSET)
        table_spec: BigQueryTableSpec | Unset
        if isinstance(_table_spec,  Unset):
            table_spec = UNSET
        else:
            table_spec = BigQueryTableSpec.from_dict(_table_spec)




        big_query_data_source_spec = cls(
            project_id=project_id,
            query_spec=query_spec,
            table_spec=table_spec,
        )


        big_query_data_source_spec.additional_properties = d
        return big_query_data_source_spec

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
