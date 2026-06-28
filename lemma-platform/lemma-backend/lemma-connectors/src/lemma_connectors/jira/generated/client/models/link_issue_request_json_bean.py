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
  from ..models.issue_link_type import IssueLinkType
  from ..models.linked_issue import LinkedIssue





T = TypeVar("T", bound="LinkIssueRequestJsonBean")



@_attrs_define
class LinkIssueRequestJsonBean:
    """ 
        Attributes:
            inward_issue (LinkedIssue): The ID or key of a linked issue.
            outward_issue (LinkedIssue): The ID or key of a linked issue.
            type_ (IssueLinkType): This object is used as follows:

                 *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it defines and reports on the type of link
                between the issues. Find a list of issue link types with [Get issue link types](#api-rest-api-3-issueLinkType-
                get).
                 *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it defines and reports on issue link
                types.
            comment (Comment | Unset): A comment.
     """

    inward_issue: LinkedIssue
    outward_issue: LinkedIssue
    type_: IssueLinkType
    comment: Comment | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.comment import Comment
        from ..models.issue_link_type import IssueLinkType
        from ..models.linked_issue import LinkedIssue
        inward_issue = self.inward_issue.to_dict()

        outward_issue = self.outward_issue.to_dict()

        type_ = self.type_.to_dict()

        comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "inwardIssue": inward_issue,
            "outwardIssue": outward_issue,
            "type": type_,
        })
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment import Comment
        from ..models.issue_link_type import IssueLinkType
        from ..models.linked_issue import LinkedIssue
        d = dict(src_dict)
        inward_issue = LinkedIssue.from_dict(d.pop("inwardIssue"))




        outward_issue = LinkedIssue.from_dict(d.pop("outwardIssue"))




        type_ = IssueLinkType.from_dict(d.pop("type"))




        _comment = d.pop("comment", UNSET)
        comment: Comment | Unset
        if isinstance(_comment,  Unset):
            comment = UNSET
        else:
            comment = Comment.from_dict(_comment)




        link_issue_request_json_bean = cls(
            inward_issue=inward_issue,
            outward_issue=outward_issue,
            type_=type_,
            comment=comment,
        )

        return link_issue_request_json_bean

