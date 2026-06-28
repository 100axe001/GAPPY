from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="WorkflowSchemeIdName")



@_attrs_define
class WorkflowSchemeIdName:
    """ The ID and the name of the workflow scheme.

        Attributes:
            id (str): The ID of the workflow scheme.
            name (str): The name of the workflow scheme.
     """

    id: str
    name: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        workflow_scheme_id_name = cls(
            id=id,
            name=name,
        )

        return workflow_scheme_id_name

