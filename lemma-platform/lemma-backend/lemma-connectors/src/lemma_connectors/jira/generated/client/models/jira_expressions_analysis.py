from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.jira_expression_analysis import JiraExpressionAnalysis





T = TypeVar("T", bound="JiraExpressionsAnalysis")



@_attrs_define
class JiraExpressionsAnalysis:
    """ Details about the analysed Jira expression.

        Attributes:
            results (list[JiraExpressionAnalysis]): The results of Jira expressions analysis.
     """

    results: list[JiraExpressionAnalysis]





    def to_dict(self) -> dict[str, Any]:
        from ..models.jira_expression_analysis import JiraExpressionAnalysis
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "results": results,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_expression_analysis import JiraExpressionAnalysis
        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = JiraExpressionAnalysis.from_dict(results_item_data)



            results.append(results_item)


        jira_expressions_analysis = cls(
            results=results,
        )

        return jira_expressions_analysis

