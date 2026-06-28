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





T = TypeVar("T", bound="ApplicationRole")



@_attrs_define
class ApplicationRole:
    """ Details of an application role.

        Attributes:
            default_groups (list[str] | Unset): The groups that are granted default access for this application role. As a
                group's name can change, use of `defaultGroupsDetails` is recommended to identify a groups.
            default_groups_details (list[GroupName] | Unset): The groups that are granted default access for this
                application role.
            defined (bool | Unset): Deprecated.
            group_details (list[GroupName] | Unset): The groups associated with the application role.
            groups (list[str] | Unset): The groups associated with the application role. As a group's name can change, use
                of `groupDetails` is recommended to identify a groups.
            has_unlimited_seats (bool | Unset):
            key (str | Unset): The key of the application role.
            name (str | Unset): The display name of the application role.
            number_of_seats (int | Unset): The maximum count of users on your license.
            platform (bool | Unset): Indicates if the application role belongs to Jira platform (`jira-core`).
            remaining_seats (int | Unset): The count of users remaining on your license.
            selected_by_default (bool | Unset): Determines whether this application role should be selected by default on
                user creation.
            user_count (int | Unset): The number of users counting against your license.
            user_count_description (str | Unset): The [type of users](https://confluence.atlassian.com/x/lRW3Ng) being
                counted against your license.
     """

    default_groups: list[str] | Unset = UNSET
    default_groups_details: list[GroupName] | Unset = UNSET
    defined: bool | Unset = UNSET
    group_details: list[GroupName] | Unset = UNSET
    groups: list[str] | Unset = UNSET
    has_unlimited_seats: bool | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    number_of_seats: int | Unset = UNSET
    platform: bool | Unset = UNSET
    remaining_seats: int | Unset = UNSET
    selected_by_default: bool | Unset = UNSET
    user_count: int | Unset = UNSET
    user_count_description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.group_name import GroupName
        default_groups: list[str] | Unset = UNSET
        if not isinstance(self.default_groups, Unset):
            default_groups = self.default_groups



        default_groups_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_groups_details, Unset):
            default_groups_details = []
            for default_groups_details_item_data in self.default_groups_details:
                default_groups_details_item = default_groups_details_item_data.to_dict()
                default_groups_details.append(default_groups_details_item)



        defined = self.defined

        group_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_details, Unset):
            group_details = []
            for group_details_item_data in self.group_details:
                group_details_item = group_details_item_data.to_dict()
                group_details.append(group_details_item)



        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups



        has_unlimited_seats = self.has_unlimited_seats

        key = self.key

        name = self.name

        number_of_seats = self.number_of_seats

        platform = self.platform

        remaining_seats = self.remaining_seats

        selected_by_default = self.selected_by_default

        user_count = self.user_count

        user_count_description = self.user_count_description


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if default_groups is not UNSET:
            field_dict["defaultGroups"] = default_groups
        if default_groups_details is not UNSET:
            field_dict["defaultGroupsDetails"] = default_groups_details
        if defined is not UNSET:
            field_dict["defined"] = defined
        if group_details is not UNSET:
            field_dict["groupDetails"] = group_details
        if groups is not UNSET:
            field_dict["groups"] = groups
        if has_unlimited_seats is not UNSET:
            field_dict["hasUnlimitedSeats"] = has_unlimited_seats
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if number_of_seats is not UNSET:
            field_dict["numberOfSeats"] = number_of_seats
        if platform is not UNSET:
            field_dict["platform"] = platform
        if remaining_seats is not UNSET:
            field_dict["remainingSeats"] = remaining_seats
        if selected_by_default is not UNSET:
            field_dict["selectedByDefault"] = selected_by_default
        if user_count is not UNSET:
            field_dict["userCount"] = user_count
        if user_count_description is not UNSET:
            field_dict["userCountDescription"] = user_count_description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_name import GroupName
        d = dict(src_dict)
        default_groups = cast(list[str], d.pop("defaultGroups", UNSET))


        _default_groups_details = d.pop("defaultGroupsDetails", UNSET)
        default_groups_details: list[GroupName] | Unset = UNSET
        if _default_groups_details is not UNSET:
            default_groups_details = []
            for default_groups_details_item_data in _default_groups_details:
                default_groups_details_item = GroupName.from_dict(default_groups_details_item_data)



                default_groups_details.append(default_groups_details_item)


        defined = d.pop("defined", UNSET)

        _group_details = d.pop("groupDetails", UNSET)
        group_details: list[GroupName] | Unset = UNSET
        if _group_details is not UNSET:
            group_details = []
            for group_details_item_data in _group_details:
                group_details_item = GroupName.from_dict(group_details_item_data)



                group_details.append(group_details_item)


        groups = cast(list[str], d.pop("groups", UNSET))


        has_unlimited_seats = d.pop("hasUnlimitedSeats", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        number_of_seats = d.pop("numberOfSeats", UNSET)

        platform = d.pop("platform", UNSET)

        remaining_seats = d.pop("remainingSeats", UNSET)

        selected_by_default = d.pop("selectedByDefault", UNSET)

        user_count = d.pop("userCount", UNSET)

        user_count_description = d.pop("userCountDescription", UNSET)

        application_role = cls(
            default_groups=default_groups,
            default_groups_details=default_groups_details,
            defined=defined,
            group_details=group_details,
            groups=groups,
            has_unlimited_seats=has_unlimited_seats,
            key=key,
            name=name,
            number_of_seats=number_of_seats,
            platform=platform,
            remaining_seats=remaining_seats,
            selected_by_default=selected_by_default,
            user_count=user_count,
            user_count_description=user_count_description,
        )

        return application_role

