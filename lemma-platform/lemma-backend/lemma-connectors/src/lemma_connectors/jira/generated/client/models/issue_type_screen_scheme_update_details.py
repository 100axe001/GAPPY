from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueTypeScreenSchemeUpdateDetails")



@_attrs_define
class IssueTypeScreenSchemeUpdateDetails:
    """ Details of an issue type screen scheme.

        Attributes:
            description (str | Unset): The description of the issue type screen scheme. The maximum length is 255
                characters.
            name (str | Unset): The name of the issue type screen scheme. The name must be unique. The maximum length is 255
                characters.
     """

    description: str | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        issue_type_screen_scheme_update_details = cls(
            description=description,
            name=name,
        )

        return issue_type_screen_scheme_update_details

