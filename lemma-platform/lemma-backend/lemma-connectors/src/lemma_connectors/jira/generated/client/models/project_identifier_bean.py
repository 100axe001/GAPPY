from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProjectIdentifierBean")



@_attrs_define
class ProjectIdentifierBean:
    """ The identifiers for a project.

        Attributes:
            id (int | Unset): The ID of the project.
            key (str | Unset): The key of the project.
     """

    id: int | Unset = UNSET
    key: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        project_identifier_bean = cls(
            id=id,
            key=key,
        )

        return project_identifier_bean

