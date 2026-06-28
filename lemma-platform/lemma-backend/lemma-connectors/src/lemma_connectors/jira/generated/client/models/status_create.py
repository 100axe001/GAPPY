from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.status_create_status_category import StatusCreateStatusCategory
from ..types import UNSET, Unset






T = TypeVar("T", bound="StatusCreate")



@_attrs_define
class StatusCreate:
    """ Details of the status being created.

        Attributes:
            name (str): The name of the status.
            status_category (StatusCreateStatusCategory): The category of the status.
            description (str | Unset): The description of the status.
     """

    name: str
    status_category: StatusCreateStatusCategory
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status_category = self.status_category.value

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "statusCategory": status_category,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        status_category = StatusCreateStatusCategory(d.pop("statusCategory"))




        description = d.pop("description", UNSET)

        status_create = cls(
            name=name,
            status_category=status_category,
            description=description,
        )

        return status_create

