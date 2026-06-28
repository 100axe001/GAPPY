from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchAutoCompleteFilter")



@_attrs_define
class SearchAutoCompleteFilter:
    """ Details of how to filter and list search auto complete information.

        Attributes:
            include_collapsed_fields (bool | Unset): Include collapsed fields for fields that have non-unique names.
                Default: False.
            project_ids (list[int] | Unset): List of project IDs used to filter the visible field details returned.
     """

    include_collapsed_fields: bool | Unset = False
    project_ids: list[int] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        include_collapsed_fields = self.include_collapsed_fields

        project_ids: list[int] | Unset = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if include_collapsed_fields is not UNSET:
            field_dict["includeCollapsedFields"] = include_collapsed_fields
        if project_ids is not UNSET:
            field_dict["projectIds"] = project_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_collapsed_fields = d.pop("includeCollapsedFields", UNSET)

        project_ids = cast(list[int], d.pop("projectIds", UNSET))


        search_auto_complete_filter = cls(
            include_collapsed_fields=include_collapsed_fields,
            project_ids=project_ids,
        )

        return search_auto_complete_filter

