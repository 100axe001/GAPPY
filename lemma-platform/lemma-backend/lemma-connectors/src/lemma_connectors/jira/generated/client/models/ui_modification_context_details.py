from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UiModificationContextDetails")



@_attrs_define
class UiModificationContextDetails:
    """ The details of a UI modification's context, which define where to activate the UI modification.

        Attributes:
            issue_type_id (str): The issue type ID of the context.
            project_id (str): The project ID of the context.
            view_type (str): The view type of the context. Only `GIC` (Global Issue Create) is supported.
            id (str | Unset): The ID of the UI modification context.
            is_available (bool | Unset): Whether a context is available. For example, when a project is deleted the context
                becomes unavailable.
     """

    issue_type_id: str
    project_id: str
    view_type: str
    id: str | Unset = UNSET
    is_available: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        issue_type_id = self.issue_type_id

        project_id = self.project_id

        view_type = self.view_type

        id = self.id

        is_available = self.is_available


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeId": issue_type_id,
            "projectId": project_id,
            "viewType": view_type,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_available is not UNSET:
            field_dict["isAvailable"] = is_available

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_id = d.pop("issueTypeId")

        project_id = d.pop("projectId")

        view_type = d.pop("viewType")

        id = d.pop("id", UNSET)

        is_available = d.pop("isAvailable", UNSET)

        ui_modification_context_details = cls(
            issue_type_id=issue_type_id,
            project_id=project_id,
            view_type=view_type,
            id=id,
            is_available=is_available,
        )

        return ui_modification_context_details

