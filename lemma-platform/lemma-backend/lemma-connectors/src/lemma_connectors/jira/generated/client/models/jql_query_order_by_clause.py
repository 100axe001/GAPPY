from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.jql_query_order_by_clause_element import JqlQueryOrderByClauseElement





T = TypeVar("T", bound="JqlQueryOrderByClause")



@_attrs_define
class JqlQueryOrderByClause:
    """ Details of the order-by JQL clause.

        Attributes:
            fields (list[JqlQueryOrderByClauseElement]): The list of order-by clause fields and their ordering directives.
     """

    fields: list[JqlQueryOrderByClauseElement]





    def to_dict(self) -> dict[str, Any]:
        from ..models.jql_query_order_by_clause_element import JqlQueryOrderByClauseElement
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fields": fields,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jql_query_order_by_clause_element import JqlQueryOrderByClauseElement
        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in (_fields):
            fields_item = JqlQueryOrderByClauseElement.from_dict(fields_item_data)



            fields.append(fields_item)


        jql_query_order_by_clause = cls(
            fields=fields,
        )

        return jql_query_order_by_clause

