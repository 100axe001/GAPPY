from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="IssueCommentListRequestBean")



@_attrs_define
class IssueCommentListRequestBean:
    """ 
        Attributes:
            ids (list[int]): The list of comment IDs. A maximum of 1000 IDs can be specified.
     """

    ids: list[int]





    def to_dict(self) -> dict[str, Any]:
        ids = self.ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ids": ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[int], d.pop("ids"))


        issue_comment_list_request_bean = cls(
            ids=ids,
        )

        return issue_comment_list_request_bean

