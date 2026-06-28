from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel

from lemma_connectors.core.results import BinaryContentResult

from lemma_connectors.google_drive.generated.pydantic_models import About, ChangeList, Channel, Comment, CommentList, Drive, DriveList, File, FileList, GeneratedIds, LabelList, ModifyLabelsRequest, ModifyLabelsResponse, Permission, PermissionList, Reply, ReplyList, Revision, RevisionList, StartPageToken, TeamDrive, TeamDriveList

class DriveAboutGetToolInput(BaseModel):
    """Input for tool `drive_about_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    model_config = ConfigDict(extra='forbid')

class DriveAboutGetToolOutput(About):
    """Output for tool `drive_about_get`."""
    pass

class DriveChangesGetStartPageTokenToolInput(BaseModel):
    """Input for tool `drive_changes_get_start_page_token`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    drive_id: str | None = Field(default=None, description='The ID of the shared drive for which the starting pageToken for listing future changes from that shared drive is returned.')
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    team_drive_id: str | None = Field(default=None, description='Deprecated use driveId instead.')
    model_config = ConfigDict(extra='forbid')

class DriveChangesGetStartPageTokenToolOutput(StartPageToken):
    """Output for tool `drive_changes_get_start_page_token`."""
    pass

class DriveChangesListToolInput(BaseModel):
    """Input for tool `drive_changes_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    page_token: str = Field(..., description="The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method.")
    drive_id: str | None = Field(default=None, description='The shared drive from which changes are returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier.')
    include_corpus_removals: bool | None = Field(default=None, description='Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.')
    include_items_from_all_drives: bool | None = Field(default=None, description='Whether both My Drive and shared drive items should be included in results.')
    include_labels: str | None = Field(default=None, description='A comma-separated list of IDs of labels to include in the labelInfo part of the response.')
    include_permissions_for_view: str | None = Field(default=None, description="Specifies which additional view's permissions to include in the response. Only 'published' is supported.")
    include_removed: bool | None = Field(default=None, description='Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.')
    include_team_drive_items: bool | None = Field(default=None, description='Deprecated use includeItemsFromAllDrives instead.')
    page_size: int | None = Field(default=None, description='The maximum number of changes to return per page.')
    restrict_to_my_drive: bool | None = Field(default=None, description='Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive.')
    spaces: str | None = Field(default=None, description="A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'.")
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    team_drive_id: str | None = Field(default=None, description='Deprecated use driveId instead.')
    model_config = ConfigDict(extra='forbid')

class DriveChangesListToolOutput(ChangeList):
    """Output for tool `drive_changes_list`."""
    pass

class DriveChangesWatchToolInput(BaseModel):
    """Input for tool `drive_changes_watch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    page_token: str = Field(..., description="The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method.")
    drive_id: str | None = Field(default=None, description='The shared drive from which changes are returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier.')
    include_corpus_removals: bool | None = Field(default=None, description='Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.')
    include_items_from_all_drives: bool | None = Field(default=None, description='Whether both My Drive and shared drive items should be included in results.')
    include_labels: str | None = Field(default=None, description='A comma-separated list of IDs of labels to include in the labelInfo part of the response.')
    include_permissions_for_view: str | None = Field(default=None, description="Specifies which additional view's permissions to include in the response. Only 'published' is supported.")
    include_removed: bool | None = Field(default=None, description='Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.')
    include_team_drive_items: bool | None = Field(default=None, description='Deprecated use includeItemsFromAllDrives instead.')
    page_size: int | None = Field(default=None, description='The maximum number of changes to return per page.')
    restrict_to_my_drive: bool | None = Field(default=None, description='Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive.')
    spaces: str | None = Field(default=None, description="A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'.")
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    team_drive_id: str | None = Field(default=None, description='Deprecated use driveId instead.')
    body: Channel | None = Field(default=None, description='Request body for `drive_changes_watch`.')
    model_config = ConfigDict(extra='forbid')

class DriveChangesWatchToolOutput(Channel):
    """Output for tool `drive_changes_watch`."""
    pass

class DriveChannelsStopToolInput(BaseModel):
    """Input for tool `drive_channels_stop`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    body: Channel | None = Field(default=None, description='Request body for `drive_channels_stop`.')
    model_config = ConfigDict(extra='forbid')

class DriveChannelsStopToolOutput(RootModel[dict[str, object]]):
    """Output for tool `drive_channels_stop`."""
    pass

class DriveCommentsCreateToolInput(BaseModel):
    """Input for tool `drive_comments_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    body: Comment | None = Field(default=None, description='Request body for `drive_comments_create`.')
    model_config = ConfigDict(extra='forbid')

