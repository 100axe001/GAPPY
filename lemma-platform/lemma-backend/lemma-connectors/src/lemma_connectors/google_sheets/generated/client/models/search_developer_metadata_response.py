from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.matched_developer_metadata import MatchedDeveloperMetadata





T = TypeVar("T", bound="SearchDeveloperMetadataResponse")



@_attrs_define
class SearchDeveloperMetadataResponse:
    """ A reply to a developer metadata search request.

        Attributes:
            matched_developer_metadata (list[MatchedDeveloperMetadata] | Unset): The metadata matching the criteria of the
                search request.
     """

    matched_developer_metadata: list[MatchedDeveloperMetadata] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.matched_developer_metadata import MatchedDeveloperMetadata
        matched_developer_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matched_developer_metadata, Unset):
            matched_developer_metadata = []
            for matched_developer_metadata_item_data in self.matched_developer_metadata:
                matched_developer_metadata_item = matched_developer_metadata_item_data.to_dict()
                matched_developer_metadata.append(matched_developer_metadata_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if matched_developer_metadata is not UNSET:
            field_dict["matchedDeveloperMetadata"] = matched_developer_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matched_developer_metadata import MatchedDeveloperMetadata
        d = dict(src_dict)
        _matched_developer_metadata = d.pop("matchedDeveloperMetadata", UNSET)
        matched_developer_metadata: list[MatchedDeveloperMetadata] | Unset = UNSET
        if _matched_developer_metadata is not UNSET:
            matched_developer_metadata = []
            for matched_developer_metadata_item_data in _matched_developer_metadata:
                matched_developer_metadata_item = MatchedDeveloperMetadata.from_dict(matched_developer_metadata_item_data)



                matched_developer_metadata.append(matched_developer_metadata_item)


        search_developer_metadata_response = cls(
            matched_developer_metadata=matched_developer_metadata,
        )


        search_developer_metadata_response.additional_properties = d
        return search_developer_metadata_response

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
