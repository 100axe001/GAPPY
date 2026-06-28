from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TeamDriveCapabilities")



@_attrs_define
class TeamDriveCapabilities:
    """ Capabilities the current user has on this Team Drive.

        Attributes:
            can_add_children (bool | Unset): Whether the current user can add children to folders in this Team Drive.
            can_change_copy_requires_writer_permission_restriction (bool | Unset): Whether the current user can change the
                copyRequiresWriterPermission restriction of this Team Drive.
            can_change_domain_users_only_restriction (bool | Unset): Whether the current user can change the domainUsersOnly
                restriction of this Team Drive.
            can_change_sharing_folders_requires_organizer_permission_restriction (bool | Unset): Whether the current user
                can change the sharingFoldersRequiresOrganizerPermission restriction of this Team Drive.
            can_change_team_drive_background (bool | Unset): Whether the current user can change the background of this Team
                Drive.
            can_change_team_members_only_restriction (bool | Unset): Whether the current user can change the teamMembersOnly
                restriction of this Team Drive.
            can_comment (bool | Unset): Whether the current user can comment on files in this Team Drive.
            can_copy (bool | Unset): Whether the current user can copy files in this Team Drive.
            can_delete_children (bool | Unset): Whether the current user can delete children from folders in this Team
                Drive.
            can_delete_team_drive (bool | Unset): Whether the current user can delete this Team Drive. Attempting to delete
                the Team Drive may still fail if there are untrashed items inside the Team Drive.
            can_download (bool | Unset): Whether the current user can download files in this Team Drive.
            can_edit (bool | Unset): Whether the current user can edit files in this Team Drive
            can_list_children (bool | Unset): Whether the current user can list the children of folders in this Team Drive.
            can_manage_members (bool | Unset): Whether the current user can add members to this Team Drive or remove them or
                change their role.
            can_read_revisions (bool | Unset): Whether the current user can read the revisions resource of files in this
                Team Drive.
            can_remove_children (bool | Unset): Deprecated - use canDeleteChildren or canTrashChildren instead.
            can_rename (bool | Unset): Whether the current user can rename files or folders in this Team Drive.
            can_rename_team_drive (bool | Unset): Whether the current user can rename this Team Drive.
            can_reset_team_drive_restrictions (bool | Unset): Whether the current user can reset the Team Drive restrictions
                to defaults.
            can_share (bool | Unset): Whether the current user can share files or folders in this Team Drive.
            can_trash_children (bool | Unset): Whether the current user can trash children from folders in this Team Drive.
     """

    can_add_children: bool | Unset = UNSET
    can_change_copy_requires_writer_permission_restriction: bool | Unset = UNSET
    can_change_domain_users_only_restriction: bool | Unset = UNSET
    can_change_sharing_folders_requires_organizer_permission_restriction: bool | Unset = UNSET
    can_change_team_drive_background: bool | Unset = UNSET
    can_change_team_members_only_restriction: bool | Unset = UNSET
    can_comment: bool | Unset = UNSET
    can_copy: bool | Unset = UNSET
    can_delete_children: bool | Unset = UNSET
    can_delete_team_drive: bool | Unset = UNSET
    can_download: bool | Unset = UNSET
    can_edit: bool | Unset = UNSET
    can_list_children: bool | Unset = UNSET
    can_manage_members: bool | Unset = UNSET
    can_read_revisions: bool | Unset = UNSET
    can_remove_children: bool | Unset = UNSET
    can_rename: bool | Unset = UNSET
    can_rename_team_drive: bool | Unset = UNSET
    can_reset_team_drive_restrictions: bool | Unset = UNSET
    can_share: bool | Unset = UNSET
    can_trash_children: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        can_add_children = self.can_add_children

        can_change_copy_requires_writer_permission_restriction = self.can_change_copy_requires_writer_permission_restriction

        can_change_domain_users_only_restriction = self.can_change_domain_users_only_restriction

        can_change_sharing_folders_requires_organizer_permission_restriction = self.can_change_sharing_folders_requires_organizer_permission_restriction

        can_change_team_drive_background = self.can_change_team_drive_background

        can_change_team_members_only_restriction = self.can_change_team_members_only_restriction

        can_comment = self.can_comment

        can_copy = self.can_copy

        can_delete_children = self.can_delete_children

        can_delete_team_drive = self.can_delete_team_drive

        can_download = self.can_download

        can_edit = self.can_edit

        can_list_children = self.can_list_children

        can_manage_members = self.can_manage_members

        can_read_revisions = self.can_read_revisions

        can_remove_children = self.can_remove_children

        can_rename = self.can_rename

        can_rename_team_drive = self.can_rename_team_drive

        can_reset_team_drive_restrictions = self.can_reset_team_drive_restrictions

        can_share = self.can_share

        can_trash_children = self.can_trash_children


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if can_add_children is not UNSET:
            field_dict["canAddChildren"] = can_add_children
        if can_change_copy_requires_writer_permission_restriction is not UNSET:
            field_dict["canChangeCopyRequiresWriterPermissionRestriction"] = can_change_copy_requires_writer_permission_restriction
        if can_change_domain_users_only_restriction is not UNSET:
            field_dict["canChangeDomainUsersOnlyRestriction"] = can_change_domain_users_only_restriction
        if can_change_sharing_folders_requires_organizer_permission_restriction is not UNSET:
            field_dict["canChangeSharingFoldersRequiresOrganizerPermissionRestriction"] = can_change_sharing_folders_requires_organizer_permission_restriction
        if can_change_team_drive_background is not UNSET:
            field_dict["canChangeTeamDriveBackground"] = can_change_team_drive_background
        if can_change_team_members_only_restriction is not UNSET:
            field_dict["canChangeTeamMembersOnlyRestriction"] = can_change_team_members_only_restriction
        if can_comment is not UNSET:
            field_dict["canComment"] = can_comment
        if can_copy is not UNSET:
            field_dict["canCopy"] = can_copy
        if can_delete_children is not UNSET:
            field_dict["canDeleteChildren"] = can_delete_children
        if can_delete_team_drive is not UNSET:
            field_dict["canDeleteTeamDrive"] = can_delete_team_drive
        if can_download is not UNSET:
            field_dict["canDownload"] = can_download
        if can_edit is not UNSET:
            field_dict["canEdit"] = can_edit
        if can_list_children is not UNSET:
            field_dict["canListChildren"] = can_list_children
        if can_manage_members is not UNSET:
            field_dict["canManageMembers"] = can_manage_members
        if can_read_revisions is not UNSET:
            field_dict["canReadRevisions"] = can_read_revisions
        if can_remove_children is not UNSET:
            field_dict["canRemoveChildren"] = can_remove_children
        if can_rename is not UNSET:
            field_dict["canRename"] = can_rename
        if can_rename_team_drive is not UNSET:
            field_dict["canRenameTeamDrive"] = can_rename_team_drive
        if can_reset_team_drive_restrictions is not UNSET:
            field_dict["canResetTeamDriveRestrictions"] = can_reset_team_drive_restrictions
        if can_share is not UNSET:
            field_dict["canShare"] = can_share
        if can_trash_children is not UNSET:
            field_dict["canTrashChildren"] = can_trash_children

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_add_children = d.pop("canAddChildren", UNSET)

        can_change_copy_requires_writer_permission_restriction = d.pop("canChangeCopyRequiresWriterPermissionRestriction", UNSET)

        can_change_domain_users_only_restriction = d.pop("canChangeDomainUsersOnlyRestriction", UNSET)

        can_change_sharing_folders_requires_organizer_permission_restriction = d.pop("canChangeSharingFoldersRequiresOrganizerPermissionRestriction", UNSET)

        can_change_team_drive_background = d.pop("canChangeTeamDriveBackground", UNSET)

        can_change_team_members_only_restriction = d.pop("canChangeTeamMembersOnlyRestriction", UNSET)

        can_comment = d.pop("canComment", UNSET)

        can_copy = d.pop("canCopy", UNSET)

        can_delete_children = d.pop("canDeleteChildren", UNSET)

        can_delete_team_drive = d.pop("canDeleteTeamDrive", UNSET)

        can_download = d.pop("canDownload", UNSET)

        can_edit = d.pop("canEdit", UNSET)

        can_list_children = d.pop("canListChildren", UNSET)

        can_manage_members = d.pop("canManageMembers", UNSET)

        can_read_revisions = d.pop("canReadRevisions", UNSET)

        can_remove_children = d.pop("canRemoveChildren", UNSET)

        can_rename = d.pop("canRename", UNSET)

        can_rename_team_drive = d.pop("canRenameTeamDrive", UNSET)

        can_reset_team_drive_restrictions = d.pop("canResetTeamDriveRestrictions", UNSET)

        can_share = d.pop("canShare", UNSET)

        can_trash_children = d.pop("canTrashChildren", UNSET)

        team_drive_capabilities = cls(
            can_add_children=can_add_children,
            can_change_copy_requires_writer_permission_restriction=can_change_copy_requires_writer_permission_restriction,
            can_change_domain_users_only_restriction=can_change_domain_users_only_restriction,
            can_change_sharing_folders_requires_organizer_permission_restriction=can_change_sharing_folders_requires_organizer_permission_restriction,
            can_change_team_drive_background=can_change_team_drive_background,
            can_change_team_members_only_restriction=can_change_team_members_only_restriction,
            can_comment=can_comment,
            can_copy=can_copy,
            can_delete_children=can_delete_children,
            can_delete_team_drive=can_delete_team_drive,
            can_download=can_download,
            can_edit=can_edit,
            can_list_children=can_list_children,
            can_manage_members=can_manage_members,
            can_read_revisions=can_read_revisions,
            can_remove_children=can_remove_children,
            can_rename=can_rename,
            can_rename_team_drive=can_rename_team_drive,
            can_reset_team_drive_restrictions=can_reset_team_drive_restrictions,
            can_share=can_share,
            can_trash_children=can_trash_children,
        )


        team_drive_capabilities.additional_properties = d
        return team_drive_capabilities

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
