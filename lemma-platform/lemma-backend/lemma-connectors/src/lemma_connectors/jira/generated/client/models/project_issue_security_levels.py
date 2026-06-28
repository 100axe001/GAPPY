from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.security_level import SecurityLevel





T = TypeVar("T", bound="ProjectIssueSecurityLevels")



@_attrs_define
class ProjectIssueSecurityLevels:
    """ List of issue level security items in a project.

        Attributes:
            levels (list[SecurityLevel]): Issue level security items list.
     """

    levels: list[SecurityLevel]





    def to_dict(self) -> dict[str, Any]:
        from ..models.security_level import SecurityLevel
        levels = []
        for levels_item_data in self.levels:
            levels_item = levels_item_data.to_dict()
            levels.append(levels_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "levels": levels,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.security_level import SecurityLevel
        d = dict(src_dict)
        levels = []
        _levels = d.pop("levels")
        for levels_item_data in (_levels):
            levels_item = SecurityLevel.from_dict(levels_item_data)



            levels.append(levels_item)


        project_issue_security_levels = cls(
            levels=levels,
        )

        return project_issue_security_levels

