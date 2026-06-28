from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issues_jql_meta_data_bean import IssuesJqlMetaDataBean





T = TypeVar("T", bound="IssuesMetaBean")



@_attrs_define
class IssuesMetaBean:
    """ Meta data describing the `issues` context variable.

        Attributes:
            jql (IssuesJqlMetaDataBean | Unset): The description of the page of issues loaded by the provided JQL query.
     """

    jql: IssuesJqlMetaDataBean | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issues_jql_meta_data_bean import IssuesJqlMetaDataBean
        jql: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jql, Unset):
            jql = self.jql.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if jql is not UNSET:
            field_dict["jql"] = jql

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issues_jql_meta_data_bean import IssuesJqlMetaDataBean
        d = dict(src_dict)
        _jql = d.pop("jql", UNSET)
        jql: IssuesJqlMetaDataBean | Unset
        if isinstance(_jql,  Unset):
            jql = UNSET
        else:
            jql = IssuesJqlMetaDataBean.from_dict(_jql)




        issues_meta_bean = cls(
            jql=jql,
        )

        return issues_meta_bean

