from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.changed_worklog import ChangedWorklog





T = TypeVar("T", bound="ChangedWorklogs")



@_attrs_define
class ChangedWorklogs:
    """ List of changed worklogs.

        Attributes:
            last_page (bool | Unset):
            next_page (str | Unset): The URL of the next list of changed worklogs.
            self_ (str | Unset): The URL of this changed worklogs list.
            since (int | Unset): The datetime of the first worklog item in the list.
            until (int | Unset): The datetime of the last worklog item in the list.
            values (list[ChangedWorklog] | Unset): Changed worklog list.
     """

    last_page: bool | Unset = UNSET
    next_page: str | Unset = UNSET
    self_: str | Unset = UNSET
    since: int | Unset = UNSET
    until: int | Unset = UNSET
    values: list[ChangedWorklog] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.changed_worklog import ChangedWorklog
        last_page = self.last_page

        next_page = self.next_page

        self_ = self.self_

        since = self.since

        until = self.until

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if last_page is not UNSET:
            field_dict["lastPage"] = last_page
        if next_page is not UNSET:
            field_dict["nextPage"] = next_page
        if self_ is not UNSET:
            field_dict["self"] = self_
        if since is not UNSET:
            field_dict["since"] = since
        if until is not UNSET:
            field_dict["until"] = until
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.changed_worklog import ChangedWorklog
        d = dict(src_dict)
        last_page = d.pop("lastPage", UNSET)

        next_page = d.pop("nextPage", UNSET)

        self_ = d.pop("self", UNSET)

        since = d.pop("since", UNSET)

        until = d.pop("until", UNSET)

        _values = d.pop("values", UNSET)
        values: list[ChangedWorklog] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = ChangedWorklog.from_dict(values_item_data)



                values.append(values_item)


        changed_worklogs = cls(
            last_page=last_page,
            next_page=next_page,
            self_=self_,
            since=since,
            until=until,
            values=values,
        )

        return changed_worklogs

