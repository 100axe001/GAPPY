from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.label_label_list_visibility import LabelLabelListVisibility
from ..models.label_message_list_visibility import LabelMessageListVisibility
from ..models.label_type import LabelType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.label_color import LabelColor





T = TypeVar("T", bound="Label")



@_attrs_define
class Label:
    """ Labels are used to categorize messages and threads within the user's mailbox. The maximum number of labels supported
    for a user's mailbox is 10,000.

        Attributes:
            color (LabelColor | Unset):
            id (str | Unset): The immutable ID of the label.
            label_list_visibility (LabelLabelListVisibility | Unset): The visibility of the label in the label list in the
                Gmail web interface.
            message_list_visibility (LabelMessageListVisibility | Unset): The visibility of messages with this label in the
                message list in the Gmail web interface.
            messages_total (int | Unset): The total number of messages with the label.
            messages_unread (int | Unset): The number of unread messages with the label.
            name (str | Unset): The display name of the label.
            threads_total (int | Unset): The total number of threads with the label.
            threads_unread (int | Unset): The number of unread threads with the label.
            type_ (LabelType | Unset): The owner type for the label. User labels are created by the user and can be modified
                and deleted by the user and can be applied to any message or thread. System labels are internally created and
                cannot be added, modified, or deleted. System labels may be able to be applied to or removed from messages and
                threads under some circumstances but this is not guaranteed. For example, users can apply and remove the `INBOX`
                and `UNREAD` labels from messages and threads, but cannot apply or remove the `DRAFTS` or `SENT` labels from
                messages or threads.
     """

    color: LabelColor | Unset = UNSET
    id: str | Unset = UNSET
    label_list_visibility: LabelLabelListVisibility | Unset = UNSET
    message_list_visibility: LabelMessageListVisibility | Unset = UNSET
    messages_total: int | Unset = UNSET
    messages_unread: int | Unset = UNSET
    name: str | Unset = UNSET
    threads_total: int | Unset = UNSET
    threads_unread: int | Unset = UNSET
    type_: LabelType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.label_color import LabelColor
        color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        id = self.id

        label_list_visibility: str | Unset = UNSET
        if not isinstance(self.label_list_visibility, Unset):
            label_list_visibility = self.label_list_visibility.value


        message_list_visibility: str | Unset = UNSET
        if not isinstance(self.message_list_visibility, Unset):
            message_list_visibility = self.message_list_visibility.value


        messages_total = self.messages_total

        messages_unread = self.messages_unread

        name = self.name

        threads_total = self.threads_total

        threads_unread = self.threads_unread

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if id is not UNSET:
            field_dict["id"] = id
        if label_list_visibility is not UNSET:
            field_dict["labelListVisibility"] = label_list_visibility
        if message_list_visibility is not UNSET:
            field_dict["messageListVisibility"] = message_list_visibility
        if messages_total is not UNSET:
            field_dict["messagesTotal"] = messages_total
        if messages_unread is not UNSET:
            field_dict["messagesUnread"] = messages_unread
        if name is not UNSET:
            field_dict["name"] = name
        if threads_total is not UNSET:
            field_dict["threadsTotal"] = threads_total
        if threads_unread is not UNSET:
            field_dict["threadsUnread"] = threads_unread
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_color import LabelColor
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: LabelColor | Unset
        if isinstance(_color,  Unset):
            color = UNSET
        else:
            color = LabelColor.from_dict(_color)




        id = d.pop("id", UNSET)

        _label_list_visibility = d.pop("labelListVisibility", UNSET)
        label_list_visibility: LabelLabelListVisibility | Unset
        if isinstance(_label_list_visibility,  Unset):
            label_list_visibility = UNSET
        else:
            label_list_visibility = LabelLabelListVisibility(_label_list_visibility)




        _message_list_visibility = d.pop("messageListVisibility", UNSET)
        message_list_visibility: LabelMessageListVisibility | Unset
        if isinstance(_message_list_visibility,  Unset):
            message_list_visibility = UNSET
        else:
            message_list_visibility = LabelMessageListVisibility(_message_list_visibility)




        messages_total = d.pop("messagesTotal", UNSET)

        messages_unread = d.pop("messagesUnread", UNSET)

        name = d.pop("name", UNSET)

        threads_total = d.pop("threadsTotal", UNSET)

        threads_unread = d.pop("threadsUnread", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: LabelType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = LabelType(_type_)




        label = cls(
            color=color,
            id=id,
            label_list_visibility=label_list_visibility,
            message_list_visibility=message_list_visibility,
            messages_total=messages_total,
            messages_unread=messages_unread,
            name=name,
            threads_total=threads_total,
            threads_unread=threads_unread,
            type_=type_,
        )


        label.additional_properties = d
        return label

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
