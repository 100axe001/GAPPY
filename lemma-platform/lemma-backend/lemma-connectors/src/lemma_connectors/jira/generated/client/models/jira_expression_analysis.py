from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jira_expression_complexity import JiraExpressionComplexity
  from ..models.jira_expression_validation_error import JiraExpressionValidationError





T = TypeVar("T", bound="JiraExpressionAnalysis")



@_attrs_define
class JiraExpressionAnalysis:
    """ Details about the analysed Jira expression.

        Attributes:
            expression (str): The analysed expression.
            valid (bool): Whether the expression is valid and the interpreter will evaluate it. Note that the expression may
                fail at runtime (for example, if it executes too many expensive operations).
            complexity (JiraExpressionComplexity | Unset): Details about the complexity of the analysed Jira expression.
            errors (list[JiraExpressionValidationError] | Unset): A list of validation errors. Not included if the
                expression is valid.
            type_ (str | Unset): EXPERIMENTAL. The inferred type of the expression.
     """

    expression: str
    valid: bool
    complexity: JiraExpressionComplexity | Unset = UNSET
    errors: list[JiraExpressionValidationError] | Unset = UNSET
    type_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jira_expression_complexity import JiraExpressionComplexity
        from ..models.jira_expression_validation_error import JiraExpressionValidationError
        expression = self.expression

        valid = self.valid

        complexity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.complexity, Unset):
            complexity = self.complexity.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        type_ = self.type_


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expression": expression,
            "valid": valid,
        })
        if complexity is not UNSET:
            field_dict["complexity"] = complexity
        if errors is not UNSET:
            field_dict["errors"] = errors
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_expression_complexity import JiraExpressionComplexity
        from ..models.jira_expression_validation_error import JiraExpressionValidationError
        d = dict(src_dict)
        expression = d.pop("expression")

        valid = d.pop("valid")

        _complexity = d.pop("complexity", UNSET)
        complexity: JiraExpressionComplexity | Unset
        if isinstance(_complexity,  Unset):
            complexity = UNSET
        else:
            complexity = JiraExpressionComplexity.from_dict(_complexity)




        _errors = d.pop("errors", UNSET)
        errors: list[JiraExpressionValidationError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = JiraExpressionValidationError.from_dict(errors_item_data)



                errors.append(errors_item)


        type_ = d.pop("type", UNSET)

        jira_expression_analysis = cls(
            expression=expression,
            valid=valid,
            complexity=complexity,
            errors=errors,
            type_=type_,
        )

        return jira_expression_analysis

