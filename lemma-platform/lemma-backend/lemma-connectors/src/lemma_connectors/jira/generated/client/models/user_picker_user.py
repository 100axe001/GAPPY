from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UserPickerUser")



@_attrs_define
class UserPickerUser:
    """ A user found in a search.

        Attributes:
            account_id (str | Unset): The account ID of the user, which uniquely identifies the user across all Atlassian
                products. For example, *5b10ac8d82e05b22cc7d4ef5*.
            avatar_url (str | Unset): The avatar URL of the user.
            display_name (str | Unset): The display name of the user. Depending on the user’s privacy setting, this may be
                returned as null.
            html (str | Unset): The display name, email address, and key of the user with the matched query string
                highlighted with the HTML bold tag.
            key (str | Unset): This property is no longer available. See the [deprecation
                notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-
                guide/) for details.
            name (str | Unset): This property is no longer available . See the [deprecation
                notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-
                guide/) for details.
     """

    account_id: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    display_name: str | Unset = UNSET
    html: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        avatar_url = self.avatar_url

        display_name = self.display_name

        html = self.html

        key = self.key

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if html is not UNSET:
            field_dict["html"] = html
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        display_name = d.pop("displayName", UNSET)

        html = d.pop("html", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        user_picker_user = cls(
            account_id=account_id,
            avatar_url=avatar_url,
            display_name=display_name,
            html=html,
            key=key,
            name=name,
        )

        return user_picker_user

