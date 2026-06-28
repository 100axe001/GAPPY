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

T = TypeVar("T", bound="ManualWorkflowStartOutput")


@_attrs_define
class ManualWorkflowStartOutput:
    """
    Attributes:
        config (None | Unset): Always `null` for manual workflow starts.
        type_ (Literal['MANUAL'] | Unset): Manual workflow start with no configuration payload. Default: 'MANUAL'.
    """

    config: None | Unset = UNSET
    type_: Literal["MANUAL"] | Unset = "MANUAL"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config = d.pop("config", UNSET)

        type_ = cast(Literal["MANUAL"] | Unset, d.pop("type", UNSET))
        if type_ != "MANUAL" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'MANUAL', got '{type_}'")

        manual_workflow_start_output = cls(
            config=config,
            type_=type_,
        )

        manual_workflow_start_output.additional_properties = d
        return manual_workflow_start_output

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
