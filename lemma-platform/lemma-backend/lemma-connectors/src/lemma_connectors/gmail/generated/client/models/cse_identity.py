from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CseIdentity")



@_attrs_define
class CseIdentity:
    """ The client-side encryption (CSE) configuration for the email address of an authenticated user. Gmail uses CSE
    configurations to save drafts of client-side encrypted email messages, and to sign and send encrypted email
    messages.

        Attributes:
            email_address (str | Unset): The email address for the sending identity. The email address must be the primary
                email address of the authenticated user.
            primary_key_pair_id (str | Unset): If a key pair is associated, the identifier of the key pair, CseKeyPair.
     """

    email_address: str | Unset = UNSET
    primary_key_pair_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        primary_key_pair_id = self.primary_key_pair_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if primary_key_pair_id is not UNSET:
            field_dict["primaryKeyPairId"] = primary_key_pair_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_address = d.pop("emailAddress", UNSET)

        primary_key_pair_id = d.pop("primaryKeyPairId", UNSET)

        cse_identity = cls(
            email_address=email_address,
            primary_key_pair_id=primary_key_pair_id,
        )


        cse_identity.additional_properties = d
        return cse_identity

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
