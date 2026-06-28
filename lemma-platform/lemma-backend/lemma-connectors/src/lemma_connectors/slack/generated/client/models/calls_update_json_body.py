from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CallsUpdateJsonBody")



@_attrs_define
class CallsUpdateJsonBody:
    """ 
        Attributes:
            id (str): `id` returned by the [`calls.add`](/methods/calls.add) method.
            title (str | Unset): The name of the Call.
            join_url (str | Unset): The URL required for a client to join the Call.
            desktop_app_join_url (str | Unset): When supplied, available Slack clients will attempt to directly launch the
                3rd-party Call with this URL.
     """

    id: str
    title: str | Unset = UNSET
    join_url: str | Unset = UNSET
    desktop_app_join_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        join_url = self.join_url

        desktop_app_join_url = self.desktop_app_join_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })
        if title is not UNSET:
            field_dict["title"] = title
        if join_url is not UNSET:
            field_dict["join_url"] = join_url
        if desktop_app_join_url is not UNSET:
            field_dict["desktop_app_join_url"] = desktop_app_join_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title", UNSET)

        join_url = d.pop("join_url", UNSET)

        desktop_app_join_url = d.pop("desktop_app_join_url", UNSET)

        calls_update_json_body = cls(
            id=id,
            title=title,
            join_url=join_url,
            desktop_app_join_url=desktop_app_join_url,
        )


        calls_update_json_body.additional_properties = d
        return calls_update_json_body

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
