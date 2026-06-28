from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueTypeScreenSchemeProjectAssociation")



@_attrs_define
class IssueTypeScreenSchemeProjectAssociation:
    """ Associated issue type screen scheme and project.

        Attributes:
            issue_type_screen_scheme_id (str | Unset): The ID of the issue type screen scheme.
            project_id (str | Unset): The ID of the project.
     """

    issue_type_screen_scheme_id: str | Unset = UNSET
    project_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        issue_type_screen_scheme_id = self.issue_type_screen_scheme_id

        project_id = self.project_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issue_type_screen_scheme_id is not UNSET:
            field_dict["issueTypeScreenSchemeId"] = issue_type_screen_scheme_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_screen_scheme_id = d.pop("issueTypeScreenSchemeId", UNSET)

        project_id = d.pop("projectId", UNSET)

        issue_type_screen_scheme_project_association = cls(
            issue_type_screen_scheme_id=issue_type_screen_scheme_id,
            project_id=project_id,
        )

        return issue_type_screen_scheme_project_association

