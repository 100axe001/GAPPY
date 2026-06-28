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
  from ..models.permission_permission_details_item import PermissionPermissionDetailsItem
  from ..models.permission_team_drive_permission_details_item import PermissionTeamDrivePermissionDetailsItem





T = TypeVar("T", bound="Permission")



@_attrs_define
class Permission:
    """ A permission for a file. A permission grants a user, group, domain, or the world access to a file or a folder
    hierarchy.

        Attributes:
            allow_file_discovery (bool | Unset): Whether the permission allows the file to be discovered through search.
                This is only applicable for permissions of type domain or anyone.
            deleted (bool | Unset): Whether the account associated with this permission has been deleted. This field only
                pertains to user and group permissions.
            display_name (str | Unset): The "pretty" name of the value of the permission. The following is a list of
                examples for each type of permission:
                - user - User's full name, as defined for their Google Account, such as "Joe Smith."
                - group - Name of the Google Group, such as "The Company Administrators."
                - domain - String domain name, such as "your-company.com."
                - anyone - No displayName is present.
            domain (str | Unset): The domain to which this permission refers. The following options are currently allowed:
                - The entire domain, such as "your-company.com."
                - A target audience, such as "ID.audience.googledomains.com."
            email_address (str | Unset): The email address of the user or group to which this permission refers.
            expiration_time (datetime.datetime | Unset): The time at which this permission will expire (RFC 3339 date-time).
                Expiration times have the following restrictions:
                - They cannot be set on shared drive items.
                - They can only be set on user and group permissions.
                - The time must be in the future.
                - The time cannot be more than one year in the future.
            id (str | Unset): The ID of this permission. This is a unique identifier for the grantee, and is published in
                User resources as permissionId. IDs should be treated as opaque values.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#permission".
                Default: 'drive#permission'.
            pending_owner (bool | Unset): Whether the account associated with this permission is a pending owner. Only
                populated for user type permissions for files that aren't in a shared drive.
            permission_details (list[PermissionPermissionDetailsItem] | Unset): Details of whether the permissions on this
                shared drive item are inherited or are directly on this item. This is an output-only field that's present only
                for shared drive items.
            photo_link (str | Unset): A link to the user's profile photo, if available.
            role (str | Unset): The role granted by this permission. While new values may be supported in the future, the
                following are currently allowed:
                - owner
                - organizer
                - fileOrganizer
                - writer
                - commenter
                - reader
            team_drive_permission_details (list[PermissionTeamDrivePermissionDetailsItem] | Unset): Deprecated - use
                permissionDetails instead.
            type_ (str | Unset): The type of the grantee. Valid values are:
                - user
                - group
                - domain
                - anyone  When creating a permission, if type is user or group, you must provide an emailAddress for the user or
                group. When type is domain, you must provide a domain. There isn't extra information required for the anyone
                type.
            view (str | Unset): Indicates the view for this permission. Only populated for permissions that belong to a
                view. published is the only supported value.
     """

    allow_file_discovery: bool | Unset = UNSET
    deleted: bool | Unset = UNSET
    display_name: str | Unset = UNSET
    domain: str | Unset = UNSET
    email_address: str | Unset = UNSET
    expiration_time: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'drive#permission'
    pending_owner: bool | Unset = UNSET
    permission_details: list[PermissionPermissionDetailsItem] | Unset = UNSET
    photo_link: str | Unset = UNSET
    role: str | Unset = UNSET
    team_drive_permission_details: list[PermissionTeamDrivePermissionDetailsItem] | Unset = UNSET
    type_: str | Unset = UNSET
    view: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_permission_details_item import PermissionPermissionDetailsItem
        from ..models.permission_team_drive_permission_details_item import PermissionTeamDrivePermissionDetailsItem
        allow_file_discovery = self.allow_file_discovery

        deleted = self.deleted

        display_name = self.display_name

        domain = self.domain

        email_address = self.email_address

        expiration_time: str | Unset = UNSET
        if not isinstance(self.expiration_time, Unset):
            expiration_time = self.expiration_time.isoformat()

        id = self.id

        kind = self.kind

        pending_owner = self.pending_owner

        permission_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permission_details, Unset):
            permission_details = []
            for permission_details_item_data in self.permission_details:
                permission_details_item = permission_details_item_data.to_dict()
                permission_details.append(permission_details_item)



        photo_link = self.photo_link

        role = self.role

        team_drive_permission_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.team_drive_permission_details, Unset):
            team_drive_permission_details = []
            for team_drive_permission_details_item_data in self.team_drive_permission_details:
                team_drive_permission_details_item = team_drive_permission_details_item_data.to_dict()
                team_drive_permission_details.append(team_drive_permission_details_item)



        type_ = self.type_

        view = self.view


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allow_file_discovery is not UNSET:
            field_dict["allowFileDiscovery"] = allow_file_discovery
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if domain is not UNSET:
            field_dict["domain"] = domain
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if pending_owner is not UNSET:
            field_dict["pendingOwner"] = pending_owner
        if permission_details is not UNSET:
            field_dict["permissionDetails"] = permission_details
        if photo_link is not UNSET:
            field_dict["photoLink"] = photo_link
        if role is not UNSET:
            field_dict["role"] = role
        if team_drive_permission_details is not UNSET:
            field_dict["teamDrivePermissionDetails"] = team_drive_permission_details
        if type_ is not UNSET:
            field_dict["type"] = type_
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_permission_details_item import PermissionPermissionDetailsItem
        from ..models.permission_team_drive_permission_details_item import PermissionTeamDrivePermissionDetailsItem
        d = dict(src_dict)
        allow_file_discovery = d.pop("allowFileDiscovery", UNSET)

        deleted = d.pop("deleted", UNSET)

        display_name = d.pop("displayName", UNSET)

        domain = d.pop("domain", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        _expiration_time = d.pop("expirationTime", UNSET)
        expiration_time: datetime.datetime | Unset
        if isinstance(_expiration_time,  Unset):
            expiration_time = UNSET
        else:
            expiration_time = isoparse(_expiration_time)




        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        pending_owner = d.pop("pendingOwner", UNSET)

        _permission_details = d.pop("permissionDetails", UNSET)
        permission_details: list[PermissionPermissionDetailsItem] | Unset = UNSET
        if _permission_details is not UNSET:
            permission_details = []
            for permission_details_item_data in _permission_details:
                permission_details_item = PermissionPermissionDetailsItem.from_dict(permission_details_item_data)



                permission_details.append(permission_details_item)


        photo_link = d.pop("photoLink", UNSET)

        role = d.pop("role", UNSET)

        _team_drive_permission_details = d.pop("teamDrivePermissionDetails", UNSET)
        team_drive_permission_details: list[PermissionTeamDrivePermissionDetailsItem] | Unset = UNSET
        if _team_drive_permission_details is not UNSET:
            team_drive_permission_details = []
            for team_drive_permission_details_item_data in _team_drive_permission_details:
                team_drive_permission_details_item = PermissionTeamDrivePermissionDetailsItem.from_dict(team_drive_permission_details_item_data)



                team_drive_permission_details.append(team_drive_permission_details_item)


        type_ = d.pop("type", UNSET)

        view = d.pop("view", UNSET)

        permission = cls(
            allow_file_discovery=allow_file_discovery,
            deleted=deleted,
            display_name=display_name,
            domain=domain,
            email_address=email_address,
            expiration_time=expiration_time,
            id=id,
            kind=kind,
            pending_owner=pending_owner,
            permission_details=permission_details,
            photo_link=photo_link,
            role=role,
            team_drive_permission_details=team_drive_permission_details,
            type_=type_,
            view=view,
        )


        permission.additional_properties = d
        return permission

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
