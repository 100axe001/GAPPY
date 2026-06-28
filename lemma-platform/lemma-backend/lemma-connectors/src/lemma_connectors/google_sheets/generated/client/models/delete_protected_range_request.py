from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteProtectedRangeRequest")



@_attrs_define
class DeleteProtectedRangeRequest:
    """ Deletes the protected range with the given ID.

        Attributes:
            protected_range_id (int | Unset): The ID of the protected range to delete.
     """

    protected_range_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        protected_range_id = self.protected_range_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if protected_range_id is not UNSET:
            field_dict["protectedRangeId"] = protected_range_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        protected_range_id = d.pop("protectedRangeId", UNSET)

        delete_protected_range_request = cls(
            protected_range_id=protected_range_id,
        )


        delete_protected_range_request.additional_properties = d
        return delete_protected_range_request

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
