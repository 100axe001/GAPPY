from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.jql_query_clause_time_predicate_operator import JqlQueryClauseTimePredicateOperator
from typing import cast

if TYPE_CHECKING:
  from ..models.function_operand import FunctionOperand
  from ..models.keyword_operand import KeywordOperand
  from ..models.list_operand import ListOperand
  from ..models.value_operand import ValueOperand





T = TypeVar("T", bound="JqlQueryClauseTimePredicate")



@_attrs_define
class JqlQueryClauseTimePredicate:
    """ A time predicate for a temporal JQL clause.

        Attributes:
            operand (FunctionOperand | KeywordOperand | ListOperand | ValueOperand): Details of an operand in a JQL clause.
            operator (JqlQueryClauseTimePredicateOperator): The operator between the field and the operand.
     """

    operand: FunctionOperand | KeywordOperand | ListOperand | ValueOperand
    operator: JqlQueryClauseTimePredicateOperator
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_operand import FunctionOperand
        from ..models.keyword_operand import KeywordOperand
        from ..models.list_operand import ListOperand
        from ..models.value_operand import ValueOperand
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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "operand": operand,
            "operator": operator,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_operand import FunctionOperand
        from ..models.keyword_operand import KeywordOperand
        from ..models.list_operand import ListOperand
        from ..models.value_operand import ValueOperand
        d = dict(src_dict)
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


        operator = JqlQueryClauseTimePredicateOperator(d.pop("operator"))




        jql_query_clause_time_predicate = cls(
            operand=operand,
            operator=operator,
        )


        jql_query_clause_time_predicate.additional_properties = d
        return jql_query_clause_time_predicate

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
