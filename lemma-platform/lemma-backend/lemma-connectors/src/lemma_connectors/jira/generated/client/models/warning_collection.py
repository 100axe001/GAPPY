from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WarningCollection")



@_attrs_define
class WarningCollection:
    """ 
        Attributes:
            warnings (list[str] | Unset):
     """

    warnings: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        warnings = cast(list[str], d.pop("warnings", UNSET))


        warning_collection = cls(
            warnings=warnings,
        )

        return warning_collection

