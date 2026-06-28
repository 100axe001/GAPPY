from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MessagePartBody")



@_attrs_define
class MessagePartBody:
    """ The body of a single MIME message part.

        Attributes:
            attachment_id (str | Unset): When present, contains the ID of an external attachment that can be retrieved in a
                separate `messages.attachments.get` request. When not present, the entire content of the message part body is
                contained in the data field.
            data (str | Unset): The body data of a MIME message part as a base64url encoded string. May be empty for MIME
                container types that have no message body or when the body data is sent as a separate attachment. An attachment
                ID is present if the body data is contained in a separate attachment.
            size (int | Unset): Number of bytes for the message part data (encoding notwithstanding).
     """

    attachment_id: str | Unset = UNSET
    data: str | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        attachment_id = self.attachment_id

        data = self.data

        size = self.size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachment_id is not UNSET:
            field_dict["attachmentId"] = attachment_id
        if data is not UNSET:
            field_dict["data"] = data
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment_id = d.pop("attachmentId", UNSET)

        data = d.pop("data", UNSET)

        size = d.pop("size", UNSET)

        message_part_body = cls(
            attachment_id=attachment_id,
            data=data,
            size=size,
        )


        message_part_body.additional_properties = d
        return message_part_body

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
