from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="JiraExpressionsComplexityValueBean")



@_attrs_define
class JiraExpressionsComplexityValueBean:
    """ 
        Attributes:
            limit (int): The maximum allowed complexity. The evaluation will fail if this value is exceeded.
            value (int): The complexity value of the current expression.
     """

    limit: int
    value: int





    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "limit": limit,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        value = d.pop("value")

        jira_expressions_complexity_value_bean = cls(
            limit=limit,
            value=value,
        )

        return jira_expressions_complexity_value_bean

