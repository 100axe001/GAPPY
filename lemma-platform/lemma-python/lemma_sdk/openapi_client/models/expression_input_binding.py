from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpressionInputBinding")


@_attrs_define
class ExpressionInputBinding:
    """Resolve a value from the run context using a JMESPath expression.

    Attributes:
        value (str): JMESPath expression evaluated against the run context. Example: `start.payload.issue.key` or
            `collect_input.amount`. Expressions that resolve to nothing fail the run unless `optional` is set.
        optional (bool | Unset): When true, an expression that resolves to nothing yields null instead of failing the
            run. Default: False.
        type_ (Literal['expression'] | Unset):  Default: 'expression'.
    """

    value: str
    optional: bool | Unset = False
    type_: Literal["expression"] | Unset = "expression"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        optional = self.optional

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if optional is not UNSET:
            field_dict["optional"] = optional
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        optional = d.pop("optional", UNSET)

        type_ = cast(Literal["expression"] | Unset, d.pop("type", UNSET))
        if type_ != "expression" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'expression', got '{type_}'")

        expression_input_binding = cls(
            value=value,
            optional=optional,
            type_=type_,
        )

        expression_input_binding.additional_properties = d
        return expression_input_binding

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
