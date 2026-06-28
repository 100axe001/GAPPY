from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="EntityProperty")



@_attrs_define
class EntityProperty:
    """ An entity property, for more information see [Entity
    properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/).

        Attributes:
            key (str | Unset): The key of the property. Required on create and update.
            value (Any | Unset): The value of the property. Required on create and update.
     """

    key: str | Unset = UNSET
    value: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        entity_property = cls(
            key=key,
            value=value,
        )

        return entity_property

