from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_types import CredentialTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_credentials_response_schema_user_data_type_0 import (
        AccountCredentialsResponseSchemaUserDataType0,
    )
    from ..models.api_key_credentials_response_schema import (
        ApiKeyCredentialsResponseSchema,
    )
    from ..models.oauth_credentials_response_schema import (
        OauthCredentialsResponseSchema,
    )


T = TypeVar("T", bound="AccountCredentialsResponseSchema")


@_attrs_define
class AccountCredentialsResponseSchema:
    """Schema for account credentials response.

    Attributes:
        data (ApiKeyCredentialsResponseSchema | OauthCredentialsResponseSchema):
        type_ (CredentialTypes | Unset): Credential types.
        user_data (AccountCredentialsResponseSchemaUserDataType0 | None | Unset):
    """

    data: ApiKeyCredentialsResponseSchema | OauthCredentialsResponseSchema
    type_: CredentialTypes | Unset = UNSET
    user_data: AccountCredentialsResponseSchemaUserDataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.account_credentials_response_schema_user_data_type_0 import (
            AccountCredentialsResponseSchemaUserDataType0,
        )
        from ..models.oauth_credentials_response_schema import (
            OauthCredentialsResponseSchema,
        )

        data: dict[str, Any]
        if isinstance(self.data, OauthCredentialsResponseSchema):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        user_data: dict[str, Any] | None | Unset
        if isinstance(self.user_data, Unset):
            user_data = UNSET
        elif isinstance(self.user_data, AccountCredentialsResponseSchemaUserDataType0):
            user_data = self.user_data.to_dict()
        else:
            user_data = self.user_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user_data is not UNSET:
            field_dict["user_data"] = user_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_credentials_response_schema_user_data_type_0 import (
            AccountCredentialsResponseSchemaUserDataType0,
        )
        from ..models.api_key_credentials_response_schema import (
            ApiKeyCredentialsResponseSchema,
        )
        from ..models.oauth_credentials_response_schema import (
            OauthCredentialsResponseSchema,
        )

        d = dict(src_dict)

        def _parse_data(
            data: object,
        ) -> ApiKeyCredentialsResponseSchema | OauthCredentialsResponseSchema:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = OauthCredentialsResponseSchema.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = ApiKeyCredentialsResponseSchema.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data"))

        _type_ = d.pop("type", UNSET)
        type_: CredentialTypes | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CredentialTypes(_type_)

        def _parse_user_data(
            data: object,
        ) -> AccountCredentialsResponseSchemaUserDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_data_type_0 = (
                    AccountCredentialsResponseSchemaUserDataType0.from_dict(data)
                )

                return user_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AccountCredentialsResponseSchemaUserDataType0 | None | Unset, data
            )

        user_data = _parse_user_data(d.pop("user_data", UNSET))

        account_credentials_response_schema = cls(
            data=data,
            type_=type_,
            user_data=user_data,
        )

        account_credentials_response_schema.additional_properties = d
        return account_credentials_response_schema

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
