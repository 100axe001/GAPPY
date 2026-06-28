from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.move_field_bean_position import MoveFieldBeanPosition
from ..types import UNSET, Unset






T = TypeVar("T", bound="MoveFieldBean")



@_attrs_define
class MoveFieldBean:
    """ 
        Attributes:
            after (str | Unset): The ID of the screen tab field after which to place the moved screen tab field. Required if
                `position` isn't provided.
            position (MoveFieldBeanPosition | Unset): The named position to which the screen tab field should be moved.
                Required if `after` isn't provided.
     """

    after: str | Unset = UNSET
    position: MoveFieldBeanPosition | Unset = UNSET





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
        position: MoveFieldBeanPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = MoveFieldBeanPosition(_position)




        move_field_bean = cls(
            after=after,
            position=position,
        )

        return move_field_bean

