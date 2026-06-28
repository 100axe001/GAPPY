from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateUpdateRoleRequestBean")



@_attrs_define
class CreateUpdateRoleRequestBean:
    """ 
        Attributes:
            description (str | Unset): A description of the project role. Required when fully updating a project role.
                Optional when creating or partially updating a project role.
            name (str | Unset): The name of the project role. Must be unique. Cannot begin or end with whitespace. The
                maximum length is 255 characters. Required when creating a project role. Optional when partially updating a
                project role.
     """

    description: str | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        create_update_role_request_bean = cls(
            description=description,
            name=name,
        )

        return create_update_role_request_bean

