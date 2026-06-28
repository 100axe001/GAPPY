from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.thread import Thread





T = TypeVar("T", bound="ListThreadsResponse")



@_attrs_define
class ListThreadsResponse:
    """ 
        Attributes:
            next_page_token (str | Unset): Page token to retrieve the next page of results in the list.
            result_size_estimate (int | Unset): Estimated total number of results.
            threads (list[Thread] | Unset): List of threads. Note that each thread resource does not contain a list of
                `messages`. The list of `messages` for a given thread can be fetched using the threads.get method.
     """

    next_page_token: str | Unset = UNSET
    result_size_estimate: int | Unset = UNSET
    threads: list[Thread] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.thread import Thread
        next_page_token = self.next_page_token

        result_size_estimate = self.result_size_estimate

        threads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.threads, Unset):
            threads = []
            for threads_item_data in self.threads:
                threads_item = threads_item_data.to_dict()
                threads.append(threads_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if result_size_estimate is not UNSET:
            field_dict["resultSizeEstimate"] = result_size_estimate
        if threads is not UNSET:
            field_dict["threads"] = threads

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thread import Thread
        d = dict(src_dict)
        next_page_token = d.pop("nextPageToken", UNSET)

        result_size_estimate = d.pop("resultSizeEstimate", UNSET)

        _threads = d.pop("threads", UNSET)
        threads: list[Thread] | Unset = UNSET
        if _threads is not UNSET:
            threads = []
            for threads_item_data in _threads:
                threads_item = Thread.from_dict(threads_item_data)



                threads.append(threads_item)


        list_threads_response = cls(
            next_page_token=next_page_token,
            result_size_estimate=result_size_estimate,
            threads=threads,
        )


        list_threads_response.additional_properties = d
        return list_threads_response

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
