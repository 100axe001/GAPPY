from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.jira_expressions_complexity_value_bean import JiraExpressionsComplexityValueBean





T = TypeVar("T", bound="JiraExpressionsComplexityBean")



@_attrs_define
class JiraExpressionsComplexityBean:
    """ 
        Attributes:
            beans (JiraExpressionsComplexityValueBean):
            expensive_operations (JiraExpressionsComplexityValueBean):
            primitive_values (JiraExpressionsComplexityValueBean):
            steps (JiraExpressionsComplexityValueBean):
     """

    beans: JiraExpressionsComplexityValueBean
    expensive_operations: JiraExpressionsComplexityValueBean
    primitive_values: JiraExpressionsComplexityValueBean
    steps: JiraExpressionsComplexityValueBean





    def to_dict(self) -> dict[str, Any]:
        from ..models.jira_expressions_complexity_value_bean import JiraExpressionsComplexityValueBean
        beans = self.beans.to_dict()

        expensive_operations = self.expensive_operations.to_dict()

        primitive_values = self.primitive_values.to_dict()

        steps = self.steps.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "beans": beans,
            "expensiveOperations": expensive_operations,
            "primitiveValues": primitive_values,
            "steps": steps,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_expressions_complexity_value_bean import JiraExpressionsComplexityValueBean
        d = dict(src_dict)
        beans = JiraExpressionsComplexityValueBean.from_dict(d.pop("beans"))




        expensive_operations = JiraExpressionsComplexityValueBean.from_dict(d.pop("expensiveOperations"))




        primitive_values = JiraExpressionsComplexityValueBean.from_dict(d.pop("primitiveValues"))




        steps = JiraExpressionsComplexityValueBean.from_dict(d.pop("steps"))




        jira_expressions_complexity_bean = cls(
            beans=beans,
            expensive_operations=expensive_operations,
            primitive_values=primitive_values,
            steps=steps,
        )

        return jira_expressions_complexity_bean

