from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.paged_list_user_details_application_user import PagedListUserDetailsApplicationUser





T = TypeVar("T", bound="Group")



@_attrs_define
class Group:
    """ 
        Attributes:
            expand (str | Unset): Expand options that include additional group details in the response.
            group_id (None | str | Unset): The ID of the group, which uniquely identifies the group across all Atlassian
                products. For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*.
            name (str | Unset): The name of group.
            self_ (str | Unset): The URL for these group details.
            users (PagedListUserDetailsApplicationUser | Unset): A paged list. To access additional details append `[start-
                index:end-index]` to the expand request. For example, `?expand=sharedUsers[10:40]` returns a list starting at
                item 10 and finishing at item 40.
     """

    expand: str | Unset = UNSET
    group_id: None | str | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET
    users: PagedListUserDetailsApplicationUser | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.paged_list_user_details_application_user import PagedListUserDetailsApplicationUser
        expand = self.expand

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        name = self.name

        self_ = self.self_

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expand is not UNSET:
            field_dict["expand"] = expand
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paged_list_user_details_application_user import PagedListUserDetailsApplicationUser
        d = dict(src_dict)
        expand = d.pop("expand", UNSET)

        def _parse_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))


        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        _users = d.pop("users", UNSET)
        users: PagedListUserDetailsApplicationUser | Unset
        if isinstance(_users,  Unset):
            users = UNSET
        else:
            users = PagedListUserDetailsApplicationUser.from_dict(_users)




        group = cls(
            expand=expand,
            group_id=group_id,
            name=name,
            self_=self_,
            users=users,
        )

        return group

