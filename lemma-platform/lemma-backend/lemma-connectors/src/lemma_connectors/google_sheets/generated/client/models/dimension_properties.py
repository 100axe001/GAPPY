from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_column_reference import DataSourceColumnReference
  from ..models.developer_metadata import DeveloperMetadata





T = TypeVar("T", bound="DimensionProperties")



@_attrs_define
class DimensionProperties:
    """ Properties about a dimension.

        Attributes:
            data_source_column_reference (DataSourceColumnReference | Unset): An unique identifier that references a data
                source column.
            developer_metadata (list[DeveloperMetadata] | Unset): The developer metadata associated with a single row or
                column.
            hidden_by_filter (bool | Unset): True if this dimension is being filtered. This field is read-only.
            hidden_by_user (bool | Unset): True if this dimension is explicitly hidden.
            pixel_size (int | Unset): The height (if a row) or width (if a column) of the dimension in pixels.
     """

    data_source_column_reference: DataSourceColumnReference | Unset = UNSET
    developer_metadata: list[DeveloperMetadata] | Unset = UNSET
    hidden_by_filter: bool | Unset = UNSET
    hidden_by_user: bool | Unset = UNSET
    pixel_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.developer_metadata import DeveloperMetadata
        data_source_column_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_column_reference, Unset):
            data_source_column_reference = self.data_source_column_reference.to_dict()

        developer_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.developer_metadata, Unset):
            developer_metadata = []
            for developer_metadata_item_data in self.developer_metadata:
                developer_metadata_item = developer_metadata_item_data.to_dict()
                developer_metadata.append(developer_metadata_item)



        hidden_by_filter = self.hidden_by_filter

        hidden_by_user = self.hidden_by_user

        pixel_size = self.pixel_size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_source_column_reference is not UNSET:
            field_dict["dataSourceColumnReference"] = data_source_column_reference
        if developer_metadata is not UNSET:
            field_dict["developerMetadata"] = developer_metadata
        if hidden_by_filter is not UNSET:
            field_dict["hiddenByFilter"] = hidden_by_filter
        if hidden_by_user is not UNSET:
            field_dict["hiddenByUser"] = hidden_by_user
        if pixel_size is not UNSET:
            field_dict["pixelSize"] = pixel_size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.developer_metadata import DeveloperMetadata
        d = dict(src_dict)
        _data_source_column_reference = d.pop("dataSourceColumnReference", UNSET)
        data_source_column_reference: DataSourceColumnReference | Unset
        if isinstance(_data_source_column_reference,  Unset):
            data_source_column_reference = UNSET
        else:
            data_source_column_reference = DataSourceColumnReference.from_dict(_data_source_column_reference)




        _developer_metadata = d.pop("developerMetadata", UNSET)
        developer_metadata: list[DeveloperMetadata] | Unset = UNSET
        if _developer_metadata is not UNSET:
            developer_metadata = []
            for developer_metadata_item_data in _developer_metadata:
                developer_metadata_item = DeveloperMetadata.from_dict(developer_metadata_item_data)



                developer_metadata.append(developer_metadata_item)


        hidden_by_filter = d.pop("hiddenByFilter", UNSET)

        hidden_by_user = d.pop("hiddenByUser", UNSET)

        pixel_size = d.pop("pixelSize", UNSET)

        dimension_properties = cls(
            data_source_column_reference=data_source_column_reference,
            developer_metadata=developer_metadata,
            hidden_by_filter=hidden_by_filter,
            hidden_by_user=hidden_by_user,
            pixel_size=pixel_size,
        )


        dimension_properties.additional_properties = d
        return dimension_properties

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
