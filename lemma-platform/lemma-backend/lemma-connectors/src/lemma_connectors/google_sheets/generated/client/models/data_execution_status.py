from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.data_execution_status_error_code import DataExecutionStatusErrorCode
from ..models.data_execution_status_state import DataExecutionStatusState
from ..types import UNSET, Unset






T = TypeVar("T", bound="DataExecutionStatus")



@_attrs_define
class DataExecutionStatus:
    """ The data execution status. A data execution is created to sync a data source object with the latest data from a
    DataSource. It is usually scheduled to run at background, you can check its state to tell if an execution completes
    There are several scenarios where a data execution is triggered to run: * Adding a data source creates an associated
    data source sheet as well as a data execution to sync the data from the data source to the sheet. * Updating a data
    source creates a data execution to refresh the associated data source sheet similarly. * You can send refresh
    request to explicitly refresh one or multiple data source objects.

        Attributes:
            error_code (DataExecutionStatusErrorCode | Unset): The error code.
            error_message (str | Unset): The error message, which may be empty.
            last_refresh_time (str | Unset): Gets the time the data last successfully refreshed.
            state (DataExecutionStatusState | Unset): The state of the data execution.
     """

    error_code: DataExecutionStatusErrorCode | Unset = UNSET
    error_message: str | Unset = UNSET
    last_refresh_time: str | Unset = UNSET
    state: DataExecutionStatusState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value


        error_message = self.error_message

        last_refresh_time = self.last_refresh_time

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if last_refresh_time is not UNSET:
            field_dict["lastRefreshTime"] = last_refresh_time
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _error_code = d.pop("errorCode", UNSET)
        error_code: DataExecutionStatusErrorCode | Unset
        if isinstance(_error_code,  Unset):
            error_code = UNSET
        else:
            error_code = DataExecutionStatusErrorCode(_error_code)




        error_message = d.pop("errorMessage", UNSET)

        last_refresh_time = d.pop("lastRefreshTime", UNSET)

        _state = d.pop("state", UNSET)
        state: DataExecutionStatusState | Unset
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = DataExecutionStatusState(_state)




        data_execution_status = cls(
            error_code=error_code,
            error_message=error_message,
            last_refresh_time=last_refresh_time,
            state=state,
        )


        data_execution_status.additional_properties = d
        return data_execution_status

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
