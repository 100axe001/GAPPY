from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.positioned_object_positioning_layout import PositionedObjectPositioningLayout
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension





T = TypeVar("T", bound="PositionedObjectPositioning")



@_attrs_define
class PositionedObjectPositioning:
    """ The positioning of a PositionedObject. The positioned object is positioned relative to the beginning of the
    Paragraph it's tethered to.

        Attributes:
            layout (PositionedObjectPositioningLayout | Unset): The layout of this positioned object.
            left_offset (Dimension | Unset): A magnitude in a single direction in the specified units.
            top_offset (Dimension | Unset): A magnitude in a single direction in the specified units.
     """

    layout: PositionedObjectPositioningLayout | Unset = UNSET
    left_offset: Dimension | Unset = UNSET
    top_offset: Dimension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        layout: str | Unset = UNSET
        if not isinstance(self.layout, Unset):
            layout = self.layout.value


        left_offset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.left_offset, Unset):
            left_offset = self.left_offset.to_dict()

        top_offset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_offset, Unset):
            top_offset = self.top_offset.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if layout is not UNSET:
            field_dict["layout"] = layout
        if left_offset is not UNSET:
            field_dict["leftOffset"] = left_offset
        if top_offset is not UNSET:
            field_dict["topOffset"] = top_offset

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        d = dict(src_dict)
        _layout = d.pop("layout", UNSET)
        layout: PositionedObjectPositioningLayout | Unset
        if isinstance(_layout,  Unset):
            layout = UNSET
        else:
            layout = PositionedObjectPositioningLayout(_layout)




        _left_offset = d.pop("leftOffset", UNSET)
        left_offset: Dimension | Unset
        if isinstance(_left_offset,  Unset):
            left_offset = UNSET
        else:
            left_offset = Dimension.from_dict(_left_offset)




        _top_offset = d.pop("topOffset", UNSET)
        top_offset: Dimension | Unset
        if isinstance(_top_offset,  Unset):
            top_offset = UNSET
        else:
            top_offset = Dimension.from_dict(_top_offset)




        positioned_object_positioning = cls(
            layout=layout,
            left_offset=left_offset,
            top_offset=top_offset,
        )


        positioned_object_positioning.additional_properties = d
        return positioned_object_positioning

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
