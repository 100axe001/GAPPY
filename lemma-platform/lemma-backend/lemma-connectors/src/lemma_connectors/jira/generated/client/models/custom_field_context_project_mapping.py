from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldContextProjectMapping")



@_attrs_define
class CustomFieldContextProjectMapping:
    """ Details of a context to project association.

        Attributes:
            context_id (str): The ID of the context.
            is_global_context (bool | Unset): Whether context is global.
            project_id (str | Unset): The ID of the project.
     """

    context_id: str
    is_global_context: bool | Unset = UNSET
    project_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        is_global_context = self.is_global_context

        project_id = self.project_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "contextId": context_id,
        })
        if is_global_context is not UNSET:
            field_dict["isGlobalContext"] = is_global_context
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_id = d.pop("contextId")

        is_global_context = d.pop("isGlobalContext", UNSET)

        project_id = d.pop("projectId", UNSET)

        custom_field_context_project_mapping = cls(
            context_id=context_id,
            is_global_context=is_global_context,
            project_id=project_id,
        )

        return custom_field_context_project_mapping

