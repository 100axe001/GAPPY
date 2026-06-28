from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.delegate_verification_status import DelegateVerificationStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="Delegate")



@_attrs_define
class Delegate:
    """ Settings for a delegate. Delegates can read, send, and delete messages, as well as view and add contacts, for the
    delegator's account. See "Set up mail delegation" for more information about delegates.

        Attributes:
            delegate_email (str | Unset): The email address of the delegate.
            verification_status (DelegateVerificationStatus | Unset): Indicates whether this address has been verified and
                can act as a delegate for the account. Read-only.
     """

    delegate_email: str | Unset = UNSET
    verification_status: DelegateVerificationStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        delegate_email = self.delegate_email

        verification_status: str | Unset = UNSET
        if not isinstance(self.verification_status, Unset):
            verification_status = self.verification_status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if delegate_email is not UNSET:
            field_dict["delegateEmail"] = delegate_email
        if verification_status is not UNSET:
            field_dict["verificationStatus"] = verification_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delegate_email = d.pop("delegateEmail", UNSET)

        _verification_status = d.pop("verificationStatus", UNSET)
        verification_status: DelegateVerificationStatus | Unset
        if isinstance(_verification_status,  Unset):
            verification_status = UNSET
        else:
            verification_status = DelegateVerificationStatus(_verification_status)




        delegate = cls(
            delegate_email=delegate_email,
            verification_status=verification_status,
        )


        delegate.additional_properties = d
        return delegate

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
