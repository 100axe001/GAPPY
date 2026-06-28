from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.project_scope_bean_attributes_item import ProjectScopeBeanAttributesItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProjectScopeBean")



@_attrs_define
class ProjectScopeBean:
    """ 
        Attributes:
            attributes (list[ProjectScopeBeanAttributesItem] | Unset): Defines the behavior of the option in the project.If
                notSelectable is set, the option cannot be set as the field's value. This is useful for archiving an option that
                has previously been selected but shouldn't be used anymore.If defaultValue is set, the option is selected by
                default.
            id (int | Unset): The ID of the project that the option's behavior applies to.
     """

    attributes: list[ProjectScopeBeanAttributesItem] | Unset = UNSET
    id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        attributes: list[str] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.value
                attributes.append(attributes_item)



        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: list[ProjectScopeBeanAttributesItem] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = ProjectScopeBeanAttributesItem(attributes_item_data)



                attributes.append(attributes_item)


        id = d.pop("id", UNSET)

        project_scope_bean = cls(
            attributes=attributes,
            id=id,
        )

        return project_scope_bean

