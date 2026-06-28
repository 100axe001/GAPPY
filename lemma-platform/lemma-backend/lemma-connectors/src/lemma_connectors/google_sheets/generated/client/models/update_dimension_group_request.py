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





T = TypeVar("T", bound="UpdateDimensionGroupRequest")



@_attrs_define
class UpdateDimensionGroupRequest:
    """ Updates the state of the specified group.

        Attributes:
            dimension_group (DimensionGroup | Unset): A group over an interval of rows or columns on a sheet, which can
                contain or be contained within other groups. A group can be collapsed or expanded as a unit on the sheet.
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `dimensionGroup` is implied and should not be specified. A single `"*"` can be used as short-hand for listing
                every field.
     """

    dimension_group: DimensionGroup | Unset = UNSET
    fields: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_group import DimensionGroup
        dimension_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension_group, Unset):
            dimension_group = self.dimension_group.to_dict()

        fields = self.fields


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dimension_group is not UNSET:
            field_dict["dimensionGroup"] = dimension_group
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_group import DimensionGroup
        d = dict(src_dict)
        _dimension_group = d.pop("dimensionGroup", UNSET)
        dimension_group: DimensionGroup | Unset
        if isinstance(_dimension_group,  Unset):
            dimension_group = UNSET
        else:
            dimension_group = DimensionGroup.from_dict(_dimension_group)




        fields = d.pop("fields", UNSET)

        update_dimension_group_request = cls(
            dimension_group=dimension_group,
            fields=fields,
        )


        update_dimension_group_request.additional_properties = d
        return update_dimension_group_request

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
