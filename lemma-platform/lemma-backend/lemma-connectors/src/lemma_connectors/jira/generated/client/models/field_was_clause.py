from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.field_was_clause_operator import FieldWasClauseOperator
from typing import cast

if TYPE_CHECKING:
  from ..models.function_operand import FunctionOperand
  from ..models.jql_query_clause_time_predicate import JqlQueryClauseTimePredicate
  from ..models.jql_query_field import JqlQueryField
  from ..models.keyword_operand import KeywordOperand
  from ..models.list_operand import ListOperand
  from ..models.value_operand import ValueOperand





T = TypeVar("T", bound="FieldWasClause")



@_attrs_define
class FieldWasClause:
    """ A clause that asserts a previous value of a field. For example, `status WAS "Resolved" BY currentUser() BEFORE
    "2019/02/02"`. See [WAS](https://confluence.atlassian.com/x/dgiiLQ#Advancedsearching-operatorsreference-WASWAS) for
    more information about the WAS operator.

        Attributes:
            field (JqlQueryField): A field used in a JQL query. See [Advanced searching - fields
                reference](https://confluence.atlassian.com/x/dAiiLQ) for more information about fields in JQL queries.
            operand (FunctionOperand | KeywordOperand | ListOperand | ValueOperand): Details of an operand in a JQL clause.
            operator (FieldWasClauseOperator): The operator between the field and operand.
            predicates (list[JqlQueryClauseTimePredicate]): The list of time predicates.
     """

    field: JqlQueryField
    operand: FunctionOperand | KeywordOperand | ListOperand | ValueOperand
    operator: FieldWasClauseOperator
    predicates: list[JqlQueryClauseTimePredicate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_operand import FunctionOperand
        from ..models.jql_query_clause_time_predicate import JqlQueryClauseTimePredicate
        from ..models.jql_query_field import JqlQueryField
        from ..models.keyword_operand import KeywordOperand
        from ..models.list_operand import ListOperand
        from ..models.value_operand import ValueOperand
        field = self.field.to_dict()

        operand: dict[str, Any]
        if isinstance(self.operand, ListOperand):
            operand = self.operand.to_dict()
        elif isinstance(self.operand, ValueOperand):
            operand = self.operand.to_dict()
        elif isinstance(self.operand, FunctionOperand):
            operand = self.operand.to_dict()
        else:
            operand = self.operand.to_dict()


        operator = self.operator.value

        predicates = []
        for predicates_item_data in self.predicates:
            predicates_item = predicates_item_data.to_dict()
            predicates.append(predicates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "operand": operand,
            "operator": operator,
            "predicates": predicates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_operand import FunctionOperand
        from ..models.jql_query_clause_time_predicate import JqlQueryClauseTimePredicate
        from ..models.jql_query_field import JqlQueryField
        from ..models.keyword_operand import KeywordOperand
        from ..models.list_operand import ListOperand
        from ..models.value_operand import ValueOperand
        d = dict(src_dict)
        field = JqlQueryField.from_dict(d.pop("field"))




        def _parse_operand(data: object) -> FunctionOperand | KeywordOperand | ListOperand | ValueOperand:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_jql_query_clause_operand_type_0 = ListOperand.from_dict(data)



                return componentsschemas_jql_query_clause_operand_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_jql_query_clause_operand_type_1 = ValueOperand.from_dict(data)



                return componentsschemas_jql_query_clause_operand_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_jql_query_clause_operand_type_2 = FunctionOperand.from_dict(data)



                return componentsschemas_jql_query_clause_operand_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_jql_query_clause_operand_type_3 = KeywordOperand.from_dict(data)



            return componentsschemas_jql_query_clause_operand_type_3

        operand = _parse_operand(d.pop("operand"))


        operator = FieldWasClauseOperator(d.pop("operator"))




        predicates = []
        _predicates = d.pop("predicates")
        for predicates_item_data in (_predicates):
            predicates_item = JqlQueryClauseTimePredicate.from_dict(predicates_item_data)



            predicates.append(predicates_item)


        field_was_clause = cls(
            field=field,
            operand=operand,
            operator=operator,
            predicates=predicates,
        )


        field_was_clause.additional_properties = d
        return field_was_clause

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
