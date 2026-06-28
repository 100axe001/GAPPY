from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="EventAttachment")



@_attrs_define
class EventAttachment:
    """ 
        Attributes:
            file_id (str | Unset): ID of the attached file. Read-only.
                For Google Drive files, this is the ID of the corresponding Files resource entry in the Drive API.
            file_url (str | Unset): URL link to the attachment.
                For adding Google Drive file attachments use the same format as in alternateLink property of the Files resource
                in the Drive API.
                Required when adding an attachment.
            icon_link (str | Unset): URL link to the attachment's icon. This field can only be modified for custom third-
                party attachments.
            mime_type (str | Unset): Internet media type (MIME type) of the attachment.
            title (str | Unset): Attachment title.
     """

    file_id: str | Unset = UNSET
    file_url: str | Unset = UNSET
    icon_link: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        file_url = self.file_url

        icon_link = self.icon_link

        mime_type = self.mime_type

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if file_url is not UNSET:
            field_dict["fileUrl"] = file_url
        if icon_link is not UNSET:
            field_dict["iconLink"] = icon_link
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("fileId", UNSET)

        file_url = d.pop("fileUrl", UNSET)

        icon_link = d.pop("iconLink", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        title = d.pop("title", UNSET)

        event_attachment = cls(
            file_id=file_id,
            file_url=file_url,
            icon_link=icon_link,
            mime_type=mime_type,
            title=title,
        )


        event_attachment.additional_properties = d
        return event_attachment

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
