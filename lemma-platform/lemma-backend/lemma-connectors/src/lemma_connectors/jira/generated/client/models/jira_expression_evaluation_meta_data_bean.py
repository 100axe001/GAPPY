from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issues_meta_bean import IssuesMetaBean
  from ..models.jira_expressions_complexity_bean import JiraExpressionsComplexityBean





T = TypeVar("T", bound="JiraExpressionEvaluationMetaDataBean")



@_attrs_define
class JiraExpressionEvaluationMetaDataBean:
    """ 
        Attributes:
            complexity (JiraExpressionsComplexityBean | Unset):
            issues (IssuesMetaBean | Unset): Meta data describing the `issues` context variable.
     """

    complexity: JiraExpressionsComplexityBean | Unset = UNSET
    issues: IssuesMetaBean | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issues_meta_bean import IssuesMetaBean
        from ..models.jira_expressions_complexity_bean import JiraExpressionsComplexityBean
        complexity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.complexity, Unset):
            complexity = self.complexity.to_dict()

        issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if complexity is not UNSET:
            field_dict["complexity"] = complexity
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issues_meta_bean import IssuesMetaBean
        from ..models.jira_expressions_complexity_bean import JiraExpressionsComplexityBean
        d = dict(src_dict)
        _complexity = d.pop("complexity", UNSET)
        complexity: JiraExpressionsComplexityBean | Unset
        if isinstance(_complexity,  Unset):
            complexity = UNSET
        else:
            complexity = JiraExpressionsComplexityBean.from_dict(_complexity)




        _issues = d.pop("issues", UNSET)
        issues: IssuesMetaBean | Unset
        if isinstance(_issues,  Unset):
            issues = UNSET
        else:
            issues = IssuesMetaBean.from_dict(_issues)




        jira_expression_evaluation_meta_data_bean = cls(
            complexity=complexity,
            issues=issues,
        )

        return jira_expression_evaluation_meta_data_bean

