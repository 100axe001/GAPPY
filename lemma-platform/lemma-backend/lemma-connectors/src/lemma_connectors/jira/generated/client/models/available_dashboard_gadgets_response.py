from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.available_dashboard_gadget import AvailableDashboardGadget





T = TypeVar("T", bound="AvailableDashboardGadgetsResponse")



@_attrs_define
class AvailableDashboardGadgetsResponse:
    """ The list of available gadgets.

        Attributes:
            gadgets (list[AvailableDashboardGadget]): The list of available gadgets.
     """

    gadgets: list[AvailableDashboardGadget]





    def to_dict(self) -> dict[str, Any]:
        from ..models.available_dashboard_gadget import AvailableDashboardGadget
        gadgets = []
        for gadgets_item_data in self.gadgets:
            gadgets_item = gadgets_item_data.to_dict()
            gadgets.append(gadgets_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "gadgets": gadgets,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.available_dashboard_gadget import AvailableDashboardGadget
        d = dict(src_dict)
        gadgets = []
        _gadgets = d.pop("gadgets")
        for gadgets_item_data in (_gadgets):
            gadgets_item = AvailableDashboardGadget.from_dict(gadgets_item_data)



            gadgets.append(gadgets_item)


        available_dashboard_gadgets_response = cls(
            gadgets=gadgets,
        )

        return available_dashboard_gadgets_response

