from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_filter import DataFilter
  from ..models.developer_metadata import DeveloperMetadata





T = TypeVar("T", bound="UpdateDeveloperMetadataRequest")



@_attrs_define
class UpdateDeveloperMetadataRequest:
    """ A request to update properties of developer metadata. Updates the properties of the developer metadata selected by
    the filters to the values provided in the DeveloperMetadata resource. Callers must specify the properties they wish
    to update in the fields parameter, as well as specify at least one DataFilter matching the metadata they wish to
    update.

        Attributes:
            data_filters (list[DataFilter] | Unset): The filters matching the developer metadata entries to update.
            developer_metadata (DeveloperMetadata | Unset): Developer metadata associated with a location or object in a
                spreadsheet. Developer metadata may be used to associate arbitrary data with various parts of a spreadsheet and
                will remain associated at those locations as they move around and the spreadsheet is edited. For example, if
                developer metadata is associated with row 5 and another row is then subsequently inserted above row 5, that
                original metadata will still be associated with the row it was first associated with (what is now row 6). If the
                associated object is deleted its metadata is deleted too.
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `developerMetadata` is implied and should not be specified. A single `"*"` can be used as short-hand for listing
                every field.
     """

    data_filters: list[DataFilter] | Unset = UNSET
    developer_metadata: DeveloperMetadata | Unset = UNSET
    fields: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_filter import DataFilter
        from ..models.developer_metadata import DeveloperMetadata
        data_filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_filters, Unset):
            data_filters = []
            for data_filters_item_data in self.data_filters:
                data_filters_item = data_filters_item_data.to_dict()
                data_filters.append(data_filters_item)



        developer_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.developer_metadata, Unset):
            developer_metadata = self.developer_metadata.to_dict()

        fields = self.fields


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_filters is not UNSET:
            field_dict["dataFilters"] = data_filters
        if developer_metadata is not UNSET:
            field_dict["developerMetadata"] = developer_metadata
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_filter import DataFilter
        from ..models.developer_metadata import DeveloperMetadata
        d = dict(src_dict)
        _data_filters = d.pop("dataFilters", UNSET)
        data_filters: list[DataFilter] | Unset = UNSET
        if _data_filters is not UNSET:
            data_filters = []
            for data_filters_item_data in _data_filters:
                data_filters_item = DataFilter.from_dict(data_filters_item_data)



                data_filters.append(data_filters_item)


        _developer_metadata = d.pop("developerMetadata", UNSET)
        developer_metadata: DeveloperMetadata | Unset
        if isinstance(_developer_metadata,  Unset):
            developer_metadata = UNSET
        else:
            developer_metadata = DeveloperMetadata.from_dict(_developer_metadata)




        fields = d.pop("fields", UNSET)

        update_developer_metadata_request = cls(
            data_filters=data_filters,
            developer_metadata=developer_metadata,
            fields=fields,
        )


        update_developer_metadata_request.additional_properties = d
        return update_developer_metadata_request

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
