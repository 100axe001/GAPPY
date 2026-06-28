from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.user_details import UserDetails





T = TypeVar("T", bound="Attachment")



@_attrs_define
class Attachment:
    """ Details about an attachment.

        Attributes:
            author (UserDetails | Unset): User details permitted by the user's Atlassian Account privacy settings. However,
                be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            content (str | Unset): The content of the attachment.
            created (datetime.datetime | Unset): The datetime the attachment was created.
            filename (str | Unset): The file name of the attachment.
            id (str | Unset): The ID of the attachment.
            mime_type (str | Unset): The MIME type of the attachment.
            self_ (str | Unset): The URL of the attachment details response.
            size (int | Unset): The size of the attachment.
            thumbnail (str | Unset): The URL of a thumbnail representing the attachment.
     """

    author: UserDetails | Unset = UNSET
    content: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    filename: str | Unset = UNSET
    id: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    self_: str | Unset = UNSET
    size: int | Unset = UNSET
    thumbnail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_details import UserDetails
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        content = self.content

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        filename = self.filename

        id = self.id

        mime_type = self.mime_type

        self_ = self.self_

        size = self.size

        thumbnail = self.thumbnail


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if author is not UNSET:
            field_dict["author"] = author
        if content is not UNSET:
            field_dict["content"] = content
        if created is not UNSET:
            field_dict["created"] = created
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if self_ is not UNSET:
            field_dict["self"] = self_
        if size is not UNSET:
            field_dict["size"] = size
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_details import UserDetails
        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: UserDetails | Unset
        if isinstance(_author,  Unset):
            author = UNSET
        else:
            author = UserDetails.from_dict(_author)




        content = d.pop("content", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        filename = d.pop("filename", UNSET)

        id = d.pop("id", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        self_ = d.pop("self", UNSET)

        size = d.pop("size", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        attachment = cls(
            author=author,
            content=content,
            created=created,
            filename=filename,
            id=id,
            mime_type=mime_type,
            self_=self_,
            size=size,
            thumbnail=thumbnail,
        )


        attachment.additional_properties = d
        return attachment

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
