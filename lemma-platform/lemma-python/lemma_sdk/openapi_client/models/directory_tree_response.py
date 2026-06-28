from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.directory_tree_node import DirectoryTreeNode


T = TypeVar("T", bound="DirectoryTreeResponse")


@_attrs_define
class DirectoryTreeResponse:
    """
    Attributes:
        files_per_directory (int):
        root_path (str):
        tree (DirectoryTreeNode):
    """

    files_per_directory: int
    root_path: str
    tree: DirectoryTreeNode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files_per_directory = self.files_per_directory

        root_path = self.root_path

        tree = self.tree.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files_per_directory": files_per_directory,
                "root_path": root_path,
                "tree": tree,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.directory_tree_node import DirectoryTreeNode

        d = dict(src_dict)
        files_per_directory = d.pop("files_per_directory")

        root_path = d.pop("root_path")

        tree = DirectoryTreeNode.from_dict(d.pop("tree"))

        directory_tree_response = cls(
            files_per_directory=files_per_directory,
            root_path=root_path,
            tree=tree,
        )

        directory_tree_response.additional_properties = d
        return directory_tree_response

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
