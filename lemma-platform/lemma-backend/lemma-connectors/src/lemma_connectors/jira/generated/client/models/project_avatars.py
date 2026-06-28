from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.avatar import Avatar





T = TypeVar("T", bound="ProjectAvatars")



@_attrs_define
class ProjectAvatars:
    """ List of project avatars.

        Attributes:
            custom (list[Avatar] | Unset): List of avatars added to Jira. These avatars may be deleted.
            system (list[Avatar] | Unset): List of avatars included with Jira. These avatars cannot be deleted.
     """

    custom: list[Avatar] | Unset = UNSET
    system: list[Avatar] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.avatar import Avatar
        custom: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom, Unset):
            custom = []
            for custom_item_data in self.custom:
                custom_item = custom_item_data.to_dict()
                custom.append(custom_item)



        system: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.system, Unset):
            system = []
            for system_item_data in self.system:
                system_item = system_item_data.to_dict()
                system.append(system_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if custom is not UNSET:
            field_dict["custom"] = custom
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar import Avatar
        d = dict(src_dict)
        _custom = d.pop("custom", UNSET)
        custom: list[Avatar] | Unset = UNSET
        if _custom is not UNSET:
            custom = []
            for custom_item_data in _custom:
                custom_item = Avatar.from_dict(custom_item_data)



                custom.append(custom_item)


        _system = d.pop("system", UNSET)
        system: list[Avatar] | Unset = UNSET
        if _system is not UNSET:
            system = []
            for system_item_data in _system:
                system_item = Avatar.from_dict(system_item_data)



                system.append(system_item)


        project_avatars = cls(
            custom=custom,
            system=system,
        )

        return project_avatars

