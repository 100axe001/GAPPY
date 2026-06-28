from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.jql_query_field_entity_property_type import JqlQueryFieldEntityPropertyType
from ..types import UNSET, Unset






T = TypeVar("T", bound="JqlQueryFieldEntityProperty")



@_attrs_define
class JqlQueryFieldEntityProperty:
    """ Details of an entity property.

        Attributes:
            entity (str): The object on which the property is set. Example: issue.
            key (str): The key of the property. Example: stats.
            path (str): The path in the property value to query. Example: comments.count.
            type_ (JqlQueryFieldEntityPropertyType | Unset): The type of the property value extraction. Not available if the
                extraction for the property is not registered on the instance with the [Entity
                property](https://developer.atlassian.com/cloud/jira/platform/modules/entity-property/) module. Example: number.
     """

    entity: str
    key: str
    path: str
    type_: JqlQueryFieldEntityPropertyType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        entity = self.entity

        key = self.key

        path = self.path

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "entity": entity,
            "key": key,
            "path": path,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity = d.pop("entity")

        key = d.pop("key")

        path = d.pop("path")

        _type_ = d.pop("type", UNSET)
        type_: JqlQueryFieldEntityPropertyType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = JqlQueryFieldEntityPropertyType(_type_)




        jql_query_field_entity_property = cls(
            entity=entity,
            key=key,
            path=path,
            type_=type_,
        )


        jql_query_field_entity_property.additional_properties = d
        return jql_query_field_entity_property

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
