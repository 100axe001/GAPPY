from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateScreenTypes")



@_attrs_define
class UpdateScreenTypes:
    """ The IDs of the screens for the screen types of the screen scheme.

        Attributes:
            create (str | Unset): The ID of the create screen. To remove the screen association, pass a null.
            default (str | Unset): The ID of the default screen. When specified, must include a screen ID as a default
                screen is required.
            edit (str | Unset): The ID of the edit screen. To remove the screen association, pass a null.
            view (str | Unset): The ID of the view screen. To remove the screen association, pass a null.
     """

    create: str | Unset = UNSET
    default: str | Unset = UNSET
    edit: str | Unset = UNSET
    view: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        create = self.create

        default = self.default

        edit = self.edit

        view = self.view


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if create is not UNSET:
            field_dict["create"] = create
        if default is not UNSET:
            field_dict["default"] = default
        if edit is not UNSET:
            field_dict["edit"] = edit
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create = d.pop("create", UNSET)

        default = d.pop("default", UNSET)

        edit = d.pop("edit", UNSET)

        view = d.pop("view", UNSET)

        update_screen_types = cls(
            create=create,
            default=default,
            edit=edit,
            view=view,
        )

        return update_screen_types

