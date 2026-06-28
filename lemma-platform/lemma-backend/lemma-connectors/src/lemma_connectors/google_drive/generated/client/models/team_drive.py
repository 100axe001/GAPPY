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
  from ..models.team_drive_background_image_file import TeamDriveBackgroundImageFile
  from ..models.team_drive_capabilities import TeamDriveCapabilities
  from ..models.team_drive_restrictions import TeamDriveRestrictions





T = TypeVar("T", bound="TeamDrive")



@_attrs_define
class TeamDrive:
    """ Deprecated: use the drive collection instead.

        Attributes:
            background_image_file (TeamDriveBackgroundImageFile | Unset): An image file and cropping parameters from which a
                background image for this Team Drive is set. This is a write only field; it can only be set on
                drive.teamdrives.update requests that don't set themeId. When specified, all fields of the backgroundImageFile
                must be set.
            background_image_link (str | Unset): A short-lived link to this Team Drive's background image.
            capabilities (TeamDriveCapabilities | Unset): Capabilities the current user has on this Team Drive.
            color_rgb (str | Unset): The color of this Team Drive as an RGB hex string. It can only be set on a
                drive.teamdrives.update request that does not set themeId.
            created_time (datetime.datetime | Unset): The time at which the Team Drive was created (RFC 3339 date-time).
            id (str | Unset): The ID of this Team Drive which is also the ID of the top level folder of this Team Drive.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#teamDrive".
                Default: 'drive#teamDrive'.
            name (str | Unset): The name of this Team Drive.
            org_unit_id (str | Unset): The organizational unit of this shared drive. This field is only populated on
                drives.list responses when the useDomainAdminAccess parameter is set to true.
            restrictions (TeamDriveRestrictions | Unset): A set of restrictions that apply to this Team Drive or items
                inside this Team Drive.
            theme_id (str | Unset): The ID of the theme from which the background image and color will be set. The set of
                possible teamDriveThemes can be retrieved from a drive.about.get response. When not specified on a
                drive.teamdrives.create request, a random theme is chosen from which the background image and color are set.
                This is a write-only field; it can only be set on requests that don't set colorRgb or backgroundImageFile.
     """

    background_image_file: TeamDriveBackgroundImageFile | Unset = UNSET
    background_image_link: str | Unset = UNSET
    capabilities: TeamDriveCapabilities | Unset = UNSET
    color_rgb: str | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'drive#teamDrive'
    name: str | Unset = UNSET
    org_unit_id: str | Unset = UNSET
    restrictions: TeamDriveRestrictions | Unset = UNSET
    theme_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_drive_background_image_file import TeamDriveBackgroundImageFile
        from ..models.team_drive_capabilities import TeamDriveCapabilities
        from ..models.team_drive_restrictions import TeamDriveRestrictions
        background_image_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_image_file, Unset):
            background_image_file = self.background_image_file.to_dict()

        background_image_link = self.background_image_link

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        color_rgb = self.color_rgb

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        id = self.id

        kind = self.kind

        name = self.name

        org_unit_id = self.org_unit_id

        restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        theme_id = self.theme_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_image_file is not UNSET:
            field_dict["backgroundImageFile"] = background_image_file
        if background_image_link is not UNSET:
            field_dict["backgroundImageLink"] = background_image_link
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if color_rgb is not UNSET:
            field_dict["colorRgb"] = color_rgb
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if org_unit_id is not UNSET:
            field_dict["orgUnitId"] = org_unit_id
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if theme_id is not UNSET:
            field_dict["themeId"] = theme_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_drive_background_image_file import TeamDriveBackgroundImageFile
        from ..models.team_drive_capabilities import TeamDriveCapabilities
        from ..models.team_drive_restrictions import TeamDriveRestrictions
        d = dict(src_dict)
        _background_image_file = d.pop("backgroundImageFile", UNSET)
        background_image_file: TeamDriveBackgroundImageFile | Unset
        if isinstance(_background_image_file,  Unset):
            background_image_file = UNSET
        else:
            background_image_file = TeamDriveBackgroundImageFile.from_dict(_background_image_file)




        background_image_link = d.pop("backgroundImageLink", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: TeamDriveCapabilities | Unset
        if isinstance(_capabilities,  Unset):
            capabilities = UNSET
        else:
            capabilities = TeamDriveCapabilities.from_dict(_capabilities)




        color_rgb = d.pop("colorRgb", UNSET)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time,  Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)




        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        name = d.pop("name", UNSET)

        org_unit_id = d.pop("orgUnitId", UNSET)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: TeamDriveRestrictions | Unset
        if isinstance(_restrictions,  Unset):
            restrictions = UNSET
        else:
            restrictions = TeamDriveRestrictions.from_dict(_restrictions)




        theme_id = d.pop("themeId", UNSET)

        team_drive = cls(
            background_image_file=background_image_file,
            background_image_link=background_image_link,
            capabilities=capabilities,
            color_rgb=color_rgb,
            created_time=created_time,
            id=id,
            kind=kind,
            name=name,
            org_unit_id=org_unit_id,
            restrictions=restrictions,
            theme_id=theme_id,
        )


        team_drive.additional_properties = d
        return team_drive

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
