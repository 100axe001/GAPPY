from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.surface_setup_field_source import SurfaceSetupFieldSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="SurfaceSetupField")


@_attrs_define
class SurfaceSetupField:
    """
    Attributes:
        description (str):
        label (str):
        name (str):
        source (SurfaceSetupFieldSource):
        example (None | str | Unset):
        required (bool | Unset):  Default: True.
        secret (bool | Unset):  Default: False.
    """

    description: str
    label: str
    name: str
    source: SurfaceSetupFieldSource
    example: None | str | Unset = UNSET
    required: bool | Unset = True
    secret: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        label = self.label

        name = self.name

        source = self.source.value

        example: None | str | Unset
        if isinstance(self.example, Unset):
            example = UNSET
        else:
            example = self.example

        required = self.required

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "label": label,
                "name": name,
                "source": source,
            }
        )
        if example is not UNSET:
            field_dict["example"] = example
        if required is not UNSET:
            field_dict["required"] = required
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        label = d.pop("label")

        name = d.pop("name")

        source = SurfaceSetupFieldSource(d.pop("source"))

        def _parse_example(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example = _parse_example(d.pop("example", UNSET))

        required = d.pop("required", UNSET)

        secret = d.pop("secret", UNSET)

        surface_setup_field = cls(
            description=description,
            label=label,
            name=name,
            source=source,
            example=example,
            required=required,
            secret=secret,
        )

        surface_setup_field.additional_properties = d
        return surface_setup_field

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
