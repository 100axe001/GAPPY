from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.issue_type_create_bean_type import IssueTypeCreateBeanType
from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueTypeCreateBean")



@_attrs_define
class IssueTypeCreateBean:
    """ 
        Attributes:
            name (str): The unique name for the issue type. The maximum length is 60 characters.
            description (str | Unset): The description of the issue type.
            hierarchy_level (int | Unset): The hierarchy level of the issue type. Use:

                 *  `-1` for Subtask.
                 *  `0` for Base.

                Defaults to `0`.
            type_ (IssueTypeCreateBeanType | Unset): Deprecated. Use `hierarchyLevel` instead. See the [deprecation
                notice](https://community.developer.atlassian.com/t/deprecation-of-the-epic-link-parent-link-and-other-related-
                fields-in-rest-apis-and-webhooks/54048) for details.

                Whether the issue type is `subtype` or `standard`. Defaults to `standard`.
     """

    name: str
    description: str | Unset = UNSET
    hierarchy_level: int | Unset = UNSET
    type_: IssueTypeCreateBeanType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        hierarchy_level = self.hierarchy_level

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if hierarchy_level is not UNSET:
            field_dict["hierarchyLevel"] = hierarchy_level
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        hierarchy_level = d.pop("hierarchyLevel", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: IssueTypeCreateBeanType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = IssueTypeCreateBeanType(_type_)




        issue_type_create_bean = cls(
            name=name,
            description=description,
            hierarchy_level=hierarchy_level,
            type_=type_,
        )

        return issue_type_create_bean

