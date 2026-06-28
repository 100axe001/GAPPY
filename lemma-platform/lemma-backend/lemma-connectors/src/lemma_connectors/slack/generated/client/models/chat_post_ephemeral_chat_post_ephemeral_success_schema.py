from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ChatPostEphemeralChatPostEphemeralSuccessSchema")



@_attrs_define
class ChatPostEphemeralChatPostEphemeralSuccessSchema:
    """ Schema for successful response from chat.postEphemeral method

        Attributes:
            message_ts (str):
            ok (bool):
     """

    message_ts: str
    ok: bool





    def to_dict(self) -> dict[str, Any]:
        message_ts = self.message_ts

        ok = self.ok


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "message_ts": message_ts,
            "ok": ok,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_ts = d.pop("message_ts")

        ok = d.pop("ok")

        chat_post_ephemeral_chat_post_ephemeral_success_schema = cls(
            message_ts=message_ts,
            ok=ok,
        )

        return chat_post_ephemeral_chat_post_ephemeral_success_schema

