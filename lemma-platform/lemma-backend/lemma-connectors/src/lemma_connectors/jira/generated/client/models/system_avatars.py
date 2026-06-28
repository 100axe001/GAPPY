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





T = TypeVar("T", bound="SystemAvatars")



@_attrs_define
class SystemAvatars:
    """ List of system avatars.

        Attributes:
            system (list[Avatar] | Unset): A list of avatar details.
     """

    system: list[Avatar] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.avatar import Avatar
        system: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.system, Unset):
            system = []
            for system_item_data in self.system:
                system_item = system_item_data.to_dict()
                system.append(system_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar import Avatar
        d = dict(src_dict)
        _system = d.pop("system", UNSET)
        system: list[Avatar] | Unset = UNSET
        if _system is not UNSET:
            system = []
            for system_item_data in _system:
                system_item = Avatar.from_dict(system_item_data)



                system.append(system_item)


        system_avatars = cls(
            system=system,
        )

        return system_avatars

