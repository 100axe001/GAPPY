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





T = TypeVar("T", bound="DeleteDeveloperMetadataRequest")



@_attrs_define
class DeleteDeveloperMetadataRequest:
    """ A request to delete developer metadata.

        Attributes:
            data_filter (DataFilter | Unset): Filter that describes what data should be selected or returned from a request.
     """

    data_filter: DataFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_filter import DataFilter
        data_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_filter, Unset):
            data_filter = self.data_filter.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_filter is not UNSET:
            field_dict["dataFilter"] = data_filter

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_filter import DataFilter
        d = dict(src_dict)
        _data_filter = d.pop("dataFilter", UNSET)
        data_filter: DataFilter | Unset
        if isinstance(_data_filter,  Unset):
            data_filter = UNSET
        else:
            data_filter = DataFilter.from_dict(_data_filter)




        delete_developer_metadata_request = cls(
            data_filter=data_filter,
        )


        delete_developer_metadata_request.additional_properties = d
        return delete_developer_metadata_request

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
