from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.screen_types import ScreenTypes





T = TypeVar("T", bound="ScreenSchemeDetails")



@_attrs_define
class ScreenSchemeDetails:
    """ Details of a screen scheme.

        Attributes:
            name (str): The name of the screen scheme. The name must be unique. The maximum length is 255 characters.
            screens (ScreenTypes): The IDs of the screens for the screen types of the screen scheme.
            description (str | Unset): The description of the screen scheme. The maximum length is 255 characters.
     """

    name: str
    screens: ScreenTypes
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.screen_types import ScreenTypes
        name = self.name

        screens = self.screens.to_dict()

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "screens": screens,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.screen_types import ScreenTypes
        d = dict(src_dict)
        name = d.pop("name")

        screens = ScreenTypes.from_dict(d.pop("screens"))




        description = d.pop("description", UNSET)

        screen_scheme_details = cls(
            name=name,
            screens=screens,
            description=description,
        )

        return screen_scheme_details

