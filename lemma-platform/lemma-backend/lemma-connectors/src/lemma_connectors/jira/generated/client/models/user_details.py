from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.avatar_urls_bean import AvatarUrlsBean





T = TypeVar("T", bound="UserDetails")



@_attrs_define
class UserDetails:
    """ User details permitted by the user's Atlassian Account privacy settings. However, be aware of these exceptions:

     *  User record deleted from Atlassian: This occurs as the result of a right to be forgotten request. In this case,
    `displayName` provides an indication and other parameters have default values or are blank (for example, email is
    blank).
     *  User record corrupted: This occurs as a results of events such as a server import and can only happen to deleted
    users. In this case, `accountId` returns *unknown* and all other parameters have fallback values.
     *  User record unavailable: This usually occurs due to an internal service outage. In this case, all parameters
    have fallback values.

        Attributes:
            account_id (str | Unset): The account ID of the user, which uniquely identifies the user across all Atlassian
                products. For example, *5b10ac8d82e05b22cc7d4ef5*.
            account_type (str | Unset): The type of account represented by this user. This will be one of 'atlassian'
                (normal users), 'app' (application user) or 'customer' (Jira Service Desk customer user)
            active (bool | Unset): Whether the user is active.
            avatar_urls (AvatarUrlsBean | Unset):
            display_name (str | Unset): The display name of the user. Depending on the user’s privacy settings, this may
                return an alternative value.
            email_address (str | Unset): The email address of the user. Depending on the user’s privacy settings, this may
                be returned as null.
            key (str | Unset): This property is no longer available and will be removed from the documentation soon. See the
                [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
                migration-guide/) for details.
            name (str | Unset): This property is no longer available and will be removed from the documentation soon. See
                the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-
                api-migration-guide/) for details.
            self_ (str | Unset): The URL of the user.
            time_zone (str | Unset): The time zone specified in the user's profile. Depending on the user’s privacy
                settings, this may be returned as null.
     """

    account_id: str | Unset = UNSET
    account_type: str | Unset = UNSET
    active: bool | Unset = UNSET
    avatar_urls: AvatarUrlsBean | Unset = UNSET
    display_name: str | Unset = UNSET
    email_address: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET
    time_zone: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.avatar_urls_bean import AvatarUrlsBean
        account_id = self.account_id

        account_type = self.account_type

        active = self.active

        avatar_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar_urls, Unset):
            avatar_urls = self.avatar_urls.to_dict()

        display_name = self.display_name

        email_address = self.email_address

        key = self.key

        name = self.name

        self_ = self.self_

        time_zone = self.time_zone


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if active is not UNSET:
            field_dict["active"] = active
        if avatar_urls is not UNSET:
            field_dict["avatarUrls"] = avatar_urls
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar_urls_bean import AvatarUrlsBean
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        account_type = d.pop("accountType", UNSET)

        active = d.pop("active", UNSET)

        _avatar_urls = d.pop("avatarUrls", UNSET)
        avatar_urls: AvatarUrlsBean | Unset
        if isinstance(_avatar_urls,  Unset):
            avatar_urls = UNSET
        else:
            avatar_urls = AvatarUrlsBean.from_dict(_avatar_urls)




        display_name = d.pop("displayName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        user_details = cls(
            account_id=account_id,
            account_type=account_type,
            active=active,
            avatar_urls=avatar_urls,
            display_name=display_name,
            email_address=email_address,
            key=key,
            name=name,
            self_=self_,
            time_zone=time_zone,
        )

        return user_details

