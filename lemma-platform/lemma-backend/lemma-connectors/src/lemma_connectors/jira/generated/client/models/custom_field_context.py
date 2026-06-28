from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CustomFieldContext")



@_attrs_define
class CustomFieldContext:
    """ The details of a custom field context.

        Attributes:
            description (str): The description of the context.
            id (str): The ID of the context.
            is_any_issue_type (bool): Whether the context apply to all issue types.
            is_global_context (bool): Whether the context is global.
            name (str): The name of the context.
     """

    description: str
    id: str
    is_any_issue_type: bool
    is_global_context: bool
    name: str





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        is_any_issue_type = self.is_any_issue_type

        is_global_context = self.is_global_context

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "description": description,
            "id": id,
            "isAnyIssueType": is_any_issue_type,
            "isGlobalContext": is_global_context,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        id = d.pop("id")

        is_any_issue_type = d.pop("isAnyIssueType")

        is_global_context = d.pop("isGlobalContext")

        name = d.pop("name")

        custom_field_context = cls(
            description=description,
            id=id,
            is_any_issue_type=is_any_issue_type,
            is_global_context=is_global_context,
            name=name,
        )

        return custom_field_context

