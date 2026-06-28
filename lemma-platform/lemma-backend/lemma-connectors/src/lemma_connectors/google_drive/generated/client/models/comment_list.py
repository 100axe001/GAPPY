from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.comment import Comment





T = TypeVar("T", bound="CommentList")



@_attrs_define
class CommentList:
    """ A list of comments on a file.

        Attributes:
            comments (list[Comment] | Unset): The list of comments. If nextPageToken is populated, then this list may be
                incomplete and an additional page of results should be fetched.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#commentList".
                Default: 'drive#commentList'.
            next_page_token (str | Unset): The page token for the next page of comments. This will be absent if the end of
                the comments list has been reached. If the token is rejected for any reason, it should be discarded, and
                pagination should be restarted from the first page of results.
     """

    comments: list[Comment] | Unset = UNSET
    kind: str | Unset = 'drive#commentList'
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.comment import Comment
        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)



        kind = self.kind

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comments is not UNSET:
            field_dict["comments"] = comments
        if kind is not UNSET:
            field_dict["kind"] = kind
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment import Comment
        d = dict(src_dict)
        _comments = d.pop("comments", UNSET)
        comments: list[Comment] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = Comment.from_dict(comments_item_data)



                comments.append(comments_item)


        kind = d.pop("kind", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        comment_list = cls(
            comments=comments,
            kind=kind,
            next_page_token=next_page_token,
        )


        comment_list.additional_properties = d
        return comment_list

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
