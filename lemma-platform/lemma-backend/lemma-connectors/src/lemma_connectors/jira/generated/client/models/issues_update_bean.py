from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_update_details import IssueUpdateDetails





T = TypeVar("T", bound="IssuesUpdateBean")



@_attrs_define
class IssuesUpdateBean:
    """ 
        Attributes:
            issue_updates (list[IssueUpdateDetails] | Unset):
     """

    issue_updates: list[IssueUpdateDetails] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_update_details import IssueUpdateDetails
        issue_updates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issue_updates, Unset):
            issue_updates = []
            for issue_updates_item_data in self.issue_updates:
                issue_updates_item = issue_updates_item_data.to_dict()
                issue_updates.append(issue_updates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if issue_updates is not UNSET:
            field_dict["issueUpdates"] = issue_updates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_update_details import IssueUpdateDetails
        d = dict(src_dict)
        _issue_updates = d.pop("issueUpdates", UNSET)
        issue_updates: list[IssueUpdateDetails] | Unset = UNSET
        if _issue_updates is not UNSET:
            issue_updates = []
            for issue_updates_item_data in _issue_updates:
                issue_updates_item = IssueUpdateDetails.from_dict(issue_updates_item_data)



                issue_updates.append(issue_updates_item)


        issues_update_bean = cls(
            issue_updates=issue_updates,
        )


        issues_update_bean.additional_properties = d
        return issues_update_bean

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
