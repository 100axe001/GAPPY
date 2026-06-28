from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.overlay_position import OverlayPosition





T = TypeVar("T", bound="EmbeddedObjectPosition")



@_attrs_define
class EmbeddedObjectPosition:
    """ The position of an embedded object such as a chart.

        Attributes:
            new_sheet (bool | Unset): If true, the embedded object is put on a new sheet whose ID is chosen for you. Used
                only when writing.
            overlay_position (OverlayPosition | Unset): The location an object is overlaid on top of a grid.
            sheet_id (int | Unset): The sheet this is on. Set only if the embedded object is on its own sheet. Must be non-
                negative.
     """

    new_sheet: bool | Unset = UNSET
    overlay_position: OverlayPosition | Unset = UNSET
    sheet_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.overlay_position import OverlayPosition
        new_sheet = self.new_sheet

        overlay_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overlay_position, Unset):
            overlay_position = self.overlay_position.to_dict()

        sheet_id = self.sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if new_sheet is not UNSET:
            field_dict["newSheet"] = new_sheet
        if overlay_position is not UNSET:
            field_dict["overlayPosition"] = overlay_position
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.overlay_position import OverlayPosition
        d = dict(src_dict)
        new_sheet = d.pop("newSheet", UNSET)

        _overlay_position = d.pop("overlayPosition", UNSET)
        overlay_position: OverlayPosition | Unset
        if isinstance(_overlay_position,  Unset):
            overlay_position = UNSET
        else:
            overlay_position = OverlayPosition.from_dict(_overlay_position)




        sheet_id = d.pop("sheetId", UNSET)

        embedded_object_position = cls(
            new_sheet=new_sheet,
            overlay_position=overlay_position,
            sheet_id=sheet_id,
        )


        embedded_object_position.additional_properties = d
        return embedded_object_position

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
