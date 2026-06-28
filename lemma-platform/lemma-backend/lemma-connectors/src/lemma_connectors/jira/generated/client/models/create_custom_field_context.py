from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateCustomFieldContext")



@_attrs_define
class CreateCustomFieldContext:
    """ The details of a created custom field context.

        Attributes:
            name (str): The name of the context.
            description (str | Unset): The description of the context.
            id (str | Unset): The ID of the context.
            issue_type_ids (list[str] | Unset): The list of issue types IDs for the context. If the list is empty, the
                context refers to all issue types.
            project_ids (list[str] | Unset): The list of project IDs associated with the context. If the list is empty, the
                context is global.
     """

    name: str
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    issue_type_ids: list[str] | Unset = UNSET
    project_ids: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        id = self.id

        issue_type_ids: list[str] | Unset = UNSET
        if not isinstance(self.issue_type_ids, Unset):
            issue_type_ids = self.issue_type_ids



        project_ids: list[str] | Unset = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if issue_type_ids is not UNSET:
            field_dict["issueTypeIds"] = issue_type_ids
        if project_ids is not UNSET:
            field_dict["projectIds"] = project_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        issue_type_ids = cast(list[str], d.pop("issueTypeIds", UNSET))


        project_ids = cast(list[str], d.pop("projectIds", UNSET))


        create_custom_field_context = cls(
            name=name,
            description=description,
            id=id,
            issue_type_ids=issue_type_ids,
            project_ids=project_ids,
        )

        return create_custom_field_context

