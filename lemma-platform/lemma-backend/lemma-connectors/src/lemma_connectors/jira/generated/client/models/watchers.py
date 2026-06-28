from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user_details import UserDetails





T = TypeVar("T", bound="Watchers")



@_attrs_define
class Watchers:
    """ The details of watchers on an issue.

        Attributes:
            is_watching (bool | Unset): Whether the calling user is watching this issue.
            self_ (str | Unset): The URL of these issue watcher details.
            watch_count (int | Unset): The number of users watching this issue.
            watchers (list[UserDetails] | Unset): Details of the users watching this issue.
     """

    is_watching: bool | Unset = UNSET
    self_: str | Unset = UNSET
    watch_count: int | Unset = UNSET
    watchers: list[UserDetails] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_details import UserDetails
        is_watching = self.is_watching

        self_ = self.self_

        watch_count = self.watch_count

        watchers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.watchers, Unset):
            watchers = []
            for watchers_item_data in self.watchers:
                watchers_item = watchers_item_data.to_dict()
                watchers.append(watchers_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_watching is not UNSET:
            field_dict["isWatching"] = is_watching
        if self_ is not UNSET:
            field_dict["self"] = self_
        if watch_count is not UNSET:
            field_dict["watchCount"] = watch_count
        if watchers is not UNSET:
            field_dict["watchers"] = watchers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_details import UserDetails
        d = dict(src_dict)
        is_watching = d.pop("isWatching", UNSET)

        self_ = d.pop("self", UNSET)

        watch_count = d.pop("watchCount", UNSET)

        _watchers = d.pop("watchers", UNSET)
        watchers: list[UserDetails] | Unset = UNSET
        if _watchers is not UNSET:
            watchers = []
            for watchers_item_data in _watchers:
                watchers_item = UserDetails.from_dict(watchers_item_data)



                watchers.append(watchers_item)


        watchers = cls(
            is_watching=is_watching,
            self_=self_,
            watch_count=watch_count,
            watchers=watchers,
        )

        return watchers

