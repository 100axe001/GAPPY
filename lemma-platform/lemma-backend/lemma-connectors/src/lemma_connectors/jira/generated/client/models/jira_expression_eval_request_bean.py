from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jira_expression_eval_context_bean import JiraExpressionEvalContextBean





T = TypeVar("T", bound="JiraExpressionEvalRequestBean")



@_attrs_define
class JiraExpressionEvalRequestBean:
    """ 
        Attributes:
            expression (str): The Jira expression to evaluate. Example: { key: issue.key, type: issue.issueType.name, links:
                issue.links.map(link => link.linkedIssue.id) }.
            context (JiraExpressionEvalContextBean | Unset):
     """

    expression: str
    context: JiraExpressionEvalContextBean | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jira_expression_eval_context_bean import JiraExpressionEvalContextBean
        expression = self.expression

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expression": expression,
        })
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_expression_eval_context_bean import JiraExpressionEvalContextBean
        d = dict(src_dict)
        expression = d.pop("expression")

        _context = d.pop("context", UNSET)
        context: JiraExpressionEvalContextBean | Unset
        if isinstance(_context,  Unset):
            context = UNSET
        else:
            context = JiraExpressionEvalContextBean.from_dict(_context)




        jira_expression_eval_request_bean = cls(
            expression=expression,
            context=context,
        )

        return jira_expression_eval_request_bean

