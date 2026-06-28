from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_function_request_input_data import (
        ExecuteFunctionRequestInputData,
    )


T = TypeVar("T", bound="ExecuteFunctionRequest")


@_attrs_define
class ExecuteFunctionRequest:
    """Request to execute a function.

    Attributes:
        input_data (ExecuteFunctionRequestInputData | Unset):
    """

    input_data: ExecuteFunctionRequestInputData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_data, Unset):
            input_data = self.input_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_data is not UNSET:
            field_dict["input_data"] = input_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_function_request_input_data import (
            ExecuteFunctionRequestInputData,
        )

        d = dict(src_dict)
        _input_data = d.pop("input_data", UNSET)
        input_data: ExecuteFunctionRequestInputData | Unset
        if isinstance(_input_data, Unset):
            input_data = UNSET
        else:
            input_data = ExecuteFunctionRequestInputData.from_dict(_input_data)

        execute_function_request = cls(
            input_data=input_data,
        )

        execute_function_request.additional_properties = d
        return execute_function_request

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
