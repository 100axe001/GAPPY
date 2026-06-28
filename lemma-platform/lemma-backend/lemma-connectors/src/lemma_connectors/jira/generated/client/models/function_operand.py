from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FunctionOperand")



@_attrs_define
class FunctionOperand:
    """ An operand that is a function. See [Advanced searching - functions
    reference](https://confluence.atlassian.com/x/dwiiLQ) for more information about JQL functions.

        Attributes:
            arguments (list[str]): The list of function arguments.
            function (str): The name of the function.
            encoded_operand (str | Unset): Encoded operand, which can be used directly in a JQL query.
     """

    arguments: list[str]
    function: str
    encoded_operand: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        arguments = self.arguments



        function = self.function

        encoded_operand = self.encoded_operand


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "arguments": arguments,
            "function": function,
        })
        if encoded_operand is not UNSET:
            field_dict["encodedOperand"] = encoded_operand

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arguments = cast(list[str], d.pop("arguments"))


        function = d.pop("function")

        encoded_operand = d.pop("encodedOperand", UNSET)

        function_operand = cls(
            arguments=arguments,
            function=function,
            encoded_operand=encoded_operand,
        )


        function_operand.additional_properties = d
        return function_operand

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
