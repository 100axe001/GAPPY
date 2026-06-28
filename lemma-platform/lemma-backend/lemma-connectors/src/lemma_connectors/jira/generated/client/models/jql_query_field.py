from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jql_query_field_entity_property import JqlQueryFieldEntityProperty





T = TypeVar("T", bound="JqlQueryField")



@_attrs_define
class JqlQueryField:
    """ A field used in a JQL query. See [Advanced searching - fields reference](https://confluence.atlassian.com/x/dAiiLQ)
    for more information about fields in JQL queries.

        Attributes:
            name (str): The name of the field.
            encoded_name (str | Unset): The encoded name of the field, which can be used directly in a JQL query.
            property_ (list[JqlQueryFieldEntityProperty] | Unset): When the field refers to a value in an entity property,
                details of the entity property value.
     """

    name: str
    encoded_name: str | Unset = UNSET
    property_: list[JqlQueryFieldEntityProperty] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jql_query_field_entity_property import JqlQueryFieldEntityProperty
        name = self.name

        encoded_name = self.encoded_name

        property_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_, Unset):
            property_ = []
            for property_item_data in self.property_:
                property_item = property_item_data.to_dict()
                property_.append(property_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if encoded_name is not UNSET:
            field_dict["encodedName"] = encoded_name
        if property_ is not UNSET:
            field_dict["property"] = property_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jql_query_field_entity_property import JqlQueryFieldEntityProperty
        d = dict(src_dict)
        name = d.pop("name")

        encoded_name = d.pop("encodedName", UNSET)

        _property_ = d.pop("property", UNSET)
        property_: list[JqlQueryFieldEntityProperty] | Unset = UNSET
        if _property_ is not UNSET:
            property_ = []
            for property_item_data in _property_:
                property_item = JqlQueryFieldEntityProperty.from_dict(property_item_data)



                property_.append(property_item)


        jql_query_field = cls(
            name=name,
            encoded_name=encoded_name,
            property_=property_,
        )

        return jql_query_field

