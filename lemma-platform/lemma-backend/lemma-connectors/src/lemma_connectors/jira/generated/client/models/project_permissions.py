from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProjectPermissions")



@_attrs_define
class ProjectPermissions:
    """ Permissions which a user has on a project.

        Attributes:
            can_edit (bool | Unset): Whether the logged user can edit the project.
     """

    can_edit: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        can_edit = self.can_edit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if can_edit is not UNSET:
            field_dict["canEdit"] = can_edit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_edit = d.pop("canEdit", UNSET)

        project_permissions = cls(
            can_edit=can_edit,
        )

        return project_permissions

