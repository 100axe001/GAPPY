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
  from ..models.user import User





T = TypeVar("T", bound="Reply")



@_attrs_define
class Reply:
    """ A reply to a comment on a file.

        Attributes:
            action (str | Unset): The action the reply performed to the parent comment. Valid values are:
                - resolve
                - reopen
            author (User | Unset): Information about a Drive user.
            content (str | Unset): The plain text content of the reply. This field is used for setting the content, while
                htmlContent should be displayed. This is required on creates if no action is specified.
            created_time (datetime.datetime | Unset): The time at which the reply was created (RFC 3339 date-time).
            deleted (bool | Unset): Whether the reply has been deleted. A deleted reply has no content.
            html_content (str | Unset): The content of the reply with HTML formatting.
            id (str | Unset): The ID of the reply.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#reply". Default:
                'drive#reply'.
            modified_time (datetime.datetime | Unset): The last time the reply was modified (RFC 3339 date-time).
     """

    action: str | Unset = UNSET
    author: User | Unset = UNSET
    content: str | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    deleted: bool | Unset = UNSET
    html_content: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'drive#reply'
    modified_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User
        action = self.action

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        content = self.content

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        deleted = self.deleted

        html_content = self.html_content

        id = self.id

        kind = self.kind

        modified_time: str | Unset = UNSET
        if not isinstance(self.modified_time, Unset):
            modified_time = self.modified_time.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if author is not UNSET:
            field_dict["author"] = author
        if content is not UNSET:
            field_dict["content"] = content
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if html_content is not UNSET:
            field_dict["htmlContent"] = html_content
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        _author = d.pop("author", UNSET)
        author: User | Unset
        if isinstance(_author,  Unset):
            author = UNSET
        else:
            author = User.from_dict(_author)




        content = d.pop("content", UNSET)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time,  Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)




        deleted = d.pop("deleted", UNSET)

        html_content = d.pop("htmlContent", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        _modified_time = d.pop("modifiedTime", UNSET)
        modified_time: datetime.datetime | Unset
        if isinstance(_modified_time,  Unset):
            modified_time = UNSET
        else:
            modified_time = isoparse(_modified_time)




        reply = cls(
            action=action,
            author=author,
            content=content,
            created_time=created_time,
            deleted=deleted,
            html_content=html_content,
            id=id,
            kind=kind,
            modified_time=modified_time,
        )


        reply.additional_properties = d
        return reply

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
