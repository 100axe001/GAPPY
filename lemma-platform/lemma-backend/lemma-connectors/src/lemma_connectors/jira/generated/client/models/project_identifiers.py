from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ProjectIdentifiers")



@_attrs_define
class ProjectIdentifiers:
    """ Identifiers for a project.

        Attributes:
            id (int): The ID of the created project.
            key (str): The key of the created project.
            self_ (str): The URL of the created project.
     """

    id: int
    key: str
    self_: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "key": key,
            "self": self_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        self_ = d.pop("self")

        project_identifiers = cls(
            id=id,
            key=key,
            self_=self_,
        )

        return project_identifiers

