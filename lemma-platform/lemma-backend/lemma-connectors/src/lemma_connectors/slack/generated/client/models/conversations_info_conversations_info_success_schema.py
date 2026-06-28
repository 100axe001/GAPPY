from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ConversationsInfoConversationsInfoSuccessSchema")



@_attrs_define
class ConversationsInfoConversationsInfoSuccessSchema:
    """ Schema for successful response conversations.info

        Attributes:
            channel (Any):
            ok (bool):
     """

    channel: Any
    ok: bool





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ok = self.ok


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel": channel,
            "ok": ok,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = d.pop("channel")

        ok = d.pop("ok")

        conversations_info_conversations_info_success_schema = cls(
            channel=channel,
            ok=ok,
        )

        return conversations_info_conversations_info_success_schema

