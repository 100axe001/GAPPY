from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.history_label_added import HistoryLabelAdded
  from ..models.history_label_removed import HistoryLabelRemoved
  from ..models.history_message_added import HistoryMessageAdded
  from ..models.history_message_deleted import HistoryMessageDeleted
  from ..models.message import Message





T = TypeVar("T", bound="History")



@_attrs_define
class History:
    """ A record of a change to the user's mailbox. Each history change may affect multiple messages in multiple ways.

        Attributes:
            id (str | Unset): The mailbox sequence ID.
            labels_added (list[HistoryLabelAdded] | Unset): Labels added to messages in this history record.
            labels_removed (list[HistoryLabelRemoved] | Unset): Labels removed from messages in this history record.
            messages (list[Message] | Unset): List of messages changed in this history record. The fields for specific
                change types, such as `messagesAdded` may duplicate messages in this field. We recommend using the specific
                change-type fields instead of this.
            messages_added (list[HistoryMessageAdded] | Unset): Messages added to the mailbox in this history record.
            messages_deleted (list[HistoryMessageDeleted] | Unset): Messages deleted (not Trashed) from the mailbox in this
                history record.
     """

    id: str | Unset = UNSET
    labels_added: list[HistoryLabelAdded] | Unset = UNSET
    labels_removed: list[HistoryLabelRemoved] | Unset = UNSET
    messages: list[Message] | Unset = UNSET
    messages_added: list[HistoryMessageAdded] | Unset = UNSET
    messages_deleted: list[HistoryMessageDeleted] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.history_label_added import HistoryLabelAdded
        from ..models.history_label_removed import HistoryLabelRemoved
        from ..models.history_message_added import HistoryMessageAdded
        from ..models.history_message_deleted import HistoryMessageDeleted
        from ..models.message import Message
        id = self.id

        labels_added: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels_added, Unset):
            labels_added = []
            for labels_added_item_data in self.labels_added:
                labels_added_item = labels_added_item_data.to_dict()
                labels_added.append(labels_added_item)



        labels_removed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels_removed, Unset):
            labels_removed = []
            for labels_removed_item_data in self.labels_removed:
                labels_removed_item = labels_removed_item_data.to_dict()
                labels_removed.append(labels_removed_item)



        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)



        messages_added: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages_added, Unset):
            messages_added = []
            for messages_added_item_data in self.messages_added:
                messages_added_item = messages_added_item_data.to_dict()
                messages_added.append(messages_added_item)



        messages_deleted: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages_deleted, Unset):
            messages_deleted = []
            for messages_deleted_item_data in self.messages_deleted:
                messages_deleted_item = messages_deleted_item_data.to_dict()
                messages_deleted.append(messages_deleted_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if labels_added is not UNSET:
            field_dict["labelsAdded"] = labels_added
        if labels_removed is not UNSET:
            field_dict["labelsRemoved"] = labels_removed
        if messages is not UNSET:
            field_dict["messages"] = messages
        if messages_added is not UNSET:
            field_dict["messagesAdded"] = messages_added
        if messages_deleted is not UNSET:
            field_dict["messagesDeleted"] = messages_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.history_label_added import HistoryLabelAdded
        from ..models.history_label_removed import HistoryLabelRemoved
        from ..models.history_message_added import HistoryMessageAdded
        from ..models.history_message_deleted import HistoryMessageDeleted
        from ..models.message import Message
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _labels_added = d.pop("labelsAdded", UNSET)
        labels_added: list[HistoryLabelAdded] | Unset = UNSET
        if _labels_added is not UNSET:
            labels_added = []
            for labels_added_item_data in _labels_added:
                labels_added_item = HistoryLabelAdded.from_dict(labels_added_item_data)



                labels_added.append(labels_added_item)


        _labels_removed = d.pop("labelsRemoved", UNSET)
        labels_removed: list[HistoryLabelRemoved] | Unset = UNSET
        if _labels_removed is not UNSET:
            labels_removed = []
            for labels_removed_item_data in _labels_removed:
                labels_removed_item = HistoryLabelRemoved.from_dict(labels_removed_item_data)



                labels_removed.append(labels_removed_item)


        _messages = d.pop("messages", UNSET)
        messages: list[Message] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = Message.from_dict(messages_item_data)



                messages.append(messages_item)


        _messages_added = d.pop("messagesAdded", UNSET)
        messages_added: list[HistoryMessageAdded] | Unset = UNSET
        if _messages_added is not UNSET:
            messages_added = []
            for messages_added_item_data in _messages_added:
                messages_added_item = HistoryMessageAdded.from_dict(messages_added_item_data)



                messages_added.append(messages_added_item)


        _messages_deleted = d.pop("messagesDeleted", UNSET)
        messages_deleted: list[HistoryMessageDeleted] | Unset = UNSET
        if _messages_deleted is not UNSET:
            messages_deleted = []
            for messages_deleted_item_data in _messages_deleted:
                messages_deleted_item = HistoryMessageDeleted.from_dict(messages_deleted_item_data)



                messages_deleted.append(messages_deleted_item)


        history = cls(
            id=id,
            labels_added=labels_added,
            labels_removed=labels_removed,
            messages=messages,
            messages_added=messages_added,
            messages_deleted=messages_deleted,
        )


        history.additional_properties = d
        return history

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
