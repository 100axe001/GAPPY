from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.compound_clause import CompoundClause
  from ..models.field_changed_clause import FieldChangedClause
  from ..models.field_value_clause import FieldValueClause
  from ..models.field_was_clause import FieldWasClause
  from ..models.jql_query_order_by_clause import JqlQueryOrderByClause





T = TypeVar("T", bound="JqlQuery")



@_attrs_define
class JqlQuery:
    """ A parsed JQL query.

        Attributes:
            order_by (JqlQueryOrderByClause | Unset): Details of the order-by JQL clause.
            where (CompoundClause | FieldChangedClause | FieldValueClause | FieldWasClause | Unset): A JQL query clause.
     """

    order_by: JqlQueryOrderByClause | Unset = UNSET
    where: CompoundClause | FieldChangedClause | FieldValueClause | FieldWasClause | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.compound_clause import CompoundClause
        from ..models.field_changed_clause import FieldChangedClause
        from ..models.field_value_clause import FieldValueClause
        from ..models.field_was_clause import FieldWasClause
        from ..models.jql_query_order_by_clause import JqlQueryOrderByClause
        order_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.order_by, Unset):
            order_by = self.order_by.to_dict()

        where: dict[str, Any] | Unset
        if isinstance(self.where, Unset):
            where = UNSET
        elif isinstance(self.where, CompoundClause):
            where = self.where.to_dict()
        elif isinstance(self.where, FieldValueClause):
            where = self.where.to_dict()
        elif isinstance(self.where, FieldWasClause):
            where = self.where.to_dict()
        else:
            where = self.where.to_dict()



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if where is not UNSET:
            field_dict["where"] = where

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compound_clause import CompoundClause
        from ..models.field_changed_clause import FieldChangedClause
        from ..models.field_value_clause import FieldValueClause
        from ..models.field_was_clause import FieldWasClause
        from ..models.jql_query_order_by_clause import JqlQueryOrderByClause
        d = dict(src_dict)
        _order_by = d.pop("orderBy", UNSET)
        order_by: JqlQueryOrderByClause | Unset
        if isinstance(_order_by,  Unset):
            order_by = UNSET
        else:
            order_by = JqlQueryOrderByClause.from_dict(_order_by)




        def _parse_where(data: object) -> CompoundClause | FieldChangedClause | FieldValueClause | FieldWasClause | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_jql_query_clause_type_0 = CompoundClause.from_dict(data)



                return componentsschemas_jql_query_clause_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_jql_query_clause_type_1 = FieldValueClause.from_dict(data)



                return componentsschemas_jql_query_clause_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_jql_query_clause_type_2 = FieldWasClause.from_dict(data)



                return componentsschemas_jql_query_clause_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_jql_query_clause_type_3 = FieldChangedClause.from_dict(data)



            return componentsschemas_jql_query_clause_type_3

        where = _parse_where(d.pop("where", UNSET))


        jql_query = cls(
            order_by=order_by,
            where=where,
        )

        return jql_query

