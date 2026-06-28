from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jira_expression_complexity_variables import JiraExpressionComplexityVariables





T = TypeVar("T", bound="JiraExpressionComplexity")



@_attrs_define
class JiraExpressionComplexity:
    """ Details about the complexity of the analysed Jira expression.

        Attributes:
            expensive_operations (str): Information that can be used to determine how many [expensive
                operations](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#expensive-operations) the
                evaluation of the expression will perform. This information may be a formula or number. For example:

                 *  `issues.map(i => i.comments)` performs as many expensive operations as there are issues on the issues list.
                So this parameter returns `N`, where `N` is the size of issue list.
                 *  `new Issue(10010).comments` gets comments for one issue, so its complexity is `2` (`1` to retrieve issue
                10010 from the database plus `1` to get its comments).
            variables (JiraExpressionComplexityVariables | Unset): Variables used in the formula, mapped to the parts of the
                expression they refer to.
     """

    expensive_operations: str
    variables: JiraExpressionComplexityVariables | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jira_expression_complexity_variables import JiraExpressionComplexityVariables
        expensive_operations = self.expensive_operations

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expensiveOperations": expensive_operations,
        })
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_expression_complexity_variables import JiraExpressionComplexityVariables
        d = dict(src_dict)
        expensive_operations = d.pop("expensiveOperations")

        _variables = d.pop("variables", UNSET)
        variables: JiraExpressionComplexityVariables | Unset
        if isinstance(_variables,  Unset):
            variables = UNSET
        else:
            variables = JiraExpressionComplexityVariables.from_dict(_variables)




        jira_expression_complexity = cls(
            expensive_operations=expensive_operations,
            variables=variables,
        )

        return jira_expression_complexity

