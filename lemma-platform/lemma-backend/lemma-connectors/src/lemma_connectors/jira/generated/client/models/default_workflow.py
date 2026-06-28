from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DefaultWorkflow")



@_attrs_define
class DefaultWorkflow:
    """ Details about the default workflow.

        Attributes:
            workflow (str): The name of the workflow to set as the default workflow.
            update_draft_if_needed (bool | Unset): Whether a draft workflow scheme is created or updated when updating an
                active workflow scheme. The draft is updated with the new default workflow. Defaults to `false`.
     """

    workflow: str
    update_draft_if_needed: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        workflow = self.workflow

        update_draft_if_needed = self.update_draft_if_needed


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "workflow": workflow,
        })
        if update_draft_if_needed is not UNSET:
            field_dict["updateDraftIfNeeded"] = update_draft_if_needed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workflow = d.pop("workflow")

        update_draft_if_needed = d.pop("updateDraftIfNeeded", UNSET)

        default_workflow = cls(
            workflow=workflow,
            update_draft_if_needed=update_draft_if_needed,
        )

        return default_workflow

