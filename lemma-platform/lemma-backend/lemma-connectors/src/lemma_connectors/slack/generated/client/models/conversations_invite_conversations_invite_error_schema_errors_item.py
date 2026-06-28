from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversations_invite_conversations_invite_error_schema_errors_item_error import ConversationsInviteConversationsInviteErrorSchemaErrorsItemError
from ..types import UNSET, Unset






T = TypeVar("T", bound="ConversationsInviteConversationsInviteErrorSchemaErrorsItem")



@_attrs_define
class ConversationsInviteConversationsInviteErrorSchemaErrorsItem:
    """ 
        Attributes:
            error (ConversationsInviteConversationsInviteErrorSchemaErrorsItemError):
            ok (bool):
            user (str | Unset):
     """

    error: ConversationsInviteConversationsInviteErrorSchemaErrorsItemError
    ok: bool
    user: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        ok = self.ok

        user = self.user


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "ok": ok,
        })
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = ConversationsInviteConversationsInviteErrorSchemaErrorsItemError(d.pop("error"))




        ok = d.pop("ok")

        user = d.pop("user", UNSET)

        conversations_invite_conversations_invite_error_schema_errors_item = cls(
            error=error,
            ok=ok,
            user=user,
        )

        return conversations_invite_conversations_invite_error_schema_errors_item

