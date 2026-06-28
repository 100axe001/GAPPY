from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.simple_error_collection import SimpleErrorCollection





T = TypeVar("T", bound="RemoveOptionFromIssuesResult")



@_attrs_define
class RemoveOptionFromIssuesResult:
    """ 
        Attributes:
            errors (SimpleErrorCollection | Unset):
            modified_issues (list[int] | Unset): The IDs of the modified issues.
            unmodified_issues (list[int] | Unset): The IDs of the unchanged issues, those issues where errors prevent
                modification.
     """

    errors: SimpleErrorCollection | Unset = UNSET
    modified_issues: list[int] | Unset = UNSET
    unmodified_issues: list[int] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_error_collection import SimpleErrorCollection
        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        modified_issues: list[int] | Unset = UNSET
        if not isinstance(self.modified_issues, Unset):
            modified_issues = self.modified_issues



        unmodified_issues: list[int] | Unset = UNSET
        if not isinstance(self.unmodified_issues, Unset):
            unmodified_issues = self.unmodified_issues




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if errors is not UNSET:
            field_dict["errors"] = errors
        if modified_issues is not UNSET:
            field_dict["modifiedIssues"] = modified_issues
        if unmodified_issues is not UNSET:
            field_dict["unmodifiedIssues"] = unmodified_issues

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_error_collection import SimpleErrorCollection
        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: SimpleErrorCollection | Unset
        if isinstance(_errors,  Unset):
            errors = UNSET
        else:
            errors = SimpleErrorCollection.from_dict(_errors)




        modified_issues = cast(list[int], d.pop("modifiedIssues", UNSET))


        unmodified_issues = cast(list[int], d.pop("unmodifiedIssues", UNSET))


        remove_option_from_issues_result = cls(
            errors=errors,
            modified_issues=modified_issues,
            unmodified_issues=unmodified_issues,
        )

        return remove_option_from_issues_result

