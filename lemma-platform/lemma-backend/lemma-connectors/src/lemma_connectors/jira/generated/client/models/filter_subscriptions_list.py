from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.filter_subscription import FilterSubscription





T = TypeVar("T", bound="FilterSubscriptionsList")



@_attrs_define
class FilterSubscriptionsList:
    """ A paginated list of subscriptions to a filter.

        Attributes:
            end_index (int | Unset): The index of the last item returned on the page.
            items (list[FilterSubscription] | Unset): The list of items.
            max_results (int | Unset): The maximum number of results that could be on the page.
            size (int | Unset): The number of items on the page.
            start_index (int | Unset): The index of the first item returned on the page.
     """

    end_index: int | Unset = UNSET
    items: list[FilterSubscription] | Unset = UNSET
    max_results: int | Unset = UNSET
    size: int | Unset = UNSET
    start_index: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_subscription import FilterSubscription
        end_index = self.end_index

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        max_results = self.max_results

        size = self.size

        start_index = self.start_index


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if end_index is not UNSET:
            field_dict["end-index"] = end_index
        if items is not UNSET:
            field_dict["items"] = items
        if max_results is not UNSET:
            field_dict["max-results"] = max_results
        if size is not UNSET:
            field_dict["size"] = size
        if start_index is not UNSET:
            field_dict["start-index"] = start_index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_subscription import FilterSubscription
        d = dict(src_dict)
        end_index = d.pop("end-index", UNSET)

        _items = d.pop("items", UNSET)
        items: list[FilterSubscription] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = FilterSubscription.from_dict(items_item_data)



                items.append(items_item)


        max_results = d.pop("max-results", UNSET)

        size = d.pop("size", UNSET)

        start_index = d.pop("start-index", UNSET)

        filter_subscriptions_list = cls(
            end_index=end_index,
            items=items,
            max_results=max_results,
            size=size,
            start_index=start_index,
        )

        return filter_subscriptions_list

