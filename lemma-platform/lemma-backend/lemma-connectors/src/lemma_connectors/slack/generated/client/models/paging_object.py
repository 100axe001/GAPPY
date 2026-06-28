from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PagingObject")



@_attrs_define
class PagingObject:
    """ 
        Attributes:
            page (int):
            total (int):
            count (int | Unset):
            pages (int | Unset):
            per_page (int | Unset):
            spill (int | Unset):
     """

    page: int
    total: int
    count: int | Unset = UNSET
    pages: int | Unset = UNSET
    per_page: int | Unset = UNSET
    spill: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        page = self.page

        total = self.total

        count = self.count

        pages = self.pages

        per_page = self.per_page

        spill = self.spill


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "page": page,
            "total": total,
        })
        if count is not UNSET:
            field_dict["count"] = count
        if pages is not UNSET:
            field_dict["pages"] = pages
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if spill is not UNSET:
            field_dict["spill"] = spill

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page")

        total = d.pop("total")

        count = d.pop("count", UNSET)

        pages = d.pop("pages", UNSET)

        per_page = d.pop("per_page", UNSET)

        spill = d.pop("spill", UNSET)

        paging_object = cls(
            page=page,
            total=total,
            count=count,
            pages=pages,
            per_page=per_page,
            spill=spill,
        )

        return paging_object

