from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteNamedRangeRequest")



@_attrs_define
class DeleteNamedRangeRequest:
    """ Removes the named range with the given ID from the spreadsheet.

        Attributes:
            named_range_id (str | Unset): The ID of the named range to delete.
     """

    named_range_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        named_range_id = self.named_range_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if named_range_id is not UNSET:
            field_dict["namedRangeId"] = named_range_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        named_range_id = d.pop("namedRangeId", UNSET)

        delete_named_range_request = cls(
            named_range_id=named_range_id,
        )


        delete_named_range_request.additional_properties = d
        return delete_named_range_request

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
