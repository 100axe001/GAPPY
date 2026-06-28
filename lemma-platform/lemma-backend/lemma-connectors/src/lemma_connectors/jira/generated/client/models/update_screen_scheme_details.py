from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_screen_types import UpdateScreenTypes





T = TypeVar("T", bound="UpdateScreenSchemeDetails")



@_attrs_define
class UpdateScreenSchemeDetails:
    """ Details of a screen scheme.

        Attributes:
            description (str | Unset): The description of the screen scheme. The maximum length is 255 characters.
            name (str | Unset): The name of the screen scheme. The name must be unique. The maximum length is 255
                characters.
            screens (UpdateScreenTypes | Unset): The IDs of the screens for the screen types of the screen scheme.
     """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    screens: UpdateScreenTypes | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_screen_types import UpdateScreenTypes
        description = self.description

        name = self.name

        screens: dict[str, Any] | Unset = UNSET
        if not isinstance(self.screens, Unset):
            screens = self.screens.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if screens is not UNSET:
            field_dict["screens"] = screens

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_screen_types import UpdateScreenTypes
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _screens = d.pop("screens", UNSET)
        screens: UpdateScreenTypes | Unset
        if isinstance(_screens,  Unset):
            screens = UNSET
        else:
            screens = UpdateScreenTypes.from_dict(_screens)




        update_screen_scheme_details = cls(
            description=description,
            name=name,
            screens=screens,
        )

        return update_screen_scheme_details

