from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conversations_list_conversations_list_success_schema_response_metadata import ConversationsListConversationsListSuccessSchemaResponseMetadata





T = TypeVar("T", bound="ConversationsListConversationsListSuccessSchema")



@_attrs_define
class ConversationsListConversationsListSuccessSchema:
    """ Schema for successful response from conversations.list method

        Attributes:
            channels (list[Any]):
            ok (bool):
            response_metadata (ConversationsListConversationsListSuccessSchemaResponseMetadata | Unset):
     """

    channels: list[Any]
    ok: bool
    response_metadata: ConversationsListConversationsListSuccessSchemaResponseMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.conversations_list_conversations_list_success_schema_response_metadata import ConversationsListConversationsListSuccessSchemaResponseMetadata
        channels = self.channels



        ok = self.ok

        response_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_metadata, Unset):
            response_metadata = self.response_metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "channels": channels,
            "ok": ok,
        })
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversations_list_conversations_list_success_schema_response_metadata import ConversationsListConversationsListSuccessSchemaResponseMetadata
        d = dict(src_dict)
        channels = cast(list[Any], d.pop("channels"))


        ok = d.pop("ok")

        _response_metadata = d.pop("response_metadata", UNSET)
        response_metadata: ConversationsListConversationsListSuccessSchemaResponseMetadata | Unset
        if isinstance(_response_metadata,  Unset):
            response_metadata = UNSET
        else:
            response_metadata = ConversationsListConversationsListSuccessSchemaResponseMetadata.from_dict(_response_metadata)




        conversations_list_conversations_list_success_schema = cls(
            channels=channels,
            ok=ok,
            response_metadata=response_metadata,
        )

        return conversations_list_conversations_list_success_schema

