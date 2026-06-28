from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source import DataSource





T = TypeVar("T", bound="AddDataSourceRequest")



@_attrs_define
class AddDataSourceRequest:
    """ Adds a data source. After the data source is added successfully, an associated DATA_SOURCE sheet is created and an
    execution is triggered to refresh the sheet to read data from the data source. The request requires an additional
    `bigquery.readonly` OAuth scope.

        Attributes:
            data_source (DataSource | Unset): Information about an external data source in the spreadsheet.
     """

    data_source: DataSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source import DataSource
        data_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_source is not UNSET:
            field_dict["dataSource"] = data_source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source import DataSource
        d = dict(src_dict)
        _data_source = d.pop("dataSource", UNSET)
        data_source: DataSource | Unset
        if isinstance(_data_source,  Unset):
            data_source = UNSET
        else:
            data_source = DataSource.from_dict(_data_source)




        add_data_source_request = cls(
            data_source=data_source,
        )


        add_data_source_request.additional_properties = d
        return add_data_source_request

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
