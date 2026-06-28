from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.developer_metadata import DeveloperMetadata





T = TypeVar("T", bound="DeleteDeveloperMetadataResponse")



@_attrs_define
class DeleteDeveloperMetadataResponse:
    """ The response from deleting developer metadata.

        Attributes:
            deleted_developer_metadata (list[DeveloperMetadata] | Unset): The metadata that was deleted.
     """

    deleted_developer_metadata: list[DeveloperMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.developer_metadata import DeveloperMetadata
        deleted_developer_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.deleted_developer_metadata, Unset):
            deleted_developer_metadata = []
            for deleted_developer_metadata_item_data in self.deleted_developer_metadata:
                deleted_developer_metadata_item = deleted_developer_metadata_item_data.to_dict()
                deleted_developer_metadata.append(deleted_developer_metadata_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if deleted_developer_metadata is not UNSET:
            field_dict["deletedDeveloperMetadata"] = deleted_developer_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_metadata import DeveloperMetadata
        d = dict(src_dict)
        _deleted_developer_metadata = d.pop("deletedDeveloperMetadata", UNSET)
        deleted_developer_metadata: list[DeveloperMetadata] | Unset = UNSET
        if _deleted_developer_metadata is not UNSET:
            deleted_developer_metadata = []
            for deleted_developer_metadata_item_data in _deleted_developer_metadata:
                deleted_developer_metadata_item = DeveloperMetadata.from_dict(deleted_developer_metadata_item_data)



                deleted_developer_metadata.append(deleted_developer_metadata_item)


        delete_developer_metadata_response = cls(
            deleted_developer_metadata=deleted_developer_metadata,
        )


        delete_developer_metadata_response.additional_properties = d
        return delete_developer_metadata_response

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
