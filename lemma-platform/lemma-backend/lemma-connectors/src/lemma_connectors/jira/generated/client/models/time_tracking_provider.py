from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TimeTrackingProvider")



@_attrs_define
class TimeTrackingProvider:
    """ Details about the time tracking provider.

        Attributes:
            key (str): The key for the time tracking provider. For example, *JIRA*.
            name (str | Unset): The name of the time tracking provider. For example, *JIRA provided time tracking*.
            url (str | Unset): The URL of the configuration page for the time tracking provider app. For example,
                */example/config/url*. This property is only returned if the `adminPageKey` property is set in the module
                descriptor of the time tracking provider app.
     """

    key: str
    name: str | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        time_tracking_provider = cls(
            key=key,
            name=name,
            url=url,
        )

        return time_tracking_provider

