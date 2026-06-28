from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_search_scope_mode import FileSearchScopeMode
from ..models.search_method import SearchMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSearchRequest")


@_attrs_define
class FileSearchRequest:
    """
    Attributes:
        query (str):
        limit (int | Unset):  Default: 10.
        scope_mode (FileSearchScopeMode | Unset):
        scope_path (None | str | Unset): Optional folder path to scope search results.
        search_method (SearchMethod | Unset):
    """

    query: str
    limit: int | Unset = 10
    scope_mode: FileSearchScopeMode | Unset = UNSET
    scope_path: None | str | Unset = UNSET
    search_method: SearchMethod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        limit = self.limit

        scope_mode: str | Unset = UNSET
        if not isinstance(self.scope_mode, Unset):
            scope_mode = self.scope_mode.value

        scope_path: None | str | Unset
        if isinstance(self.scope_path, Unset):
            scope_path = UNSET
        else:
            scope_path = self.scope_path

        search_method: str | Unset = UNSET
        if not isinstance(self.search_method, Unset):
            search_method = self.search_method.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if scope_mode is not UNSET:
            field_dict["scope_mode"] = scope_mode
        if scope_path is not UNSET:
            field_dict["scope_path"] = scope_path
        if search_method is not UNSET:
            field_dict["search_method"] = search_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        limit = d.pop("limit", UNSET)

        _scope_mode = d.pop("scope_mode", UNSET)
        scope_mode: FileSearchScopeMode | Unset
        if isinstance(_scope_mode, Unset):
            scope_mode = UNSET
        else:
            scope_mode = FileSearchScopeMode(_scope_mode)

        def _parse_scope_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope_path = _parse_scope_path(d.pop("scope_path", UNSET))

        _search_method = d.pop("search_method", UNSET)
        search_method: SearchMethod | Unset
        if isinstance(_search_method, Unset):
            search_method = UNSET
        else:
            search_method = SearchMethod(_search_method)

        file_search_request = cls(
            query=query,
            limit=limit,
            scope_mode=scope_mode,
            scope_path=scope_path,
            search_method=search_method,
        )

        file_search_request.additional_properties = d
        return file_search_request

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
