from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.team_drive import TeamDrive





T = TypeVar("T", bound="TeamDriveList")



@_attrs_define
class TeamDriveList:
    """ A list of Team Drives.

        Attributes:
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#teamDriveList".
                Default: 'drive#teamDriveList'.
            next_page_token (str | Unset): The page token for the next page of Team Drives. This will be absent if the end
                of the Team Drives list has been reached. If the token is rejected for any reason, it should be discarded, and
                pagination should be restarted from the first page of results.
            team_drives (list[TeamDrive] | Unset): The list of Team Drives. If nextPageToken is populated, then this list
                may be incomplete and an additional page of results should be fetched.
     """

    kind: str | Unset = 'drive#teamDriveList'
    next_page_token: str | Unset = UNSET
    team_drives: list[TeamDrive] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_drive import TeamDrive
        kind = self.kind

        next_page_token = self.next_page_token

        team_drives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.team_drives, Unset):
            team_drives = []
            for team_drives_item_data in self.team_drives:
                team_drives_item = team_drives_item_data.to_dict()
                team_drives.append(team_drives_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if team_drives is not UNSET:
            field_dict["teamDrives"] = team_drives

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_drive import TeamDrive
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        _team_drives = d.pop("teamDrives", UNSET)
        team_drives: list[TeamDrive] | Unset = UNSET
        if _team_drives is not UNSET:
            team_drives = []
            for team_drives_item_data in _team_drives:
                team_drives_item = TeamDrive.from_dict(team_drives_item_data)



                team_drives.append(team_drives_item)


        team_drive_list = cls(
            kind=kind,
            next_page_token=next_page_token,
            team_drives=team_drives,
        )


        team_drive_list.additional_properties = d
        return team_drive_list

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
