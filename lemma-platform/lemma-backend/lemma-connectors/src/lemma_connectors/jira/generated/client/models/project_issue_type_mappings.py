from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.project_issue_type_mapping import ProjectIssueTypeMapping





T = TypeVar("T", bound="ProjectIssueTypeMappings")



@_attrs_define
class ProjectIssueTypeMappings:
    """ The project and issue type mappings.

        Attributes:
            mappings (list[ProjectIssueTypeMapping]): The project and issue type mappings.
     """

    mappings: list[ProjectIssueTypeMapping]





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_issue_type_mapping import ProjectIssueTypeMapping
        mappings = []
        for mappings_item_data in self.mappings:
            mappings_item = mappings_item_data.to_dict()
            mappings.append(mappings_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "mappings": mappings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_issue_type_mapping import ProjectIssueTypeMapping
        d = dict(src_dict)
        mappings = []
        _mappings = d.pop("mappings")
        for mappings_item_data in (_mappings):
            mappings_item = ProjectIssueTypeMapping.from_dict(mappings_item_data)



            mappings.append(mappings_item)


        project_issue_type_mappings = cls(
            mappings=mappings,
        )

        return project_issue_type_mappings

