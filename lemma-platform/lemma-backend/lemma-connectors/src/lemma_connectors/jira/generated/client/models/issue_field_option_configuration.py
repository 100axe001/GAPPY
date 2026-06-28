from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.issue_field_option_configuration_attributes_item import IssueFieldOptionConfigurationAttributesItem
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_field_option_scope_bean import IssueFieldOptionScopeBean





T = TypeVar("T", bound="IssueFieldOptionConfiguration")



@_attrs_define
class IssueFieldOptionConfiguration:
    """ Details of the projects the option is available in.

        Attributes:
            attributes (list[IssueFieldOptionConfigurationAttributesItem] | Unset): DEPRECATED
            scope (IssueFieldOptionScopeBean | Unset):
     """

    attributes: list[IssueFieldOptionConfigurationAttributesItem] | Unset = UNSET
    scope: IssueFieldOptionScopeBean | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_field_option_scope_bean import IssueFieldOptionScopeBean
        attributes: list[str] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.value
                attributes.append(attributes_item)



        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_field_option_scope_bean import IssueFieldOptionScopeBean
        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: list[IssueFieldOptionConfigurationAttributesItem] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = IssueFieldOptionConfigurationAttributesItem(attributes_item_data)



                attributes.append(attributes_item)


        _scope = d.pop("scope", UNSET)
        scope: IssueFieldOptionScopeBean | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = IssueFieldOptionScopeBean.from_dict(_scope)




        issue_field_option_configuration = cls(
            attributes=attributes,
            scope=scope,
        )

        return issue_field_option_configuration