class DriveCommentsCreateToolOutput(Comment):
    """Output for tool `drive_comments_create`."""
    pass

class DriveCommentsDeleteToolInput(BaseModel):
    """Input for tool `drive_comments_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    comment_id: str = Field(..., description='The ID of the comment.')
    model_config = ConfigDict(extra='forbid')

class DriveCommentsDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `drive_comments_delete`."""
    pass

class DriveCommentsGetToolInput(BaseModel):
    """Input for tool `drive_comments_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    comment_id: str = Field(..., description='The ID of the comment.')
    include_deleted: bool | None = Field(default=None, description='Whether to return deleted comments. Deleted comments will not include their original content.')
    model_config = ConfigDict(extra='forbid')

class DriveCommentsGetToolOutput(Comment):
    """Output for tool `drive_comments_get`."""
    pass

class DriveCommentsListToolInput(BaseModel):
    """Input for tool `drive_comments_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    include_deleted: bool | None = Field(default=None, description='Whether to include deleted comments. Deleted comments will not include their original content.')
    page_size: int | None = Field(default=None, description='The maximum number of comments to return per page.')
    page_token: str | None = Field(default=None, description="The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.")
    start_modified_time: str | None = Field(default=None, description="The minimum value of 'modifiedTime' for the result comments (RFC 3339 date-time).")
    model_config = ConfigDict(extra='forbid')

class DriveCommentsListToolOutput(CommentList):
    """Output for tool `drive_comments_list`."""
    pass

class DriveCommentsUpdateToolInput(BaseModel):
    """Input for tool `drive_comments_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    comment_id: str = Field(..., description='The ID of the comment.')
    body: Comment | None = Field(default=None, description='Request body for `drive_comments_update`.')
    model_config = ConfigDict(extra='forbid')

class DriveCommentsUpdateToolOutput(Comment):
    """Output for tool `drive_comments_update`."""
    pass

class DriveDrivesCreateToolInput(BaseModel):
    """Input for tool `drive_drives_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    request_id: str = Field(..., description="An ID, such as a random UUID, which uniquely identifies this user's request for idempotent creation of a shared drive. A repeated request by the same user and with the same request ID will avoid creating duplicates by attempting to create the same shared drive. If the shared drive already exists a 409 error will be returned.")
    body: Drive | None = Field(default=None, description='Request body for `drive_drives_create`.')
    model_config = ConfigDict(extra='forbid')

class DriveDrivesCreateToolOutput(Drive):
    """Output for tool `drive_drives_create`."""
    pass

class DriveDrivesDeleteToolInput(BaseModel):
    """Input for tool `drive_drives_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    drive_id: str = Field(..., description='The ID of the shared drive.')
    allow_item_deletion: bool | None = Field(default=None, description='Whether any items inside the shared drive should also be deleted. This option is only supported when useDomainAdminAccess is also set to true.')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs.')
    model_config = ConfigDict(extra='forbid')

class DriveDrivesDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `drive_drives_delete`."""
    pass

class DriveDrivesGetToolInput(BaseModel):
    """Input for tool `drive_drives_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    drive_id: str = Field(..., description='The ID of the shared drive.')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the shared drive belongs.')
    model_config = ConfigDict(extra='forbid')

class DriveDrivesGetToolOutput(Drive):
    """Output for tool `drive_drives_get`."""
    pass

class DriveDrivesHideToolInput(BaseModel):
    """Input for tool `drive_drives_hide`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    drive_id: str = Field(..., description='The ID of the shared drive.')
    model_config = ConfigDict(extra='forbid')

class DriveDrivesHideToolOutput(Drive):
    """Output for tool `drive_drives_hide`."""
    pass

class DriveDrivesListToolInput(BaseModel):
    """Input for tool `drive_drives_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    page_size: int | None = Field(default=None, description='Maximum number of shared drives to return per page.')
    page_token: str | None = Field(default=None, description='Page token for shared drives.')
    q: str | None = Field(default=None, description='Query string for searching shared drives.')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then all shared drives of the domain in which the requester is an administrator are returned.')
    model_config = ConfigDict(extra='forbid')

class DriveDrivesListToolOutput(DriveList):
    """Output for tool `drive_drives_list`."""
    pass

class DriveDrivesUnhideToolInput(BaseModel):
    """Input for tool `drive_drives_unhide`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    drive_id: str = Field(..., description='The ID of the shared drive.')
    model_config = ConfigDict(extra='forbid')

class DriveDrivesUnhideToolOutput(Drive):
    """Output for tool `drive_drives_unhide`."""
    pass

class DriveDrivesUpdateToolInput(BaseModel):
    """Input for tool `drive_drives_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    drive_id: str = Field(..., description='The ID of the shared drive.')
    use_domain_admin_access: bool | None = Field(default=None, description="Issue the request as a domain administrator. If set to true, then the requester is granted access if they're an administrator of the domain to which the shared drive belongs.")
    body: Drive | None = Field(default=None, description='Request body for `drive_drives_update`.')
    model_config = ConfigDict(extra='forbid')

