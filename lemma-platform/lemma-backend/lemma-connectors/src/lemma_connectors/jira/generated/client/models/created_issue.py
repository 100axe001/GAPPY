from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.nested_response import NestedResponse





T = TypeVar("T", bound="CreatedIssue")



@_attrs_define
class CreatedIssue:
    """ Details about a created issue or subtask.

        Attributes:
            id (str | Unset): The ID of the created issue or subtask.
            key (str | Unset): The key of the created issue or subtask.
            self_ (str | Unset): The URL of the created issue or subtask.
            transition (NestedResponse | Unset):
            watchers (NestedResponse | Unset):
     """

    id: str | Unset = UNSET
    key: str | Unset = UNSET
    self_: str | Unset = UNSET
    transition: NestedResponse | Unset = UNSET
    watchers: NestedResponse | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.nested_response import NestedResponse
        id = self.id

        key = self.key

        self_ = self.self_

        transition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transition, Unset):
            transition = self.transition.to_dict()

        watchers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.watchers, Unset):
            watchers = self.watchers.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if self_ is not UNSET:
            field_dict["self"] = self_
        if transition is not UNSET:
            field_dict["transition"] = transition
        if watchers is not UNSET:
            field_dict["watchers"] = watchers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_response import NestedResponse
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        self_ = d.pop("self", UNSET)

        _transition = d.pop("transition", UNSET)
        transition: NestedResponse | Unset
        if isinstance(_transition,  Unset):
            transition = UNSET
        else:
            transition = NestedResponse.from_dict(_transition)




        _watchers = d.pop("watchers", UNSET)
        watchers: NestedResponse | Unset
        if isinstance(_watchers,  Unset):
            watchers = UNSET
        else:
            watchers = NestedResponse.from_dict(_watchers)




        created_issue = cls(
            id=id,
            key=key,
            self_=self_,
            transition=transition,
            watchers=watchers,
        )

        return created_issue

