from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.message_part_body import MessagePartBody
  from ..models.message_part_header import MessagePartHeader





T = TypeVar("T", bound="MessagePart")



@_attrs_define
class MessagePart:
    """ A single MIME message part.

        Attributes:
            body (MessagePartBody | Unset): The body of a single MIME message part.
            filename (str | Unset): The filename of the attachment. Only present if this message part represents an
                attachment.
            headers (list[MessagePartHeader] | Unset): List of headers on this message part. For the top-level message part,
                representing the entire message payload, it will contain the standard RFC 2822 email headers such as `To`,
                `From`, and `Subject`.
            mime_type (str | Unset): The MIME type of the message part.
            part_id (str | Unset): The immutable ID of the message part.
            parts (list[MessagePart] | Unset): The child MIME message parts of this part. This only applies to container
                MIME message parts, for example `multipart/*`. For non- container MIME message part types, such as `text/plain`,
                this field is empty. For more information, see RFC 1521.
     """

    body: MessagePartBody | Unset = UNSET
    filename: str | Unset = UNSET
    headers: list[MessagePartHeader] | Unset = UNSET
    mime_type: str | Unset = UNSET
    part_id: str | Unset = UNSET
    parts: list[MessagePart] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.message_part_body import MessagePartBody
        from ..models.message_part_header import MessagePartHeader
        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        filename = self.filename

        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)



        mime_type = self.mime_type

        part_id = self.part_id

        parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if body is not UNSET:
            field_dict["body"] = body
        if filename is not UNSET:
            field_dict["filename"] = filename
        if headers is not UNSET:
            field_dict["headers"] = headers
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if parts is not UNSET:
            field_dict["parts"] = parts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_part_body import MessagePartBody
        from ..models.message_part_header import MessagePartHeader
        d = dict(src_dict)
        _body = d.pop("body", UNSET)
        body: MessagePartBody | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = MessagePartBody.from_dict(_body)




        filename = d.pop("filename", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: list[MessagePartHeader] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = MessagePartHeader.from_dict(headers_item_data)



                headers.append(headers_item)


        mime_type = d.pop("mimeType", UNSET)

        part_id = d.pop("partId", UNSET)

        _parts = d.pop("parts", UNSET)
        parts: list[MessagePart] | Unset = UNSET
        if _parts is not UNSET:
            parts = []
            for parts_item_data in _parts:
                parts_item = MessagePart.from_dict(parts_item_data)



                parts.append(parts_item)


        message_part = cls(
            body=body,
            filename=filename,
            headers=headers,
            mime_type=mime_type,
            part_id=part_id,
            parts=parts,
        )


        message_part.additional_properties = d
        return message_part

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
