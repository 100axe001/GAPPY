from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CreateWorkflowTransitionScreenDetails")



@_attrs_define
class CreateWorkflowTransitionScreenDetails:
    """ The details of a transition screen.

        Attributes:
            id (str): The ID of the screen.
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

        create_workflow_transition_screen_details = cls(
            id=id,
        )

        return create_workflow_transition_screen_details

