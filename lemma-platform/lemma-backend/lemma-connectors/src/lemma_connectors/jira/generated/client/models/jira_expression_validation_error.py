from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.jira_expression_validation_error_type import JiraExpressionValidationErrorType
from ..types import UNSET, Unset






T = TypeVar("T", bound="JiraExpressionValidationError")



@_attrs_define
class JiraExpressionValidationError:
    """ Details about syntax and type errors. The error details apply to the entire expression, unless the object includes:

     *  `line` and `column`
     *  `expression`

        Attributes:
            message (str): Details about the error. Example: !, -, typeof, (, IDENTIFIER, null, true, false, NUMBER, STRING,
                TEMPLATE_LITERAL, new, [ or { expected, > encountered..
            type_ (JiraExpressionValidationErrorType): The error type.
            column (int | Unset): The text column in which the error occurred.
            expression (str | Unset): The part of the expression in which the error occurred.
            line (int | Unset): The text line in which the error occurred.
     """

    message: str
    type_: JiraExpressionValidationErrorType
    column: int | Unset = UNSET
    expression: str | Unset = UNSET
    line: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        type_ = self.type_.value

        column = self.column

        expression = self.expression

        line = self.line


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "message": message,
            "type": type_,
        })
        if column is not UNSET:
            field_dict["column"] = column
        if expression is not UNSET:
            field_dict["expression"] = expression
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        type_ = JiraExpressionValidationErrorType(d.pop("type"))




        column = d.pop("column", UNSET)

        expression = d.pop("expression", UNSET)

        line = d.pop("line", UNSET)

        jira_expression_validation_error = cls(
            message=message,
            type_=type_,
            column=column,
            expression=expression,
            line=line,
        )

        return jira_expression_validation_error

