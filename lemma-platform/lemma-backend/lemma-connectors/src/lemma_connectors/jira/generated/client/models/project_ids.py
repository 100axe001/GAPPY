from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ProjectIds")



@_attrs_define
class ProjectIds:
    """ A list of project IDs.

        Attributes:
            project_ids (list[str]): The IDs of projects.
     """

    project_ids: list[str]





    def to_dict(self) -> dict[str, Any]:
        project_ids = self.project_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "projectIds": project_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_ids = cast(list[str], d.pop("projectIds"))


        project_ids = cls(
            project_ids=project_ids,
        )

        return project_ids

