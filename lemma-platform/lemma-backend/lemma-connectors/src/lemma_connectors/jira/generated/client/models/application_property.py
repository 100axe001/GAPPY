from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ApplicationProperty")



@_attrs_define
class ApplicationProperty:
    """ Details of an application property.

        Attributes:
            allowed_values (list[str] | Unset): The allowed values, if applicable.
            default_value (str | Unset): The default value of the application property.
            desc (str | Unset): The description of the application property.
            example (str | Unset):
            id (str | Unset): The ID of the application property. The ID and key are the same.
            key (str | Unset): The key of the application property. The ID and key are the same.
            name (str | Unset): The name of the application property.
            type_ (str | Unset): The data type of the application property.
            value (str | Unset): The new value.
     """

    allowed_values: list[str] | Unset = UNSET
    default_value: str | Unset = UNSET
    desc: str | Unset = UNSET
    example: str | Unset = UNSET
    id: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        allowed_values: list[str] | Unset = UNSET
        if not isinstance(self.allowed_values, Unset):
            allowed_values = self.allowed_values



        default_value = self.default_value

        desc = self.desc

        example = self.example

        id = self.id

        key = self.key

        name = self.name

        type_ = self.type_

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if allowed_values is not UNSET:
            field_dict["allowedValues"] = allowed_values
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if desc is not UNSET:
            field_dict["desc"] = desc
        if example is not UNSET:
            field_dict["example"] = example
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_values = cast(list[str], d.pop("allowedValues", UNSET))


        default_value = d.pop("defaultValue", UNSET)

        desc = d.pop("desc", UNSET)

        example = d.pop("example", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        application_property = cls(
            allowed_values=allowed_values,
            default_value=default_value,
            desc=desc,
            example=example,
            id=id,
            key=key,
            name=name,
            type_=type_,
            value=value,
        )

        return application_property

