from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="WorkflowId")



@_attrs_define
class WorkflowId:
    """ Properties that identify a workflow.

        Attributes:
            draft (bool): Whether the workflow is in the draft state.
            name (str): The name of the workflow.
     """

    draft: bool
    name: str





    def to_dict(self) -> dict[str, Any]:
        draft = self.draft

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "draft": draft,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        draft = d.pop("draft")

        name = d.pop("name")

        workflow_id = cls(
            draft=draft,
            name=name,
        )

        return workflow_id

