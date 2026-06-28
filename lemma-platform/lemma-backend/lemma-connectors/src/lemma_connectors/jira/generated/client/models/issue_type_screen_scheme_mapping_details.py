from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.issue_type_screen_scheme_mapping import IssueTypeScreenSchemeMapping





T = TypeVar("T", bound="IssueTypeScreenSchemeMappingDetails")



@_attrs_define
class IssueTypeScreenSchemeMappingDetails:
    """ A list of issue type screen scheme mappings.

        Attributes:
            issue_type_mappings (list[IssueTypeScreenSchemeMapping]): The list of issue type to screen scheme mappings. A
                *default* entry cannot be specified because a default entry is added when an issue type screen scheme is
                created.
     """

    issue_type_mappings: list[IssueTypeScreenSchemeMapping]





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_type_screen_scheme_mapping import IssueTypeScreenSchemeMapping
        issue_type_mappings = []
        for issue_type_mappings_item_data in self.issue_type_mappings:
            issue_type_mappings_item = issue_type_mappings_item_data.to_dict()
            issue_type_mappings.append(issue_type_mappings_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeMappings": issue_type_mappings,
        })

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


        issue_type_screen_scheme_mapping_details = cls(
            issue_type_mappings=issue_type_mappings,
        )

        return issue_type_screen_scheme_mapping_details

