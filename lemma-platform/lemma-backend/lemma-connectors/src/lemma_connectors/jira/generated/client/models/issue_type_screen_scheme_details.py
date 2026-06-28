from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_type_screen_scheme_mapping import IssueTypeScreenSchemeMapping





T = TypeVar("T", bound="IssueTypeScreenSchemeDetails")



@_attrs_define
class IssueTypeScreenSchemeDetails:
    """ The details of an issue type screen scheme.

        Attributes:
            issue_type_mappings (list[IssueTypeScreenSchemeMapping]): The IDs of the screen schemes for the issue type IDs
                and *default*. A *default* entry is required to create an issue type screen scheme, it defines the mapping for
                all issue types without a screen scheme.
            name (str): The name of the issue type screen scheme. The name must be unique. The maximum length is 255
                characters.
            description (str | Unset): The description of the issue type screen scheme. The maximum length is 255
                characters.
     """

    issue_type_mappings: list[IssueTypeScreenSchemeMapping]
    name: str
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_type_screen_scheme_mapping import IssueTypeScreenSchemeMapping
        issue_type_mappings = []
        for issue_type_mappings_item_data in self.issue_type_mappings:
            issue_type_mappings_item = issue_type_mappings_item_data.to_dict()
            issue_type_mappings.append(issue_type_mappings_item)



        name = self.name

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeMappings": issue_type_mappings,
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_type_screen_scheme_mapping import IssueTypeScreenSchemeMapping
        d = dict(src_dict)
        issue_type_mappings = []
        _issue_type_mappings = d.pop("issueTypeMappings")
        for issue_type_mappings_item_data in (_issue_type_mappings):
            issue_type_mappings_item = IssueTypeScreenSchemeMapping.from_dict(issue_type_mappings_item_data)



            issue_type_mappings.append(issue_type_mappings_item)


        name = d.pop("name")

        description = d.pop("description", UNSET)

        issue_type_screen_scheme_details = cls(
            issue_type_mappings=issue_type_mappings,
            name=name,
            description=description,
        )

        return issue_type_screen_scheme_details

