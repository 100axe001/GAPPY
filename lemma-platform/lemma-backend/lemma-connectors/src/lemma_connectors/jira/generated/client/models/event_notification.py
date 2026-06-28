from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.event_notification_notification_type import EventNotificationNotificationType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.field_details import FieldDetails
  from ..models.group_name import GroupName
  from ..models.project_role import ProjectRole
  from ..models.user_details import UserDetails





T = TypeVar("T", bound="EventNotification")



@_attrs_define
class EventNotification:
    """ Details about a notification associated with an event.

        Attributes:
            email_address (str | Unset): The email address.
            expand (str | Unset): Expand options that include additional event notification details in the response.
            field (FieldDetails | Unset): Details about a field.
            group (GroupName | Unset): Details about a group.
            id (int | Unset): The ID of the notification.
            notification_type (EventNotificationNotificationType | Unset): Identifies the recipients of the notification.
            parameter (str | Unset): As a group's name can change, use of `recipient` is recommended. The identifier
                associated with the `notificationType` value that defines the receiver of the notification, where the receiver
                isn't implied by `notificationType` value. So, when `notificationType` is:

                 *  `User` The `parameter` is the user account ID.
                 *  `Group` The `parameter` is the group name.
                 *  `ProjectRole` The `parameter` is the project role ID.
                 *  `UserCustomField` The `parameter` is the ID of the custom field.
                 *  `GroupCustomField` The `parameter` is the ID of the custom field.
            project_role (ProjectRole | Unset): Details about the roles in a project.
            recipient (str | Unset): The identifier associated with the `notificationType` value that defines the receiver
                of the notification, where the receiver isn't implied by the `notificationType` value. So, when
                `notificationType` is:

                 *  `User`, `recipient` is the user account ID.
                 *  `Group`, `recipient` is the group ID.
                 *  `ProjectRole`, `recipient` is the project role ID.
                 *  `UserCustomField`, `recipient` is the ID of the custom field.
                 *  `GroupCustomField`, `recipient` is the ID of the custom field.
            user (UserDetails | Unset): User details permitted by the user's Atlassian Account privacy settings. However, be
                aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
     """

    email_address: str | Unset = UNSET
    expand: str | Unset = UNSET
    field: FieldDetails | Unset = UNSET
    group: GroupName | Unset = UNSET
    id: int | Unset = UNSET
    notification_type: EventNotificationNotificationType | Unset = UNSET
    parameter: str | Unset = UNSET
    project_role: ProjectRole | Unset = UNSET
    recipient: str | Unset = UNSET
    user: UserDetails | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_details import FieldDetails
        from ..models.group_name import GroupName
        from ..models.project_role import ProjectRole
        from ..models.user_details import UserDetails
        email_address = self.email_address

        expand = self.expand

        field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        id = self.id

        notification_type: str | Unset = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type.value


        parameter = self.parameter

        project_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_role, Unset):
            project_role = self.project_role.to_dict()

        recipient = self.recipient

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if expand is not UNSET:
            field_dict["expand"] = expand
        if field is not UNSET:
            field_dict["field"] = field
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if notification_type is not UNSET:
            field_dict["notificationType"] = notification_type
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if project_role is not UNSET:
            field_dict["projectRole"] = project_role
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_details import FieldDetails
        from ..models.group_name import GroupName
        from ..models.project_role import ProjectRole
        from ..models.user_details import UserDetails
        d = dict(src_dict)
        email_address = d.pop("emailAddress", UNSET)

        expand = d.pop("expand", UNSET)

        _field = d.pop("field", UNSET)
        field: FieldDetails | Unset
        if isinstance(_field,  Unset):
            field = UNSET
        else:
            field = FieldDetails.from_dict(_field)




        _group = d.pop("group", UNSET)
        group: GroupName | Unset
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = GroupName.from_dict(_group)




        id = d.pop("id", UNSET)

        _notification_type = d.pop("notificationType", UNSET)
        notification_type: EventNotificationNotificationType | Unset
        if isinstance(_notification_type,  Unset):
            notification_type = UNSET
        else:
            notification_type = EventNotificationNotificationType(_notification_type)




        parameter = d.pop("parameter", UNSET)

        _project_role = d.pop("projectRole", UNSET)
        project_role: ProjectRole | Unset
        if isinstance(_project_role,  Unset):
            project_role = UNSET
        else:
            project_role = ProjectRole.from_dict(_project_role)




        recipient = d.pop("recipient", UNSET)

        _user = d.pop("user", UNSET)
        user: UserDetails | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = UserDetails.from_dict(_user)




        event_notification = cls(
            email_address=email_address,
            expand=expand,
            field=field,
            group=group,
            id=id,
            notification_type=notification_type,
            parameter=parameter,
            project_role=project_role,
            recipient=recipient,
            user=user,
        )

        return event_notification

