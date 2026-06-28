from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.surface_setup_phase import SurfaceSetupPhase

T = TypeVar("T", bound="SurfaceSetupStep")


@_attrs_define
class SurfaceSetupStep:
    """
    Attributes:
        description (str):
        phase (SurfaceSetupPhase):
        title (str):
    """

    description: str
    phase: SurfaceSetupPhase
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        phase = self.phase.value

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "phase": phase,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        phase = SurfaceSetupPhase(d.pop("phase"))

        title = d.pop("title")

        surface_setup_step = cls(
            description=description,
            phase=phase,
            title=title,
        )

        surface_setup_step.additional_properties = d
        return surface_setup_step

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
