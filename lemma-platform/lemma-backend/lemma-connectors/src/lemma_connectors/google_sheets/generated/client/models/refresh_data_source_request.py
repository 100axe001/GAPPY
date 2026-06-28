from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_object_references import DataSourceObjectReferences





T = TypeVar("T", bound="RefreshDataSourceRequest")



@_attrs_define
class RefreshDataSourceRequest:
    """ Refreshes one or multiple data source objects in the spreadsheet by the specified references. The request requires
    an additional `bigquery.readonly` OAuth scope. If there are multiple refresh requests referencing the same data
    source objects in one batch, only the last refresh request is processed, and all those requests will have the same
    response accordingly.

        Attributes:
            data_source_id (str | Unset): Reference to a DataSource. If specified, refreshes all associated data source
                objects for the data source.
            force (bool | Unset): Refreshes the data source objects regardless of the current state. If not set and a
                referenced data source object was in error state, the refresh will fail immediately.
            is_all (bool | Unset): Refreshes all existing data source objects in the spreadsheet.
            references (DataSourceObjectReferences | Unset): A list of references to data source objects.
     """

    data_source_id: str | Unset = UNSET
    force: bool | Unset = UNSET
    is_all: bool | Unset = UNSET
    references: DataSourceObjectReferences | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_object_references import DataSourceObjectReferences
        data_source_id = self.data_source_id

        force = self.force

        is_all = self.is_all

        references: dict[str, Any] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if force is not UNSET:
            field_dict["force"] = force
        if is_all is not UNSET:
            field_dict["isAll"] = is_all
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_object_references import DataSourceObjectReferences
        d = dict(src_dict)
        data_source_id = d.pop("dataSourceId", UNSET)

        force = d.pop("force", UNSET)

        is_all = d.pop("isAll", UNSET)

        _references = d.pop("references", UNSET)
        references: DataSourceObjectReferences | Unset
        if isinstance(_references,  Unset):
            references = UNSET
        else:
            references = DataSourceObjectReferences.from_dict(_references)




        refresh_data_source_request = cls(
            data_source_id=data_source_id,
            force=force,
            is_all=is_all,
            references=references,
        )


        refresh_data_source_request.additional_properties = d
        return refresh_data_source_request

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
