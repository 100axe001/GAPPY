from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteDuplicatesResponse")



@_attrs_define
class DeleteDuplicatesResponse:
    """ The result of removing duplicates in a range.

        Attributes:
            duplicates_removed_count (int | Unset): The number of duplicate rows removed.
     """

    duplicates_removed_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        duplicates_removed_count = self.duplicates_removed_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if duplicates_removed_count is not UNSET:
            field_dict["duplicatesRemovedCount"] = duplicates_removed_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duplicates_removed_count = d.pop("duplicatesRemovedCount", UNSET)

        delete_duplicates_response = cls(
            duplicates_removed_count=duplicates_removed_count,
        )


        delete_duplicates_response.additional_properties = d
        return delete_duplicates_response

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
