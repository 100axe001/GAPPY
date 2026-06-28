from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ConversationsKickConversationsKickSuccessSchema")



@_attrs_define
class ConversationsKickConversationsKickSuccessSchema:
    """ Schema for successful response conversations.kick method

        Attributes:
            ok (bool):
     """

    ok: bool





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        conversations_kick_conversations_kick_success_schema = cls(
            ok=ok,
        )

        return conversations_kick_conversations_kick_success_schema

