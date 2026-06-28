from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BigQueryTableSpec")



@_attrs_define
class BigQueryTableSpec:
    """ Specifies a BigQuery table definition. Only [native tables](https://cloud.google.com/bigquery/docs/tables-intro) is
    allowed.

        Attributes:
            dataset_id (str | Unset): The BigQuery dataset id.
            table_id (str | Unset): The BigQuery table id.
            table_project_id (str | Unset): The ID of a BigQuery project the table belongs to. If not specified, the
                project_id is assumed.
     """

    dataset_id: str | Unset = UNSET
    table_id: str | Unset = UNSET
    table_project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        table_id = self.table_id

        table_project_id = self.table_project_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if table_id is not UNSET:
            field_dict["tableId"] = table_id
        if table_project_id is not UNSET:
            field_dict["tableProjectId"] = table_project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId", UNSET)

        table_id = d.pop("tableId", UNSET)

        table_project_id = d.pop("tableProjectId", UNSET)

        big_query_table_spec = cls(
            dataset_id=dataset_id,
            table_id=table_id,
            table_project_id=table_project_id,
        )


        big_query_table_spec.additional_properties = d
        return big_query_table_spec

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
