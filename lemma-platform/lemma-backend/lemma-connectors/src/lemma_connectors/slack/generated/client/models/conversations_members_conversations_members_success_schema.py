from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.conversations_members_conversations_members_success_schema_response_metadata import ConversationsMembersConversationsMembersSuccessSchemaResponseMetadata





T = TypeVar("T", bound="ConversationsMembersConversationsMembersSuccessSchema")



@_attrs_define
class ConversationsMembersConversationsMembersSuccessSchema:
    """ Schema for successful response conversations.members method

        Attributes:
            members (list[str]):
            ok (bool):
            response_metadata (ConversationsMembersConversationsMembersSuccessSchemaResponseMetadata):
     """

    members: list[str]
    ok: bool
    response_metadata: ConversationsMembersConversationsMembersSuccessSchemaResponseMetadata





    def to_dict(self) -> dict[str, Any]:
        from ..models.conversations_members_conversations_members_success_schema_response_metadata import ConversationsMembersConversationsMembersSuccessSchemaResponseMetadata
        members = self.members



        ok = self.ok

        response_metadata = self.response_metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "members": members,
            "ok": ok,
            "response_metadata": response_metadata,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversations_members_conversations_members_success_schema_response_metadata import ConversationsMembersConversationsMembersSuccessSchemaResponseMetadata
        d = dict(src_dict)
        members = cast(list[str], d.pop("members"))


        ok = d.pop("ok")

        response_metadata = ConversationsMembersConversationsMembersSuccessSchemaResponseMetadata.from_dict(d.pop("response_metadata"))




        conversations_members_conversations_members_success_schema = cls(
            members=members,
            ok=ok,
            response_metadata=response_metadata,
        )

        return conversations_members_conversations_members_success_schema

