from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConferenceSolutionKey")



@_attrs_define
class ConferenceSolutionKey:
    """ 
        Attributes:
            type_ (str | Unset): The conference solution type.
                If a client encounters an unfamiliar or empty type, it should still be able to display the entry points.
                However, it should disallow modifications.
                The possible values are:
                - "eventHangout" for Hangouts for consumers (deprecated; existing events may show this conference solution type
                but new conferences cannot be created)
                - "eventNamedHangout" for classic Hangouts for Google Workspace users (deprecated; existing events may show this
                conference solution type but new conferences cannot be created)
                - "hangoutsMeet" for Google Meet (http://meet.google.com)
                - "addOn" for 3P conference providers
     """

    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        conference_solution_key = cls(
            type_=type_,
        )


        conference_solution_key.additional_properties = d
        return conference_solution_key

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
