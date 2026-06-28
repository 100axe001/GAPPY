from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jira_expression_evaluation_meta_data_bean import JiraExpressionEvaluationMetaDataBean





T = TypeVar("T", bound="JiraExpressionResult")



@_attrs_define
class JiraExpressionResult:
    """ The result of evaluating a Jira expression.

        Attributes:
            value (Any): The value of the evaluated expression. It may be a primitive JSON value or a Jira REST API object.
                (Some expressions do not produce any meaningful results—for example, an expression that returns a lambda
                function—if that's the case a simple string representation is returned. These string representations should not
                be relied upon and may change without notice.)
            meta (JiraExpressionEvaluationMetaDataBean | Unset):
     """

    value: Any
    meta: JiraExpressionEvaluationMetaDataBean | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jira_expression_evaluation_meta_data_bean import JiraExpressionEvaluationMetaDataBean
        value = self.value

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "value": value,
        })
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_expression_evaluation_meta_data_bean import JiraExpressionEvaluationMetaDataBean
        d = dict(src_dict)
        value = d.pop("value")

        _meta = d.pop("meta", UNSET)
        meta: JiraExpressionEvaluationMetaDataBean | Unset
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = JiraExpressionEvaluationMetaDataBean.from_dict(_meta)




        jira_expression_result = cls(
            value=value,
            meta=meta,
        )

        return jira_expression_result

