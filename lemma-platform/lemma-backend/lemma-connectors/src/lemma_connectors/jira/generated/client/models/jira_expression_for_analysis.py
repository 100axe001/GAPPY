from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jira_expression_for_analysis_context_variables import JiraExpressionForAnalysisContextVariables





T = TypeVar("T", bound="JiraExpressionForAnalysis")



@_attrs_define
class JiraExpressionForAnalysis:
    """ Details of Jira expressions for analysis.

        Attributes:
            expressions (list[str]): The list of Jira expressions to analyse. Example: issues.map(issue =>
                issue.properties['property_key']).
            context_variables (JiraExpressionForAnalysisContextVariables | Unset): Context variables and their types. The
                type checker assumes that [common context variables](https://developer.atlassian.com/cloud/jira/platform/jira-
                expressions/#context-variables), such as `issue` or `project`, are available in context and sets their type. Use
                this property to override the default types or provide details of new variables.
     """

    expressions: list[str]
    context_variables: JiraExpressionForAnalysisContextVariables | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jira_expression_for_analysis_context_variables import JiraExpressionForAnalysisContextVariables
        expressions = self.expressions



        context_variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context_variables, Unset):
            context_variables = self.context_variables.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expressions": expressions,
        })
        if context_variables is not UNSET:
            field_dict["contextVariables"] = context_variables

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_expression_for_analysis_context_variables import JiraExpressionForAnalysisContextVariables
        d = dict(src_dict)
        expressions = cast(list[str], d.pop("expressions"))


        _context_variables = d.pop("contextVariables", UNSET)
        context_variables: JiraExpressionForAnalysisContextVariables | Unset
        if isinstance(_context_variables,  Unset):
            context_variables = UNSET
        else:
            context_variables = JiraExpressionForAnalysisContextVariables.from_dict(_context_variables)




        jira_expression_for_analysis = cls(
            expressions=expressions,
            context_variables=context_variables,
        )

        return jira_expression_for_analysis

