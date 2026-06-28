from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UiModificationIdentifiers")



@_attrs_define
class UiModificationIdentifiers:
    """ Identifiers for a UI modification.

        Attributes:
            id (str): The ID of the UI modification.
            self_ (str): The URL of the UI modification.
     """

    id: str
    self_: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "self": self_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        self_ = d.pop("self")

        ui_modification_identifiers = cls(
            id=id,
            self_=self_,
        )

        return ui_modification_identifiers

