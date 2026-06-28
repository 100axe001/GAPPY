from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.drive import Drive
  from ..models.file import File
  from ..models.team_drive import TeamDrive





T = TypeVar("T", bound="Change")



@_attrs_define
class Change:
    """ A change to a file or shared drive.

        Attributes:
            change_type (str | Unset): The type of the change. Possible values are file and drive.
            drive (Drive | Unset): Representation of a shared drive.
            drive_id (str | Unset): The ID of the shared drive associated with this change.
            file (File | Unset): The metadata for a file.
            file_id (str | Unset): The ID of the file which has changed.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#change". Default:
                'drive#change'.
            removed (bool | Unset): Whether the file or shared drive has been removed from this list of changes, for example
                by deletion or loss of access.
            team_drive (TeamDrive | Unset): Deprecated: use the drive collection instead.
            team_drive_id (str | Unset): Deprecated - use driveId instead.
            time (datetime.datetime | Unset): The time of this change (RFC 3339 date-time).
            type_ (str | Unset): Deprecated - use changeType instead.
     """

    change_type: str | Unset = UNSET
    drive: Drive | Unset = UNSET
    drive_id: str | Unset = UNSET
    file: File | Unset = UNSET
    file_id: str | Unset = UNSET
    kind: str | Unset = 'drive#change'
    removed: bool | Unset = UNSET
    team_drive: TeamDrive | Unset = UNSET
    team_drive_id: str | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.drive import Drive
        from ..models.file import File
        from ..models.team_drive import TeamDrive
        change_type = self.change_type

        drive: dict[str, Any] | Unset = UNSET
        if not isinstance(self.drive, Unset):
            drive = self.drive.to_dict()

        drive_id = self.drive_id

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        file_id = self.file_id

        kind = self.kind

        removed = self.removed

        team_drive: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team_drive, Unset):
            team_drive = self.team_drive.to_dict()

        team_drive_id = self.team_drive_id

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if change_type is not UNSET:
            field_dict["changeType"] = change_type
        if drive is not UNSET:
            field_dict["drive"] = drive
        if drive_id is not UNSET:
            field_dict["driveId"] = drive_id
        if file is not UNSET:
            field_dict["file"] = file
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if removed is not UNSET:
            field_dict["removed"] = removed
        if team_drive is not UNSET:
            field_dict["teamDrive"] = team_drive
        if team_drive_id is not UNSET:
            field_dict["teamDriveId"] = team_drive_id
        if time is not UNSET:
            field_dict["time"] = time
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drive import Drive
        from ..models.file import File
        from ..models.team_drive import TeamDrive
        d = dict(src_dict)
        change_type = d.pop("changeType", UNSET)

        _drive = d.pop("drive", UNSET)
        drive: Drive | Unset
        if isinstance(_drive,  Unset):
            drive = UNSET
        else:
            drive = Drive.from_dict(_drive)




        drive_id = d.pop("driveId", UNSET)

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file,  Unset):
            file = UNSET
        else:
            file = File.from_dict(_file)




        file_id = d.pop("fileId", UNSET)

        kind = d.pop("kind", UNSET)

        removed = d.pop("removed", UNSET)

        _team_drive = d.pop("teamDrive", UNSET)
        team_drive: TeamDrive | Unset
        if isinstance(_team_drive,  Unset):
            team_drive = UNSET
        else:
            team_drive = TeamDrive.from_dict(_team_drive)




        team_drive_id = d.pop("teamDriveId", UNSET)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = isoparse(_time)




        type_ = d.pop("type", UNSET)

        change = cls(
            change_type=change_type,
            drive=drive,
            drive_id=drive_id,
            file=file,
            file_id=file_id,
            kind=kind,
            removed=removed,
            team_drive=team_drive,
            team_drive_id=team_drive_id,
            time=time,
            type_=type_,
        )


        change.additional_properties = d
        return change

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
