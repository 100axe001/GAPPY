from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CustomFieldContextDefaultValueProject")



@_attrs_define
class CustomFieldContextDefaultValueProject:
    """ The default value for a project custom field.

        Attributes:
            context_id (str): The ID of the context.
            project_id (str): The ID of the default project.
            type_ (str):
     """

    context_id: str
    project_id: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        project_id = self.project_id

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "contextId": context_id,
            "projectId": project_id,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_id = d.pop("contextId")

        project_id = d.pop("projectId")

        type_ = d.pop("type")

        custom_field_context_default_value_project = cls(
            context_id=context_id,
            project_id=project_id,
            type_=type_,
        )


        custom_field_context_default_value_project.additional_properties = d
        return custom_field_context_default_value_project

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
