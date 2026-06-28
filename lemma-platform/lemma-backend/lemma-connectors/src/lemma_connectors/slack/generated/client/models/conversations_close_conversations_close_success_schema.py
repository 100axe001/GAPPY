from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConversationsCloseConversationsCloseSuccessSchema")



@_attrs_define
class ConversationsCloseConversationsCloseSuccessSchema:
    """ Schema for successful response conversations.close method

        Attributes:
            ok (bool):
            already_closed (bool | Unset):
            no_op (bool | Unset):
     """

    ok: bool
    already_closed: bool | Unset = UNSET
    no_op: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        already_closed = self.already_closed

        no_op = self.no_op


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
        })
        if already_closed is not UNSET:
            field_dict["already_closed"] = already_closed
        if no_op is not UNSET:
            field_dict["no_op"] = no_op

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        already_closed = d.pop("already_closed", UNSET)

        no_op = d.pop("no_op", UNSET)

        conversations_close_conversations_close_success_schema = cls(
            ok=ok,
            already_closed=already_closed,
            no_op=no_op,
        )

        return conversations_close_conversations_close_success_schema

