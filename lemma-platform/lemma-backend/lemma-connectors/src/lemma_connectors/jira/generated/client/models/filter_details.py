from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.filter_subscription import FilterSubscription
  from ..models.share_permission import SharePermission
  from ..models.user import User





T = TypeVar("T", bound="FilterDetails")



@_attrs_define
class FilterDetails:
    """ Details of a filter.

        Attributes:
            name (str): The name of the filter.
            description (str | Unset): The description of the filter.
            edit_permissions (list[SharePermission] | Unset): The groups and projects that can edit the filter. This can be
                specified when updating a filter, but not when creating a filter.
            expand (str | Unset): Expand options that include additional filter details in the response.
            favourite (bool | Unset): Whether the filter is selected as a favorite by any users, not including the filter
                owner.
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
            share_permissions (list[SharePermission] | Unset): The groups and projects that the filter is shared with. This
                can be specified when updating a filter, but not when creating a filter.
            subscriptions (list[FilterSubscription] | Unset): The users that are subscribed to the filter.
            view_url (str | Unset): A URL to view the filter results in Jira, using the ID of the filter. For example,
                *https://your-domain.atlassian.net/issues/?filter=10100*.
     """

    name: str
    description: str | Unset = UNSET
    edit_permissions: list[SharePermission] | Unset = UNSET
    expand: str | Unset = UNSET
    favourite: bool | Unset = UNSET
    favourited_count: int | Unset = UNSET
    id: str | Unset = UNSET
    jql: str | Unset = UNSET
    owner: User | Unset = UNSET
    search_url: str | Unset = UNSET
    self_: str | Unset = UNSET
    share_permissions: list[SharePermission] | Unset = UNSET
    subscriptions: list[FilterSubscription] | Unset = UNSET
    view_url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_subscription import FilterSubscription
        from ..models.share_permission import SharePermission
        from ..models.user import User
        name = self.name

        description = self.description

        edit_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edit_permissions, Unset):
            edit_permissions = []
            for edit_permissions_item_data in self.edit_permissions:
                edit_permissions_item = edit_permissions_item_data.to_dict()
                edit_permissions.append(edit_permissions_item)



        expand = self.expand

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



        subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)



        view_url = self.view_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if edit_permissions is not UNSET:
            field_dict["editPermissions"] = edit_permissions
        if expand is not UNSET:
            field_dict["expand"] = expand
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
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if view_url is not UNSET:
            field_dict["viewUrl"] = view_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_subscription import FilterSubscription
        from ..models.share_permission import SharePermission
        from ..models.user import User
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


        expand = d.pop("expand", UNSET)

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


        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[FilterSubscription] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = FilterSubscription.from_dict(subscriptions_item_data)



                subscriptions.append(subscriptions_item)


        view_url = d.pop("viewUrl", UNSET)

        filter_details = cls(
            name=name,
            description=description,
            edit_permissions=edit_permissions,
            expand=expand,
            favourite=favourite,
            favourited_count=favourited_count,
            id=id,
            jql=jql,
            owner=owner,
            search_url=search_url,
            self_=self_,
            share_permissions=share_permissions,
            subscriptions=subscriptions,
            view_url=view_url,
        )

        return filter_details

