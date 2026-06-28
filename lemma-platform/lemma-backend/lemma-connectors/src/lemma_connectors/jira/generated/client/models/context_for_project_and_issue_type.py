from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ContextForProjectAndIssueType")



@_attrs_define
class ContextForProjectAndIssueType:
    """ The project and issue type mapping with a matching custom field context.

        Attributes:
            context_id (str): The ID of the custom field context.
            issue_type_id (str): The ID of the issue type.
            project_id (str): The ID of the project.
     """

    context_id: str
    issue_type_id: str
    project_id: str





    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        issue_type_id = self.issue_type_id

        project_id = self.project_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "contextId": context_id,
            "issueTypeId": issue_type_id,
            "projectId": project_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_id = d.pop("contextId")

        issue_type_id = d.pop("issueTypeId")

        project_id = d.pop("projectId")

        context_for_project_and_issue_type = cls(
            context_id=context_id,
            issue_type_id=issue_type_id,
            project_id=project_id,
        )

        return context_for_project_and_issue_type

