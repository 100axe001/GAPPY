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





T = TypeVar("T", bound="DataSourceChartProperties")



@_attrs_define
class DataSourceChartProperties:
    """ Properties of a data source chart.

        Attributes:
            data_execution_status (DataExecutionStatus | Unset): The data execution status. A data execution is created to
                sync a data source object with the latest data from a DataSource. It is usually scheduled to run at background,
                you can check its state to tell if an execution completes There are several scenarios where a data execution is
                triggered to run: * Adding a data source creates an associated data source sheet as well as a data execution to
                sync the data from the data source to the sheet. * Updating a data source creates a data execution to refresh
                the associated data source sheet similarly. * You can send refresh request to explicitly refresh one or multiple
                data source objects.
            data_source_id (str | Unset): ID of the data source that the chart is associated with.
     """

    data_execution_status: DataExecutionStatus | Unset = UNSET
    data_source_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_execution_status import DataExecutionStatus
        data_execution_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_execution_status, Unset):
            data_execution_status = self.data_execution_status.to_dict()

        data_source_id = self.data_source_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_execution_status is not UNSET:
            field_dict["dataExecutionStatus"] = data_execution_status
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_execution_status import DataExecutionStatus
        d = dict(src_dict)
        _data_execution_status = d.pop("dataExecutionStatus", UNSET)
        data_execution_status: DataExecutionStatus | Unset
        if isinstance(_data_execution_status,  Unset):
            data_execution_status = UNSET
        else:
            data_execution_status = DataExecutionStatus.from_dict(_data_execution_status)




        data_source_id = d.pop("dataSourceId", UNSET)

        data_source_chart_properties = cls(
            data_execution_status=data_execution_status,
            data_source_id=data_source_id,
        )


        data_source_chart_properties.additional_properties = d
        return data_source_chart_properties

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
