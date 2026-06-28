from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.function_node_config_input_mapping import (
        FunctionNodeConfigInputMapping,
    )


T = TypeVar("T", bound="FunctionNodeConfig")


@_attrs_define
class FunctionNodeConfig:
    """Configuration for Function node.

    Attributes:
        function_name (str): Function resource name to execute.
        input_mapping (FunctionNodeConfigInputMapping | Unset): Explicit mapping from function argument key to either an
            expression or a literal JSON value. Strings are never auto-interpreted. Example: {'amount': {'type':
            'expression', 'value': 'collect_input.amount'}, 'currency': {'type': 'literal', 'value': 'USD'}}.
    """

    function_name: str
    input_mapping: FunctionNodeConfigInputMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function_name = self.function_name

        input_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_mapping, Unset):
            input_mapping = self.input_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function_name": function_name,
            }
        )
        if input_mapping is not UNSET:
            field_dict["input_mapping"] = input_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_node_config_input_mapping import (
            FunctionNodeConfigInputMapping,
        )

        d = dict(src_dict)
        function_name = d.pop("function_name")

        _input_mapping = d.pop("input_mapping", UNSET)
        input_mapping: FunctionNodeConfigInputMapping | Unset
        if isinstance(_input_mapping, Unset):
            input_mapping = UNSET
        else:
            input_mapping = FunctionNodeConfigInputMapping.from_dict(_input_mapping)

        function_node_config = cls(
            function_name=function_name,
            input_mapping=input_mapping,
        )

        function_node_config.additional_properties = d
        return function_node_config

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
