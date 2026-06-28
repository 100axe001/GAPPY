from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension_group import DimensionGroup





T = TypeVar("T", bound="AddDimensionGroupResponse")



@_attrs_define
class AddDimensionGroupResponse:
    """ The result of adding a group.

        Attributes:
            dimension_groups (list[DimensionGroup] | Unset): All groups of a dimension after adding a group to that
                dimension.
     """

    dimension_groups: list[DimensionGroup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_group import DimensionGroup
        dimension_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dimension_groups, Unset):
            dimension_groups = []
            for dimension_groups_item_data in self.dimension_groups:
                dimension_groups_item = dimension_groups_item_data.to_dict()
                dimension_groups.append(dimension_groups_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dimension_groups is not UNSET:
            field_dict["dimensionGroups"] = dimension_groups

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_group import DimensionGroup
        d = dict(src_dict)
        _dimension_groups = d.pop("dimensionGroups", UNSET)
        dimension_groups: list[DimensionGroup] | Unset = UNSET
        if _dimension_groups is not UNSET:
            dimension_groups = []
            for dimension_groups_item_data in _dimension_groups:
                dimension_groups_item = DimensionGroup.from_dict(dimension_groups_item_data)



                dimension_groups.append(dimension_groups_item)


        add_dimension_group_response = cls(
            dimension_groups=dimension_groups,
        )


        add_dimension_group_response.additional_properties = d
        return add_dimension_group_response

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
