from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.share_permission import SharePermission
  from ..models.user_bean import UserBean





T = TypeVar("T", bound="Dashboard")



@_attrs_define
class Dashboard:
    """ Details of a dashboard.

        Attributes:
            automatic_refresh_ms (int | Unset): The automatic refresh interval for the dashboard in milliseconds.
            description (str | Unset):
            edit_permissions (list[SharePermission] | Unset): The details of any edit share permissions for the dashboard.
            id (str | Unset): The ID of the dashboard.
            is_favourite (bool | Unset): Whether the dashboard is selected as a favorite by the user.
            is_writable (bool | Unset): Whether the current user has permission to edit the dashboard.
            name (str | Unset): The name of the dashboard.
            owner (UserBean | Unset):
            popularity (int | Unset): The number of users who have this dashboard as a favorite.
            rank (int | Unset): The rank of this dashboard.
            self_ (str | Unset): The URL of these dashboard details.
            share_permissions (list[SharePermission] | Unset): The details of any view share permissions for the dashboard.
            system_dashboard (bool | Unset): Whether the current dashboard is system dashboard.
            view (str | Unset): The URL of the dashboard.
     """

    automatic_refresh_ms: int | Unset = UNSET
    description: str | Unset = UNSET
    edit_permissions: list[SharePermission] | Unset = UNSET
    id: str | Unset = UNSET
    is_favourite: bool | Unset = UNSET
    is_writable: bool | Unset = UNSET
    name: str | Unset = UNSET
    owner: UserBean | Unset = UNSET
    popularity: int | Unset = UNSET
    rank: int | Unset = UNSET
    self_: str | Unset = UNSET
    share_permissions: list[SharePermission] | Unset = UNSET
    system_dashboard: bool | Unset = UNSET
    view: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.share_permission import SharePermission
        from ..models.user_bean import UserBean
        automatic_refresh_ms = self.automatic_refresh_ms

        description = self.description

        edit_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edit_permissions, Unset):
            edit_permissions = []
            for edit_permissions_item_data in self.edit_permissions:
                edit_permissions_item = edit_permissions_item_data.to_dict()
                edit_permissions.append(edit_permissions_item)



        id = self.id

        is_favourite = self.is_favourite

        is_writable = self.is_writable

        name = self.name

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        popularity = self.popularity

        rank = self.rank

        self_ = self.self_

        share_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.share_permissions, Unset):
            share_permissions = []
            for share_permissions_item_data in self.share_permissions:
                share_permissions_item = share_permissions_item_data.to_dict()
                share_permissions.append(share_permissions_item)



        system_dashboard = self.system_dashboard

        view = self.view


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if automatic_refresh_ms is not UNSET:
            field_dict["automaticRefreshMs"] = automatic_refresh_ms
        if description is not UNSET:
            field_dict["description"] = description
        if edit_permissions is not UNSET:
            field_dict["editPermissions"] = edit_permissions
        if id is not UNSET:
            field_dict["id"] = id
        if is_favourite is not UNSET:
            field_dict["isFavourite"] = is_favourite
        if is_writable is not UNSET:
            field_dict["isWritable"] = is_writable
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if popularity is not UNSET:
            field_dict["popularity"] = popularity
        if rank is not UNSET:
            field_dict["rank"] = rank
        if self_ is not UNSET:
            field_dict["self"] = self_
        if share_permissions is not UNSET:
            field_dict["sharePermissions"] = share_permissions
        if system_dashboard is not UNSET:
            field_dict["systemDashboard"] = system_dashboard
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.share_permission import SharePermission
        from ..models.user_bean import UserBean
        d = dict(src_dict)
        automatic_refresh_ms = d.pop("automaticRefreshMs", UNSET)

        description = d.pop("description", UNSET)

        _edit_permissions = d.pop("editPermissions", UNSET)
        edit_permissions: list[SharePermission] | Unset = UNSET
        if _edit_permissions is not UNSET:
            edit_permissions = []
            for edit_permissions_item_data in _edit_permissions:
                edit_permissions_item = SharePermission.from_dict(edit_permissions_item_data)



                edit_permissions.append(edit_permissions_item)


        id = d.pop("id", UNSET)

        is_favourite = d.pop("isFavourite", UNSET)

        is_writable = d.pop("isWritable", UNSET)

        name = d.pop("name", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: UserBean | Unset
        if isinstance(_owner,  Unset):
            owner = UNSET
        else:
            owner = UserBean.from_dict(_owner)




        popularity = d.pop("popularity", UNSET)

        rank = d.pop("rank", UNSET)

        self_ = d.pop("self", UNSET)

        _share_permissions = d.pop("sharePermissions", UNSET)
        share_permissions: list[SharePermission] | Unset = UNSET
        if _share_permissions is not UNSET:
            share_permissions = []
            for share_permissions_item_data in _share_permissions:
                share_permissions_item = SharePermission.from_dict(share_permissions_item_data)



                share_permissions.append(share_permissions_item)


        system_dashboard = d.pop("systemDashboard", UNSET)

        view = d.pop("view", UNSET)

        dashboard = cls(
            automatic_refresh_ms=automatic_refresh_ms,
            description=description,
            edit_permissions=edit_permissions,
            id=id,
            is_favourite=is_favourite,
            is_writable=is_writable,
            name=name,
            owner=owner,
            popularity=popularity,
            rank=rank,
            self_=self_,
            share_permissions=share_permissions,
            system_dashboard=system_dashboard,
            view=view,
        )

        return dashboard

