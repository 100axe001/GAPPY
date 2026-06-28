from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatDeleteDataBody")



@_attrs_define
class ChatDeleteDataBody:
    """ 
        Attributes:
            ts (float | Unset): Timestamp of the message to be deleted.
            channel (str | Unset): Channel containing the message to be deleted.
            as_user (bool | Unset): Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot
                users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted
                with `chat:write:bot` scope.
     """

    ts: float | Unset = UNSET
    channel: str | Unset = UNSET
    as_user: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ts = self.ts

        channel = self.channel

        as_user = self.as_user


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ts is not UNSET:
            field_dict["ts"] = ts
        if channel is not UNSET:
            field_dict["channel"] = channel
        if as_user is not UNSET:
            field_dict["as_user"] = as_user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ts = d.pop("ts", UNSET)

        channel = d.pop("channel", UNSET)

        as_user = d.pop("as_user", UNSET)

        chat_delete_data_body = cls(
            ts=ts,
            channel=channel,
            as_user=as_user,
        )


        chat_delete_data_body.additional_properties = d
        return chat_delete_data_body

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
