from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user_bean_avatar_urls import UserBeanAvatarUrls





T = TypeVar("T", bound="UserBean")



@_attrs_define
class UserBean:
    """ 
        Attributes:
            account_id (str | Unset): The account ID of the user, which uniquely identifies the user across all Atlassian
                products. For example, *5b10ac8d82e05b22cc7d4ef5*.
            active (bool | Unset): Whether the user is active.
            avatar_urls (UserBeanAvatarUrls | Unset):
            display_name (str | Unset): The display name of the user. Depending on the user’s privacy setting, this may
                return an alternative value.
            key (str | Unset): This property is deprecated in favor of `accountId` because of privacy changes. See the
                [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
                migration-guide/) for details.
                The key of the user.
            name (str | Unset): This property is deprecated in favor of `accountId` because of privacy changes. See the
                [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
                migration-guide/) for details.
                The username of the user.
            self_ (str | Unset): The URL of the user.
     """

    account_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    avatar_urls: UserBeanAvatarUrls | Unset = UNSET
    display_name: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_bean_avatar_urls import UserBeanAvatarUrls
        account_id = self.account_id

        active = self.active

        avatar_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar_urls, Unset):
            avatar_urls = self.avatar_urls.to_dict()

        display_name = self.display_name

        key = self.key

        name = self.name

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if active is not UNSET:
            field_dict["active"] = active
        if avatar_urls is not UNSET:
            field_dict["avatarUrls"] = avatar_urls
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_bean_avatar_urls import UserBeanAvatarUrls
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        active = d.pop("active", UNSET)

        _avatar_urls = d.pop("avatarUrls", UNSET)
        avatar_urls: UserBeanAvatarUrls | Unset
        if isinstance(_avatar_urls,  Unset):
            avatar_urls = UNSET
        else:
            avatar_urls = UserBeanAvatarUrls.from_dict(_avatar_urls)




        display_name = d.pop("displayName", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        user_bean = cls(
            account_id=account_id,
            active=active,
            avatar_urls=avatar_urls,
            display_name=display_name,
            key=key,
            name=name,
            self_=self_,
        )

        return user_bean

