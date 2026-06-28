from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="FileSignedUrlResponse")


@_attrs_define
class FileSignedUrlResponse:
    """
    Attributes:
        expires_at (datetime.datetime):
        max_hits (int):
        path (str):
        signed_url (str):
    """

    expires_at: datetime.datetime
    max_hits: int
    path: str
    signed_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at.isoformat()

        max_hits = self.max_hits

        path = self.path

        signed_url = self.signed_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expires_at": expires_at,
                "max_hits": max_hits,
                "path": path,
                "signed_url": signed_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = isoparse(d.pop("expires_at"))

        max_hits = d.pop("max_hits")

        path = d.pop("path")

        signed_url = d.pop("signed_url")

        file_signed_url_response = cls(
            expires_at=expires_at,
            max_hits=max_hits,
            path=path,
            signed_url=signed_url,
        )

        file_signed_url_response.additional_properties = d
        return file_signed_url_response

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
