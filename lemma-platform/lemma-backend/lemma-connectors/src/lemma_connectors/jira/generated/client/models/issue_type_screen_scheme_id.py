from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IssueTypeScreenSchemeId")



@_attrs_define
class IssueTypeScreenSchemeId:
    """ The ID of an issue type screen scheme.

        Attributes:
            id (str): The ID of the issue type screen scheme.
     """

    id: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        issue_type_screen_scheme_id = cls(
            id=id,
        )

        return issue_type_screen_scheme_id

