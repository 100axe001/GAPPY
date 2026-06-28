from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="NewUserDetails")



@_attrs_define
class NewUserDetails:
    """ The user details.

        Attributes:
            email_address (str): The email address for the user.
            application_keys (list[str] | Unset): Deprecated, do not use.
            display_name (str | Unset): This property is no longer available. If the user has an Atlassian account, their
                display name is not changed. If the user does not have an Atlassian account, they are sent an email asking them
                set up an account.
            key (str | Unset): This property is no longer available. See the [migration
                guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/)
                for details.
            name (str | Unset): This property is no longer available. See the [migration
                guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/)
                for details.
            password (str | Unset): This property is no longer available. If the user has an Atlassian account, their
                password is not changed. If the user does not have an Atlassian account, they are sent an email asking them set
                up an account.
            self_ (str | Unset): The URL of the user.
     """

    email_address: str
    application_keys: list[str] | Unset = UNSET
    display_name: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    password: str | Unset = UNSET
    self_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        application_keys: list[str] | Unset = UNSET
        if not isinstance(self.application_keys, Unset):
            application_keys = self.application_keys



        display_name = self.display_name

        key = self.key

        name = self.name

        password = self.password

        self_ = self.self_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "emailAddress": email_address,
        })
        if application_keys is not UNSET:
            field_dict["applicationKeys"] = application_keys
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if password is not UNSET:
            field_dict["password"] = password
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_address = d.pop("emailAddress")

        application_keys = cast(list[str], d.pop("applicationKeys", UNSET))


        display_name = d.pop("displayName", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        password = d.pop("password", UNSET)

        self_ = d.pop("self", UNSET)

        new_user_details = cls(
            email_address=email_address,
            application_keys=application_keys,
            display_name=display_name,
            key=key,
            name=name,
            password=password,
            self_=self_,
        )


        new_user_details.additional_properties = d
        return new_user_details

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
