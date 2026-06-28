from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.filter_action import FilterAction
  from ..models.filter_criteria import FilterCriteria





T = TypeVar("T", bound="Filter")



@_attrs_define
class Filter:
    """ Resource definition for Gmail filters. Filters apply to specific messages instead of an entire email thread.

        Attributes:
            action (FilterAction | Unset): A set of actions to perform on a message.
            criteria (FilterCriteria | Unset): Message matching criteria.
            id (str | Unset): The server assigned ID of the filter.
     """

    action: FilterAction | Unset = UNSET
    criteria: FilterCriteria | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_action import FilterAction
        from ..models.filter_criteria import FilterCriteria
        action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_action import FilterAction
        from ..models.filter_criteria import FilterCriteria
        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: FilterAction | Unset
        if isinstance(_action,  Unset):
            action = UNSET
        else:
            action = FilterAction.from_dict(_action)




        _criteria = d.pop("criteria", UNSET)
        criteria: FilterCriteria | Unset
        if isinstance(_criteria,  Unset):
            criteria = UNSET
        else:
            criteria = FilterCriteria.from_dict(_criteria)




        id = d.pop("id", UNSET)

        filter_ = cls(
            action=action,
            criteria=criteria,
            id=id,
        )


        filter_.additional_properties = d
        return filter_

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
