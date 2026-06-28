from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Profile")



@_attrs_define
class Profile:
    """ Profile for a Gmail user.

        Attributes:
            email_address (str | Unset): The user's email address.
            history_id (str | Unset): The ID of the mailbox's current history record.
            messages_total (int | Unset): The total number of messages in the mailbox.
            threads_total (int | Unset): The total number of threads in the mailbox.
     """

    email_address: str | Unset = UNSET
    history_id: str | Unset = UNSET
    messages_total: int | Unset = UNSET
    threads_total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        history_id = self.history_id

        messages_total = self.messages_total

        threads_total = self.threads_total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if history_id is not UNSET:
            field_dict["historyId"] = history_id
        if messages_total is not UNSET:
            field_dict["messagesTotal"] = messages_total
        if threads_total is not UNSET:
            field_dict["threadsTotal"] = threads_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_address = d.pop("emailAddress", UNSET)

        history_id = d.pop("historyId", UNSET)

        messages_total = d.pop("messagesTotal", UNSET)

        threads_total = d.pop("threadsTotal", UNSET)

        profile = cls(
            email_address=email_address,
            history_id=history_id,
            messages_total=messages_total,
            threads_total=threads_total,
        )


        profile.additional_properties = d
        return profile

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
