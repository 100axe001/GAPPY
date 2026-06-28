from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.about_drive_themes_item import AboutDriveThemesItem
  from ..models.about_export_formats import AboutExportFormats
  from ..models.about_import_formats import AboutImportFormats
  from ..models.about_max_import_sizes import AboutMaxImportSizes
  from ..models.about_storage_quota import AboutStorageQuota
  from ..models.about_team_drive_themes_item import AboutTeamDriveThemesItem
  from ..models.user import User





T = TypeVar("T", bound="About")



@_attrs_define
class About:
    """ Information about the user, the user's Drive, and system capabilities.

        Attributes:
            app_installed (bool | Unset): Whether the user has installed the requesting app.
            can_create_drives (bool | Unset): Whether the user can create shared drives.
            can_create_team_drives (bool | Unset): Deprecated - use canCreateDrives instead.
            drive_themes (list[AboutDriveThemesItem] | Unset): A list of themes that are supported for shared drives.
            export_formats (AboutExportFormats | Unset): A map of source MIME type to possible targets for all supported
                exports.
            folder_color_palette (list[str] | Unset): The currently supported folder colors as RGB hex strings.
            import_formats (AboutImportFormats | Unset): A map of source MIME type to possible targets for all supported
                imports.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#about". Default:
                'drive#about'.
            max_import_sizes (AboutMaxImportSizes | Unset): A map of maximum import sizes by MIME type, in bytes.
            max_upload_size (str | Unset): The maximum upload size in bytes.
            storage_quota (AboutStorageQuota | Unset): The user's storage quota limits and usage. All fields are measured in
                bytes.
            team_drive_themes (list[AboutTeamDriveThemesItem] | Unset): Deprecated - use driveThemes instead.
            user (User | Unset): Information about a Drive user.
     """

    app_installed: bool | Unset = UNSET
    can_create_drives: bool | Unset = UNSET
    can_create_team_drives: bool | Unset = UNSET
    drive_themes: list[AboutDriveThemesItem] | Unset = UNSET
    export_formats: AboutExportFormats | Unset = UNSET
    folder_color_palette: list[str] | Unset = UNSET
    import_formats: AboutImportFormats | Unset = UNSET
    kind: str | Unset = 'drive#about'
    max_import_sizes: AboutMaxImportSizes | Unset = UNSET
    max_upload_size: str | Unset = UNSET
    storage_quota: AboutStorageQuota | Unset = UNSET
    team_drive_themes: list[AboutTeamDriveThemesItem] | Unset = UNSET
    user: User | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.about_drive_themes_item import AboutDriveThemesItem
        from ..models.about_export_formats import AboutExportFormats
        from ..models.about_import_formats import AboutImportFormats
        from ..models.about_max_import_sizes import AboutMaxImportSizes
        from ..models.about_storage_quota import AboutStorageQuota
        from ..models.about_team_drive_themes_item import AboutTeamDriveThemesItem
        from ..models.user import User
        app_installed = self.app_installed

        can_create_drives = self.can_create_drives

        can_create_team_drives = self.can_create_team_drives

        drive_themes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.drive_themes, Unset):
            drive_themes = []
            for drive_themes_item_data in self.drive_themes:
                drive_themes_item = drive_themes_item_data.to_dict()
                drive_themes.append(drive_themes_item)



        export_formats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.export_formats, Unset):
            export_formats = self.export_formats.to_dict()

        folder_color_palette: list[str] | Unset = UNSET
        if not isinstance(self.folder_color_palette, Unset):
            folder_color_palette = self.folder_color_palette



        import_formats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.import_formats, Unset):
            import_formats = self.import_formats.to_dict()

        kind = self.kind

        max_import_sizes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_import_sizes, Unset):
            max_import_sizes = self.max_import_sizes.to_dict()

        max_upload_size = self.max_upload_size

        storage_quota: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_quota, Unset):
            storage_quota = self.storage_quota.to_dict()

        team_drive_themes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.team_drive_themes, Unset):
            team_drive_themes = []
            for team_drive_themes_item_data in self.team_drive_themes:
                team_drive_themes_item = team_drive_themes_item_data.to_dict()
                team_drive_themes.append(team_drive_themes_item)



        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if app_installed is not UNSET:
            field_dict["appInstalled"] = app_installed
        if can_create_drives is not UNSET:
            field_dict["canCreateDrives"] = can_create_drives
        if can_create_team_drives is not UNSET:
            field_dict["canCreateTeamDrives"] = can_create_team_drives
        if drive_themes is not UNSET:
            field_dict["driveThemes"] = drive_themes
        if export_formats is not UNSET:
            field_dict["exportFormats"] = export_formats
        if folder_color_palette is not UNSET:
            field_dict["folderColorPalette"] = folder_color_palette
        if import_formats is not UNSET:
            field_dict["importFormats"] = import_formats
        if kind is not UNSET:
            field_dict["kind"] = kind
        if max_import_sizes is not UNSET:
            field_dict["maxImportSizes"] = max_import_sizes
        if max_upload_size is not UNSET:
            field_dict["maxUploadSize"] = max_upload_size
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota
        if team_drive_themes is not UNSET:
            field_dict["teamDriveThemes"] = team_drive_themes
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.about_drive_themes_item import AboutDriveThemesItem
        from ..models.about_export_formats import AboutExportFormats
        from ..models.about_import_formats import AboutImportFormats
        from ..models.about_max_import_sizes import AboutMaxImportSizes
        from ..models.about_storage_quota import AboutStorageQuota
        from ..models.about_team_drive_themes_item import AboutTeamDriveThemesItem
        from ..models.user import User
        d = dict(src_dict)
        app_installed = d.pop("appInstalled", UNSET)

        can_create_drives = d.pop("canCreateDrives", UNSET)

        can_create_team_drives = d.pop("canCreateTeamDrives", UNSET)

        _drive_themes = d.pop("driveThemes", UNSET)
        drive_themes: list[AboutDriveThemesItem] | Unset = UNSET
        if _drive_themes is not UNSET:
            drive_themes = []
            for drive_themes_item_data in _drive_themes:
                drive_themes_item = AboutDriveThemesItem.from_dict(drive_themes_item_data)



                drive_themes.append(drive_themes_item)


        _export_formats = d.pop("exportFormats", UNSET)
        export_formats: AboutExportFormats | Unset
        if isinstance(_export_formats,  Unset):
            export_formats = UNSET
        else:
            export_formats = AboutExportFormats.from_dict(_export_formats)




        folder_color_palette = cast(list[str], d.pop("folderColorPalette", UNSET))


        _import_formats = d.pop("importFormats", UNSET)
        import_formats: AboutImportFormats | Unset
        if isinstance(_import_formats,  Unset):
            import_formats = UNSET
        else:
            import_formats = AboutImportFormats.from_dict(_import_formats)




        kind = d.pop("kind", UNSET)

        _max_import_sizes = d.pop("maxImportSizes", UNSET)
        max_import_sizes: AboutMaxImportSizes | Unset
        if isinstance(_max_import_sizes,  Unset):
            max_import_sizes = UNSET
        else:
            max_import_sizes = AboutMaxImportSizes.from_dict(_max_import_sizes)




        max_upload_size = d.pop("maxUploadSize", UNSET)

        _storage_quota = d.pop("storageQuota", UNSET)
        storage_quota: AboutStorageQuota | Unset
        if isinstance(_storage_quota,  Unset):
            storage_quota = UNSET
        else:
            storage_quota = AboutStorageQuota.from_dict(_storage_quota)




        _team_drive_themes = d.pop("teamDriveThemes", UNSET)
        team_drive_themes: list[AboutTeamDriveThemesItem] | Unset = UNSET
        if _team_drive_themes is not UNSET:
            team_drive_themes = []
            for team_drive_themes_item_data in _team_drive_themes:
                team_drive_themes_item = AboutTeamDriveThemesItem.from_dict(team_drive_themes_item_data)



                team_drive_themes.append(team_drive_themes_item)


        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)




        about = cls(
            app_installed=app_installed,
            can_create_drives=can_create_drives,
            can_create_team_drives=can_create_team_drives,
            drive_themes=drive_themes,
            export_formats=export_formats,
            folder_color_palette=folder_color_palette,
            import_formats=import_formats,
            kind=kind,
            max_import_sizes=max_import_sizes,
            max_upload_size=max_upload_size,
            storage_quota=storage_quota,
            team_drive_themes=team_drive_themes,
            user=user,
        )


        about.additional_properties = d
        return about

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
