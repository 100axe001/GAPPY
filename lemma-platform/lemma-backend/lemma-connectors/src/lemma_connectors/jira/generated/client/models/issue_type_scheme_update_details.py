from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueTypeSchemeUpdateDetails")



@_attrs_define
class IssueTypeSchemeUpdateDetails:
    """ Details of the name, description, and default issue type for an issue type scheme.

        Attributes:
            default_issue_type_id (str | Unset): The ID of the default issue type of the issue type scheme.
            description (str | Unset): The description of the issue type scheme. The maximum length is 4000 characters.
            name (str | Unset): The name of the issue type scheme. The name must be unique. The maximum length is 255
                characters.
     """

    default_issue_type_id: str | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        default_issue_type_id = self.default_issue_type_id

        description = self.description

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if default_issue_type_id is not UNSET:
            field_dict["defaultIssueTypeId"] = default_issue_type_id
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_issue_type_id = d.pop("defaultIssueTypeId", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        issue_type_scheme_update_details = cls(
            default_issue_type_id=default_issue_type_id,
            description=description,
            name=name,
        )

        return issue_type_scheme_update_details

