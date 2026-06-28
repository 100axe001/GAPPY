from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyCredentialsResponseSchema")


@_attrs_define
class ApiKeyCredentialsResponseSchema:
    """Schema for API key credentials response.

    Attributes:
        api_key (str):
        api_secret (None | str | Unset):
    """

    api_key: str
    api_secret: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        api_secret: None | str | Unset
        if isinstance(self.api_secret, Unset):
            api_secret = UNSET
        else:
            api_secret = self.api_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key": api_key,
            }
        )
        if api_secret is not UNSET:
            field_dict["api_secret"] = api_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("api_key")

        def _parse_api_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_secret = _parse_api_secret(d.pop("api_secret", UNSET))

        api_key_credentials_response_schema = cls(
            api_key=api_key,
            api_secret=api_secret,
        )

        api_key_credentials_response_schema.additional_properties = d
        return api_key_credentials_response_schema

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
