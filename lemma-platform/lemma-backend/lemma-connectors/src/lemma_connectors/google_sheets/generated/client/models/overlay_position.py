from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.grid_coordinate import GridCoordinate





T = TypeVar("T", bound="OverlayPosition")



@_attrs_define
class OverlayPosition:
    """ The location an object is overlaid on top of a grid.

        Attributes:
            anchor_cell (GridCoordinate | Unset): A coordinate in a sheet. All indexes are zero-based.
            height_pixels (int | Unset): The height of the object, in pixels. Defaults to 371.
            offset_x_pixels (int | Unset): The horizontal offset, in pixels, that the object is offset from the anchor cell.
            offset_y_pixels (int | Unset): The vertical offset, in pixels, that the object is offset from the anchor cell.
            width_pixels (int | Unset): The width of the object, in pixels. Defaults to 600.
     """

    anchor_cell: GridCoordinate | Unset = UNSET
    height_pixels: int | Unset = UNSET
    offset_x_pixels: int | Unset = UNSET
    offset_y_pixels: int | Unset = UNSET
    width_pixels: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_coordinate import GridCoordinate
        anchor_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.anchor_cell, Unset):
            anchor_cell = self.anchor_cell.to_dict()

        height_pixels = self.height_pixels

        offset_x_pixels = self.offset_x_pixels

        offset_y_pixels = self.offset_y_pixels

        width_pixels = self.width_pixels


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if anchor_cell is not UNSET:
            field_dict["anchorCell"] = anchor_cell
        if height_pixels is not UNSET:
            field_dict["heightPixels"] = height_pixels
        if offset_x_pixels is not UNSET:
            field_dict["offsetXPixels"] = offset_x_pixels
        if offset_y_pixels is not UNSET:
            field_dict["offsetYPixels"] = offset_y_pixels
        if width_pixels is not UNSET:
            field_dict["widthPixels"] = width_pixels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_coordinate import GridCoordinate
        d = dict(src_dict)
        _anchor_cell = d.pop("anchorCell", UNSET)
        anchor_cell: GridCoordinate | Unset
        if isinstance(_anchor_cell,  Unset):
            anchor_cell = UNSET
        else:
            anchor_cell = GridCoordinate.from_dict(_anchor_cell)




        height_pixels = d.pop("heightPixels", UNSET)

        offset_x_pixels = d.pop("offsetXPixels", UNSET)

        offset_y_pixels = d.pop("offsetYPixels", UNSET)

        width_pixels = d.pop("widthPixels", UNSET)

        overlay_position = cls(
            anchor_cell=anchor_cell,
            height_pixels=height_pixels,
            offset_x_pixels=offset_x_pixels,
            offset_y_pixels=offset_y_pixels,
            width_pixels=width_pixels,
        )


        overlay_position.additional_properties = d
        return overlay_position

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
