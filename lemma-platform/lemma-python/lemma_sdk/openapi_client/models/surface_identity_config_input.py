from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SurfaceIdentityConfigInput")


@_attrs_define
class SurfaceIdentityConfigInput:
    """
    Attributes:
        allowed_domains (list[str] | Unset):
        allowed_email_addresses (list[str] | Unset):
    """

    allowed_domains: list[str] | Unset = UNSET
    allowed_email_addresses: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_domains: list[str] | Unset = UNSET
        if not isinstance(self.allowed_domains, Unset):
            allowed_domains = self.allowed_domains

        allowed_email_addresses: list[str] | Unset = UNSET
        if not isinstance(self.allowed_email_addresses, Unset):
            allowed_email_addresses = self.allowed_email_addresses

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_domains is not UNSET:
            field_dict["allowed_domains"] = allowed_domains
        if allowed_email_addresses is not UNSET:
            field_dict["allowed_email_addresses"] = allowed_email_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_domains = cast(list[str], d.pop("allowed_domains", UNSET))

        allowed_email_addresses = cast(
            list[str], d.pop("allowed_email_addresses", UNSET)
        )

        surface_identity_config_input = cls(
            allowed_domains=allowed_domains,
            allowed_email_addresses=allowed_email_addresses,
        )

        return surface_identity_config_input
