from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.suggested_issue import SuggestedIssue





T = TypeVar("T", bound="IssuePickerSuggestionsIssueType")



@_attrs_define
class IssuePickerSuggestionsIssueType:
    """ A type of issue suggested for use in auto-completion.

        Attributes:
            id (str | Unset): The ID of the type of issues suggested for use in auto-completion.
            issues (list[SuggestedIssue] | Unset): A list of issues suggested for use in auto-completion.
            label (str | Unset): The label of the type of issues suggested for use in auto-completion.
            msg (str | Unset): If no issue suggestions are found, returns a message indicating no suggestions were found,
            sub (str | Unset): If issue suggestions are found, returns a message indicating the number of issues suggestions
                found and returned.
     """

    id: str | Unset = UNSET
    issues: list[SuggestedIssue] | Unset = UNSET
    label: str | Unset = UNSET
    msg: str | Unset = UNSET
    sub: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.suggested_issue import SuggestedIssue
        id = self.id

        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)



        label = self.label

        msg = self.msg

        sub = self.sub


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if issues is not UNSET:
            field_dict["issues"] = issues
        if label is not UNSET:
            field_dict["label"] = label
        if msg is not UNSET:
            field_dict["msg"] = msg
        if sub is not UNSET:
            field_dict["sub"] = sub

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suggested_issue import SuggestedIssue
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _issues = d.pop("issues", UNSET)
        issues: list[SuggestedIssue] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = SuggestedIssue.from_dict(issues_item_data)



                issues.append(issues_item)


        label = d.pop("label", UNSET)

        msg = d.pop("msg", UNSET)

        sub = d.pop("sub", UNSET)

        issue_picker_suggestions_issue_type = cls(
            id=id,
            issues=issues,
            label=label,
            msg=msg,
            sub=sub,
        )

        return issue_picker_suggestions_issue_type

