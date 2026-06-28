from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ConferenceProperties")



@_attrs_define
class ConferenceProperties:
    """ 
        Attributes:
            allowed_conference_solution_types (list[str] | Unset): The types of conference solutions that are supported for
                this calendar.
                The possible values are:
                - "eventHangout"
                - "eventNamedHangout"
                - "hangoutsMeet"  Optional.
     """

    allowed_conference_solution_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allowed_conference_solution_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_conference_solution_types, Unset):
            allowed_conference_solution_types = self.allowed_conference_solution_types




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed_conference_solution_types is not UNSET:
            field_dict["allowedConferenceSolutionTypes"] = allowed_conference_solution_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_conference_solution_types = cast(list[str], d.pop("allowedConferenceSolutionTypes", UNSET))


        conference_properties = cls(
            allowed_conference_solution_types=allowed_conference_solution_types,
        )


        conference_properties.additional_properties = d
        return conference_properties

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
