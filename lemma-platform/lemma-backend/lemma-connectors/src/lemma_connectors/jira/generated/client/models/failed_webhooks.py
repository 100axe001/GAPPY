from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.failed_webhook import FailedWebhook





T = TypeVar("T", bound="FailedWebhooks")



@_attrs_define
class FailedWebhooks:
    """ A page of failed webhooks.

        Attributes:
            max_results (int): The maximum number of items on the page. If the list of values is shorter than this number,
                then there are no more pages.
            values (list[FailedWebhook]): The list of webhooks.
            next_ (str | Unset): The URL to the next page of results. Present only if the request returned at least one
                result.The next page may be empty at the time of receiving the response, but new failed webhooks may appear in
                time. You can save the URL to the next page and query for new results periodically (for example, every hour).
     """

    max_results: int
    values: list[FailedWebhook]
    next_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.failed_webhook import FailedWebhook
        max_results = self.max_results

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)



        next_ = self.next_


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "maxResults": max_results,
            "values": values,
        })
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failed_webhook import FailedWebhook
        d = dict(src_dict)
        max_results = d.pop("maxResults")

        values = []
        _values = d.pop("values")
        for values_item_data in (_values):
            values_item = FailedWebhook.from_dict(values_item_data)



            values.append(values_item)


        next_ = d.pop("next", UNSET)

        failed_webhooks = cls(
            max_results=max_results,
            values=values,
            next_=next_,
        )

        return failed_webhooks

