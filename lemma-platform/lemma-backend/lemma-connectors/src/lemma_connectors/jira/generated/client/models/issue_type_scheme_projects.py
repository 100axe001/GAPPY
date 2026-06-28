from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.issue_type_scheme import IssueTypeScheme





T = TypeVar("T", bound="IssueTypeSchemeProjects")



@_attrs_define
class IssueTypeSchemeProjects:
    """ Issue type scheme with a list of the projects that use it.

        Attributes:
            issue_type_scheme (IssueTypeScheme): Details of an issue type scheme.
            project_ids (list[str]): The IDs of the projects using the issue type scheme.
     """

    issue_type_scheme: IssueTypeScheme
    project_ids: list[str]





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_type_scheme import IssueTypeScheme
        issue_type_scheme = self.issue_type_scheme.to_dict()

        project_ids = self.project_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeScheme": issue_type_scheme,
            "projectIds": project_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_type_scheme import IssueTypeScheme
        d = dict(src_dict)
        issue_type_scheme = IssueTypeScheme.from_dict(d.pop("issueTypeScheme"))




        project_ids = cast(list[str], d.pop("projectIds"))


        issue_type_scheme_projects = cls(
            issue_type_scheme=issue_type_scheme,
            project_ids=project_ids,
        )

        return issue_type_scheme_projects

