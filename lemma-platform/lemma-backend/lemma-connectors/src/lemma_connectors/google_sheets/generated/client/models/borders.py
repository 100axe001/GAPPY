from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.border import Border





T = TypeVar("T", bound="Borders")



@_attrs_define
class Borders:
    """ The borders of the cell.

        Attributes:
            bottom (Border | Unset): A border along a cell.
            left (Border | Unset): A border along a cell.
            right (Border | Unset): A border along a cell.
            top (Border | Unset): A border along a cell.
     """

    bottom: Border | Unset = UNSET
    left: Border | Unset = UNSET
    right: Border | Unset = UNSET
    top: Border | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.border import Border
        bottom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bottom, Unset):
            bottom = self.bottom.to_dict()

        left: dict[str, Any] | Unset = UNSET
        if not isinstance(self.left, Unset):
            left = self.left.to_dict()

        right: dict[str, Any] | Unset = UNSET
        if not isinstance(self.right, Unset):
            right = self.right.to_dict()

        top: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top, Unset):
            top = self.top.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bottom is not UNSET:
            field_dict["bottom"] = bottom
        if left is not UNSET:
            field_dict["left"] = left
        if right is not UNSET:
            field_dict["right"] = right
        if top is not UNSET:
            field_dict["top"] = top

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.border import Border
        d = dict(src_dict)
        _bottom = d.pop("bottom", UNSET)
        bottom: Border | Unset
        if isinstance(_bottom,  Unset):
            bottom = UNSET
        else:
            bottom = Border.from_dict(_bottom)




        _left = d.pop("left", UNSET)
        left: Border | Unset
        if isinstance(_left,  Unset):
            left = UNSET
        else:
            left = Border.from_dict(_left)




        _right = d.pop("right", UNSET)
        right: Border | Unset
        if isinstance(_right,  Unset):
            right = UNSET
        else:
            right = Border.from_dict(_right)




        _top = d.pop("top", UNSET)
        top: Border | Unset
        if isinstance(_top,  Unset):
            top = UNSET
        else:
            top = Border.from_dict(_top)




        borders = cls(
            bottom=bottom,
            left=left,
            right=right,
            top=top,
        )


        borders.additional_properties = d
        return borders

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
