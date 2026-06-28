from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AvailableDashboardGadget")



@_attrs_define
class AvailableDashboardGadget:
    """ The details of the available dashboard gadget.

        Attributes:
            title (str): The title of the gadget.
            module_key (str | Unset): The module key of the gadget type.
            uri (str | Unset): The URI of the gadget type.
     """

    title: str
    module_key: str | Unset = UNSET
    uri: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        module_key = self.module_key

        uri = self.uri


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "title": title,
        })
        if module_key is not UNSET:
            field_dict["moduleKey"] = module_key
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        module_key = d.pop("moduleKey", UNSET)

        uri = d.pop("uri", UNSET)

        available_dashboard_gadget = cls(
            title=title,
            module_key=module_key,
            uri=uri,
        )

        return available_dashboard_gadget

