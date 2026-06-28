from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.issue_type_screen_scheme import IssueTypeScreenScheme





T = TypeVar("T", bound="IssueTypeScreenSchemesProjects")



@_attrs_define
class IssueTypeScreenSchemesProjects:
    """ Issue type screen scheme with a list of the projects that use it.

        Attributes:
            issue_type_screen_scheme (IssueTypeScreenScheme): Details of an issue type screen scheme.
            project_ids (list[str]): The IDs of the projects using the issue type screen scheme.
     """

    issue_type_screen_scheme: IssueTypeScreenScheme
    project_ids: list[str]





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_type_screen_scheme import IssueTypeScreenScheme
        issue_type_screen_scheme = self.issue_type_screen_scheme.to_dict()

        project_ids = self.project_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeScreenScheme": issue_type_screen_scheme,
            "projectIds": project_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_type_screen_scheme import IssueTypeScreenScheme
        d = dict(src_dict)
        issue_type_screen_scheme = IssueTypeScreenScheme.from_dict(d.pop("issueTypeScreenScheme"))




        project_ids = cast(list[str], d.pop("projectIds"))


        issue_type_screen_schemes_projects = cls(
            issue_type_screen_scheme=issue_type_screen_scheme,
            project_ids=project_ids,
        )

        return issue_type_screen_schemes_projects

