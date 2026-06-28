from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.status_update_status_category import StatusUpdateStatusCategory
from ..types import UNSET, Unset






T = TypeVar("T", bound="StatusUpdate")



@_attrs_define
class StatusUpdate:
    """ Details of the status being updated.

        Attributes:
            id (str): The ID of the status.
            name (str): The name of the status.
            status_category (StatusUpdateStatusCategory): The category of the status.
            description (str | Unset): The description of the status.
     """

    id: str
    name: str
    status_category: StatusUpdateStatusCategory
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status_category = self.status_category.value

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "statusCategory": status_category,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status_category = StatusUpdateStatusCategory(d.pop("statusCategory"))




        description = d.pop("description", UNSET)

        status_update = cls(
            id=id,
            name=name,
            status_category=status_category,
            description=description,
        )

        return status_update