class DriveDrivesUpdateToolOutput(Drive):
    """Output for tool `drive_drives_update`."""
    pass

class DriveFilesCopyToolInput(BaseModel):
    """Input for tool `drive_files_copy`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    enforce_single_parent: bool | None = Field(default=None, description='Deprecated. Copying files into multiple folders is no longer supported. Use shortcuts instead.')
    ignore_default_visibility: bool | None = Field(default=None, description="Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.")
    include_labels: str | None = Field(default=None, description='A comma-separated list of IDs of labels to include in the labelInfo part of the response.')
    include_permissions_for_view: str | None = Field(default=None, description="Specifies which additional view's permissions to include in the response. Only 'published' is supported.")
    keep_revision_forever: bool | None = Field(default=None, description="Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.")
    ocr_language: str | None = Field(default=None, description='A language hint for OCR processing during image import (ISO 639-1 code).')
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    body: File | None = Field(default=None, description='Request body for `drive_files_copy`.')
    model_config = ConfigDict(extra='forbid')

class DriveFilesCopyToolOutput(File):
    """Output for tool `drive_files_copy`."""
    pass

class DriveFilesCreateToolInput(BaseModel):
    """Input for tool `drive_files_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    enforce_single_parent: bool | None = Field(default=None, description='Deprecated. Creating files in multiple folders is no longer supported.')
    ignore_default_visibility: bool | None = Field(default=None, description="Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.")
    include_labels: str | None = Field(default=None, description='A comma-separated list of IDs of labels to include in the labelInfo part of the response.')
    include_permissions_for_view: str | None = Field(default=None, description="Specifies which additional view's permissions to include in the response. Only 'published' is supported.")
    keep_revision_forever: bool | None = Field(default=None, description="Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.")
    ocr_language: str | None = Field(default=None, description='A language hint for OCR processing during image import (ISO 639-1 code).')
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    use_content_as_indexable_text: bool | None = Field(default=None, description='Whether to use the uploaded content as indexable text.')
    body: File | None = Field(default=None, description='Request body for `drive_files_create`.')
    model_config = ConfigDict(extra='forbid')

class DriveFilesCreateToolOutput(File):
    """Output for tool `drive_files_create`."""
    pass

class DriveFilesDeleteToolInput(BaseModel):
    """Input for tool `drive_files_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    enforce_single_parent: bool | None = Field(default=None, description="Deprecated. If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner's root.")
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    model_config = ConfigDict(extra='forbid')

class DriveFilesDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `drive_files_delete`."""
    pass

class DriveFilesEmptyTrashToolInput(BaseModel):
    """Input for tool `drive_files_empty_trash`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    drive_id: str | None = Field(default=None, description='If set, empties the trash of the provided shared drive.')
    enforce_single_parent: bool | None = Field(default=None, description="Deprecated. If an item is not in a shared drive and its last parent is deleted but the item itself is not, the item will be placed under its owner's root.")
    model_config = ConfigDict(extra='forbid')

class DriveFilesEmptyTrashToolOutput(RootModel[dict[str, object]]):
    """Output for tool `drive_files_empty_trash`."""
    pass

class DriveFilesExportToolInput(BaseModel):
    """Input for tool `drive_files_export`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    mime_type: str = Field(..., description='The MIME type of the format requested for this export.')
    model_config = ConfigDict(extra='forbid')

class DriveFilesExportToolOutput(BinaryContentResult):
    """Binary output for tool `drive_files_export`."""
    pass

class DriveFilesGenerateIdsToolInput(BaseModel):
    """Input for tool `drive_files_generate_ids`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    count: int | None = Field(default=None, description='The number of IDs to return.')
    space: str | None = Field(default=None, description="The space in which the IDs can be used to create new files. Supported values are 'drive' and 'appDataFolder'. (Default: 'drive')")
    type: str | None = Field(default=None, description="The type of items which the IDs can be used for. Supported values are 'files' and 'shortcuts'. Note that 'shortcuts' are only supported in the drive 'space'. (Default: 'files')")
    model_config = ConfigDict(extra='forbid')

class DriveFilesGenerateIdsToolOutput(GeneratedIds):
    """Output for tool `drive_files_generate_ids`."""
    pass

