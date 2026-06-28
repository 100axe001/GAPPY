from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="HistoryMetadataParticipant")



@_attrs_define
class HistoryMetadataParticipant:
    """ Details of user or system associated with a issue history metadata item.

        Attributes:
            avatar_url (str | Unset): The URL to an avatar for the user or system associated with a history record.
            display_name (str | Unset): The display name of the user or system associated with a history record.
            display_name_key (str | Unset): The key of the display name of the user or system associated with a history
                record.
            id (str | Unset): The ID of the user or system associated with a history record.
            type_ (str | Unset): The type of the user or system associated with a history record.
            url (str | Unset): The URL of the user or system associated with a history record.
     """

    avatar_url: str | Unset = UNSET
    display_name: str | Unset = UNSET
    display_name_key: str | Unset = UNSET
    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        display_name = self.display_name

        display_name_key = self.display_name_key

        id = self.id

        type_ = self.type_

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_name_key is not UNSET:
            field_dict["displayNameKey"] = display_name_key
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_url = d.pop("avatarUrl", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_name_key = d.pop("displayNameKey", UNSET)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        history_metadata_participant = cls(
            avatar_url=avatar_url,
            display_name=display_name,
            display_name_key=display_name_key,
            id=id,
            type_=type_,
            url=url,
        )


        history_metadata_participant.additional_properties = d
        return history_metadata_participant

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
