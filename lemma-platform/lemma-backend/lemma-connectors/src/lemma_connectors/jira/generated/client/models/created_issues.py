from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_operation_error_result import BulkOperationErrorResult
  from ..models.created_issue import CreatedIssue





T = TypeVar("T", bound="CreatedIssues")



@_attrs_define
class CreatedIssues:
    """ Details about the issues created and the errors for requests that failed.

        Attributes:
            errors (list[BulkOperationErrorResult] | Unset): Error details for failed issue creation requests.
            issues (list[CreatedIssue] | Unset): Details of the issues created.
     """

    errors: list[BulkOperationErrorResult] | Unset = UNSET
    issues: list[CreatedIssue] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_operation_error_result import BulkOperationErrorResult
        from ..models.created_issue import CreatedIssue
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if errors is not UNSET:
            field_dict["errors"] = errors
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_operation_error_result import BulkOperationErrorResult
        from ..models.created_issue import CreatedIssue
        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[BulkOperationErrorResult] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BulkOperationErrorResult.from_dict(errors_item_data)



                errors.append(errors_item)


        _issues = d.pop("issues", UNSET)
        issues: list[CreatedIssue] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = CreatedIssue.from_dict(issues_item_data)



                issues.append(issues_item)


        created_issues = cls(
            errors=errors,
            issues=issues,
        )

        return created_issues

