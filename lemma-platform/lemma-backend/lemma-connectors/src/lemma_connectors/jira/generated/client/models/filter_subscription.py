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
  from ..models.user import User





T = TypeVar("T", bound="FilterSubscription")



@_attrs_define
class FilterSubscription:
    """ Details of a user or group subscribing to a filter.

        Attributes:
            group (GroupName | Unset): Details about a group.
            id (int | Unset): The ID of the filter subscription.
            user (User | Unset): A user with details as permitted by the user's Atlassian Account privacy settings. However,
                be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
     """

    group: GroupName | Unset = UNSET
    id: int | Unset = UNSET
    user: User | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.group_name import GroupName
        from ..models.user import User
        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        id = self.id

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_name import GroupName
        from ..models.user import User
        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: GroupName | Unset
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = GroupName.from_dict(_group)




        id = d.pop("id", UNSET)

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)




        filter_subscription = cls(
            group=group,
            id=id,
            user=user,
        )

        return filter_subscription

