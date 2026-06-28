from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user_picker_user import UserPickerUser





T = TypeVar("T", bound="FoundUsers")



@_attrs_define
class FoundUsers:
    """ The list of users found in a search, including header text (Showing X of Y matching users) and total of matched
    users.

        Attributes:
            header (str | Unset): Header text indicating the number of users in the response and the total number of users
                found in the search.
            total (int | Unset): The total number of users found in the search.
            users (list[UserPickerUser] | Unset):
     """

    header: str | Unset = UNSET
    total: int | Unset = UNSET
    users: list[UserPickerUser] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_picker_user import UserPickerUser
        header = self.header

        total = self.total

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if header is not UNSET:
            field_dict["header"] = header
        if total is not UNSET:
            field_dict["total"] = total
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_picker_user import UserPickerUser
        d = dict(src_dict)
        header = d.pop("header", UNSET)

        total = d.pop("total", UNSET)

        _users = d.pop("users", UNSET)
        users: list[UserPickerUser] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = UserPickerUser.from_dict(users_item_data)



                users.append(users_item)


        found_users = cls(
            header=header,
            total=total,
            users=users,
        )

        return found_users