class DriveFilesGetToolInput(BaseModel):
    """Input for tool `drive_files_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    acknowledge_abuse: bool | None = Field(default=None, description='Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.')
    include_labels: str | None = Field(default=None, description='A comma-separated list of IDs of labels to include in the labelInfo part of the response.')
    include_permissions_for_view: str | None = Field(default=None, description="Specifies which additional view's permissions to include in the response. Only 'published' is supported.")
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    model_config = ConfigDict(extra='forbid')

class DriveFilesGetToolOutput(File):
    """Output for tool `drive_files_get`."""
    pass

class DriveFilesListToolInput(BaseModel):
    """Input for tool `drive_files_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    corpora: str | None = Field(default=None, description="Groupings of files to which the query applies. Supported groupings are: 'user' (files created by, opened by, or shared directly with the user), 'drive' (files in the specified shared drive as indicated by the 'driveId'), 'domain' (files shared to the user's domain), and 'allDrives' (A combination of 'user' and 'drive' for all drives where the user is a member). When able, use 'user' or 'drive', instead of 'allDrives', for efficiency.")
    corpus: Literal['domain', 'user'] | None = Field(default=None, description="The source of files to list. Deprecated: use 'corpora' instead.")
    drive_id: str | None = Field(default=None, description='ID of the shared drive to search.')
    include_items_from_all_drives: bool | None = Field(default=None, description='Whether both My Drive and shared drive items should be included in results.')
    include_labels: str | None = Field(default=None, description='A comma-separated list of IDs of labels to include in the labelInfo part of the response.')
    include_permissions_for_view: str | None = Field(default=None, description="Specifies which additional view's permissions to include in the response. Only 'published' is supported.")
    include_team_drive_items: bool | None = Field(default=None, description='Deprecated use includeItemsFromAllDrives instead.')
    order_by: str | None = Field(default=None, description="A comma-separated list of sort keys. Valid keys are 'createdTime', 'folder', 'modifiedByMeTime', 'modifiedTime', 'name', 'name_natural', 'quotaBytesUsed', 'recency', 'sharedWithMeTime', 'starred', and 'viewedByMeTime'. Each key sorts ascending by default, but may be reversed with the 'desc' modifier. Example usage: ?orderBy=folder,modifiedTime desc,name. Please note that there is a current limitation for users with approximately one million files in which the requested sort order is ignored.")
    page_size: int | None = Field(default=None, description='The maximum number of files to return per page. Partial or empty result pages are possible even before the end of the files list has been reached.')
    page_token: str | None = Field(default=None, description="The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.")
    q: str | None = Field(default=None, description='A query for filtering the file results. See the "Search for Files" guide for supported syntax.')
    spaces: str | None = Field(default=None, description="A comma-separated list of spaces to query within the corpora. Supported values are 'drive' and 'appDataFolder'.")
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    team_drive_id: str | None = Field(default=None, description='Deprecated use driveId instead.')
    model_config = ConfigDict(extra='forbid')

class DriveFilesListToolOutput(FileList):
    """Output for tool `drive_files_list`."""
    pass

class DriveFilesListLabelsToolInput(BaseModel):
    """Input for tool `drive_files_list_labels`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    max_results: int | None = Field(default=None, description='The maximum number of labels to return per page. When not set, this defaults to 100.')
    page_token: str | None = Field(default=None, description="The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.")
    model_config = ConfigDict(extra='forbid')

class DriveFilesListLabelsToolOutput(LabelList):
    """Output for tool `drive_files_list_labels`."""
    pass

class DriveFilesModifyLabelsToolInput(BaseModel):
    """Input for tool `drive_files_modify_labels`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file for which the labels are modified.')
    body: ModifyLabelsRequest | None = Field(default=None, description='Request body for `drive_files_modify_labels`.')
    model_config = ConfigDict(extra='forbid')

class DriveFilesModifyLabelsToolOutput(ModifyLabelsResponse):
    """Output for tool `drive_files_modify_labels`."""
    pass

class DriveFilesUpdateToolInput(BaseModel):
    """Input for tool `drive_files_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    add_parents: str | None = Field(default=None, description='A comma-separated list of parent IDs to add.')
    enforce_single_parent: bool | None = Field(default=None, description='Deprecated. Adding files to multiple folders is no longer supported. Use shortcuts instead.')
    include_labels: str | None = Field(default=None, description='A comma-separated list of IDs of labels to include in the labelInfo part of the response.')
    include_permissions_for_view: str | None = Field(default=None, description="Specifies which additional view's permissions to include in the response. Only 'published' is supported.")
    keep_revision_forever: bool | None = Field(default=None, description="Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Google Drive. Only 200 revisions for the file can be kept forever. If the limit is reached, try deleting pinned revisions.")
    ocr_language: str | None = Field(default=None, description='A language hint for OCR processing during image import (ISO 639-1 code).')
    remove_parents: str | None = Field(default=None, description='A comma-separated list of parent IDs to remove.')
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    use_content_as_indexable_text: bool | None = Field(default=None, description='Whether to use the uploaded content as indexable text.')
    body: File | None = Field(default=None, description='Request body for `drive_files_update`.')
    model_config = ConfigDict(extra='forbid')

