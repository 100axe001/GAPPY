from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DirectoryTreeNode")


@_attrs_define
class DirectoryTreeNode:
    """
    Attributes:
        kind (str):
        name (str):
        path (str):
        children (list[DirectoryTreeNode] | Unset):
        has_more_files (bool | Unset):  Default: False.
        visibility (None | str | Unset):
    """

    kind: str
    name: str
    path: str
    children: list[DirectoryTreeNode] | Unset = UNSET
    has_more_files: bool | Unset = False
    visibility: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        name = self.name

        path = self.path

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        has_more_files = self.has_more_files

        visibility: None | str | Unset
        if isinstance(self.visibility, Unset):
            visibility = UNSET
        else:
            visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "path": path,
            }
        )
        if children is not UNSET:
            field_dict["children"] = children
        if has_more_files is not UNSET:
            field_dict["has_more_files"] = has_more_files
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

        name = d.pop("name")

        path = d.pop("path")

        _children = d.pop("children", UNSET)
        children: list[DirectoryTreeNode] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = DirectoryTreeNode.from_dict(children_item_data)

                children.append(children_item)

        has_more_files = d.pop("has_more_files", UNSET)

        def _parse_visibility(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visibility = _parse_visibility(d.pop("visibility", UNSET))

        directory_tree_node = cls(
            kind=kind,
            name=name,
            path=path,
            children=children,
            has_more_files=has_more_files,
            visibility=visibility,
        )

        directory_tree_node.additional_properties = d
        return directory_tree_node

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
