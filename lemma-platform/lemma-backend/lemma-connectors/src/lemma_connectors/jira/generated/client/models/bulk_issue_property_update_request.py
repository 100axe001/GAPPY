from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_filter_for_bulk_property_set import IssueFilterForBulkPropertySet





T = TypeVar("T", bound="BulkIssuePropertyUpdateRequest")



@_attrs_define
class BulkIssuePropertyUpdateRequest:
    """ Bulk issue property update request details.

        Attributes:
            expression (str | Unset): EXPERIMENTAL. The Jira expression to calculate the value of the property. The value of
                the expression must be an object that can be converted to JSON, such as a number, boolean, string, list, or map.
                The context variables available to the expression are `issue` and `user`. Issues for which the expression
                returns a value whose JSON representation is longer than 32768 characters are ignored.
            filter_ (IssueFilterForBulkPropertySet | Unset): Bulk operation filter details.
            value (Any | Unset): The value of the property. The value must be a
                [valid](https://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.
     """

    expression: str | Unset = UNSET
    filter_: IssueFilterForBulkPropertySet | Unset = UNSET
    value: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_filter_for_bulk_property_set import IssueFilterForBulkPropertySet
        expression = self.expression

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expression is not UNSET:
            field_dict["expression"] = expression
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_filter_for_bulk_property_set import IssueFilterForBulkPropertySet
        d = dict(src_dict)
        expression = d.pop("expression", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: IssueFilterForBulkPropertySet | Unset
        if isinstance(_filter_,  Unset):
            filter_ = UNSET
        else:
            filter_ = IssueFilterForBulkPropertySet.from_dict(_filter_)




        value = d.pop("value", UNSET)

        bulk_issue_property_update_request = cls(
            expression=expression,
            filter_=filter_,
            value=value,
        )

        return bulk_issue_property_update_request

