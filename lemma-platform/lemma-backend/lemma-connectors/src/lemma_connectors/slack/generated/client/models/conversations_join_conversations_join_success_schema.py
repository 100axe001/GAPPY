from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conversations_join_conversations_join_success_schema_response_metadata import ConversationsJoinConversationsJoinSuccessSchemaResponseMetadata





T = TypeVar("T", bound="ConversationsJoinConversationsJoinSuccessSchema")



@_attrs_define
class ConversationsJoinConversationsJoinSuccessSchema:
    """ Schema for successful response from conversations.join method

        Attributes:
            channel (Any):
            ok (bool):
            response_metadata (ConversationsJoinConversationsJoinSuccessSchemaResponseMetadata | Unset):
            warning (str | Unset):
     """

    channel: Any
    ok: bool
    response_metadata: ConversationsJoinConversationsJoinSuccessSchemaResponseMetadata | Unset = UNSET
    warning: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.conversations_join_conversations_join_success_schema_response_metadata import ConversationsJoinConversationsJoinSuccessSchemaResponseMetadata
        channel = self.channel

        ok = self.ok

        response_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_metadata, Unset):
            response_metadata = self.response_metadata.to_dict()

        warning = self.warning


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channel": channel,
            "ok": ok,
        })
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversations_join_conversations_join_success_schema_response_metadata import ConversationsJoinConversationsJoinSuccessSchemaResponseMetadata
        d = dict(src_dict)
        channel = d.pop("channel")

        ok = d.pop("ok")

        _response_metadata = d.pop("response_metadata", UNSET)
        response_metadata: ConversationsJoinConversationsJoinSuccessSchemaResponseMetadata | Unset
        if isinstance(_response_metadata,  Unset):
            response_metadata = UNSET
        else:
            response_metadata = ConversationsJoinConversationsJoinSuccessSchemaResponseMetadata.from_dict(_response_metadata)




        warning = d.pop("warning", UNSET)

        conversations_join_conversations_join_success_schema = cls(
            channel=channel,
            ok=ok,
            response_metadata=response_metadata,
            warning=warning,
        )

        return conversations_join_conversations_join_success_schema

