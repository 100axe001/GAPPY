from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IssueTypeSchemeDetails")



@_attrs_define
class IssueTypeSchemeDetails:
    """ Details of an issue type scheme and its associated issue types.

        Attributes:
            issue_type_ids (list[str]): The list of issue types IDs of the issue type scheme. At least one standard issue
                type ID is required.
            name (str): The name of the issue type scheme. The name must be unique. The maximum length is 255 characters.
            default_issue_type_id (str | Unset): The ID of the default issue type of the issue type scheme. This ID must be
                included in `issueTypeIds`.
            description (str | Unset): The description of the issue type scheme. The maximum length is 4000 characters.
     """

    issue_type_ids: list[str]
    name: str
    default_issue_type_id: str | Unset = UNSET
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        issue_type_ids = self.issue_type_ids



        name = self.name

        default_issue_type_id = self.default_issue_type_id

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeIds": issue_type_ids,
            "name": name,
        })
        if default_issue_type_id is not UNSET:
            field_dict["defaultIssueTypeId"] = default_issue_type_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_ids = cast(list[str], d.pop("issueTypeIds"))


        name = d.pop("name")

        default_issue_type_id = d.pop("defaultIssueTypeId", UNSET)

        description = d.pop("description", UNSET)

        issue_type_scheme_details = cls(
            issue_type_ids=issue_type_ids,
            name=name,
            default_issue_type_id=default_issue_type_id,
            description=description,
        )

        return issue_type_scheme_details