class DriveFilesUpdateToolOutput(File):
    """Output for tool `drive_files_update`."""
    pass

class DriveFilesWatchToolInput(BaseModel):
    """Input for tool `drive_files_watch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    acknowledge_abuse: bool | None = Field(default=None, description='Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.')
    include_labels: str | None = Field(default=None, description='A comma-separated list of IDs of labels to include in the labelInfo part of the response.')
    include_permissions_for_view: str | None = Field(default=None, description="Specifies which additional view's permissions to include in the response. Only 'published' is supported.")
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    body: Channel | None = Field(default=None, description='Request body for `drive_files_watch`.')
    model_config = ConfigDict(extra='forbid')

class DriveFilesWatchToolOutput(Channel):
    """Output for tool `drive_files_watch`."""
    pass

class DrivePermissionsCreateToolInput(BaseModel):
    """Input for tool `drive_permissions_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file or shared drive.')
    email_message: str | None = Field(default=None, description='A plain text custom message to include in the notification email.')
    enforce_single_parent: bool | None = Field(default=None, description='Deprecated. See moveToNewOwnersRoot for details.')
    move_to_new_owners_root: bool | None = Field(default=None, description="This parameter will only take effect if the item is not in a shared drive and the request is attempting to transfer the ownership of the item. If set to true, the item will be moved to the new owner's My Drive root folder and all prior parents removed. If set to false, parents are not changed.")
    send_notification_email: bool | None = Field(default=None, description='Whether to send a notification email when sharing to users or groups. This defaults to true for users and groups, and is not allowed for other requests. It must not be disabled for ownership transfers.')
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    transfer_ownership: bool | None = Field(default=None, description='Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect. File owners can only transfer ownership of files existing on My Drive. Files existing in a shared drive are owned by the organization that owns that shared drive. Ownership transfers are not supported for files and folders in shared drives. Organizers of a shared drive can move items from that shared drive into their My Drive which transfers the ownership to them.')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.')
    body: Permission | None = Field(default=None, description='Request body for `drive_permissions_create`.')
    model_config = ConfigDict(extra='forbid')

class DrivePermissionsCreateToolOutput(Permission):
    """Output for tool `drive_permissions_create`."""
    pass

class DrivePermissionsDeleteToolInput(BaseModel):
    """Input for tool `drive_permissions_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file or shared drive.')
    permission_id: str = Field(..., description='The ID of the permission.')
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.')
    model_config = ConfigDict(extra='forbid')

class DrivePermissionsDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `drive_permissions_delete`."""
    pass

class DrivePermissionsGetToolInput(BaseModel):
    """Input for tool `drive_permissions_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    permission_id: str = Field(..., description='The ID of the permission.')
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.')
    model_config = ConfigDict(extra='forbid')

class DrivePermissionsGetToolOutput(Permission):
    """Output for tool `drive_permissions_get`."""
    pass

class DrivePermissionsListToolInput(BaseModel):
    """Input for tool `drive_permissions_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file or shared drive.')
    include_permissions_for_view: str | None = Field(default=None, description="Specifies which additional view's permissions to include in the response. Only 'published' is supported.")
    page_size: int | None = Field(default=None, description='The maximum number of permissions to return per page. When not set for files in a shared drive, at most 100 results will be returned. When not set for files that are not in a shared drive, the entire list will be returned.')
    page_token: str | None = Field(default=None, description="The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.")
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.')
    model_config = ConfigDict(extra='forbid')

class DrivePermissionsListToolOutput(PermissionList):
    """Output for tool `drive_permissions_list`."""
    pass

