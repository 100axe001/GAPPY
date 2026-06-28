from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.worklog import Worklog





T = TypeVar("T", bound="PageOfWorklogs")



@_attrs_define
class PageOfWorklogs:
    """ Paginated list of worklog details

        Attributes:
            max_results (int | Unset): The maximum number of results that could be on the page.
            start_at (int | Unset): The index of the first item returned on the page.
            total (int | Unset): The number of results on the page.
            worklogs (list[Worklog] | Unset): List of worklogs.
     """

    max_results: int | Unset = UNSET
    start_at: int | Unset = UNSET
    total: int | Unset = UNSET
    worklogs: list[Worklog] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.worklog import Worklog
        max_results = self.max_results

        start_at = self.start_at

        total = self.total

        worklogs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.worklogs, Unset):
            worklogs = []
            for worklogs_item_data in self.worklogs:
                worklogs_item = worklogs_item_data.to_dict()
                worklogs.append(worklogs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if total is not UNSET:
            field_dict["total"] = total
        if worklogs is not UNSET:
            field_dict["worklogs"] = worklogs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worklog import Worklog
        d = dict(src_dict)
        max_results = d.pop("maxResults", UNSET)

        start_at = d.pop("startAt", UNSET)

        total = d.pop("total", UNSET)

        _worklogs = d.pop("worklogs", UNSET)
        worklogs: list[Worklog] | Unset = UNSET
        if _worklogs is not UNSET:
            worklogs = []
            for worklogs_item_data in _worklogs:
                worklogs_item = Worklog.from_dict(worklogs_item_data)



                worklogs.append(worklogs_item)


        page_of_worklogs = cls(
            max_results=max_results,
            start_at=start_at,
            total=total,
            worklogs=worklogs,
        )


        page_of_worklogs.additional_properties = d
        return page_of_worklogs

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
