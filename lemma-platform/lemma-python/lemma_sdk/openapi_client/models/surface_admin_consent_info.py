from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SurfaceAdminConsentInfo")


@_attrs_define
class SurfaceAdminConsentInfo:
    """Admin-consent state for surfaces that require an OAuth grant (Teams).

    Attributes:
        consent_url (None | str | Unset):
        granted (bool | Unset):  Default: False.
        required (bool | Unset):  Default: False.
    """

    consent_url: None | str | Unset = UNSET
    granted: bool | Unset = False
    required: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consent_url: None | str | Unset
        if isinstance(self.consent_url, Unset):
            consent_url = UNSET
        else:
            consent_url = self.consent_url

        granted = self.granted

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consent_url is not UNSET:
            field_dict["consent_url"] = consent_url
        if granted is not UNSET:
            field_dict["granted"] = granted
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_consent_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consent_url = _parse_consent_url(d.pop("consent_url", UNSET))

        granted = d.pop("granted", UNSET)

        required = d.pop("required", UNSET)

        surface_admin_consent_info = cls(
            consent_url=consent_url,
            granted=granted,
            required=required,
        )

        surface_admin_consent_info.additional_properties = d
        return surface_admin_consent_info

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
