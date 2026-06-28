from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IssueFilterForBulkPropertyDelete")



@_attrs_define
class IssueFilterForBulkPropertyDelete:
    """ Bulk operation filter details.

        Attributes:
            current_value (Any | Unset): The value of properties to perform the bulk operation on.
            entity_ids (list[int] | Unset): List of issues to perform the bulk delete operation on.
     """

    current_value: Any | Unset = UNSET
    entity_ids: list[int] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        current_value = self.current_value

        entity_ids: list[int] | Unset = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if entity_ids is not UNSET:
            field_dict["entityIds"] = entity_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_value = d.pop("currentValue", UNSET)

        entity_ids = cast(list[int], d.pop("entityIds", UNSET))


        issue_filter_for_bulk_property_delete = cls(
            current_value=current_value,
            entity_ids=entity_ids,
        )

        return issue_filter_for_bulk_property_delete

