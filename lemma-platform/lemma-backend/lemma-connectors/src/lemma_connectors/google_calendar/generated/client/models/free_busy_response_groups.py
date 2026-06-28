from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.free_busy_group import FreeBusyGroup





T = TypeVar("T", bound="FreeBusyResponseGroups")



@_attrs_define
class FreeBusyResponseGroups:
    """ Expansion of groups.

     """

    additional_properties: dict[str, FreeBusyGroup] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.free_busy_group import FreeBusyGroup
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.free_busy_group import FreeBusyGroup
        d = dict(src_dict)
        free_busy_response_groups = cls(
        )


        from ..models.error import Error
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FreeBusyGroup.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        free_busy_response_groups.additional_properties = additional_properties
        return free_busy_response_groups

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> FreeBusyGroup:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: FreeBusyGroup) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
