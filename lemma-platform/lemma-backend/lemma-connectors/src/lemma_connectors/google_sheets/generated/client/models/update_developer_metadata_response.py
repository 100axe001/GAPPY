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





T = TypeVar("T", bound="UpdateDeveloperMetadataResponse")



@_attrs_define
class UpdateDeveloperMetadataResponse:
    """ The response from updating developer metadata.

        Attributes:
            developer_metadata (list[DeveloperMetadata] | Unset): The updated developer metadata.
     """

    developer_metadata: list[DeveloperMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.developer_metadata import DeveloperMetadata
        developer_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.developer_metadata, Unset):
            developer_metadata = []
            for developer_metadata_item_data in self.developer_metadata:
                developer_metadata_item = developer_metadata_item_data.to_dict()
                developer_metadata.append(developer_metadata_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if developer_metadata is not UNSET:
            field_dict["developerMetadata"] = developer_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_metadata import DeveloperMetadata
        d = dict(src_dict)
        _developer_metadata = d.pop("developerMetadata", UNSET)
        developer_metadata: list[DeveloperMetadata] | Unset = UNSET
        if _developer_metadata is not UNSET:
            developer_metadata = []
            for developer_metadata_item_data in _developer_metadata:
                developer_metadata_item = DeveloperMetadata.from_dict(developer_metadata_item_data)



                developer_metadata.append(developer_metadata_item)


        update_developer_metadata_response = cls(
            developer_metadata=developer_metadata,
        )


        update_developer_metadata_response.additional_properties = d
        return update_developer_metadata_response

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
