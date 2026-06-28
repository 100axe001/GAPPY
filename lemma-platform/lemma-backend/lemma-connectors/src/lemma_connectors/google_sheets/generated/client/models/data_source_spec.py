from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.big_query_data_source_spec import BigQueryDataSourceSpec
  from ..models.data_source_parameter import DataSourceParameter





T = TypeVar("T", bound="DataSourceSpec")



@_attrs_define
class DataSourceSpec:
    """ This specifies the details of the data source. For example, for BigQuery, this specifies information about the
    BigQuery source.

        Attributes:
            big_query (BigQueryDataSourceSpec | Unset): The specification of a BigQuery data source that's connected to a
                sheet.
            parameters (list[DataSourceParameter] | Unset): The parameters of the data source, used when querying the data
                source.
     """

    big_query: BigQueryDataSourceSpec | Unset = UNSET
    parameters: list[DataSourceParameter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.big_query_data_source_spec import BigQueryDataSourceSpec
        from ..models.data_source_parameter import DataSourceParameter
        big_query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.big_query, Unset):
            big_query = self.big_query.to_dict()

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if big_query is not UNSET:
            field_dict["bigQuery"] = big_query
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.big_query_data_source_spec import BigQueryDataSourceSpec
        from ..models.data_source_parameter import DataSourceParameter
        d = dict(src_dict)
        _big_query = d.pop("bigQuery", UNSET)
        big_query: BigQueryDataSourceSpec | Unset
        if isinstance(_big_query,  Unset):
            big_query = UNSET
        else:
            big_query = BigQueryDataSourceSpec.from_dict(_big_query)




        _parameters = d.pop("parameters", UNSET)
        parameters: list[DataSourceParameter] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = DataSourceParameter.from_dict(parameters_item_data)



                parameters.append(parameters_item)


        data_source_spec = cls(
            big_query=big_query,
            parameters=parameters,
        )


        data_source_spec.additional_properties = d
        return data_source_spec

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