class DrivePermissionsUpdateToolInput(BaseModel):
    """Input for tool `drive_permissions_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file or shared drive.')
    permission_id: str = Field(..., description='The ID of the permission.')
    remove_expiration: bool | None = Field(default=None, description='Whether to remove the expiration date.')
    supports_all_drives: bool | None = Field(default=None, description='Whether the requesting application supports both My Drives and shared drives.')
    supports_team_drives: bool | None = Field(default=None, description='Deprecated use supportsAllDrives instead.')
    transfer_ownership: bool | None = Field(default=None, description='Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect. File owners can only transfer ownership of files existing on My Drive. Files existing in a shared drive are owned by the organization that owns that shared drive. Ownership transfers are not supported for files and folders in shared drives. Organizers of a shared drive can move items from that shared drive into their My Drive which transfers the ownership to them.')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.')
    body: Permission | None = Field(default=None, description='Request body for `drive_permissions_update`.')
    model_config = ConfigDict(extra='forbid')

class DrivePermissionsUpdateToolOutput(Permission):
    """Output for tool `drive_permissions_update`."""
    pass

class DriveRepliesCreateToolInput(BaseModel):
    """Input for tool `drive_replies_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    comment_id: str = Field(..., description='The ID of the comment.')
    body: Reply | None = Field(default=None, description='Request body for `drive_replies_create`.')
    model_config = ConfigDict(extra='forbid')

class DriveRepliesCreateToolOutput(Reply):
    """Output for tool `drive_replies_create`."""
    pass

class DriveRepliesDeleteToolInput(BaseModel):
    """Input for tool `drive_replies_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    comment_id: str = Field(..., description='The ID of the comment.')
    reply_id: str = Field(..., description='The ID of the reply.')
    model_config = ConfigDict(extra='forbid')

class DriveRepliesDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `drive_replies_delete`."""
    pass

class DriveRepliesGetToolInput(BaseModel):
    """Input for tool `drive_replies_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    comment_id: str = Field(..., description='The ID of the comment.')
    reply_id: str = Field(..., description='The ID of the reply.')
    include_deleted: bool | None = Field(default=None, description='Whether to return deleted replies. Deleted replies will not include their original content.')
    model_config = ConfigDict(extra='forbid')

class DriveRepliesGetToolOutput(Reply):
    """Output for tool `drive_replies_get`."""
    pass

class DriveRepliesListToolInput(BaseModel):
    """Input for tool `drive_replies_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    comment_id: str = Field(..., description='The ID of the comment.')
    include_deleted: bool | None = Field(default=None, description='Whether to include deleted replies. Deleted replies will not include their original content.')
    page_size: int | None = Field(default=None, description='The maximum number of replies to return per page.')
    page_token: str | None = Field(default=None, description="The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.")
    model_config = ConfigDict(extra='forbid')

class DriveRepliesListToolOutput(ReplyList):
    """Output for tool `drive_replies_list`."""
    pass

class DriveRepliesUpdateToolInput(BaseModel):
    """Input for tool `drive_replies_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    comment_id: str = Field(..., description='The ID of the comment.')
    reply_id: str = Field(..., description='The ID of the reply.')
    body: Reply | None = Field(default=None, description='Request body for `drive_replies_update`.')
    model_config = ConfigDict(extra='forbid')

class DriveRepliesUpdateToolOutput(Reply):
    """Output for tool `drive_replies_update`."""
    pass

class DriveRevisionsDeleteToolInput(BaseModel):
    """Input for tool `drive_revisions_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    revision_id: str = Field(..., description='The ID of the revision.')
    model_config = ConfigDict(extra='forbid')

class DriveRevisionsDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `drive_revisions_delete`."""
    pass

class DriveRevisionsGetToolInput(BaseModel):
    """Input for tool `drive_revisions_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    revision_id: str = Field(..., description='The ID of the revision.')
    acknowledge_abuse: bool | None = Field(default=None, description='Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.')
    model_config = ConfigDict(extra='forbid')

class DriveRevisionsGetToolOutput(Revision):
    """Output for tool `drive_revisions_get`."""
    pass

class DriveRevisionsListToolInput(BaseModel):
    """Input for tool `drive_revisions_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    page_size: int | None = Field(default=None, description='The maximum number of revisions to return per page.')
    page_token: str | None = Field(default=None, description="The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response.")
    model_config = ConfigDict(extra='forbid')

class DriveRevisionsListToolOutput(RevisionList):
    """Output for tool `drive_revisions_list`."""
    pass

class DriveRevisionsUpdateToolInput(BaseModel):
    """Input for tool `drive_revisions_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    file_id: str = Field(..., description='The ID of the file.')
    revision_id: str = Field(..., description='The ID of the revision.')
    body: Revision | None = Field(default=None, description='Request body for `drive_revisions_update`.')
    model_config = ConfigDict(extra='forbid')

class DriveRevisionsUpdateToolOutput(Revision):
    """Output for tool `drive_revisions_update`."""
    pass

class DriveTeamdrivesCreateToolInput(BaseModel):
    """Input for tool `drive_teamdrives_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    request_id: str = Field(..., description="An ID, such as a random UUID, which uniquely identifies this user's request for idempotent creation of a Team Drive. A repeated request by the same user and with the same request ID will avoid creating duplicates by attempting to create the same Team Drive. If the Team Drive already exists a 409 error will be returned.")
    body: TeamDrive | None = Field(default=None, description='Request body for `drive_teamdrives_create`.')
    model_config = ConfigDict(extra='forbid')

