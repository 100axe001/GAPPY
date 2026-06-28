from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.group_name import GroupName
  from ..models.user_details import UserDetails





T = TypeVar("T", bound="NotificationRecipients")



@_attrs_define
class NotificationRecipients:
    """ Details of the users and groups to receive the notification.

        Attributes:
            assignee (bool | Unset): Whether the notification should be sent to the issue's assignees.
            group_ids (list[str] | Unset): List of groupIds to receive the notification.
            groups (list[GroupName] | Unset): List of groups to receive the notification.
            reporter (bool | Unset): Whether the notification should be sent to the issue's reporter.
            users (list[UserDetails] | Unset): List of users to receive the notification.
            voters (bool | Unset): Whether the notification should be sent to the issue's voters.
            watchers (bool | Unset): Whether the notification should be sent to the issue's watchers.
     """

    assignee: bool | Unset = UNSET
    group_ids: list[str] | Unset = UNSET
    groups: list[GroupName] | Unset = UNSET
    reporter: bool | Unset = UNSET
    users: list[UserDetails] | Unset = UNSET
    voters: bool | Unset = UNSET
    watchers: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.group_name import GroupName
        from ..models.user_details import UserDetails
        assignee = self.assignee

        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids



        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)



        reporter = self.reporter

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)



        voters = self.voters

        watchers = self.watchers


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if groups is not UNSET:
            field_dict["groups"] = groups
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if users is not UNSET:
            field_dict["users"] = users
        if voters is not UNSET:
            field_dict["voters"] = voters
        if watchers is not UNSET:
            field_dict["watchers"] = watchers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_name import GroupName
        from ..models.user_details import UserDetails
        d = dict(src_dict)
        assignee = d.pop("assignee", UNSET)

        group_ids = cast(list[str], d.pop("groupIds", UNSET))


        _groups = d.pop("groups", UNSET)
        groups: list[GroupName] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = GroupName.from_dict(groups_item_data)



                groups.append(groups_item)


        reporter = d.pop("reporter", UNSET)

        _users = d.pop("users", UNSET)
        users: list[UserDetails] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = UserDetails.from_dict(users_item_data)



                users.append(users_item)


        voters = d.pop("voters", UNSET)

        watchers = d.pop("watchers", UNSET)

        notification_recipients = cls(
            assignee=assignee,
            group_ids=group_ids,
            groups=groups,
            reporter=reporter,
            users=users,
            voters=voters,
            watchers=watchers,
        )


        notification_recipients.additional_properties = d
        return notification_recipients

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
