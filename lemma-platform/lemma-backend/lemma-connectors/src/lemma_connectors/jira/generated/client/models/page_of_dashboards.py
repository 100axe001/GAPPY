from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dashboard import Dashboard





T = TypeVar("T", bound="PageOfDashboards")



@_attrs_define
class PageOfDashboards:
    """ A page containing dashboard details.

        Attributes:
            dashboards (list[Dashboard] | Unset): List of dashboards.
            max_results (int | Unset): The maximum number of results that could be on the page.
            next_ (str | Unset): The URL of the next page of results, if any.
            prev (str | Unset): The URL of the previous page of results, if any.
            start_at (int | Unset): The index of the first item returned on the page.
            total (int | Unset): The number of results on the page.
     """

    dashboards: list[Dashboard] | Unset = UNSET
    max_results: int | Unset = UNSET
    next_: str | Unset = UNSET
    prev: str | Unset = UNSET
    start_at: int | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard import Dashboard
        dashboards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dashboards, Unset):
            dashboards = []
            for dashboards_item_data in self.dashboards:
                dashboards_item = dashboards_item_data.to_dict()
                dashboards.append(dashboards_item)



        max_results = self.max_results

        next_ = self.next_

        prev = self.prev

        start_at = self.start_at

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if dashboards is not UNSET:
            field_dict["dashboards"] = dashboards
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if next_ is not UNSET:
            field_dict["next"] = next_
        if prev is not UNSET:
            field_dict["prev"] = prev
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard import Dashboard
        d = dict(src_dict)
        _dashboards = d.pop("dashboards", UNSET)
        dashboards: list[Dashboard] | Unset = UNSET
        if _dashboards is not UNSET:
            dashboards = []
            for dashboards_item_data in _dashboards:
                dashboards_item = Dashboard.from_dict(dashboards_item_data)



                dashboards.append(dashboards_item)


        max_results = d.pop("maxResults", UNSET)

        next_ = d.pop("next", UNSET)

        prev = d.pop("prev", UNSET)

        start_at = d.pop("startAt", UNSET)

        total = d.pop("total", UNSET)

        page_of_dashboards = cls(
            dashboards=dashboards,
            max_results=max_results,
            next_=next_,
            prev=prev,
            start_at=start_at,
            total=total,
        )

        return page_of_dashboards

