from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ScreenTypes")



@_attrs_define
class ScreenTypes:
    """ The IDs of the screens for the screen types of the screen scheme.

        Attributes:
            create (int | Unset): The ID of the create screen.
            default (int | Unset): The ID of the default screen. Required when creating a screen scheme.
            edit (int | Unset): The ID of the edit screen.
            view (int | Unset): The ID of the view screen.
     """

    create: int | Unset = UNSET
    default: int | Unset = UNSET
    edit: int | Unset = UNSET
    view: int | Unset = UNSET





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

        screen_types = cls(
            create=create,
            default=default,
            edit=edit,
            view=view,
        )

        return screen_types

