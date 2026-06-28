from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Locale")



@_attrs_define
class Locale:
    r""" Details of a locale.

        Attributes:
            locale (str | Unset): The locale code. The Java the locale format is used: a two character language code (ISO
                639), an underscore, and two letter country code (ISO 3166). For example, en\_US represents a locale of English
                (United States). Required on create.
     """

    locale: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        locale = self.locale


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale", UNSET)

        locale = cls(
            locale=locale,
        )

        return locale

