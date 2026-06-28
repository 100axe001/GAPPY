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





T = TypeVar("T", bound="CreateDeveloperMetadataRequest")



@_attrs_define
class CreateDeveloperMetadataRequest:
    """ A request to create developer metadata.

        Attributes:
            developer_metadata (DeveloperMetadata | Unset): Developer metadata associated with a location or object in a
                spreadsheet. Developer metadata may be used to associate arbitrary data with various parts of a spreadsheet and
                will remain associated at those locations as they move around and the spreadsheet is edited. For example, if
                developer metadata is associated with row 5 and another row is then subsequently inserted above row 5, that
                original metadata will still be associated with the row it was first associated with (what is now row 6). If the
                associated object is deleted its metadata is deleted too.
     """

    developer_metadata: DeveloperMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.developer_metadata import DeveloperMetadata
        developer_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.developer_metadata, Unset):
            developer_metadata = self.developer_metadata.to_dict()


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
        developer_metadata: DeveloperMetadata | Unset
        if isinstance(_developer_metadata,  Unset):
            developer_metadata = UNSET
        else:
            developer_metadata = DeveloperMetadata.from_dict(_developer_metadata)




        create_developer_metadata_request = cls(
            developer_metadata=developer_metadata,
        )


        create_developer_metadata_request.additional_properties = d
        return create_developer_metadata_request

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
