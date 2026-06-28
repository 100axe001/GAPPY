from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.changelog import Changelog





T = TypeVar("T", bound="PageOfChangelogs")



@_attrs_define
class PageOfChangelogs:
    """ A page of changelogs.

        Attributes:
            histories (list[Changelog] | Unset): The list of changelogs.
            max_results (int | Unset): The maximum number of results that could be on the page.
            start_at (int | Unset): The index of the first item returned on the page.
            total (int | Unset): The number of results on the page.
     """

    histories: list[Changelog] | Unset = UNSET
    max_results: int | Unset = UNSET
    start_at: int | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.changelog import Changelog
        histories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.histories, Unset):
            histories = []
            for histories_item_data in self.histories:
                histories_item = histories_item_data.to_dict()
                histories.append(histories_item)



        max_results = self.max_results

        start_at = self.start_at

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if histories is not UNSET:
            field_dict["histories"] = histories
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.changelog import Changelog
        d = dict(src_dict)
        _histories = d.pop("histories", UNSET)
        histories: list[Changelog] | Unset = UNSET
        if _histories is not UNSET:
            histories = []
            for histories_item_data in _histories:
                histories_item = Changelog.from_dict(histories_item_data)



                histories.append(histories_item)


        max_results = d.pop("maxResults", UNSET)

        start_at = d.pop("startAt", UNSET)

        total = d.pop("total", UNSET)

        page_of_changelogs = cls(
            histories=histories,
            max_results=max_results,
            start_at=start_at,
            total=total,
        )

        return page_of_changelogs

