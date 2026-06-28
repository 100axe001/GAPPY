from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dashboard_gadget_color import DashboardGadgetColor
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dashboard_gadget_position import DashboardGadgetPosition





T = TypeVar("T", bound="DashboardGadget")



@_attrs_define
class DashboardGadget:
    """ Details of a gadget.

        Attributes:
            color (DashboardGadgetColor): The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`,
                `cyan`, `purple`, `gray`, or `white`.
            id (int): The ID of the gadget instance.
            position (DashboardGadgetPosition): Details of a gadget position.
            title (str): The title of the gadget.
            module_key (str | Unset): The module key of the gadget type.
            uri (str | Unset): The URI of the gadget type.
     """

    color: DashboardGadgetColor
    id: int
    position: DashboardGadgetPosition
    title: str
    module_key: str | Unset = UNSET
    uri: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_gadget_position import DashboardGadgetPosition
        color = self.color.value

        id = self.id

        position = self.position.to_dict()

        title = self.title

        module_key = self.module_key

        uri = self.uri


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "color": color,
            "id": id,
            "position": position,
            "title": title,
        })
        if module_key is not UNSET:
            field_dict["moduleKey"] = module_key
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_gadget_position import DashboardGadgetPosition
        d = dict(src_dict)
        color = DashboardGadgetColor(d.pop("color"))




        id = d.pop("id")

        position = DashboardGadgetPosition.from_dict(d.pop("position"))




        title = d.pop("title")

        module_key = d.pop("moduleKey", UNSET)

        uri = d.pop("uri", UNSET)

        dashboard_gadget = cls(
            color=color,
            id=id,
            position=position,
            title=title,
            module_key=module_key,
            uri=uri,
        )

        return dashboard_gadget

