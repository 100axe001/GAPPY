from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSignedUrlRequest")


@_attrs_define
class FileSignedUrlRequest:
    """
    Attributes:
        expires_seconds (int | None | Unset):
        max_hits (int | None | Unset):
    """

    expires_seconds: int | None | Unset = UNSET
    max_hits: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_seconds: int | None | Unset
        if isinstance(self.expires_seconds, Unset):
            expires_seconds = UNSET
        else:
            expires_seconds = self.expires_seconds

        max_hits: int | None | Unset
        if isinstance(self.max_hits, Unset):
            max_hits = UNSET
        else:
            max_hits = self.max_hits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_seconds is not UNSET:
            field_dict["expires_seconds"] = expires_seconds
        if max_hits is not UNSET:
            field_dict["max_hits"] = max_hits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expires_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_seconds = _parse_expires_seconds(d.pop("expires_seconds", UNSET))

        def _parse_max_hits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_hits = _parse_max_hits(d.pop("max_hits", UNSET))

        file_signed_url_request = cls(
            expires_seconds=expires_seconds,
            max_hits=max_hits,
        )

        file_signed_url_request.additional_properties = d
        return file_signed_url_request

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
