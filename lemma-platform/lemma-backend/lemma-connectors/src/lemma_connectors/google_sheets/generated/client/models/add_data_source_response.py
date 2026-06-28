from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_execution_status import DataExecutionStatus
  from ..models.data_source import DataSource





T = TypeVar("T", bound="AddDataSourceResponse")



@_attrs_define
class AddDataSourceResponse:
    """ The result of adding a data source.

        Attributes:
            data_execution_status (DataExecutionStatus | Unset): The data execution status. A data execution is created to
                sync a data source object with the latest data from a DataSource. It is usually scheduled to run at background,
                you can check its state to tell if an execution completes There are several scenarios where a data execution is
                triggered to run: * Adding a data source creates an associated data source sheet as well as a data execution to
                sync the data from the data source to the sheet. * Updating a data source creates a data execution to refresh
                the associated data source sheet similarly. * You can send refresh request to explicitly refresh one or multiple
                data source objects.
            data_source (DataSource | Unset): Information about an external data source in the spreadsheet.
     """

    data_execution_status: DataExecutionStatus | Unset = UNSET
    data_source: DataSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_execution_status import DataExecutionStatus
        from ..models.data_source import DataSource
        data_execution_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_execution_status, Unset):
            data_execution_status = self.data_execution_status.to_dict()

        data_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_execution_status is not UNSET:
            field_dict["dataExecutionStatus"] = data_execution_status
        if data_source is not UNSET:
            field_dict["dataSource"] = data_source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_execution_status import DataExecutionStatus
        from ..models.data_source import DataSource
        d = dict(src_dict)
        _data_execution_status = d.pop("dataExecutionStatus", UNSET)
        data_execution_status: DataExecutionStatus | Unset
        if isinstance(_data_execution_status,  Unset):
            data_execution_status = UNSET
        else:
            data_execution_status = DataExecutionStatus.from_dict(_data_execution_status)




        _data_source = d.pop("dataSource", UNSET)
        data_source: DataSource | Unset
        if isinstance(_data_source,  Unset):
            data_source = UNSET
        else:
            data_source = DataSource.from_dict(_data_source)




        add_data_source_response = cls(
            data_execution_status=data_execution_status,
            data_source=data_source,
        )


        add_data_source_response.additional_properties = d
        return add_data_source_response

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
