from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chat_update_chat_update_success_schema_message_object_attachments_item import ChatUpdateChatUpdateSuccessSchemaMessageObjectAttachmentsItem
  from ..models.chat_update_chat_update_success_schema_message_object_blocks import ChatUpdateChatUpdateSuccessSchemaMessageObjectBlocks





T = TypeVar("T", bound="ChatUpdateChatUpdateSuccessSchemaMessageObject")



@_attrs_define
class ChatUpdateChatUpdateSuccessSchemaMessageObject:
    """ 
        Attributes:
            text (str):
            attachments (list[ChatUpdateChatUpdateSuccessSchemaMessageObjectAttachmentsItem] | Unset):
            blocks (ChatUpdateChatUpdateSuccessSchemaMessageObjectBlocks | Unset):
     """

    text: str
    attachments: list[ChatUpdateChatUpdateSuccessSchemaMessageObjectAttachmentsItem] | Unset = UNSET
    blocks: ChatUpdateChatUpdateSuccessSchemaMessageObjectBlocks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_update_chat_update_success_schema_message_object_attachments_item import ChatUpdateChatUpdateSuccessSchemaMessageObjectAttachmentsItem
        from ..models.chat_update_chat_update_success_schema_message_object_blocks import ChatUpdateChatUpdateSuccessSchemaMessageObjectBlocks
        text = self.text

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        blocks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blocks, Unset):
            blocks = self.blocks.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "text": text,
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if blocks is not UNSET:
            field_dict["blocks"] = blocks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_update_chat_update_success_schema_message_object_attachments_item import ChatUpdateChatUpdateSuccessSchemaMessageObjectAttachmentsItem
        from ..models.chat_update_chat_update_success_schema_message_object_blocks import ChatUpdateChatUpdateSuccessSchemaMessageObjectBlocks
        d = dict(src_dict)
        text = d.pop("text")

        _attachments = d.pop("attachments", UNSET)
        attachments: list[ChatUpdateChatUpdateSuccessSchemaMessageObjectAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ChatUpdateChatUpdateSuccessSchemaMessageObjectAttachmentsItem.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        _blocks = d.pop("blocks", UNSET)
        blocks: ChatUpdateChatUpdateSuccessSchemaMessageObjectBlocks | Unset
        if isinstance(_blocks,  Unset):
            blocks = UNSET
        else:
            blocks = ChatUpdateChatUpdateSuccessSchemaMessageObjectBlocks.from_dict(_blocks)




        chat_update_chat_update_success_schema_message_object = cls(
            text=text,
            attachments=attachments,
            blocks=blocks,
        )


        chat_update_chat_update_success_schema_message_object.additional_properties = d
        return chat_update_chat_update_success_schema_message_object

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
