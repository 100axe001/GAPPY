from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.message import Message





T = TypeVar("T", bound="HistoryLabelRemoved")



@_attrs_define
class HistoryLabelRemoved:
    """ 
        Attributes:
            label_ids (list[str] | Unset): Label IDs removed from the message.
            message (Message | Unset): An email message.
     """

    label_ids: list[str] | Unset = UNSET
    message: Message | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.message import Message
        label_ids: list[str] | Unset = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids



        message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message
        d = dict(src_dict)
        label_ids = cast(list[str], d.pop("labelIds", UNSET))


        _message = d.pop("message", UNSET)
        message: Message | Unset
        if isinstance(_message,  Unset):
            message = UNSET
        else:
            message = Message.from_dict(_message)




        history_label_removed = cls(
            label_ids=label_ids,
            message=message,
        )


        history_label_removed.additional_properties = d
        return history_label_removed

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
