from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.jql_query_order_by_clause_element_direction import JqlQueryOrderByClauseElementDirection
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jql_query_field import JqlQueryField





T = TypeVar("T", bound="JqlQueryOrderByClauseElement")



@_attrs_define
class JqlQueryOrderByClauseElement:
    """ An element of the order-by JQL clause.

        Attributes:
            field (JqlQueryField): A field used in a JQL query. See [Advanced searching - fields
                reference](https://confluence.atlassian.com/x/dAiiLQ) for more information about fields in JQL queries.
            direction (JqlQueryOrderByClauseElementDirection | Unset): The direction in which to order the results.
     """

    field: JqlQueryField
    direction: JqlQueryOrderByClauseElementDirection | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jql_query_field import JqlQueryField
        field = self.field.to_dict()

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "field": field,
        })
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jql_query_field import JqlQueryField
        d = dict(src_dict)
        field = JqlQueryField.from_dict(d.pop("field"))




        _direction = d.pop("direction", UNSET)
        direction: JqlQueryOrderByClauseElementDirection | Unset
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = JqlQueryOrderByClauseElementDirection(_direction)




        jql_query_order_by_clause_element = cls(
            field=field,
            direction=direction,
        )

        return jql_query_order_by_clause_element

