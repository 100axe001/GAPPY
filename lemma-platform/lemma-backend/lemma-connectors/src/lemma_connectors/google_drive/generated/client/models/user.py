from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="User")



@_attrs_define
class User:
    """ Information about a Drive user.

        Attributes:
            display_name (str | Unset): A plain text displayable name for this user.
            email_address (str | Unset): The email address of the user. This may not be present in certain contexts if the
                user has not made their email address visible to the requester.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#user". Default:
                'drive#user'.
            me (bool | Unset): Whether this user is the requesting user.
            permission_id (str | Unset): The user's ID as visible in Permission resources.
            photo_link (str | Unset): A link to the user's profile photo, if available.
     """

    display_name: str | Unset = UNSET
    email_address: str | Unset = UNSET
    kind: str | Unset = 'drive#user'
    me: bool | Unset = UNSET
    permission_id: str | Unset = UNSET
    photo_link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        email_address = self.email_address

        kind = self.kind

        me = self.me

        permission_id = self.permission_id

        photo_link = self.photo_link


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if kind is not UNSET:
            field_dict["kind"] = kind
        if me is not UNSET:
            field_dict["me"] = me
        if permission_id is not UNSET:
            field_dict["permissionId"] = permission_id
        if photo_link is not UNSET:
            field_dict["photoLink"] = photo_link

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        kind = d.pop("kind", UNSET)

        me = d.pop("me", UNSET)

        permission_id = d.pop("permissionId", UNSET)

        photo_link = d.pop("photoLink", UNSET)

        user = cls(
            display_name=display_name,
            email_address=email_address,
            kind=kind,
            me=me,
            permission_id=permission_id,
            photo_link=photo_link,
        )


        user.additional_properties = d
        return user

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
