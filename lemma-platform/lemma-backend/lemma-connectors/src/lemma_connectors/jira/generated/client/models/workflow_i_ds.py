from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WorkflowIDs")



@_attrs_define
class WorkflowIDs:
    """ The classic workflow identifiers.

        Attributes:
            name (str): The name of the workflow.
            entity_id (str | Unset): The entity ID of the workflow.
     """

    name: str
    entity_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        entity_id = self.entity_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        entity_id = d.pop("entityId", UNSET)

        workflow_i_ds = cls(
            name=name,
            entity_id=entity_id,
        )

        return workflow_i_ds

