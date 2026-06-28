from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueTypeScheme")



@_attrs_define
class IssueTypeScheme:
    """ Details of an issue type scheme.

        Attributes:
            id (str): The ID of the issue type scheme.
            name (str): The name of the issue type scheme.
            default_issue_type_id (str | Unset): The ID of the default issue type of the issue type scheme.
            description (str | Unset): The description of the issue type scheme.
            is_default (bool | Unset): Whether the issue type scheme is the default.
     """

    id: str
    name: str
    default_issue_type_id: str | Unset = UNSET
    description: str | Unset = UNSET
    is_default: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        default_issue_type_id = self.default_issue_type_id

        description = self.description

        is_default = self.is_default


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
        })
        if default_issue_type_id is not UNSET:
            field_dict["defaultIssueTypeId"] = default_issue_type_id
        if description is not UNSET:
            field_dict["description"] = description
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        default_issue_type_id = d.pop("defaultIssueTypeId", UNSET)

        description = d.pop("description", UNSET)

        is_default = d.pop("isDefault", UNSET)

        issue_type_scheme = cls(
            id=id,
            name=name,
            default_issue_type_id=default_issue_type_id,
            description=description,
            is_default=is_default,
        )

        return issue_type_scheme

