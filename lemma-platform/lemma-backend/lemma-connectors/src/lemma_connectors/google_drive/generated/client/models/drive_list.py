from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.drive import Drive





T = TypeVar("T", bound="DriveList")



@_attrs_define
class DriveList:
    """ A list of shared drives.

        Attributes:
            drives (list[Drive] | Unset): The list of shared drives. If nextPageToken is populated, then this list may be
                incomplete and an additional page of results should be fetched.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#driveList".
                Default: 'drive#driveList'.
            next_page_token (str | Unset): The page token for the next page of shared drives. This will be absent if the end
                of the list has been reached. If the token is rejected for any reason, it should be discarded, and pagination
                should be restarted from the first page of results.
     """

    drives: list[Drive] | Unset = UNSET
    kind: str | Unset = 'drive#driveList'
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.drive import Drive
        drives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.drives, Unset):
            drives = []
            for drives_item_data in self.drives:
                drives_item = drives_item_data.to_dict()
                drives.append(drives_item)



        kind = self.kind

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if drives is not UNSET:
            field_dict["drives"] = drives
        if kind is not UNSET:
            field_dict["kind"] = kind
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drive import Drive
        d = dict(src_dict)
        _drives = d.pop("drives", UNSET)
        drives: list[Drive] | Unset = UNSET
        if _drives is not UNSET:
            drives = []
            for drives_item_data in _drives:
                drives_item = Drive.from_dict(drives_item_data)



                drives.append(drives_item)


        kind = d.pop("kind", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        drive_list = cls(
            drives=drives,
            kind=kind,
            next_page_token=next_page_token,
        )


        drive_list.additional_properties = d
        return drive_list

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
