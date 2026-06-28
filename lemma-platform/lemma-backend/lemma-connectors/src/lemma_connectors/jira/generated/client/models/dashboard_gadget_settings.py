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





T = TypeVar("T", bound="DashboardGadgetSettings")



@_attrs_define
class DashboardGadgetSettings:
    """ Details of the settings for a dashboard gadget.

        Attributes:
            color (str | Unset): The color of the gadget. Should be one of `blue`, `red`, `yellow`, `green`, `cyan`,
                `purple`, `gray`, or `white`.
            ignore_uri_and_module_key_validation (bool | Unset): Whether to ignore the validation of module key and URI. For
                example, when a gadget is created that is a part of an application that isn't installed.
            module_key (str | Unset): The module key of the gadget type. Can't be provided with `uri`.
            position (DashboardGadgetPosition | Unset): Details of a gadget position.
            title (str | Unset): The title of the gadget.
            uri (str | Unset): The URI of the gadget type. Can't be provided with `moduleKey`.
     """

    color: str | Unset = UNSET
    ignore_uri_and_module_key_validation: bool | Unset = UNSET
    module_key: str | Unset = UNSET
    position: DashboardGadgetPosition | Unset = UNSET
    title: str | Unset = UNSET
    uri: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_gadget_position import DashboardGadgetPosition
        color = self.color

        ignore_uri_and_module_key_validation = self.ignore_uri_and_module_key_validation

        module_key = self.module_key

        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        title = self.title

        uri = self.uri


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if ignore_uri_and_module_key_validation is not UNSET:
            field_dict["ignoreUriAndModuleKeyValidation"] = ignore_uri_and_module_key_validation
        if module_key is not UNSET:
            field_dict["moduleKey"] = module_key
        if position is not UNSET:
            field_dict["position"] = position
        if title is not UNSET:
            field_dict["title"] = title
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_gadget_position import DashboardGadgetPosition
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        ignore_uri_and_module_key_validation = d.pop("ignoreUriAndModuleKeyValidation", UNSET)

        module_key = d.pop("moduleKey", UNSET)

        _position = d.pop("position", UNSET)
        position: DashboardGadgetPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = DashboardGadgetPosition.from_dict(_position)




        title = d.pop("title", UNSET)

        uri = d.pop("uri", UNSET)

        dashboard_gadget_settings = cls(
            color=color,
            ignore_uri_and_module_key_validation=ignore_uri_and_module_key_validation,
            module_key=module_key,
            position=position,
            title=title,
            uri=uri,
        )

        return dashboard_gadget_settings

