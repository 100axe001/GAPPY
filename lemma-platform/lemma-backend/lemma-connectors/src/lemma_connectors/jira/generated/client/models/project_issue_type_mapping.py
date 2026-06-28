from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ProjectIssueTypeMapping")



@_attrs_define
class ProjectIssueTypeMapping:
    """ The project and issue type mapping.

        Attributes:
            issue_type_id (str): The ID of the issue type.
            project_id (str): The ID of the project.
     """

    issue_type_id: str
    project_id: str





    def to_dict(self) -> dict[str, Any]:
        issue_type_id = self.issue_type_id

        project_id = self.project_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeId": issue_type_id,
            "projectId": project_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_id = d.pop("issueTypeId")

        project_id = d.pop("projectId")

        project_issue_type_mapping = cls(
            issue_type_id=issue_type_id,
            project_id=project_id,
        )

        return project_issue_type_mapping

