from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.conference_solution_key import ConferenceSolutionKey





T = TypeVar("T", bound="ConferenceSolution")



@_attrs_define
class ConferenceSolution:
    """ 
        Attributes:
            icon_uri (str | Unset): The user-visible icon for this solution.
            key (ConferenceSolutionKey | Unset):
            name (str | Unset): The user-visible name of this solution. Not localized.
     """

    icon_uri: str | Unset = UNSET
    key: ConferenceSolutionKey | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conference_solution_key import ConferenceSolutionKey
        icon_uri = self.icon_uri

        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if icon_uri is not UNSET:
            field_dict["iconUri"] = icon_uri
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conference_solution_key import ConferenceSolutionKey
        d = dict(src_dict)
        icon_uri = d.pop("iconUri", UNSET)

        _key = d.pop("key", UNSET)
        key: ConferenceSolutionKey | Unset
        if isinstance(_key,  Unset):
            key = UNSET
        else:
            key = ConferenceSolutionKey.from_dict(_key)




        name = d.pop("name", UNSET)

        conference_solution = cls(
            icon_uri=icon_uri,
            key=key,
            name=name,
        )


        conference_solution.additional_properties = d
        return conference_solution

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