class DriveTeamdrivesCreateToolOutput(TeamDrive):
    """Output for tool `drive_teamdrives_create`."""
    pass

class DriveTeamdrivesDeleteToolInput(BaseModel):
    """Input for tool `drive_teamdrives_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    team_drive_id: str = Field(..., description='The ID of the Team Drive')
    model_config = ConfigDict(extra='forbid')

class DriveTeamdrivesDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `drive_teamdrives_delete`."""
    pass

class DriveTeamdrivesGetToolInput(BaseModel):
    """Input for tool `drive_teamdrives_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    team_drive_id: str = Field(..., description='The ID of the Team Drive')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the Team Drive belongs.')
    model_config = ConfigDict(extra='forbid')

class DriveTeamdrivesGetToolOutput(TeamDrive):
    """Output for tool `drive_teamdrives_get`."""
    pass

class DriveTeamdrivesListToolInput(BaseModel):
    """Input for tool `drive_teamdrives_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    page_size: int | None = Field(default=None, description='Maximum number of Team Drives to return.')
    page_token: str | None = Field(default=None, description='Page token for Team Drives.')
    q: str | None = Field(default=None, description='Query string for searching Team Drives.')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then all Team Drives of the domain in which the requester is an administrator are returned.')
    model_config = ConfigDict(extra='forbid')

class DriveTeamdrivesListToolOutput(TeamDriveList):
    """Output for tool `drive_teamdrives_list`."""
    pass

class DriveTeamdrivesUpdateToolInput(BaseModel):
    """Input for tool `drive_teamdrives_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    team_drive_id: str = Field(..., description='The ID of the Team Drive')
    use_domain_admin_access: bool | None = Field(default=None, description='Issue the request as a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the Team Drive belongs.')
    body: TeamDrive | None = Field(default=None, description='Request body for `drive_teamdrives_update`.')
    model_config = ConfigDict(extra='forbid')

class DriveTeamdrivesUpdateToolOutput(TeamDrive):
    """Output for tool `drive_teamdrives_update`."""
    pass

INPUT_MODELS = {
    'drive_about_get': DriveAboutGetToolInput,
    'drive_changes_get_start_page_token': DriveChangesGetStartPageTokenToolInput,
    'drive_changes_list': DriveChangesListToolInput,
    'drive_changes_watch': DriveChangesWatchToolInput,
    'drive_channels_stop': DriveChannelsStopToolInput,
    'drive_comments_create': DriveCommentsCreateToolInput,
    'drive_comments_delete': DriveCommentsDeleteToolInput,
    'drive_comments_get': DriveCommentsGetToolInput,
    'drive_comments_list': DriveCommentsListToolInput,
    'drive_comments_update': DriveCommentsUpdateToolInput,
    'drive_drives_create': DriveDrivesCreateToolInput,
    'drive_drives_delete': DriveDrivesDeleteToolInput,
    'drive_drives_get': DriveDrivesGetToolInput,
    'drive_drives_hide': DriveDrivesHideToolInput,
    'drive_drives_list': DriveDrivesListToolInput,
    'drive_drives_unhide': DriveDrivesUnhideToolInput,
    'drive_drives_update': DriveDrivesUpdateToolInput,
    'drive_files_copy': DriveFilesCopyToolInput,
    'drive_files_create': DriveFilesCreateToolInput,
    'drive_files_delete': DriveFilesDeleteToolInput,
    'drive_files_empty_trash': DriveFilesEmptyTrashToolInput,
    'drive_files_export': DriveFilesExportToolInput,
    'drive_files_generate_ids': DriveFilesGenerateIdsToolInput,
    'drive_files_get': DriveFilesGetToolInput,
    'drive_files_list': DriveFilesListToolInput,
    'drive_files_list_labels': DriveFilesListLabelsToolInput,
    'drive_files_modify_labels': DriveFilesModifyLabelsToolInput,
    'drive_files_update': DriveFilesUpdateToolInput,
    'drive_files_watch': DriveFilesWatchToolInput,
    'drive_permissions_create': DrivePermissionsCreateToolInput,
    'drive_permissions_delete': DrivePermissionsDeleteToolInput,
    'drive_permissions_get': DrivePermissionsGetToolInput,
    'drive_permissions_list': DrivePermissionsListToolInput,
    'drive_permissions_update': DrivePermissionsUpdateToolInput,
    'drive_replies_create': DriveRepliesCreateToolInput,
    'drive_replies_delete': DriveRepliesDeleteToolInput,
    'drive_replies_get': DriveRepliesGetToolInput,
    'drive_replies_list': DriveRepliesListToolInput,
    'drive_replies_update': DriveRepliesUpdateToolInput,
    'drive_revisions_delete': DriveRevisionsDeleteToolInput,
    'drive_revisions_get': DriveRevisionsGetToolInput,
    'drive_revisions_list': DriveRevisionsListToolInput,
    'drive_revisions_update': DriveRevisionsUpdateToolInput,
    'drive_teamdrives_create': DriveTeamdrivesCreateToolInput,
    'drive_teamdrives_delete': DriveTeamdrivesDeleteToolInput,
    'drive_teamdrives_get': DriveTeamdrivesGetToolInput,
    'drive_teamdrives_list': DriveTeamdrivesListToolInput,
    'drive_teamdrives_update': DriveTeamdrivesUpdateToolInput,
}

