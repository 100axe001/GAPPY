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





T = TypeVar("T", bound="PageOfComments")



@_attrs_define
class PageOfComments:
    """ A page of comments.

        Attributes:
            comments (list[Comment] | Unset): The list of comments.
            max_results (int | Unset): The maximum number of items that could be returned.
            start_at (int | Unset): The index of the first item returned.
            total (int | Unset): The number of items returned.
     """

    comments: list[Comment] | Unset = UNSET
    max_results: int | Unset = UNSET
    start_at: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.comment import Comment
        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)



        max_results = self.max_results

        start_at = self.start_at

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comments is not UNSET:
            field_dict["comments"] = comments
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if total is not UNSET:
            field_dict["total"] = total

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


        max_results = d.pop("maxResults", UNSET)

        start_at = d.pop("startAt", UNSET)

        total = d.pop("total", UNSET)

        page_of_comments = cls(
            comments=comments,
            max_results=max_results,
            start_at=start_at,
            total=total,
        )


        page_of_comments.additional_properties = d
        return page_of_comments

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
