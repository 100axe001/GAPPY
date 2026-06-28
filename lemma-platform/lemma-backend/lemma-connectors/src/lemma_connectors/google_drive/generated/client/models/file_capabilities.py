from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FileCapabilities")



@_attrs_define
class FileCapabilities:
    """ Capabilities the current user has on this file. Each capability corresponds to a fine-grained action that a user can
    take.

        Attributes:
            can_accept_ownership (bool | Unset): Whether the current user is the pending owner of the file. Not populated
                for shared drive files.
            can_add_children (bool | Unset): Whether the current user can add children to this folder. This is always false
                when the item isn't a folder.
            can_add_folder_from_another_drive (bool | Unset): Whether the current user can add a folder from another drive
                (different shared drive or My Drive) to this folder. This is false when the item isn't a folder. Only populated
                for items in shared drives.
            can_add_my_drive_parent (bool | Unset): Whether the current user can add a parent for the item without removing
                an existing parent in the same request. Not populated for shared drive files.
            can_change_copy_requires_writer_permission (bool | Unset): Whether the current user can change the
                copyRequiresWriterPermission restriction of this file.
            can_change_security_update_enabled (bool | Unset): Whether the current user can change the securityUpdateEnabled
                field on link share metadata.
            can_change_viewers_can_copy_content (bool | Unset): Deprecated
            can_comment (bool | Unset): Whether the current user can comment on this file.
            can_copy (bool | Unset): Whether the current user can copy this file. For an item in a shared drive, whether the
                current user can copy non-folder descendants of this item, or this item itself if it's not a folder.
            can_delete (bool | Unset): Whether the current user can delete this file.
            can_delete_children (bool | Unset): Whether the current user can delete children of this folder. This is false
                when the item isn't a folder. Only populated for items in shared drives.
            can_download (bool | Unset): Whether the current user can download this file.
            can_edit (bool | Unset): Whether the current user can edit this file. Other factors might limit the type of
                changes a user can make to a file. For example, see canChangeCopyRequiresWriterPermission or canModifyContent.
            can_list_children (bool | Unset): Whether the current user can list the children of this folder. This is always
                false when the item isn't a folder.
            can_modify_content (bool | Unset): Whether the current user can modify the content of this file.
            can_modify_content_restriction (bool | Unset): Whether the current user can modify restrictions on content of
                this file.
            can_modify_labels (bool | Unset): Whether the current user can modify the labels on this file.
            can_move_children_out_of_drive (bool | Unset): Whether the current user can move children of this folder outside
                of the shared drive. This is false when the item isn't a folder. Only populated for items in shared drives.
            can_move_children_out_of_team_drive (bool | Unset): Deprecated - use canMoveChildrenOutOfDrive instead.
            can_move_children_within_drive (bool | Unset): Whether the current user can move children of this folder within
                this shared drive or My Drive. This is false when the item isn't a folder. Note that a request to move the child
                might still fail depending on the current user's access to the child and to the destination folder.
            can_move_children_within_team_drive (bool | Unset): Deprecated - use canMoveChildrenWithinDrive instead.
            can_move_item_into_team_drive (bool | Unset): Deprecated - use canMoveItemOutOfDrive instead.
            can_move_item_out_of_drive (bool | Unset): Whether the current user can move this item outside of this shared
                drive or My Drive by changing its parent. Note that a request to change the parent of the item might still fail
                depending on the new parent that's being added.
            can_move_item_out_of_team_drive (bool | Unset): Deprecated - use canMoveItemOutOfDrive instead.
            can_move_item_within_drive (bool | Unset): Whether the current user can move this item within this shared drive
                or My Drive. Note that a request to change the parent of the item might still fail depending on the new parent
                that's being added and the parent that's being removed.
            can_move_item_within_team_drive (bool | Unset): Deprecated - use canMoveItemWithinDrive instead.
            can_move_team_drive_item (bool | Unset): Deprecated - use canMoveItemWithinDrive or canMoveItemOutOfDrive
                instead.
            can_read_drive (bool | Unset): Whether the current user can read the shared drive to which this file belongs.
                Only populated for items in shared drives.
            can_read_labels (bool | Unset): Whether the current user can read the labels on this file.
            can_read_revisions (bool | Unset): Whether the current user can read the revisions resource of this file. For a
                shared drive item, whether revisions of non-folder descendants of this item, or this item itself if it's not a
                folder, can be read.
            can_read_team_drive (bool | Unset): Deprecated - use canReadDrive instead.
            can_remove_children (bool | Unset): Whether the current user can remove children from this folder. This is
                always false when the item isn't a folder. For a folder in a shared drive, use canDeleteChildren or
                canTrashChildren instead.
            can_remove_my_drive_parent (bool | Unset): Whether the current user can remove a parent from the item without
                adding another parent in the same request. Not populated for shared drive files.
            can_rename (bool | Unset): Whether the current user can rename this file.
            can_share (bool | Unset): Whether the current user can modify the sharing settings for this file.
            can_trash (bool | Unset): Whether the current user can move this file to trash.
            can_trash_children (bool | Unset): Whether the current user can trash children of this folder. This is false
                when the item isn't a folder. Only populated for items in shared drives.
            can_untrash (bool | Unset): Whether the current user can restore this file from trash.
     """

    can_accept_ownership: bool | Unset = UNSET
    can_add_children: bool | Unset = UNSET
    can_add_folder_from_another_drive: bool | Unset = UNSET
    can_add_my_drive_parent: bool | Unset = UNSET
    can_change_copy_requires_writer_permission: bool | Unset = UNSET
    can_change_security_update_enabled: bool | Unset = UNSET
    can_change_viewers_can_copy_content: bool | Unset = UNSET
    can_comment: bool | Unset = UNSET
    can_copy: bool | Unset = UNSET
    can_delete: bool | Unset = UNSET
    can_delete_children: bool | Unset = UNSET
    can_download: bool | Unset = UNSET
    can_edit: bool | Unset = UNSET
    can_list_children: bool | Unset = UNSET
    can_modify_content: bool | Unset = UNSET
    can_modify_content_restriction: bool | Unset = UNSET
    can_modify_labels: bool | Unset = UNSET
    can_move_children_out_of_drive: bool | Unset = UNSET
    can_move_children_out_of_team_drive: bool | Unset = UNSET
    can_move_children_within_drive: bool | Unset = UNSET
    can_move_children_within_team_drive: bool | Unset = UNSET
    can_move_item_into_team_drive: bool | Unset = UNSET
    can_move_item_out_of_drive: bool | Unset = UNSET
    can_move_item_out_of_team_drive: bool | Unset = UNSET
    can_move_item_within_drive: bool | Unset = UNSET
    can_move_item_within_team_drive: bool | Unset = UNSET
    can_move_team_drive_item: bool | Unset = UNSET
    can_read_drive: bool | Unset = UNSET
    can_read_labels: bool | Unset = UNSET
    can_read_revisions: bool | Unset = UNSET
    can_read_team_drive: bool | Unset = UNSET
    can_remove_children: bool | Unset = UNSET
    can_remove_my_drive_parent: bool | Unset = UNSET
    can_rename: bool | Unset = UNSET
    can_share: bool | Unset = UNSET
    can_trash: bool | Unset = UNSET
    can_trash_children: bool | Unset = UNSET
    can_untrash: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        can_accept_ownership = self.can_accept_ownership

        can_add_children = self.can_add_children

        can_add_folder_from_another_drive = self.can_add_folder_from_another_drive

        can_add_my_drive_parent = self.can_add_my_drive_parent

        can_change_copy_requires_writer_permission = self.can_change_copy_requires_writer_permission

        can_change_security_update_enabled = self.can_change_security_update_enabled

        can_change_viewers_can_copy_content = self.can_change_viewers_can_copy_content

        can_comment = self.can_comment

        can_copy = self.can_copy

        can_delete = self.can_delete

        can_delete_children = self.can_delete_children

        can_download = self.can_download

        can_edit = self.can_edit

        can_list_children = self.can_list_children

        can_modify_content = self.can_modify_content

        can_modify_content_restriction = self.can_modify_content_restriction

        can_modify_labels = self.can_modify_labels

        can_move_children_out_of_drive = self.can_move_children_out_of_drive

        can_move_children_out_of_team_drive = self.can_move_children_out_of_team_drive

        can_move_children_within_drive = self.can_move_children_within_drive

        can_move_children_within_team_drive = self.can_move_children_within_team_drive

        can_move_item_into_team_drive = self.can_move_item_into_team_drive

        can_move_item_out_of_drive = self.can_move_item_out_of_drive

        can_move_item_out_of_team_drive = self.can_move_item_out_of_team_drive

        can_move_item_within_drive = self.can_move_item_within_drive

        can_move_item_within_team_drive = self.can_move_item_within_team_drive

        can_move_team_drive_item = self.can_move_team_drive_item

        can_read_drive = self.can_read_drive

        can_read_labels = self.can_read_labels

        can_read_revisions = self.can_read_revisions

        can_read_team_drive = self.can_read_team_drive

        can_remove_children = self.can_remove_children

        can_remove_my_drive_parent = self.can_remove_my_drive_parent

        can_rename = self.can_rename

        can_share = self.can_share

        can_trash = self.can_trash

        can_trash_children = self.can_trash_children

        can_untrash = self.can_untrash


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if can_accept_ownership is not UNSET:
            field_dict["canAcceptOwnership"] = can_accept_ownership
        if can_add_children is not UNSET:
            field_dict["canAddChildren"] = can_add_children
        if can_add_folder_from_another_drive is not UNSET:
            field_dict["canAddFolderFromAnotherDrive"] = can_add_folder_from_another_drive
        if can_add_my_drive_parent is not UNSET:
            field_dict["canAddMyDriveParent"] = can_add_my_drive_parent
        if can_change_copy_requires_writer_permission is not UNSET:
            field_dict["canChangeCopyRequiresWriterPermission"] = can_change_copy_requires_writer_permission
        if can_change_security_update_enabled is not UNSET:
            field_dict["canChangeSecurityUpdateEnabled"] = can_change_security_update_enabled
        if can_change_viewers_can_copy_content is not UNSET:
            field_dict["canChangeViewersCanCopyContent"] = can_change_viewers_can_copy_content
        if can_comment is not UNSET:
            field_dict["canComment"] = can_comment
        if can_copy is not UNSET:
            field_dict["canCopy"] = can_copy
        if can_delete is not UNSET:
            field_dict["canDelete"] = can_delete
        if can_delete_children is not UNSET:
            field_dict["canDeleteChildren"] = can_delete_children
        if can_download is not UNSET:
            field_dict["canDownload"] = can_download
        if can_edit is not UNSET:
            field_dict["canEdit"] = can_edit
        if can_list_children is not UNSET:
            field_dict["canListChildren"] = can_list_children
        if can_modify_content is not UNSET:
            field_dict["canModifyContent"] = can_modify_content
        if can_modify_content_restriction is not UNSET:
            field_dict["canModifyContentRestriction"] = can_modify_content_restriction
        if can_modify_labels is not UNSET:
            field_dict["canModifyLabels"] = can_modify_labels
        if can_move_children_out_of_drive is not UNSET:
            field_dict["canMoveChildrenOutOfDrive"] = can_move_children_out_of_drive
        if can_move_children_out_of_team_drive is not UNSET:
            field_dict["canMoveChildrenOutOfTeamDrive"] = can_move_children_out_of_team_drive
        if can_move_children_within_drive is not UNSET:
            field_dict["canMoveChildrenWithinDrive"] = can_move_children_within_drive
        if can_move_children_within_team_drive is not UNSET:
            field_dict["canMoveChildrenWithinTeamDrive"] = can_move_children_within_team_drive
        if can_move_item_into_team_drive is not UNSET:
            field_dict["canMoveItemIntoTeamDrive"] = can_move_item_into_team_drive
        if can_move_item_out_of_drive is not UNSET:
            field_dict["canMoveItemOutOfDrive"] = can_move_item_out_of_drive
        if can_move_item_out_of_team_drive is not UNSET:
            field_dict["canMoveItemOutOfTeamDrive"] = can_move_item_out_of_team_drive
        if can_move_item_within_drive is not UNSET:
            field_dict["canMoveItemWithinDrive"] = can_move_item_within_drive
        if can_move_item_within_team_drive is not UNSET:
            field_dict["canMoveItemWithinTeamDrive"] = can_move_item_within_team_drive
        if can_move_team_drive_item is not UNSET:
            field_dict["canMoveTeamDriveItem"] = can_move_team_drive_item
        if can_read_drive is not UNSET:
            field_dict["canReadDrive"] = can_read_drive
        if can_read_labels is not UNSET:
            field_dict["canReadLabels"] = can_read_labels
        if can_read_revisions is not UNSET:
            field_dict["canReadRevisions"] = can_read_revisions
        if can_read_team_drive is not UNSET:
            field_dict["canReadTeamDrive"] = can_read_team_drive
        if can_remove_children is not UNSET:
            field_dict["canRemoveChildren"] = can_remove_children
        if can_remove_my_drive_parent is not UNSET:
            field_dict["canRemoveMyDriveParent"] = can_remove_my_drive_parent
        if can_rename is not UNSET:
            field_dict["canRename"] = can_rename
        if can_share is not UNSET:
            field_dict["canShare"] = can_share
        if can_trash is not UNSET:
            field_dict["canTrash"] = can_trash
        if can_trash_children is not UNSET:
            field_dict["canTrashChildren"] = can_trash_children
        if can_untrash is not UNSET:
            field_dict["canUntrash"] = can_untrash

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_accept_ownership = d.pop("canAcceptOwnership", UNSET)

        can_add_children = d.pop("canAddChildren", UNSET)

        can_add_folder_from_another_drive = d.pop("canAddFolderFromAnotherDrive", UNSET)

        can_add_my_drive_parent = d.pop("canAddMyDriveParent", UNSET)

        can_change_copy_requires_writer_permission = d.pop("canChangeCopyRequiresWriterPermission", UNSET)

        can_change_security_update_enabled = d.pop("canChangeSecurityUpdateEnabled", UNSET)

        can_change_viewers_can_copy_content = d.pop("canChangeViewersCanCopyContent", UNSET)

        can_comment = d.pop("canComment", UNSET)

        can_copy = d.pop("canCopy", UNSET)

        can_delete = d.pop("canDelete", UNSET)

        can_delete_children = d.pop("canDeleteChildren", UNSET)

        can_download = d.pop("canDownload", UNSET)

        can_edit = d.pop("canEdit", UNSET)

        can_list_children = d.pop("canListChildren", UNSET)

        can_modify_content = d.pop("canModifyContent", UNSET)

        can_modify_content_restriction = d.pop("canModifyContentRestriction", UNSET)

        can_modify_labels = d.pop("canModifyLabels", UNSET)

        can_move_children_out_of_drive = d.pop("canMoveChildrenOutOfDrive", UNSET)

        can_move_children_out_of_team_drive = d.pop("canMoveChildrenOutOfTeamDrive", UNSET)

        can_move_children_within_drive = d.pop("canMoveChildrenWithinDrive", UNSET)

        can_move_children_within_team_drive = d.pop("canMoveChildrenWithinTeamDrive", UNSET)

        can_move_item_into_team_drive = d.pop("canMoveItemIntoTeamDrive", UNSET)

        can_move_item_out_of_drive = d.pop("canMoveItemOutOfDrive", UNSET)

        can_move_item_out_of_team_drive = d.pop("canMoveItemOutOfTeamDrive", UNSET)

        can_move_item_within_drive = d.pop("canMoveItemWithinDrive", UNSET)

        can_move_item_within_team_drive = d.pop("canMoveItemWithinTeamDrive", UNSET)

        can_move_team_drive_item = d.pop("canMoveTeamDriveItem", UNSET)

        can_read_drive = d.pop("canReadDrive", UNSET)

        can_read_labels = d.pop("canReadLabels", UNSET)

        can_read_revisions = d.pop("canReadRevisions", UNSET)

        can_read_team_drive = d.pop("canReadTeamDrive", UNSET)

        can_remove_children = d.pop("canRemoveChildren", UNSET)

        can_remove_my_drive_parent = d.pop("canRemoveMyDriveParent", UNSET)

        can_rename = d.pop("canRename", UNSET)

        can_share = d.pop("canShare", UNSET)

        can_trash = d.pop("canTrash", UNSET)

        can_trash_children = d.pop("canTrashChildren", UNSET)

        can_untrash = d.pop("canUntrash", UNSET)

        file_capabilities = cls(
            can_accept_ownership=can_accept_ownership,
            can_add_children=can_add_children,
            can_add_folder_from_another_drive=can_add_folder_from_another_drive,
            can_add_my_drive_parent=can_add_my_drive_parent,
            can_change_copy_requires_writer_permission=can_change_copy_requires_writer_permission,
            can_change_security_update_enabled=can_change_security_update_enabled,
            can_change_viewers_can_copy_content=can_change_viewers_can_copy_content,
            can_comment=can_comment,
            can_copy=can_copy,
            can_delete=can_delete,
            can_delete_children=can_delete_children,
            can_download=can_download,
            can_edit=can_edit,
            can_list_children=can_list_children,
            can_modify_content=can_modify_content,
            can_modify_content_restriction=can_modify_content_restriction,
            can_modify_labels=can_modify_labels,
            can_move_children_out_of_drive=can_move_children_out_of_drive,
            can_move_children_out_of_team_drive=can_move_children_out_of_team_drive,
            can_move_children_within_drive=can_move_children_within_drive,
            can_move_children_within_team_drive=can_move_children_within_team_drive,
            can_move_item_into_team_drive=can_move_item_into_team_drive,
            can_move_item_out_of_drive=can_move_item_out_of_drive,
            can_move_item_out_of_team_drive=can_move_item_out_of_team_drive,
            can_move_item_within_drive=can_move_item_within_drive,
            can_move_item_within_team_drive=can_move_item_within_team_drive,
            can_move_team_drive_item=can_move_team_drive_item,
            can_read_drive=can_read_drive,
            can_read_labels=can_read_labels,
            can_read_revisions=can_read_revisions,
            can_read_team_drive=can_read_team_drive,
            can_remove_children=can_remove_children,
            can_remove_my_drive_parent=can_remove_my_drive_parent,
            can_rename=can_rename,
            can_share=can_share,
            can_trash=can_trash,
            can_trash_children=can_trash_children,
            can_untrash=can_untrash,
        )


        file_capabilities.additional_properties = d
        return file_capabilities

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
