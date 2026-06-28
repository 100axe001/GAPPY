from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_defaults_response_schema_extra_params import (
        OAuth2DefaultsResponseSchemaExtraParams,
    )


T = TypeVar("T", bound="OAuth2DefaultsResponseSchema")


@_attrs_define
class OAuth2DefaultsResponseSchema:
    """
    Attributes:
        authorization_url (str):
        access_token_path (str | Unset):  Default: 'access_token'.
        default_scopes (list[str] | Unset):
        extra_params (OAuth2DefaultsResponseSchemaExtraParams | Unset):
        refresh_token_path (str | Unset):  Default: 'refresh_token'.
        revoke_url (None | str | Unset):
        token_url (None | str | Unset):
        userinfo_url (None | str | Unset):
    """

    authorization_url: str
    access_token_path: str | Unset = "access_token"
    default_scopes: list[str] | Unset = UNSET
    extra_params: OAuth2DefaultsResponseSchemaExtraParams | Unset = UNSET
    refresh_token_path: str | Unset = "refresh_token"
    revoke_url: None | str | Unset = UNSET
    token_url: None | str | Unset = UNSET
    userinfo_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorization_url = self.authorization_url

        access_token_path = self.access_token_path

        default_scopes: list[str] | Unset = UNSET
        if not isinstance(self.default_scopes, Unset):
            default_scopes = self.default_scopes

        extra_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_params, Unset):
            extra_params = self.extra_params.to_dict()

        refresh_token_path = self.refresh_token_path

        revoke_url: None | str | Unset
        if isinstance(self.revoke_url, Unset):
            revoke_url = UNSET
        else:
            revoke_url = self.revoke_url

        token_url: None | str | Unset
        if isinstance(self.token_url, Unset):
            token_url = UNSET
        else:
            token_url = self.token_url

        userinfo_url: None | str | Unset
        if isinstance(self.userinfo_url, Unset):
            userinfo_url = UNSET
        else:
            userinfo_url = self.userinfo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorization_url": authorization_url,
            }
        )
        if access_token_path is not UNSET:
            field_dict["access_token_path"] = access_token_path
        if default_scopes is not UNSET:
            field_dict["default_scopes"] = default_scopes
        if extra_params is not UNSET:
            field_dict["extra_params"] = extra_params
        if refresh_token_path is not UNSET:
            field_dict["refresh_token_path"] = refresh_token_path
        if revoke_url is not UNSET:
            field_dict["revoke_url"] = revoke_url
        if token_url is not UNSET:
            field_dict["token_url"] = token_url
        if userinfo_url is not UNSET:
            field_dict["userinfo_url"] = userinfo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_defaults_response_schema_extra_params import (
            OAuth2DefaultsResponseSchemaExtraParams,
        )

        d = dict(src_dict)
        authorization_url = d.pop("authorization_url")

        access_token_path = d.pop("access_token_path", UNSET)

        default_scopes = cast(list[str], d.pop("default_scopes", UNSET))

        _extra_params = d.pop("extra_params", UNSET)
        extra_params: OAuth2DefaultsResponseSchemaExtraParams | Unset
        if isinstance(_extra_params, Unset):
            extra_params = UNSET
        else:
            extra_params = OAuth2DefaultsResponseSchemaExtraParams.from_dict(
                _extra_params
            )

        refresh_token_path = d.pop("refresh_token_path", UNSET)

        def _parse_revoke_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revoke_url = _parse_revoke_url(d.pop("revoke_url", UNSET))

        def _parse_token_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token_url = _parse_token_url(d.pop("token_url", UNSET))

        def _parse_userinfo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        userinfo_url = _parse_userinfo_url(d.pop("userinfo_url", UNSET))

        o_auth_2_defaults_response_schema = cls(
            authorization_url=authorization_url,
            access_token_path=access_token_path,
            default_scopes=default_scopes,
            extra_params=extra_params,
            refresh_token_path=refresh_token_path,
            revoke_url=revoke_url,
            token_url=token_url,
            userinfo_url=userinfo_url,
        )

        o_auth_2_defaults_response_schema.additional_properties = d
        return o_auth_2_defaults_response_schema

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
