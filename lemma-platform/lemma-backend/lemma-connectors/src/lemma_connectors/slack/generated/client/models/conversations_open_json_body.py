from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConversationsOpenJsonBody")



@_attrs_define
class ConversationsOpenJsonBody:
    """ 
        Attributes:
            channel (str | Unset): Resume a conversation by supplying an `im` or `mpim`'s ID. Or provide the `users` field
                instead.
            users (str | Unset): Comma separated lists of users. If only one user is included, this creates a 1:1 DM.  The
                ordering of the users is preserved whenever a multi-person direct message is returned. Supply a `channel` when
                not supplying `users`.
            return_im (bool | Unset): Boolean, indicates you want the full IM channel definition in the response.
     """

    channel: str | Unset = UNSET
    users: str | Unset = UNSET
    return_im: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        users = self.users

        return_im = self.return_im


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if users is not UNSET:
            field_dict["users"] = users
        if return_im is not UNSET:
            field_dict["return_im"] = return_im

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        users = d.pop("users", UNSET)

        return_im = d.pop("return_im", UNSET)

        conversations_open_json_body = cls(
            channel=channel,
            users=users,
            return_im=return_im,
        )


        conversations_open_json_body.additional_properties = d
        return conversations_open_json_body

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
