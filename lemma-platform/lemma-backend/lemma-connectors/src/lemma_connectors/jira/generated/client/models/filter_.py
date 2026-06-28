from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.filter_subscriptions_list import FilterSubscriptionsList
  from ..models.share_permission import SharePermission
  from ..models.user import User
  from ..models.user_list import UserList





T = TypeVar("T", bound="Filter")



@_attrs_define
class Filter:
    """ Details about a filter.

        Attributes:
            name (str): The name of the filter. Must be unique.
            description (str | Unset): A description of the filter.
            edit_permissions (list[SharePermission] | Unset): The groups and projects that can edit the filter.
            favourite (bool | Unset): Whether the filter is selected as a favorite.
            favourited_count (int | Unset): The count of how many users have selected this filter as a favorite, including
                the filter owner.
            id (str | Unset): The unique identifier for the filter.
            jql (str | Unset): The JQL query for the filter. For example, *project = SSP AND issuetype = Bug*.
            owner (User | Unset): A user with details as permitted by the user's Atlassian Account privacy settings.
                However, be aware of these exceptions:

                 *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this
                case, `displayName` provides an indication and other parameters have default values or are blank (for example,
                email is blank).
                 *  User record corrupted: This occurs as a results of events such as a server import and can only happen to
                deleted users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
                 *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
                have fallback values.
            search_url (str | Unset): A URL to view the filter results in Jira, using the [Search for issues using
                JQL](#api-rest-api-3-filter-search-get) operation with the filter's JQL string to return the filter results. For
                example, *https://your-domain.atlassian.net/rest/api/3/search?jql=project+%3D+SSP+AND+issuetype+%3D+Bug*.
            self_ (str | Unset): The URL of the filter.
            share_permissions (list[SharePermission] | Unset): The groups and projects that the filter is shared with.
            shared_users (UserList | Unset): A paginated list of users sharing the filter. This includes users that are
                members of the groups or can browse the projects that the filter is shared with.
            subscriptions (FilterSubscriptionsList | Unset): A paginated list of subscriptions to a filter.
            view_url (str | Unset): A URL to view the filter results in Jira, using the ID of the filter. For example,
                *https://your-domain.atlassian.net/issues/?filter=10100*.
     """

    name: str
    description: str | Unset = UNSET
    edit_permissions: list[SharePermission] | Unset = UNSET
    favourite: bool | Unset = UNSET
    favourited_count: int | Unset = UNSET
    id: str | Unset = UNSET
    jql: str | Unset = UNSET
    owner: User | Unset = UNSET
    search_url: str | Unset = UNSET
    self_: str | Unset = UNSET
    share_permissions: list[SharePermission] | Unset = UNSET
    shared_users: UserList | Unset = UNSET
    subscriptions: FilterSubscriptionsList | Unset = UNSET
    view_url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_subscriptions_list import FilterSubscriptionsList
        from ..models.share_permission import SharePermission
        from ..models.user import User
        from ..models.user_list import UserList
        name = self.name

        description = self.description

        edit_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edit_permissions, Unset):
            edit_permissions = []
            for edit_permissions_item_data in self.edit_permissions:
                edit_permissions_item = edit_permissions_item_data.to_dict()
                edit_permissions.append(edit_permissions_item)



        favourite = self.favourite

        favourited_count = self.favourited_count

        id = self.id

        jql = self.jql

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        search_url = self.search_url

        self_ = self.self_

        share_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.share_permissions, Unset):
            share_permissions = []
            for share_permissions_item_data in self.share_permissions:
                share_permissions_item = share_permissions_item_data.to_dict()
                share_permissions.append(share_permissions_item)



        shared_users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shared_users, Unset):
            shared_users = self.shared_users.to_dict()

        subscriptions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions.to_dict()

        view_url = self.view_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if edit_permissions is not UNSET:
            field_dict["editPermissions"] = edit_permissions
        if favourite is not UNSET:
            field_dict["favourite"] = favourite
        if favourited_count is not UNSET:
            field_dict["favouritedCount"] = favourited_count
        if id is not UNSET:
            field_dict["id"] = id
        if jql is not UNSET:
            field_dict["jql"] = jql
        if owner is not UNSET:
            field_dict["owner"] = owner
        if search_url is not UNSET:
            field_dict["searchUrl"] = search_url
        if self_ is not UNSET:
            field_dict["self"] = self_
        if share_permissions is not UNSET:
            field_dict["sharePermissions"] = share_permissions
        if shared_users is not UNSET:
            field_dict["sharedUsers"] = shared_users
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if view_url is not UNSET:
            field_dict["viewUrl"] = view_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_subscriptions_list import FilterSubscriptionsList
        from ..models.share_permission import SharePermission
        from ..models.user import User
        from ..models.user_list import UserList
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _edit_permissions = d.pop("editPermissions", UNSET)
        edit_permissions: list[SharePermission] | Unset = UNSET
        if _edit_permissions is not UNSET:
            edit_permissions = []
            for edit_permissions_item_data in _edit_permissions:
                edit_permissions_item = SharePermission.from_dict(edit_permissions_item_data)



                edit_permissions.append(edit_permissions_item)


        favourite = d.pop("favourite", UNSET)

        favourited_count = d.pop("favouritedCount", UNSET)

        id = d.pop("id", UNSET)

        jql = d.pop("jql", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: User | Unset
        if isinstance(_owner,  Unset):
            owner = UNSET
        else:
            owner = User.from_dict(_owner)




        search_url = d.pop("searchUrl", UNSET)

        self_ = d.pop("self", UNSET)

        _share_permissions = d.pop("sharePermissions", UNSET)
        share_permissions: list[SharePermission] | Unset = UNSET
        if _share_permissions is not UNSET:
            share_permissions = []
            for share_permissions_item_data in _share_permissions:
                share_permissions_item = SharePermission.from_dict(share_permissions_item_data)



                share_permissions.append(share_permissions_item)


        _shared_users = d.pop("sharedUsers", UNSET)
        shared_users: UserList | Unset
        if isinstance(_shared_users,  Unset):
            shared_users = UNSET
        else:
            shared_users = UserList.from_dict(_shared_users)




        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: FilterSubscriptionsList | Unset
        if isinstance(_subscriptions,  Unset):
            subscriptions = UNSET
        else:
            subscriptions = FilterSubscriptionsList.from_dict(_subscriptions)




        view_url = d.pop("viewUrl", UNSET)

        filter_ = cls(
            name=name,
            description=description,
            edit_permissions=edit_permissions,
            favourite=favourite,
            favourited_count=favourited_count,
            id=id,
            jql=jql,
            owner=owner,
            search_url=search_url,
            self_=self_,
            share_permissions=share_permissions,
            shared_users=shared_users,
            subscriptions=subscriptions,
            view_url=view_url,
        )

        return filter_

