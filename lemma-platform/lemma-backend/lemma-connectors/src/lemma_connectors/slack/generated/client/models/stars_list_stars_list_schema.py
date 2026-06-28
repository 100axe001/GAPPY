from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.paging_object import PagingObject





T = TypeVar("T", bound="StarsListStarsListSchema")



@_attrs_define
class StarsListStarsListSchema:
    """ Schema for successful response from stars.list method

        Attributes:
            items (list[Any]):
            ok (bool):
            paging (PagingObject | Unset):
     """

    items: list[Any]
    ok: bool
    paging: PagingObject | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.paging_object import PagingObject
        items = self.items



        ok = self.ok

        paging: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paging, Unset):
            paging = self.paging.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "items": items,
            "ok": ok,
        })
        if paging is not UNSET:
            field_dict["paging"] = paging

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paging_object import PagingObject
        d = dict(src_dict)
        items = cast(list[Any], d.pop("items"))


        ok = d.pop("ok")

        _paging = d.pop("paging", UNSET)
        paging: PagingObject | Unset
        if isinstance(_paging,  Unset):
            paging = UNSET
        else:
            paging = PagingObject.from_dict(_paging)




        stars_list_stars_list_schema = cls(
            items=items,
            ok=ok,
            paging=paging,
        )

        return stars_list_stars_list_schema

