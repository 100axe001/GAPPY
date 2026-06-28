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
  from ..models.content_restriction import ContentRestriction
  from ..models.file_app_properties import FileAppProperties
  from ..models.file_capabilities import FileCapabilities
  from ..models.file_content_hints import FileContentHints
  from ..models.file_export_links import FileExportLinks
  from ..models.file_image_media_metadata import FileImageMediaMetadata
  from ..models.file_label_info import FileLabelInfo
  from ..models.file_link_share_metadata import FileLinkShareMetadata
  from ..models.file_properties import FileProperties
  from ..models.file_shortcut_details import FileShortcutDetails
  from ..models.file_video_media_metadata import FileVideoMediaMetadata
  from ..models.permission import Permission
  from ..models.user import User





T = TypeVar("T", bound="File")



@_attrs_define
class File:
    """ The metadata for a file.

        Attributes:
            app_properties (FileAppProperties | Unset): A collection of arbitrary key-value pairs that are private to the
                requesting app.
                Entries with null values are cleared in update and copy requests. These properties can only be retrieved using
                an authenticated request. An authenticated request uses an access token obtained with an OAuth 2 client ID. You
                cannot use an API key to retrieve private properties.
            capabilities (FileCapabilities | Unset): Capabilities the current user has on this file. Each capability
                corresponds to a fine-grained action that a user can take.
            content_hints (FileContentHints | Unset): Additional information about the content of the file. These fields are
                never populated in responses.
            content_restrictions (list[ContentRestriction] | Unset): Restrictions for accessing the content of the file.
                Only populated if such a restriction exists.
            copy_requires_writer_permission (bool | Unset): Whether the options to copy, print, or download this file,
                should be disabled for readers and commenters.
            created_time (datetime.datetime | Unset): The time at which the file was created (RFC 3339 date-time).
            description (str | Unset): A short description of the file.
            drive_id (str | Unset): ID of the shared drive the file resides in. Only populated for items in shared drives.
            explicitly_trashed (bool | Unset): Whether the file has been explicitly trashed, as opposed to recursively
                trashed from a parent folder.
            export_links (FileExportLinks | Unset): Links for exporting Docs Editors files to specific formats.
            file_extension (str | Unset): The final component of fullFileExtension. This is only available for files with
                binary content in Google Drive.
            folder_color_rgb (str | Unset): The color for a folder or shortcut to a folder as an RGB hex string. The
                supported colors are published in the folderColorPalette field of the About resource.
                If an unsupported color is specified, the closest color in the palette will be used instead.
            full_file_extension (str | Unset): The full file extension extracted from the name field. Can contain multiple
                concatenated extensions, such as "tar.gz". This is only available for files with binary content in Google Drive.
                This is automatically updated when the name field changes, however it's not cleared if the new name does not
                contain a valid extension.
            has_augmented_permissions (bool | Unset): Whether there are permissions directly on this file. This field is
                only populated for items in shared drives.
            has_thumbnail (bool | Unset): Whether this file has a thumbnail. This does not indicate whether the requesting
                app has access to the thumbnail. To check access, look for the presence of the thumbnailLink field.
            head_revision_id (str | Unset): The ID of the file's head revision. This is only available for files with binary
                content in Google Drive.
            icon_link (str | Unset): A static, unauthenticated link to the file's icon.
            id (str | Unset): The ID of the file.
            image_media_metadata (FileImageMediaMetadata | Unset): Additional metadata about image media, if available.
            is_app_authorized (bool | Unset): Whether the requesting app created or opened the file.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#file". Default:
                'drive#file'.
            label_info (FileLabelInfo | Unset): An overview of the labels on the file.
            last_modifying_user (User | Unset): Information about a Drive user.
            link_share_metadata (FileLinkShareMetadata | Unset): Contains details about the link URLs that clients are using
                to refer to this item.
            md_5_checksum (str | Unset): The MD5 checksum for the content of the file. This is only applicable to files with
                binary content in Google Drive.
            mime_type (str | Unset): The MIME type of the file.
                Google Drive will attempt to automatically detect an appropriate value from uploaded content if no value is
                provided. The value cannot be changed unless a new revision is uploaded.
                If a file is created with a Google Doc MIME type, the uploaded content will be imported if possible. The
                supported import formats are published in the About resource.
            modified_by_me (bool | Unset): Whether this user has modified the file.
            modified_by_me_time (datetime.datetime | Unset): The last time the user modified the file (RFC 3339 date-time).
            modified_time (datetime.datetime | Unset): The last time anyone modified the file (RFC 3339 date-time).
                Note that setting modifiedTime will also update modifiedByMeTime for the user.
            name (str | Unset): The name of the file. This isn't necessarily unique within a folder. Note that for immutable
                items such as the top-level folders of shared drives, My Drive root folder, and Application Data folder the name
                is constant.
            original_filename (str | Unset): The original filename of the uploaded content if available, or else the
                original value of the name field. This is only available for files with binary content in Google Drive.
            owned_by_me (bool | Unset): Whether the user owns the file. Not populated for items in shared drives.
            owners (list[User] | Unset): The owner of this file. Only certain legacy files might have more than one owner.
                This field isn't populated for items in shared drives.
            parents (list[str] | Unset): The IDs of the parent folders that contain the file.
                If not specified as part of a create request, the file will be placed directly in the user's My Drive folder. If
                not specified as part of a copy request, the file will inherit any discoverable parents of the source file.
                Update requests must use the addParents and removeParents parameters to modify the parents list.
            permission_ids (list[str] | Unset): List of permission IDs for users with access to this file.
            permissions (list[Permission] | Unset): The full list of permissions for the file. This is only available if the
                requesting user can share the file. Not populated for items in shared drives.
            properties (FileProperties | Unset): A collection of arbitrary key-value pairs that are visible to all apps.
                Entries with null values are cleared in update and copy requests.
            quota_bytes_used (str | Unset): The number of storage quota bytes used by the file. This includes the head
                revision as well as previous revisions with keepForever enabled.
            resource_key (str | Unset): A key needed to access the item via a shared link.
            sha_1_checksum (str | Unset): The SHA1 checksum associated with this file, if available. This field is only
                populated for files with content stored in Google Drive; it's not populated for Docs Editors or shortcut files.
            sha_256_checksum (str | Unset): The SHA256 checksum associated with this file, if available. This field is only
                populated for files with content stored in Google Drive; it's not populated for Docs Editors or shortcut files.
            shared (bool | Unset): Whether the file has been shared. Not populated for items in shared drives.
            shared_with_me_time (datetime.datetime | Unset): The time at which the file was shared with the user, if
                applicable (RFC 3339 date-time).
            sharing_user (User | Unset): Information about a Drive user.
            shortcut_details (FileShortcutDetails | Unset): Shortcut file details. Only populated for shortcut files, which
                have the mimeType field set to application/vnd.google-apps.shortcut.
            size (str | Unset): The size of the file's content in bytes. This field is populated for files with binary
                content stored in Google Drive and for Docs Editors files; it's not populated for shortcuts or folders.
            spaces (list[str] | Unset): The list of spaces that contain the file. The currently supported values are
                'drive', 'appDataFolder' and 'photos'.
            starred (bool | Unset): Whether the user has starred the file.
            team_drive_id (str | Unset): Deprecated - use driveId instead.
            thumbnail_link (str | Unset): A short-lived link to the file's thumbnail, if available. Typically lasts on the
                order of hours. Only populated when the requesting app can access the file's content. If the file isn't shared
                publicly, the URL returned in Files.thumbnailLink must be fetched using a credentialed request.
            thumbnail_version (str | Unset): The thumbnail version for use in thumbnail cache invalidation.
            trashed (bool | Unset): Whether the file has been trashed, either explicitly or from a trashed parent folder.
                Only the owner can trash a file. The trashed item is excluded from all files.list responses returned for any
                user who does not own the file. However, all users with access to the file can see the trashed item metadata in
                an API response. All users with access can copy, download, export, and share the file.
            trashed_time (datetime.datetime | Unset): The time that the item was trashed (RFC 3339 date-time). Only
                populated for items in shared drives.
            trashing_user (User | Unset): Information about a Drive user.
            version (str | Unset): A monotonically increasing version number for the file. This reflects every change made
                to the file on the server, even those not visible to the user.
            video_media_metadata (FileVideoMediaMetadata | Unset): Additional metadata about video media. This might not be
                available immediately upon upload.
            viewed_by_me (bool | Unset): Whether this user has viewed the file.
            viewed_by_me_time (datetime.datetime | Unset): The last time the user viewed the file (RFC 3339 date-time).
            viewers_can_copy_content (bool | Unset): Deprecated - use copyRequiresWriterPermission instead.
            web_content_link (str | Unset): A link for downloading the content of the file in a browser. This is only
                available for files with binary content in Google Drive.
            web_view_link (str | Unset): A link for opening the file in a relevant Google editor or viewer in a browser.
            writers_can_share (bool | Unset): Whether users with only writer permission can modify the file's permissions.
                Not populated for items in shared drives.
     """

    app_properties: FileAppProperties | Unset = UNSET
    capabilities: FileCapabilities | Unset = UNSET
    content_hints: FileContentHints | Unset = UNSET
    content_restrictions: list[ContentRestriction] | Unset = UNSET
    copy_requires_writer_permission: bool | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    drive_id: str | Unset = UNSET
    explicitly_trashed: bool | Unset = UNSET
    export_links: FileExportLinks | Unset = UNSET
    file_extension: str | Unset = UNSET
    folder_color_rgb: str | Unset = UNSET
    full_file_extension: str | Unset = UNSET
    has_augmented_permissions: bool | Unset = UNSET
    has_thumbnail: bool | Unset = UNSET
    head_revision_id: str | Unset = UNSET
    icon_link: str | Unset = UNSET
    id: str | Unset = UNSET
    image_media_metadata: FileImageMediaMetadata | Unset = UNSET
    is_app_authorized: bool | Unset = UNSET
    kind: str | Unset = 'drive#file'
    label_info: FileLabelInfo | Unset = UNSET
    last_modifying_user: User | Unset = UNSET
    link_share_metadata: FileLinkShareMetadata | Unset = UNSET
    md_5_checksum: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    modified_by_me: bool | Unset = UNSET
    modified_by_me_time: datetime.datetime | Unset = UNSET
    modified_time: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    original_filename: str | Unset = UNSET
    owned_by_me: bool | Unset = UNSET
    owners: list[User] | Unset = UNSET
    parents: list[str] | Unset = UNSET
    permission_ids: list[str] | Unset = UNSET
    permissions: list[Permission] | Unset = UNSET
    properties: FileProperties | Unset = UNSET
    quota_bytes_used: str | Unset = UNSET
    resource_key: str | Unset = UNSET
    sha_1_checksum: str | Unset = UNSET
    sha_256_checksum: str | Unset = UNSET
    shared: bool | Unset = UNSET
    shared_with_me_time: datetime.datetime | Unset = UNSET
    sharing_user: User | Unset = UNSET
    shortcut_details: FileShortcutDetails | Unset = UNSET
    size: str | Unset = UNSET
    spaces: list[str] | Unset = UNSET
    starred: bool | Unset = UNSET
    team_drive_id: str | Unset = UNSET
    thumbnail_link: str | Unset = UNSET
    thumbnail_version: str | Unset = UNSET
    trashed: bool | Unset = UNSET
    trashed_time: datetime.datetime | Unset = UNSET
    trashing_user: User | Unset = UNSET
    version: str | Unset = UNSET
    video_media_metadata: FileVideoMediaMetadata | Unset = UNSET
    viewed_by_me: bool | Unset = UNSET
    viewed_by_me_time: datetime.datetime | Unset = UNSET
    viewers_can_copy_content: bool | Unset = UNSET
    web_content_link: str | Unset = UNSET
    web_view_link: str | Unset = UNSET
    writers_can_share: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.content_restriction import ContentRestriction
        from ..models.file_app_properties import FileAppProperties
        from ..models.file_capabilities import FileCapabilities
        from ..models.file_content_hints import FileContentHints
        from ..models.file_export_links import FileExportLinks
        from ..models.file_image_media_metadata import FileImageMediaMetadata
        from ..models.file_label_info import FileLabelInfo
        from ..models.file_link_share_metadata import FileLinkShareMetadata
        from ..models.file_properties import FileProperties
        from ..models.file_shortcut_details import FileShortcutDetails
        from ..models.file_video_media_metadata import FileVideoMediaMetadata
        from ..models.permission import Permission
        from ..models.user import User
        app_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_properties, Unset):
            app_properties = self.app_properties.to_dict()

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        content_hints: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_hints, Unset):
            content_hints = self.content_hints.to_dict()

        content_restrictions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content_restrictions, Unset):
            content_restrictions = []
            for content_restrictions_item_data in self.content_restrictions:
                content_restrictions_item = content_restrictions_item_data.to_dict()
                content_restrictions.append(content_restrictions_item)



        copy_requires_writer_permission = self.copy_requires_writer_permission

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        description = self.description

        drive_id = self.drive_id

        explicitly_trashed = self.explicitly_trashed

        export_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.export_links, Unset):
            export_links = self.export_links.to_dict()

        file_extension = self.file_extension

        folder_color_rgb = self.folder_color_rgb

        full_file_extension = self.full_file_extension

        has_augmented_permissions = self.has_augmented_permissions

        has_thumbnail = self.has_thumbnail

        head_revision_id = self.head_revision_id

        icon_link = self.icon_link

        id = self.id

        image_media_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_media_metadata, Unset):
            image_media_metadata = self.image_media_metadata.to_dict()

        is_app_authorized = self.is_app_authorized

        kind = self.kind

        label_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_info, Unset):
            label_info = self.label_info.to_dict()

        last_modifying_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modifying_user, Unset):
            last_modifying_user = self.last_modifying_user.to_dict()

        link_share_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_share_metadata, Unset):
            link_share_metadata = self.link_share_metadata.to_dict()

        md_5_checksum = self.md_5_checksum

        mime_type = self.mime_type

        modified_by_me = self.modified_by_me

        modified_by_me_time: str | Unset = UNSET
        if not isinstance(self.modified_by_me_time, Unset):
            modified_by_me_time = self.modified_by_me_time.isoformat()

        modified_time: str | Unset = UNSET
        if not isinstance(self.modified_time, Unset):
            modified_time = self.modified_time.isoformat()

        name = self.name

        original_filename = self.original_filename

        owned_by_me = self.owned_by_me

        owners: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.owners, Unset):
            owners = []
            for owners_item_data in self.owners:
                owners_item = owners_item_data.to_dict()
                owners.append(owners_item)



        parents: list[str] | Unset = UNSET
        if not isinstance(self.parents, Unset):
            parents = self.parents



        permission_ids: list[str] | Unset = UNSET
        if not isinstance(self.permission_ids, Unset):
            permission_ids = self.permission_ids



        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)



        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        quota_bytes_used = self.quota_bytes_used

        resource_key = self.resource_key

        sha_1_checksum = self.sha_1_checksum

        sha_256_checksum = self.sha_256_checksum

        shared = self.shared

        shared_with_me_time: str | Unset = UNSET
        if not isinstance(self.shared_with_me_time, Unset):
            shared_with_me_time = self.shared_with_me_time.isoformat()

        sharing_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sharing_user, Unset):
            sharing_user = self.sharing_user.to_dict()

        shortcut_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shortcut_details, Unset):
            shortcut_details = self.shortcut_details.to_dict()

        size = self.size

        spaces: list[str] | Unset = UNSET
        if not isinstance(self.spaces, Unset):
            spaces = self.spaces



        starred = self.starred

        team_drive_id = self.team_drive_id

        thumbnail_link = self.thumbnail_link

        thumbnail_version = self.thumbnail_version

        trashed = self.trashed

        trashed_time: str | Unset = UNSET
        if not isinstance(self.trashed_time, Unset):
            trashed_time = self.trashed_time.isoformat()

        trashing_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trashing_user, Unset):
            trashing_user = self.trashing_user.to_dict()

        version = self.version

        video_media_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_media_metadata, Unset):
            video_media_metadata = self.video_media_metadata.to_dict()

        viewed_by_me = self.viewed_by_me

        viewed_by_me_time: str | Unset = UNSET
        if not isinstance(self.viewed_by_me_time, Unset):
            viewed_by_me_time = self.viewed_by_me_time.isoformat()

        viewers_can_copy_content = self.viewers_can_copy_content

        web_content_link = self.web_content_link

        web_view_link = self.web_view_link

        writers_can_share = self.writers_can_share


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if app_properties is not UNSET:
            field_dict["appProperties"] = app_properties
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if content_hints is not UNSET:
            field_dict["contentHints"] = content_hints
        if content_restrictions is not UNSET:
            field_dict["contentRestrictions"] = content_restrictions
        if copy_requires_writer_permission is not UNSET:
            field_dict["copyRequiresWriterPermission"] = copy_requires_writer_permission
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if description is not UNSET:
            field_dict["description"] = description
        if drive_id is not UNSET:
            field_dict["driveId"] = drive_id
        if explicitly_trashed is not UNSET:
            field_dict["explicitlyTrashed"] = explicitly_trashed
        if export_links is not UNSET:
            field_dict["exportLinks"] = export_links
        if file_extension is not UNSET:
            field_dict["fileExtension"] = file_extension
        if folder_color_rgb is not UNSET:
            field_dict["folderColorRgb"] = folder_color_rgb
        if full_file_extension is not UNSET:
            field_dict["fullFileExtension"] = full_file_extension
        if has_augmented_permissions is not UNSET:
            field_dict["hasAugmentedPermissions"] = has_augmented_permissions
        if has_thumbnail is not UNSET:
            field_dict["hasThumbnail"] = has_thumbnail
        if head_revision_id is not UNSET:
            field_dict["headRevisionId"] = head_revision_id
        if icon_link is not UNSET:
            field_dict["iconLink"] = icon_link
        if id is not UNSET:
            field_dict["id"] = id
        if image_media_metadata is not UNSET:
            field_dict["imageMediaMetadata"] = image_media_metadata
        if is_app_authorized is not UNSET:
            field_dict["isAppAuthorized"] = is_app_authorized
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label_info is not UNSET:
            field_dict["labelInfo"] = label_info
        if last_modifying_user is not UNSET:
            field_dict["lastModifyingUser"] = last_modifying_user
        if link_share_metadata is not UNSET:
            field_dict["linkShareMetadata"] = link_share_metadata
        if md_5_checksum is not UNSET:
            field_dict["md5Checksum"] = md_5_checksum
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if modified_by_me is not UNSET:
            field_dict["modifiedByMe"] = modified_by_me
        if modified_by_me_time is not UNSET:
            field_dict["modifiedByMeTime"] = modified_by_me_time
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time
        if name is not UNSET:
            field_dict["name"] = name
        if original_filename is not UNSET:
            field_dict["originalFilename"] = original_filename
        if owned_by_me is not UNSET:
            field_dict["ownedByMe"] = owned_by_me
        if owners is not UNSET:
            field_dict["owners"] = owners
        if parents is not UNSET:
            field_dict["parents"] = parents
        if permission_ids is not UNSET:
            field_dict["permissionIds"] = permission_ids
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if properties is not UNSET:
            field_dict["properties"] = properties
        if quota_bytes_used is not UNSET:
            field_dict["quotaBytesUsed"] = quota_bytes_used
        if resource_key is not UNSET:
            field_dict["resourceKey"] = resource_key
        if sha_1_checksum is not UNSET:
            field_dict["sha1Checksum"] = sha_1_checksum
        if sha_256_checksum is not UNSET:
            field_dict["sha256Checksum"] = sha_256_checksum
        if shared is not UNSET:
            field_dict["shared"] = shared
        if shared_with_me_time is not UNSET:
            field_dict["sharedWithMeTime"] = shared_with_me_time
        if sharing_user is not UNSET:
            field_dict["sharingUser"] = sharing_user
        if shortcut_details is not UNSET:
            field_dict["shortcutDetails"] = shortcut_details
        if size is not UNSET:
            field_dict["size"] = size
        if spaces is not UNSET:
            field_dict["spaces"] = spaces
        if starred is not UNSET:
            field_dict["starred"] = starred
        if team_drive_id is not UNSET:
            field_dict["teamDriveId"] = team_drive_id
        if thumbnail_link is not UNSET:
            field_dict["thumbnailLink"] = thumbnail_link
        if thumbnail_version is not UNSET:
            field_dict["thumbnailVersion"] = thumbnail_version
        if trashed is not UNSET:
            field_dict["trashed"] = trashed
        if trashed_time is not UNSET:
            field_dict["trashedTime"] = trashed_time
        if trashing_user is not UNSET:
            field_dict["trashingUser"] = trashing_user
        if version is not UNSET:
            field_dict["version"] = version
        if video_media_metadata is not UNSET:
            field_dict["videoMediaMetadata"] = video_media_metadata
        if viewed_by_me is not UNSET:
            field_dict["viewedByMe"] = viewed_by_me
        if viewed_by_me_time is not UNSET:
            field_dict["viewedByMeTime"] = viewed_by_me_time
        if viewers_can_copy_content is not UNSET:
            field_dict["viewersCanCopyContent"] = viewers_can_copy_content
        if web_content_link is not UNSET:
            field_dict["webContentLink"] = web_content_link
        if web_view_link is not UNSET:
            field_dict["webViewLink"] = web_view_link
        if writers_can_share is not UNSET:
            field_dict["writersCanShare"] = writers_can_share

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_restriction import ContentRestriction
        from ..models.file_app_properties import FileAppProperties
        from ..models.file_capabilities import FileCapabilities
        from ..models.file_content_hints import FileContentHints
        from ..models.file_export_links import FileExportLinks
        from ..models.file_image_media_metadata import FileImageMediaMetadata
        from ..models.file_label_info import FileLabelInfo
        from ..models.file_link_share_metadata import FileLinkShareMetadata
        from ..models.file_properties import FileProperties
        from ..models.file_shortcut_details import FileShortcutDetails
        from ..models.file_video_media_metadata import FileVideoMediaMetadata
        from ..models.permission import Permission
        from ..models.user import User
        d = dict(src_dict)
        _app_properties = d.pop("appProperties", UNSET)
        app_properties: FileAppProperties | Unset
        if isinstance(_app_properties,  Unset):
            app_properties = UNSET
        else:
            app_properties = FileAppProperties.from_dict(_app_properties)




        _capabilities = d.pop("capabilities", UNSET)
        capabilities: FileCapabilities | Unset
        if isinstance(_capabilities,  Unset):
            capabilities = UNSET
        else:
            capabilities = FileCapabilities.from_dict(_capabilities)




        _content_hints = d.pop("contentHints", UNSET)
        content_hints: FileContentHints | Unset
        if isinstance(_content_hints,  Unset):
            content_hints = UNSET
        else:
            content_hints = FileContentHints.from_dict(_content_hints)




        _content_restrictions = d.pop("contentRestrictions", UNSET)
        content_restrictions: list[ContentRestriction] | Unset = UNSET
        if _content_restrictions is not UNSET:
            content_restrictions = []
            for content_restrictions_item_data in _content_restrictions:
                content_restrictions_item = ContentRestriction.from_dict(content_restrictions_item_data)



                content_restrictions.append(content_restrictions_item)


        copy_requires_writer_permission = d.pop("copyRequiresWriterPermission", UNSET)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time,  Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)




        description = d.pop("description", UNSET)

        drive_id = d.pop("driveId", UNSET)

        explicitly_trashed = d.pop("explicitlyTrashed", UNSET)

        _export_links = d.pop("exportLinks", UNSET)
        export_links: FileExportLinks | Unset
        if isinstance(_export_links,  Unset):
            export_links = UNSET
        else:
            export_links = FileExportLinks.from_dict(_export_links)




        file_extension = d.pop("fileExtension", UNSET)

        folder_color_rgb = d.pop("folderColorRgb", UNSET)

        full_file_extension = d.pop("fullFileExtension", UNSET)

        has_augmented_permissions = d.pop("hasAugmentedPermissions", UNSET)

        has_thumbnail = d.pop("hasThumbnail", UNSET)

        head_revision_id = d.pop("headRevisionId", UNSET)

        icon_link = d.pop("iconLink", UNSET)

        id = d.pop("id", UNSET)

        _image_media_metadata = d.pop("imageMediaMetadata", UNSET)
        image_media_metadata: FileImageMediaMetadata | Unset
        if isinstance(_image_media_metadata,  Unset):
            image_media_metadata = UNSET
        else:
            image_media_metadata = FileImageMediaMetadata.from_dict(_image_media_metadata)




        is_app_authorized = d.pop("isAppAuthorized", UNSET)

        kind = d.pop("kind", UNSET)

        _label_info = d.pop("labelInfo", UNSET)
        label_info: FileLabelInfo | Unset
        if isinstance(_label_info,  Unset):
            label_info = UNSET
        else:
            label_info = FileLabelInfo.from_dict(_label_info)




        _last_modifying_user = d.pop("lastModifyingUser", UNSET)
        last_modifying_user: User | Unset
        if isinstance(_last_modifying_user,  Unset):
            last_modifying_user = UNSET
        else:
            last_modifying_user = User.from_dict(_last_modifying_user)




        _link_share_metadata = d.pop("linkShareMetadata", UNSET)
        link_share_metadata: FileLinkShareMetadata | Unset
        if isinstance(_link_share_metadata,  Unset):
            link_share_metadata = UNSET
        else:
            link_share_metadata = FileLinkShareMetadata.from_dict(_link_share_metadata)




        md_5_checksum = d.pop("md5Checksum", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        modified_by_me = d.pop("modifiedByMe", UNSET)

        _modified_by_me_time = d.pop("modifiedByMeTime", UNSET)
        modified_by_me_time: datetime.datetime | Unset
        if isinstance(_modified_by_me_time,  Unset):
            modified_by_me_time = UNSET
        else:
            modified_by_me_time = isoparse(_modified_by_me_time)




        _modified_time = d.pop("modifiedTime", UNSET)
        modified_time: datetime.datetime | Unset
        if isinstance(_modified_time,  Unset):
            modified_time = UNSET
        else:
            modified_time = isoparse(_modified_time)




        name = d.pop("name", UNSET)

        original_filename = d.pop("originalFilename", UNSET)

        owned_by_me = d.pop("ownedByMe", UNSET)

        _owners = d.pop("owners", UNSET)
        owners: list[User] | Unset = UNSET
        if _owners is not UNSET:
            owners = []
            for owners_item_data in _owners:
                owners_item = User.from_dict(owners_item_data)



                owners.append(owners_item)


        parents = cast(list[str], d.pop("parents", UNSET))


        permission_ids = cast(list[str], d.pop("permissionIds", UNSET))


        _permissions = d.pop("permissions", UNSET)
        permissions: list[Permission] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = Permission.from_dict(permissions_item_data)



                permissions.append(permissions_item)


        _properties = d.pop("properties", UNSET)
        properties: FileProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = FileProperties.from_dict(_properties)




        quota_bytes_used = d.pop("quotaBytesUsed", UNSET)

        resource_key = d.pop("resourceKey", UNSET)

        sha_1_checksum = d.pop("sha1Checksum", UNSET)

        sha_256_checksum = d.pop("sha256Checksum", UNSET)

        shared = d.pop("shared", UNSET)

        _shared_with_me_time = d.pop("sharedWithMeTime", UNSET)
        shared_with_me_time: datetime.datetime | Unset
        if isinstance(_shared_with_me_time,  Unset):
            shared_with_me_time = UNSET
        else:
            shared_with_me_time = isoparse(_shared_with_me_time)




        _sharing_user = d.pop("sharingUser", UNSET)
        sharing_user: User | Unset
        if isinstance(_sharing_user,  Unset):
            sharing_user = UNSET
        else:
            sharing_user = User.from_dict(_sharing_user)




        _shortcut_details = d.pop("shortcutDetails", UNSET)
        shortcut_details: FileShortcutDetails | Unset
        if isinstance(_shortcut_details,  Unset):
            shortcut_details = UNSET
        else:
            shortcut_details = FileShortcutDetails.from_dict(_shortcut_details)




        size = d.pop("size", UNSET)

        spaces = cast(list[str], d.pop("spaces", UNSET))


        starred = d.pop("starred", UNSET)

        team_drive_id = d.pop("teamDriveId", UNSET)

        thumbnail_link = d.pop("thumbnailLink", UNSET)

        thumbnail_version = d.pop("thumbnailVersion", UNSET)

        trashed = d.pop("trashed", UNSET)

        _trashed_time = d.pop("trashedTime", UNSET)
        trashed_time: datetime.datetime | Unset
        if isinstance(_trashed_time,  Unset):
            trashed_time = UNSET
        else:
            trashed_time = isoparse(_trashed_time)




        _trashing_user = d.pop("trashingUser", UNSET)
        trashing_user: User | Unset
        if isinstance(_trashing_user,  Unset):
            trashing_user = UNSET
        else:
            trashing_user = User.from_dict(_trashing_user)




        version = d.pop("version", UNSET)

        _video_media_metadata = d.pop("videoMediaMetadata", UNSET)
        video_media_metadata: FileVideoMediaMetadata | Unset
        if isinstance(_video_media_metadata,  Unset):
            video_media_metadata = UNSET
        else:
            video_media_metadata = FileVideoMediaMetadata.from_dict(_video_media_metadata)




        viewed_by_me = d.pop("viewedByMe", UNSET)

        _viewed_by_me_time = d.pop("viewedByMeTime", UNSET)
        viewed_by_me_time: datetime.datetime | Unset
        if isinstance(_viewed_by_me_time,  Unset):
            viewed_by_me_time = UNSET
        else:
            viewed_by_me_time = isoparse(_viewed_by_me_time)




        viewers_can_copy_content = d.pop("viewersCanCopyContent", UNSET)

        web_content_link = d.pop("webContentLink", UNSET)

        web_view_link = d.pop("webViewLink", UNSET)

        writers_can_share = d.pop("writersCanShare", UNSET)

        file = cls(
            app_properties=app_properties,
            capabilities=capabilities,
            content_hints=content_hints,
            content_restrictions=content_restrictions,
            copy_requires_writer_permission=copy_requires_writer_permission,
            created_time=created_time,
            description=description,
            drive_id=drive_id,
            explicitly_trashed=explicitly_trashed,
            export_links=export_links,
            file_extension=file_extension,
            folder_color_rgb=folder_color_rgb,
            full_file_extension=full_file_extension,
            has_augmented_permissions=has_augmented_permissions,
            has_thumbnail=has_thumbnail,
            head_revision_id=head_revision_id,
            icon_link=icon_link,
            id=id,
            image_media_metadata=image_media_metadata,
            is_app_authorized=is_app_authorized,
            kind=kind,
            label_info=label_info,
            last_modifying_user=last_modifying_user,
            link_share_metadata=link_share_metadata,
            md_5_checksum=md_5_checksum,
            mime_type=mime_type,
            modified_by_me=modified_by_me,
            modified_by_me_time=modified_by_me_time,
            modified_time=modified_time,
            name=name,
            original_filename=original_filename,
            owned_by_me=owned_by_me,
            owners=owners,
            parents=parents,
            permission_ids=permission_ids,
            permissions=permissions,
            properties=properties,
            quota_bytes_used=quota_bytes_used,
            resource_key=resource_key,
            sha_1_checksum=sha_1_checksum,
            sha_256_checksum=sha_256_checksum,
            shared=shared,
            shared_with_me_time=shared_with_me_time,
            sharing_user=sharing_user,
            shortcut_details=shortcut_details,
            size=size,
            spaces=spaces,
            starred=starred,
            team_drive_id=team_drive_id,
            thumbnail_link=thumbnail_link,
            thumbnail_version=thumbnail_version,
            trashed=trashed,
            trashed_time=trashed_time,
            trashing_user=trashing_user,
            version=version,
            video_media_metadata=video_media_metadata,
            viewed_by_me=viewed_by_me,
            viewed_by_me_time=viewed_by_me_time,
            viewers_can_copy_content=viewers_can_copy_content,
            web_content_link=web_content_link,
            web_view_link=web_view_link,
            writers_can_share=writers_can_share,
        )


        file.additional_properties = d
        return file

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
