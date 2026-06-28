from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DriveRestrictions")



@_attrs_define
class DriveRestrictions:
    """ A set of restrictions that apply to this shared drive or items inside this shared drive.

        Attributes:
            admin_managed_restrictions (bool | Unset): Whether administrative privileges on this shared drive are required
                to modify restrictions.
            copy_requires_writer_permission (bool | Unset): Whether the options to copy, print, or download files inside
                this shared drive, should be disabled for readers and commenters. When this restriction is set to true, it will
                override the similarly named field to true for any file inside this shared drive.
            domain_users_only (bool | Unset): Whether access to this shared drive and items inside this shared drive is
                restricted to users of the domain to which this shared drive belongs. This restriction may be overridden by
                other sharing policies controlled outside of this shared drive.
            drive_members_only (bool | Unset): Whether access to items inside this shared drive is restricted to its
                members.
            sharing_folders_requires_organizer_permission (bool | Unset): If true, only users with the organizer role can
                share folders. If false, users with either the organizer role or the file organizer role can share folders.
     """

    admin_managed_restrictions: bool | Unset = UNSET
    copy_requires_writer_permission: bool | Unset = UNSET
    domain_users_only: bool | Unset = UNSET
    drive_members_only: bool | Unset = UNSET
    sharing_folders_requires_organizer_permission: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        admin_managed_restrictions = self.admin_managed_restrictions

        copy_requires_writer_permission = self.copy_requires_writer_permission

        domain_users_only = self.domain_users_only

        drive_members_only = self.drive_members_only

        sharing_folders_requires_organizer_permission = self.sharing_folders_requires_organizer_permission


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if admin_managed_restrictions is not UNSET:
            field_dict["adminManagedRestrictions"] = admin_managed_restrictions
        if copy_requires_writer_permission is not UNSET:
            field_dict["copyRequiresWriterPermission"] = copy_requires_writer_permission
        if domain_users_only is not UNSET:
            field_dict["domainUsersOnly"] = domain_users_only
        if drive_members_only is not UNSET:
            field_dict["driveMembersOnly"] = drive_members_only
        if sharing_folders_requires_organizer_permission is not UNSET:
            field_dict["sharingFoldersRequiresOrganizerPermission"] = sharing_folders_requires_organizer_permission

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_managed_restrictions = d.pop("adminManagedRestrictions", UNSET)

        copy_requires_writer_permission = d.pop("copyRequiresWriterPermission", UNSET)

        domain_users_only = d.pop("domainUsersOnly", UNSET)

        drive_members_only = d.pop("driveMembersOnly", UNSET)

        sharing_folders_requires_organizer_permission = d.pop("sharingFoldersRequiresOrganizerPermission", UNSET)

        drive_restrictions = cls(
            admin_managed_restrictions=admin_managed_restrictions,
            copy_requires_writer_permission=copy_requires_writer_permission,
            domain_users_only=domain_users_only,
            drive_members_only=drive_members_only,
            sharing_folders_requires_organizer_permission=sharing_folders_requires_organizer_permission,
        )


        drive_restrictions.additional_properties = d
        return drive_restrictions

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
