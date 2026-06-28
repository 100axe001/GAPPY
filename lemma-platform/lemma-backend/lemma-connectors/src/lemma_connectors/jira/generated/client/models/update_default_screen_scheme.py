from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpdateDefaultScreenScheme")



@_attrs_define
class UpdateDefaultScreenScheme:
    """ The ID of a screen scheme.

        Attributes:
            screen_scheme_id (str): The ID of the screen scheme.
     """

    screen_scheme_id: str





    def to_dict(self) -> dict[str, Any]:
        screen_scheme_id = self.screen_scheme_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "screenSchemeId": screen_scheme_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        screen_scheme_id = d.pop("screenSchemeId")

        update_default_screen_scheme = cls(
            screen_scheme_id=screen_scheme_id,
        )

        return update_default_screen_scheme

