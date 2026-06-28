from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.link_group import LinkGroup





T = TypeVar("T", bound="Operations")



@_attrs_define
class Operations:
    """ Details of the operations that can be performed on the issue.

        Attributes:
            link_groups (list[LinkGroup] | Unset): Details of the link groups defining issue operations.
     """

    link_groups: list[LinkGroup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.link_group import LinkGroup
        link_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.link_groups, Unset):
            link_groups = []
            for link_groups_item_data in self.link_groups:
                link_groups_item = link_groups_item_data.to_dict()
                link_groups.append(link_groups_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if link_groups is not UNSET:
            field_dict["linkGroups"] = link_groups

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_group import LinkGroup
        d = dict(src_dict)
        _link_groups = d.pop("linkGroups", UNSET)
        link_groups: list[LinkGroup] | Unset = UNSET
        if _link_groups is not UNSET:
            link_groups = []
            for link_groups_item_data in _link_groups:
                link_groups_item = LinkGroup.from_dict(link_groups_item_data)



                link_groups.append(link_groups_item)


        operations = cls(
            link_groups=link_groups,
        )


        operations.additional_properties = d
        return operations

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
