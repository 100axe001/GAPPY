from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CallsAddJsonBody")



@_attrs_define
class CallsAddJsonBody:
    """ 
        Attributes:
            external_unique_id (str): An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from
                that service.
            join_url (str): The URL required for a client to join the Call.
            external_display_id (str | Unset): An optional, human-readable ID supplied by the 3rd-party Call provider. If
                supplied, this ID will be displayed in the Call object.
            desktop_app_join_url (str | Unset): When supplied, available Slack clients will attempt to directly launch the
                3rd-party Call with this URL.
            date_start (int | Unset): Call start time in UTC UNIX timestamp format
            title (str | Unset): The name of the Call.
            created_by (str | Unset): The valid Slack user ID of the user who created this Call. When this method is called
                with a user token, the `created_by` field is optional and defaults to the authed user of the token. Otherwise,
                the field is required.
            users (str | Unset): The list of users to register as participants in the Call. [Read more on how to specify
                users here](/apis/calls#users).
     """

    external_unique_id: str
    join_url: str
    external_display_id: str | Unset = UNSET
    desktop_app_join_url: str | Unset = UNSET
    date_start: int | Unset = UNSET
    title: str | Unset = UNSET
    created_by: str | Unset = UNSET
    users: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        external_unique_id = self.external_unique_id

        join_url = self.join_url

        external_display_id = self.external_display_id

        desktop_app_join_url = self.desktop_app_join_url

        date_start = self.date_start

        title = self.title

        created_by = self.created_by

        users = self.users


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "external_unique_id": external_unique_id,
            "join_url": join_url,
        })
        if external_display_id is not UNSET:
            field_dict["external_display_id"] = external_display_id
        if desktop_app_join_url is not UNSET:
            field_dict["desktop_app_join_url"] = desktop_app_join_url
        if date_start is not UNSET:
            field_dict["date_start"] = date_start
        if title is not UNSET:
            field_dict["title"] = title
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_unique_id = d.pop("external_unique_id")

        join_url = d.pop("join_url")

        external_display_id = d.pop("external_display_id", UNSET)

        desktop_app_join_url = d.pop("desktop_app_join_url", UNSET)

        date_start = d.pop("date_start", UNSET)

        title = d.pop("title", UNSET)

        created_by = d.pop("created_by", UNSET)

        users = d.pop("users", UNSET)

        calls_add_json_body = cls(
            external_unique_id=external_unique_id,
            join_url=join_url,
            external_display_id=external_display_id,
            desktop_app_join_url=desktop_app_join_url,
            date_start=date_start,
            title=title,
            created_by=created_by,
            users=users,
        )


        calls_add_json_body.additional_properties = d
        return calls_add_json_body

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
