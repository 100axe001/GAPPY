from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PermissionHolder")



@_attrs_define
class PermissionHolder:
    """ Details of a user, group, field, or project role that holds a permission. See [Holder object](../api-group-
    permission-schemes/#holder-object) in *Get all permission schemes* for more information.

        Attributes:
            type_ (str): The type of permission holder.
            expand (str | Unset): Expand options that include additional permission holder details in the response.
            parameter (str | Unset): As a group's name can change, use of `value` is recommended. The identifier associated
                withthe `type` value that defines the holder of the permission.
            value (str | Unset): The identifier associated with the `type` value that defines the holder of the permission.
     """

    type_: str
    expand: str | Unset = UNSET
    parameter: str | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        expand = self.expand

        parameter = self.parameter

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if expand is not UNSET:
            field_dict["expand"] = expand
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        expand = d.pop("expand", UNSET)

        parameter = d.pop("parameter", UNSET)

        value = d.pop("value", UNSET)

        permission_holder = cls(
            type_=type_,
            expand=expand,
            parameter=parameter,
            value=value,
        )

        return permission_holder

