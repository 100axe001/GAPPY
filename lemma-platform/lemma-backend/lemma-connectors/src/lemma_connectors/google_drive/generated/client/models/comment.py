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
  from ..models.comment_quoted_file_content import CommentQuotedFileContent
  from ..models.reply import Reply
  from ..models.user import User





T = TypeVar("T", bound="Comment")



@_attrs_define
class Comment:
    """ A comment on a file.

        Attributes:
            anchor (str | Unset): A region of the document represented as a JSON string. For details on defining anchor
                properties, refer to  Add comments and replies.
            author (User | Unset): Information about a Drive user.
            content (str | Unset): The plain text content of the comment. This field is used for setting the content, while
                htmlContent should be displayed.
            created_time (datetime.datetime | Unset): The time at which the comment was created (RFC 3339 date-time).
            deleted (bool | Unset): Whether the comment has been deleted. A deleted comment has no content.
            html_content (str | Unset): The content of the comment with HTML formatting.
            id (str | Unset): The ID of the comment.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#comment". Default:
                'drive#comment'.
            modified_time (datetime.datetime | Unset): The last time the comment or any of its replies was modified (RFC
                3339 date-time).
            quoted_file_content (CommentQuotedFileContent | Unset): The file content to which the comment refers, typically
                within the anchor region. For a text file, for example, this would be the text at the location of the comment.
            replies (list[Reply] | Unset): The full list of replies to the comment in chronological order.
            resolved (bool | Unset): Whether the comment has been resolved by one of its replies.
     """

    anchor: str | Unset = UNSET
    author: User | Unset = UNSET
    content: str | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    deleted: bool | Unset = UNSET
    html_content: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'drive#comment'
    modified_time: datetime.datetime | Unset = UNSET
    quoted_file_content: CommentQuotedFileContent | Unset = UNSET
    replies: list[Reply] | Unset = UNSET
    resolved: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.comment_quoted_file_content import CommentQuotedFileContent
        from ..models.reply import Reply
        from ..models.user import User
        anchor = self.anchor

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

        quoted_file_content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quoted_file_content, Unset):
            quoted_file_content = self.quoted_file_content.to_dict()

        replies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replies, Unset):
            replies = []
            for replies_item_data in self.replies:
                replies_item = replies_item_data.to_dict()
                replies.append(replies_item)



        resolved = self.resolved


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if anchor is not UNSET:
            field_dict["anchor"] = anchor
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
        if quoted_file_content is not UNSET:
            field_dict["quotedFileContent"] = quoted_file_content
        if replies is not UNSET:
            field_dict["replies"] = replies
        if resolved is not UNSET:
            field_dict["resolved"] = resolved

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_quoted_file_content import CommentQuotedFileContent
        from ..models.reply import Reply
        from ..models.user import User
        d = dict(src_dict)
        anchor = d.pop("anchor", UNSET)

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




        _quoted_file_content = d.pop("quotedFileContent", UNSET)
        quoted_file_content: CommentQuotedFileContent | Unset
        if isinstance(_quoted_file_content,  Unset):
            quoted_file_content = UNSET
        else:
            quoted_file_content = CommentQuotedFileContent.from_dict(_quoted_file_content)




        _replies = d.pop("replies", UNSET)
        replies: list[Reply] | Unset = UNSET
        if _replies is not UNSET:
            replies = []
            for replies_item_data in _replies:
                replies_item = Reply.from_dict(replies_item_data)



                replies.append(replies_item)


        resolved = d.pop("resolved", UNSET)

        comment = cls(
            anchor=anchor,
            author=author,
            content=content,
            created_time=created_time,
            deleted=deleted,
            html_content=html_content,
            id=id,
            kind=kind,
            modified_time=modified_time,
            quoted_file_content=quoted_file_content,
            replies=replies,
            resolved=resolved,
        )


        comment.additional_properties = d
        return comment

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
