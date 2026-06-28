from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatUnfurlDataBody")



@_attrs_define
class ChatUnfurlDataBody:
    """ 
        Attributes:
            channel (str): Channel ID of the message
            ts (str): Timestamp of the message to add unfurl behavior to.
            unfurls (str | Unset): URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their
                unfurl blocks or message attachments.
            user_auth_message (str | Unset): Provide a simply-formatted string to send as an ephemeral message to the user
                as invitation to authenticate further and enable full unfurling behavior
            user_auth_required (bool | Unset): Set to `true` or `1` to indicate the user must install your Slack app to
                trigger unfurls for this domain
            user_auth_url (str | Unset): Send users to this custom URL where they will complete authentication in your app
                to fully trigger unfurling. Value should be properly URL-encoded.
     """

    channel: str
    ts: str
    unfurls: str | Unset = UNSET
    user_auth_message: str | Unset = UNSET
    user_auth_required: bool | Unset = UNSET
    user_auth_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ts = self.ts

        unfurls = self.unfurls

        user_auth_message = self.user_auth_message

        user_auth_required = self.user_auth_required

        user_auth_url = self.user_auth_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channel": channel,
            "ts": ts,
        })
        if unfurls is not UNSET:
            field_dict["unfurls"] = unfurls
        if user_auth_message is not UNSET:
            field_dict["user_auth_message"] = user_auth_message
        if user_auth_required is not UNSET:
            field_dict["user_auth_required"] = user_auth_required
        if user_auth_url is not UNSET:
            field_dict["user_auth_url"] = user_auth_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel")

        ts = d.pop("ts")

        unfurls = d.pop("unfurls", UNSET)

        user_auth_message = d.pop("user_auth_message", UNSET)

        user_auth_required = d.pop("user_auth_required", UNSET)

        user_auth_url = d.pop("user_auth_url", UNSET)

        chat_unfurl_data_body = cls(
            channel=channel,
            ts=ts,
            unfurls=unfurls,
            user_auth_message=user_auth_message,
            user_auth_required=user_auth_required,
            user_auth_url=user_auth_url,
        )


        chat_unfurl_data_body.additional_properties = d
        return chat_unfurl_data_body

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
