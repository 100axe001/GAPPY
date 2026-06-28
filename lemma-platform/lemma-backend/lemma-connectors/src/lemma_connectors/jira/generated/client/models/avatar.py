from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.avatar_urls import AvatarUrls





T = TypeVar("T", bound="Avatar")



@_attrs_define
class Avatar:
    """ Details of an avatar.

        Attributes:
            id (str): The ID of the avatar.
            file_name (str | Unset): The file name of the avatar icon. Returned for system avatars.
            is_deletable (bool | Unset): Whether the avatar can be deleted.
            is_selected (bool | Unset): Whether the avatar is used in Jira. For example, shown as a project's avatar.
            is_system_avatar (bool | Unset): Whether the avatar is a system avatar.
            owner (str | Unset): The owner of the avatar. For a system avatar the owner is null (and nothing is returned).
                For non-system avatars this is the appropriate identifier, such as the ID for a project or the account ID for a
                user.
            urls (AvatarUrls | Unset): The list of avatar icon URLs.
     """

    id: str
    file_name: str | Unset = UNSET
    is_deletable: bool | Unset = UNSET
    is_selected: bool | Unset = UNSET
    is_system_avatar: bool | Unset = UNSET
    owner: str | Unset = UNSET
    urls: AvatarUrls | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.avatar_urls import AvatarUrls
        id = self.id

        file_name = self.file_name

        is_deletable = self.is_deletable

        is_selected = self.is_selected

        is_system_avatar = self.is_system_avatar

        owner = self.owner

        urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if is_deletable is not UNSET:
            field_dict["isDeletable"] = is_deletable
        if is_selected is not UNSET:
            field_dict["isSelected"] = is_selected
        if is_system_avatar is not UNSET:
            field_dict["isSystemAvatar"] = is_system_avatar
        if owner is not UNSET:
            field_dict["owner"] = owner
        if urls is not UNSET:
            field_dict["urls"] = urls

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar_urls import AvatarUrls
        d = dict(src_dict)
        id = d.pop("id")

        file_name = d.pop("fileName", UNSET)

        is_deletable = d.pop("isDeletable", UNSET)

        is_selected = d.pop("isSelected", UNSET)

        is_system_avatar = d.pop("isSystemAvatar", UNSET)

        owner = d.pop("owner", UNSET)

        _urls = d.pop("urls", UNSET)
        urls: AvatarUrls | Unset
        if isinstance(_urls,  Unset):
            urls = UNSET
        else:
            urls = AvatarUrls.from_dict(_urls)




        avatar = cls(
            id=id,
            file_name=file_name,
            is_deletable=is_deletable,
            is_selected=is_selected,
            is_system_avatar=is_system_avatar,
            owner=owner,
            urls=urls,
        )


        avatar.additional_properties = d
        return avatar

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
