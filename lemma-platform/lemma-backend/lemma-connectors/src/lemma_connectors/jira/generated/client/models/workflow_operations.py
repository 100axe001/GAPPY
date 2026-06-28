from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="WorkflowOperations")



@_attrs_define
class WorkflowOperations:
    """ Operations allowed on a workflow

        Attributes:
            can_delete (bool): Whether the workflow can be deleted.
            can_edit (bool): Whether the workflow can be updated.
     """

    can_delete: bool
    can_edit: bool





    def to_dict(self) -> dict[str, Any]:
        can_delete = self.can_delete

        can_edit = self.can_edit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "canDelete": can_delete,
            "canEdit": can_edit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_delete = d.pop("canDelete")

        can_edit = d.pop("canEdit")

        workflow_operations = cls(
            can_delete=can_delete,
            can_edit=can_edit,
        )

        return workflow_operations