OUTPUT_MODELS = {
    'drive_about_get': DriveAboutGetToolOutput,
    'drive_changes_get_start_page_token': DriveChangesGetStartPageTokenToolOutput,
    'drive_changes_list': DriveChangesListToolOutput,
    'drive_changes_watch': DriveChangesWatchToolOutput,
    'drive_channels_stop': DriveChannelsStopToolOutput,
    'drive_comments_create': DriveCommentsCreateToolOutput,
    'drive_comments_delete': DriveCommentsDeleteToolOutput,
    'drive_comments_get': DriveCommentsGetToolOutput,
    'drive_comments_list': DriveCommentsListToolOutput,
    'drive_comments_update': DriveCommentsUpdateToolOutput,
    'drive_drives_create': DriveDrivesCreateToolOutput,
    'drive_drives_delete': DriveDrivesDeleteToolOutput,
    'drive_drives_get': DriveDrivesGetToolOutput,
    'drive_drives_hide': DriveDrivesHideToolOutput,
    'drive_drives_list': DriveDrivesListToolOutput,
    'drive_drives_unhide': DriveDrivesUnhideToolOutput,
    'drive_drives_update': DriveDrivesUpdateToolOutput,
    'drive_files_copy': DriveFilesCopyToolOutput,
    'drive_files_create': DriveFilesCreateToolOutput,
    'drive_files_delete': DriveFilesDeleteToolOutput,
    'drive_files_empty_trash': DriveFilesEmptyTrashToolOutput,
    'drive_files_export': DriveFilesExportToolOutput,
    'drive_files_generate_ids': DriveFilesGenerateIdsToolOutput,
    'drive_files_get': DriveFilesGetToolOutput,
    'drive_files_list': DriveFilesListToolOutput,
    'drive_files_list_labels': DriveFilesListLabelsToolOutput,
    'drive_files_modify_labels': DriveFilesModifyLabelsToolOutput,
    'drive_files_update': DriveFilesUpdateToolOutput,
    'drive_files_watch': DriveFilesWatchToolOutput,
    'drive_permissions_create': DrivePermissionsCreateToolOutput,
    'drive_permissions_delete': DrivePermissionsDeleteToolOutput,
    'drive_permissions_get': DrivePermissionsGetToolOutput,
    'drive_permissions_list': DrivePermissionsListToolOutput,
    'drive_permissions_update': DrivePermissionsUpdateToolOutput,
    'drive_replies_create': DriveRepliesCreateToolOutput,
    'drive_replies_delete': DriveRepliesDeleteToolOutput,
    'drive_replies_get': DriveRepliesGetToolOutput,
    'drive_replies_list': DriveRepliesListToolOutput,
    'drive_replies_update': DriveRepliesUpdateToolOutput,
    'drive_revisions_delete': DriveRevisionsDeleteToolOutput,
    'drive_revisions_get': DriveRevisionsGetToolOutput,
    'drive_revisions_list': DriveRevisionsListToolOutput,
    'drive_revisions_update': DriveRevisionsUpdateToolOutput,
    'drive_teamdrives_create': DriveTeamdrivesCreateToolOutput,
    'drive_teamdrives_delete': DriveTeamdrivesDeleteToolOutput,
    'drive_teamdrives_get': DriveTeamdrivesGetToolOutput,
    'drive_teamdrives_list': DriveTeamdrivesListToolOutput,
    'drive_teamdrives_update': DriveTeamdrivesUpdateToolOutput,
}
