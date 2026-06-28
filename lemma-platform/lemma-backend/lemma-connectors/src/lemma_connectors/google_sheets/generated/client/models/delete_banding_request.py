from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteBandingRequest")



@_attrs_define
class DeleteBandingRequest:
    """ Removes the banded range with the given ID from the spreadsheet.

        Attributes:
            banded_range_id (int | Unset): The ID of the banded range to delete.
     """

    banded_range_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        banded_range_id = self.banded_range_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if banded_range_id is not UNSET:
            field_dict["bandedRangeId"] = banded_range_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        banded_range_id = d.pop("bandedRangeId", UNSET)

        delete_banding_request = cls(
            banded_range_id=banded_range_id,
        )


        delete_banding_request.additional_properties = d
        return delete_banding_request

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
