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

T = TypeVar("T", bound="LiteralInputBinding")


@_attrs_define
class LiteralInputBinding:
    """Pass a literal JSON value into the target input without resolution.

    Attributes:
        value (Any): Literal JSON value forwarded exactly as provided. Use this for strings, numbers, booleans, arrays,
            or objects that should not be interpreted as JMESPath expressions.
        type_ (Literal['literal'] | Unset):  Default: 'literal'.
    """

    value: Any
    type_: Literal["literal"] | Unset = "literal"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        type_ = cast(Literal["literal"] | Unset, d.pop("type", UNSET))
        if type_ != "literal" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'literal', got '{type_}'")

        literal_input_binding = cls(
            value=value,
            type_=type_,
        )

        literal_input_binding.additional_properties = d
        return literal_input_binding

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
