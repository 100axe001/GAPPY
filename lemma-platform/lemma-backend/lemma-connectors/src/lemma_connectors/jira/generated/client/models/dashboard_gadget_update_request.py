from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dashboard_gadget_position import DashboardGadgetPosition





T = TypeVar("T", bound="DashboardGadgetUpdateRequest")



@_attrs_define
class DashboardGadgetUpdateRequest:
    """ The details of the gadget to update.

        Attributes:
            color (str | Unset): The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`,
                `purple`, `gray`, or `white`.
            position (DashboardGadgetPosition | Unset): Details of a gadget position.
            title (str | Unset): The title of the gadget.
     """

    color: str | Unset = UNSET
    position: DashboardGadgetPosition | Unset = UNSET
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_gadget_position import DashboardGadgetPosition
        color = self.color

        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if position is not UNSET:
            field_dict["position"] = position
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_gadget_position import DashboardGadgetPosition
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        _position = d.pop("position", UNSET)
        position: DashboardGadgetPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = DashboardGadgetPosition.from_dict(_position)




        title = d.pop("title", UNSET)

        dashboard_gadget_update_request = cls(
            color=color,
            position=position,
            title=title,
        )

        return dashboard_gadget_update_request

