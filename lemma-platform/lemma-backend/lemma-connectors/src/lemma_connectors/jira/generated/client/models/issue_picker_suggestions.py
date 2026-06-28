from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_picker_suggestions_issue_type import IssuePickerSuggestionsIssueType





T = TypeVar("T", bound="IssuePickerSuggestions")



@_attrs_define
class IssuePickerSuggestions:
    """ A list of issues suggested for use in auto-completion.

        Attributes:
            sections (list[IssuePickerSuggestionsIssueType] | Unset): A list of issues for an issue type suggested for use
                in auto-completion.
     """

    sections: list[IssuePickerSuggestionsIssueType] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_picker_suggestions_issue_type import IssuePickerSuggestionsIssueType
        sections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()
                sections.append(sections_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if sections is not UNSET:
            field_dict["sections"] = sections

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_picker_suggestions_issue_type import IssuePickerSuggestionsIssueType
        d = dict(src_dict)
        _sections = d.pop("sections", UNSET)
        sections: list[IssuePickerSuggestionsIssueType] | Unset = UNSET
        if _sections is not UNSET:
            sections = []
            for sections_item_data in _sections:
                sections_item = IssuePickerSuggestionsIssueType.from_dict(sections_item_data)



                sections.append(sections_item)


        issue_picker_suggestions = cls(
            sections=sections,
        )

        return issue_picker_suggestions

