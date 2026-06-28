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
  from ..models.drive_background_image_file import DriveBackgroundImageFile
  from ..models.drive_capabilities import DriveCapabilities
  from ..models.drive_restrictions import DriveRestrictions





T = TypeVar("T", bound="Drive")



@_attrs_define
class Drive:
    """ Representation of a shared drive.

        Attributes:
            background_image_file (DriveBackgroundImageFile | Unset): An image file and cropping parameters from which a
                background image for this shared drive is set. This is a write-only field; it can only be set on
                drive.drives.update requests that don't set themeId. When specified, all fields of the backgroundImageFile must
                be set.
            background_image_link (str | Unset): A short-lived link to this shared drive's background image.
            capabilities (DriveCapabilities | Unset): Capabilities the current user has on this shared drive.
            color_rgb (str | Unset): The color of this shared drive as an RGB hex string. It can only be set on
                drive.drives.update requests that don't set themeId.
            created_time (datetime.datetime | Unset): The time at which the shared drive was created (RFC 3339 date-time).
            hidden (bool | Unset): Whether the shared drive is hidden from default view.
            id (str | Unset): The ID of this shared drive which is also the ID of the top level folder of this shared drive.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#drive". Default:
                'drive#drive'.
            name (str | Unset): The name of this shared drive.
            org_unit_id (str | Unset): The organizational unit of this shared drive. This field is only populated on
                drives.list responses when the useDomainAdminAccess parameter is set to true.
            restrictions (DriveRestrictions | Unset): A set of restrictions that apply to this shared drive or items inside
                this shared drive.
            theme_id (str | Unset): The ID of the theme from which the background image and color are set. The set of
                possible driveThemes can be retrieved from a drive.about.get response. When not specified on a
                drive.drives.create request, a random theme is chosen from which the background image and color are set. This is
                a write-only field; it can only be set on requests that don't set colorRgb or backgroundImageFile.
     """

    background_image_file: DriveBackgroundImageFile | Unset = UNSET
    background_image_link: str | Unset = UNSET
    capabilities: DriveCapabilities | Unset = UNSET
    color_rgb: str | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    hidden: bool | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'drive#drive'
    name: str | Unset = UNSET
    org_unit_id: str | Unset = UNSET
    restrictions: DriveRestrictions | Unset = UNSET
    theme_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.drive_background_image_file import DriveBackgroundImageFile
        from ..models.drive_capabilities import DriveCapabilities
        from ..models.drive_restrictions import DriveRestrictions
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

        hidden = self.hidden

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
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
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
        from ..models.drive_background_image_file import DriveBackgroundImageFile
        from ..models.drive_capabilities import DriveCapabilities
        from ..models.drive_restrictions import DriveRestrictions
        d = dict(src_dict)
        _background_image_file = d.pop("backgroundImageFile", UNSET)
        background_image_file: DriveBackgroundImageFile | Unset
        if isinstance(_background_image_file,  Unset):
            background_image_file = UNSET
        else:
            background_image_file = DriveBackgroundImageFile.from_dict(_background_image_file)




        background_image_link = d.pop("backgroundImageLink", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: DriveCapabilities | Unset
        if isinstance(_capabilities,  Unset):
            capabilities = UNSET
        else:
            capabilities = DriveCapabilities.from_dict(_capabilities)




        color_rgb = d.pop("colorRgb", UNSET)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time,  Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)




        hidden = d.pop("hidden", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        name = d.pop("name", UNSET)

        org_unit_id = d.pop("orgUnitId", UNSET)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: DriveRestrictions | Unset
        if isinstance(_restrictions,  Unset):
            restrictions = UNSET
        else:
            restrictions = DriveRestrictions.from_dict(_restrictions)




        theme_id = d.pop("themeId", UNSET)

        drive = cls(
            background_image_file=background_image_file,
            background_image_link=background_image_link,
            capabilities=capabilities,
            color_rgb=color_rgb,
            created_time=created_time,
            hidden=hidden,
            id=id,
            kind=kind,
            name=name,
            org_unit_id=org_unit_id,
            restrictions=restrictions,
            theme_id=theme_id,
        )


        drive.additional_properties = d
        return drive

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
