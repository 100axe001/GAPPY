from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DashboardGadgetPosition")



@_attrs_define
class DashboardGadgetPosition:
    """ Details of a gadget position.

        Attributes:
            the_column_position_of_the_gadget (int):
            the_row_position_of_the_gadget (int):
     """

    the_column_position_of_the_gadget: int
    the_row_position_of_the_gadget: int





    def to_dict(self) -> dict[str, Any]:
        the_column_position_of_the_gadget = self.the_column_position_of_the_gadget

        the_row_position_of_the_gadget = self.the_row_position_of_the_gadget


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "The column position of the gadget.": the_column_position_of_the_gadget,
            "The row position of the gadget.": the_row_position_of_the_gadget,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        the_column_position_of_the_gadget = d.pop("The column position of the gadget.")

        the_row_position_of_the_gadget = d.pop("The row position of the gadget.")

        dashboard_gadget_position = cls(
            the_column_position_of_the_gadget=the_column_position_of_the_gadget,
            the_row_position_of_the_gadget=the_row_position_of_the_gadget,
        )

        return dashboard_gadget_position

