from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.auto_forwarding_disposition import AutoForwardingDisposition
from ..types import UNSET, Unset






T = TypeVar("T", bound="AutoForwarding")



@_attrs_define
class AutoForwarding:
    """ Auto-forwarding settings for an account.

        Attributes:
            disposition (AutoForwardingDisposition | Unset): The state that a message should be left in after it has been
                forwarded.
            email_address (str | Unset): Email address to which all incoming messages are forwarded. This email address must
                be a verified member of the forwarding addresses.
            enabled (bool | Unset): Whether all incoming mail is automatically forwarded to another address.
     """

    disposition: AutoForwardingDisposition | Unset = UNSET
    email_address: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        disposition: str | Unset = UNSET
        if not isinstance(self.disposition, Unset):
            disposition = self.disposition.value


        email_address = self.email_address

        enabled = self.enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if disposition is not UNSET:
            field_dict["disposition"] = disposition
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _disposition = d.pop("disposition", UNSET)
        disposition: AutoForwardingDisposition | Unset
        if isinstance(_disposition,  Unset):
            disposition = UNSET
        else:
            disposition = AutoForwardingDisposition(_disposition)




        email_address = d.pop("emailAddress", UNSET)

        enabled = d.pop("enabled", UNSET)

        auto_forwarding = cls(
            disposition=disposition,
            email_address=email_address,
            enabled=enabled,
        )


        auto_forwarding.additional_properties = d
        return auto_forwarding

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
