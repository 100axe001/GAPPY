from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.version_move_bean_position import VersionMoveBeanPosition
from ..types import UNSET, Unset






T = TypeVar("T", bound="VersionMoveBean")



@_attrs_define
class VersionMoveBean:
    """ 
        Attributes:
            after (str | Unset): The URL (self link) of the version after which to place the moved version. Cannot be used
                with `position`.
            position (VersionMoveBeanPosition | Unset): An absolute position in which to place the moved version. Cannot be
                used with `after`.
     """

    after: str | Unset = UNSET
    position: VersionMoveBeanPosition | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        after = self.after

        position: str | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if after is not UNSET:
            field_dict["after"] = after
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after = d.pop("after", UNSET)

        _position = d.pop("position", UNSET)
        position: VersionMoveBeanPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = VersionMoveBeanPosition(_position)




        version_move_bean = cls(
            after=after,
            position=position,
        )

        return version_move_bean

