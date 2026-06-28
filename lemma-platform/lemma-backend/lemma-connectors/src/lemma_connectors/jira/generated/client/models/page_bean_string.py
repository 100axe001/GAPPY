from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PageBeanString")



@_attrs_define
class PageBeanString:
    """ A page of items.

        Attributes:
            is_last (bool | Unset): Whether this is the last page.
            max_results (int | Unset): The maximum number of items that could be returned.
            next_page (str | Unset): If there is another page of results, the URL of the next page.
            self_ (str | Unset): The URL of the page.
            start_at (int | Unset): The index of the first item returned.
            total (int | Unset): The number of items returned.
            values (list[str] | Unset): The list of items.
     """

    is_last: bool | Unset = UNSET
    max_results: int | Unset = UNSET
    next_page: str | Unset = UNSET
    self_: str | Unset = UNSET
    start_at: int | Unset = UNSET
    total: int | Unset = UNSET
    values: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_last = self.is_last

        max_results = self.max_results

        next_page = self.next_page

        self_ = self.self_

        start_at = self.start_at

        total = self.total

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_last is not UNSET:
            field_dict["isLast"] = is_last
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if next_page is not UNSET:
            field_dict["nextPage"] = next_page
        if self_ is not UNSET:
            field_dict["self"] = self_
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if total is not UNSET:
            field_dict["total"] = total
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_last = d.pop("isLast", UNSET)

        max_results = d.pop("maxResults", UNSET)

        next_page = d.pop("nextPage", UNSET)

        self_ = d.pop("self", UNSET)

        start_at = d.pop("startAt", UNSET)

        total = d.pop("total", UNSET)

        values = cast(list[str], d.pop("values", UNSET))


        page_bean_string = cls(
            is_last=is_last,
            max_results=max_results,
            next_page=next_page,
            self_=self_,
            start_at=start_at,
            total=total,
            values=values,
        )

        return page_bean_string

