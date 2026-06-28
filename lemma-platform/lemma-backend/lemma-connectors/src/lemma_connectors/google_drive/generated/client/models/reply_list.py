from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reply import Reply





T = TypeVar("T", bound="ReplyList")



@_attrs_define
class ReplyList:
    """ A list of replies to a comment on a file.

        Attributes:
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#replyList".
                Default: 'drive#replyList'.
            next_page_token (str | Unset): The page token for the next page of replies. This will be absent if the end of
                the replies list has been reached. If the token is rejected for any reason, it should be discarded, and
                pagination should be restarted from the first page of results.
            replies (list[Reply] | Unset): The list of replies. If nextPageToken is populated, then this list may be
                incomplete and an additional page of results should be fetched.
     """

    kind: str | Unset = 'drive#replyList'
    next_page_token: str | Unset = UNSET
    replies: list[Reply] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reply import Reply
        kind = self.kind

        next_page_token = self.next_page_token

        replies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replies, Unset):
            replies = []
            for replies_item_data in self.replies:
                replies_item = replies_item_data.to_dict()
                replies.append(replies_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if replies is not UNSET:
            field_dict["replies"] = replies

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reply import Reply
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        _replies = d.pop("replies", UNSET)
        replies: list[Reply] | Unset = UNSET
        if _replies is not UNSET:
            replies = []
            for replies_item_data in _replies:
                replies_item = Reply.from_dict(replies_item_data)



                replies.append(replies_item)


        reply_list = cls(
            kind=kind,
            next_page_token=next_page_token,
            replies=replies,
        )


        reply_list.additional_properties = d
        return reply_list

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
