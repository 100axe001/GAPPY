from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.field_changed_clause_operator import FieldChangedClauseOperator
from typing import cast

if TYPE_CHECKING:
  from ..models.jql_query_clause_time_predicate import JqlQueryClauseTimePredicate
  from ..models.jql_query_field import JqlQueryField





T = TypeVar("T", bound="FieldChangedClause")



@_attrs_define
class FieldChangedClause:
    """ A clause that asserts whether a field was changed. For example, `status CHANGED AFTER startOfMonth(-1M)`.See
    [CHANGED](https://confluence.atlassian.com/x/dgiiLQ#Advancedsearching-operatorsreference-CHANGEDCHANGED) for more
    information about the CHANGED operator.

        Attributes:
            field (JqlQueryField): A field used in a JQL query. See [Advanced searching - fields
                reference](https://confluence.atlassian.com/x/dAiiLQ) for more information about fields in JQL queries.
            operator (FieldChangedClauseOperator): The operator applied to the field.
            predicates (list[JqlQueryClauseTimePredicate]): The list of time predicates.
     """

    field: JqlQueryField
    operator: FieldChangedClauseOperator
    predicates: list[JqlQueryClauseTimePredicate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.jql_query_clause_time_predicate import JqlQueryClauseTimePredicate
        from ..models.jql_query_field import JqlQueryField
        field = self.field.to_dict()

        operator = self.operator.value

        predicates = []
        for predicates_item_data in self.predicates:
            predicates_item = predicates_item_data.to_dict()
            predicates.append(predicates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "operator": operator,
            "predicates": predicates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jql_query_clause_time_predicate import JqlQueryClauseTimePredicate
        from ..models.jql_query_field import JqlQueryField
        d = dict(src_dict)
        field = JqlQueryField.from_dict(d.pop("field"))




        operator = FieldChangedClauseOperator(d.pop("operator"))




        predicates = []
        _predicates = d.pop("predicates")
        for predicates_item_data in (_predicates):
            predicates_item = JqlQueryClauseTimePredicate.from_dict(predicates_item_data)



            predicates.append(predicates_item)


        field_changed_clause = cls(
            field=field,
            operator=operator,
            predicates=predicates,
        )


        field_changed_clause.additional_properties = d
        return field_changed_clause

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
