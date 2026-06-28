from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueTypeToContextMapping")



@_attrs_define
class IssueTypeToContextMapping:
    """ Mapping of an issue type to a context.

        Attributes:
            context_id (str): The ID of the context.
            is_any_issue_type (bool | Unset): Whether the context is mapped to any issue type.
            issue_type_id (str | Unset): The ID of the issue type.
     """

    context_id: str
    is_any_issue_type: bool | Unset = UNSET
    issue_type_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        is_any_issue_type = self.is_any_issue_type

        issue_type_id = self.issue_type_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "contextId": context_id,
        })
        if is_any_issue_type is not UNSET:
            field_dict["isAnyIssueType"] = is_any_issue_type
        if issue_type_id is not UNSET:
            field_dict["issueTypeId"] = issue_type_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_id = d.pop("contextId")

        is_any_issue_type = d.pop("isAnyIssueType", UNSET)

        issue_type_id = d.pop("issueTypeId", UNSET)

        issue_type_to_context_mapping = cls(
            context_id=context_id,
            is_any_issue_type=is_any_issue_type,
            issue_type_id=issue_type_id,
        )

        return issue_type_to_context_mapping

