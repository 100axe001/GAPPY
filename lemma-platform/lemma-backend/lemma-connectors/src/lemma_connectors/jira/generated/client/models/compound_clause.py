from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.compound_clause_operator import CompoundClauseOperator
from typing import cast

if TYPE_CHECKING:
  from ..models.field_changed_clause import FieldChangedClause
  from ..models.field_value_clause import FieldValueClause
  from ..models.field_was_clause import FieldWasClause





T = TypeVar("T", bound="CompoundClause")



@_attrs_define
class CompoundClause:
    """ A JQL query clause that consists of nested clauses. For example, `(labels in (urgent, blocker) OR lastCommentedBy =
    currentUser()). Note that, where nesting is not defined, the parser nests JQL clauses based on the operator
    precedence. For example, "A OR B AND C" is parsed as "(A OR B) AND C". See Setting the precedence of operators for
    more information about precedence in JQL queries.`

        Attributes:
            clauses (list[CompoundClause | FieldChangedClause | FieldValueClause | FieldWasClause]): The list of nested
                clauses.
            operator (CompoundClauseOperator): The operator between the clauses.
     """

    clauses: list[CompoundClause | FieldChangedClause | FieldValueClause | FieldWasClause]
    operator: CompoundClauseOperator
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_changed_clause import FieldChangedClause
        from ..models.field_value_clause import FieldValueClause
        from ..models.field_was_clause import FieldWasClause
        clauses = []
        for clauses_item_data in self.clauses:
            clauses_item: dict[str, Any]
            if isinstance(clauses_item_data, CompoundClause):
                clauses_item = clauses_item_data.to_dict()
            elif isinstance(clauses_item_data, FieldValueClause):
                clauses_item = clauses_item_data.to_dict()
            elif isinstance(clauses_item_data, FieldWasClause):
                clauses_item = clauses_item_data.to_dict()
            else:
                clauses_item = clauses_item_data.to_dict()

            clauses.append(clauses_item)



        operator = self.operator.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "clauses": clauses,
            "operator": operator,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_changed_clause import FieldChangedClause
        from ..models.field_value_clause import FieldValueClause
        from ..models.field_was_clause import FieldWasClause
        d = dict(src_dict)
        clauses = []
        _clauses = d.pop("clauses")
        for clauses_item_data in (_clauses):
            def _parse_clauses_item(data: object) -> CompoundClause | FieldChangedClause | FieldValueClause | FieldWasClause:
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

            clauses_item = _parse_clauses_item(clauses_item_data)

            clauses.append(clauses_item)


        operator = CompoundClauseOperator(d.pop("operator"))




        compound_clause = cls(
            clauses=clauses,
            operator=operator,
        )


        compound_clause.additional_properties = d
        return compound_clause

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
