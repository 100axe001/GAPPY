from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension





T = TypeVar("T", bound="Size")



@_attrs_define
class Size:
    """ A width and height.

        Attributes:
            height (Dimension | Unset): A magnitude in a single direction in the specified units.
            width (Dimension | Unset): A magnitude in a single direction in the specified units.
     """

    height: Dimension | Unset = UNSET
    width: Dimension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        height: dict[str, Any] | Unset = UNSET
        if not isinstance(self.height, Unset):
            height = self.height.to_dict()

        width: dict[str, Any] | Unset = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        d = dict(src_dict)
        _height = d.pop("height", UNSET)
        height: Dimension | Unset
        if isinstance(_height,  Unset):
            height = UNSET
        else:
            height = Dimension.from_dict(_height)




        _width = d.pop("width", UNSET)
        width: Dimension | Unset
        if isinstance(_width,  Unset):
            width = UNSET
        else:
            width = Dimension.from_dict(_width)




        size = cls(
            height=height,
            width=width,
        )


        size.additional_properties = d
        return size

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
