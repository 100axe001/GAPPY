from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.forwarding_address_verification_status import ForwardingAddressVerificationStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="ForwardingAddress")



@_attrs_define
class ForwardingAddress:
    """ Settings for a forwarding address.

        Attributes:
            forwarding_email (str | Unset): An email address to which messages can be forwarded.
            verification_status (ForwardingAddressVerificationStatus | Unset): Indicates whether this address has been
                verified and is usable for forwarding. Read-only.
     """

    forwarding_email: str | Unset = UNSET
    verification_status: ForwardingAddressVerificationStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        forwarding_email = self.forwarding_email

        verification_status: str | Unset = UNSET
        if not isinstance(self.verification_status, Unset):
            verification_status = self.verification_status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if forwarding_email is not UNSET:
            field_dict["forwardingEmail"] = forwarding_email
        if verification_status is not UNSET:
            field_dict["verificationStatus"] = verification_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forwarding_email = d.pop("forwardingEmail", UNSET)

        _verification_status = d.pop("verificationStatus", UNSET)
        verification_status: ForwardingAddressVerificationStatus | Unset
        if isinstance(_verification_status,  Unset):
            verification_status = UNSET
        else:
            verification_status = ForwardingAddressVerificationStatus(_verification_status)




        forwarding_address = cls(
            forwarding_email=forwarding_email,
            verification_status=verification_status,
        )


        forwarding_address.additional_properties = d
        return forwarding_address

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
