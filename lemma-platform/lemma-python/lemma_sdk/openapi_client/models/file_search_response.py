from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_method import SearchMethod

if TYPE_CHECKING:
    from ..models.file_search_result_schema import FileSearchResultSchema


T = TypeVar("T", bound="FileSearchResponse")


@_attrs_define
class FileSearchResponse:
    """
    Attributes:
        items (list[FileSearchResultSchema]):
        query (str):
        search_method (SearchMethod):
        total (int):
    """

    items: list[FileSearchResultSchema]
    query: str
    search_method: SearchMethod
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        query = self.query

        search_method = self.search_method.value

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "query": query,
                "search_method": search_method,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_search_result_schema import FileSearchResultSchema

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = FileSearchResultSchema.from_dict(items_item_data)

            items.append(items_item)

        query = d.pop("query")

        search_method = SearchMethod(d.pop("search_method"))

        total = d.pop("total")

        file_search_response = cls(
            items=items,
            query=query,
            search_method=search_method,
            total=total,
        )

        file_search_response.additional_properties = d
        return file_search_response

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
