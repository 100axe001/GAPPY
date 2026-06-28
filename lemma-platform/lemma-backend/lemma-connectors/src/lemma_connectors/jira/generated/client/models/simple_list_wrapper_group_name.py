from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.group_name import GroupName
  from ..models.list_wrapper_callback_group_name import ListWrapperCallbackGroupName





T = TypeVar("T", bound="SimpleListWrapperGroupName")



@_attrs_define
class SimpleListWrapperGroupName:
    """ 
        Attributes:
            callback (ListWrapperCallbackGroupName | Unset):
            items (list[GroupName] | Unset):
            max_results (int | Unset):
            paging_callback (ListWrapperCallbackGroupName | Unset):
            size (int | Unset):
     """

    callback: ListWrapperCallbackGroupName | Unset = UNSET
    items: list[GroupName] | Unset = UNSET
    max_results: int | Unset = UNSET
    paging_callback: ListWrapperCallbackGroupName | Unset = UNSET
    size: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.group_name import GroupName
        from ..models.list_wrapper_callback_group_name import ListWrapperCallbackGroupName
        callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        max_results = self.max_results

        paging_callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paging_callback, Unset):
            paging_callback = self.paging_callback.to_dict()

        size = self.size


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if callback is not UNSET:
            field_dict["callback"] = callback
        if items is not UNSET:
            field_dict["items"] = items
        if max_results is not UNSET:
            field_dict["max-results"] = max_results
        if paging_callback is not UNSET:
            field_dict["pagingCallback"] = paging_callback
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_name import GroupName
        from ..models.list_wrapper_callback_group_name import ListWrapperCallbackGroupName
        d = dict(src_dict)
        _callback = d.pop("callback", UNSET)
        callback: ListWrapperCallbackGroupName | Unset
        if isinstance(_callback,  Unset):
            callback = UNSET
        else:
            callback = ListWrapperCallbackGroupName.from_dict(_callback)




        _items = d.pop("items", UNSET)
        items: list[GroupName] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = GroupName.from_dict(items_item_data)



                items.append(items_item)


        max_results = d.pop("max-results", UNSET)

        _paging_callback = d.pop("pagingCallback", UNSET)
        paging_callback: ListWrapperCallbackGroupName | Unset
        if isinstance(_paging_callback,  Unset):
            paging_callback = UNSET
        else:
            paging_callback = ListWrapperCallbackGroupName.from_dict(_paging_callback)




        size = d.pop("size", UNSET)

        simple_list_wrapper_group_name = cls(
            callback=callback,
            items=items,
            max_results=max_results,
            paging_callback=paging_callback,
            size=size,
        )

        return simple_list_wrapper_group_name

