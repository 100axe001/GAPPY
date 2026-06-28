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
  from ..models.data_source_object_reference import DataSourceObjectReference





T = TypeVar("T", bound="RefreshDataSourceObjectExecutionStatus")



@_attrs_define
class RefreshDataSourceObjectExecutionStatus:
    """ The execution status of refreshing one data source object.

        Attributes:
            data_execution_status (DataExecutionStatus | Unset): The data execution status. A data execution is created to
                sync a data source object with the latest data from a DataSource. It is usually scheduled to run at background,
                you can check its state to tell if an execution completes There are several scenarios where a data execution is
                triggered to run: * Adding a data source creates an associated data source sheet as well as a data execution to
                sync the data from the data source to the sheet. * Updating a data source creates a data execution to refresh
                the associated data source sheet similarly. * You can send refresh request to explicitly refresh one or multiple
                data source objects.
            reference (DataSourceObjectReference | Unset): Reference to a data source object.
     """

    data_execution_status: DataExecutionStatus | Unset = UNSET
    reference: DataSourceObjectReference | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_execution_status import DataExecutionStatus
        from ..models.data_source_object_reference import DataSourceObjectReference
        data_execution_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_execution_status, Unset):
            data_execution_status = self.data_execution_status.to_dict()

        reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference, Unset):
            reference = self.reference.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_execution_status is not UNSET:
            field_dict["dataExecutionStatus"] = data_execution_status
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_execution_status import DataExecutionStatus
        from ..models.data_source_object_reference import DataSourceObjectReference
        d = dict(src_dict)
        _data_execution_status = d.pop("dataExecutionStatus", UNSET)
        data_execution_status: DataExecutionStatus | Unset
        if isinstance(_data_execution_status,  Unset):
            data_execution_status = UNSET
        else:
            data_execution_status = DataExecutionStatus.from_dict(_data_execution_status)




        _reference = d.pop("reference", UNSET)
        reference: DataSourceObjectReference | Unset
        if isinstance(_reference,  Unset):
            reference = UNSET
        else:
            reference = DataSourceObjectReference.from_dict(_reference)




        refresh_data_source_object_execution_status = cls(
            data_execution_status=data_execution_status,
            reference=reference,
        )


        refresh_data_source_object_execution_status.additional_properties = d
        return refresh_data_source_object_execution_status

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
