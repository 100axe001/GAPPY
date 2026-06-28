from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.icon import Icon
  from ..models.status import Status





T = TypeVar("T", bound="RemoteObject")



@_attrs_define
class RemoteObject:
    """ The linked item.

        Attributes:
            title (str): The title of the item.
            url (str): The URL of the item.
            icon (Icon | Unset): An icon. If no icon is defined:

                 *  for a status icon, no status icon displays in Jira.
                 *  for the remote object icon, the default link icon displays in Jira.
            status (Status | Unset): The status of the item.
            summary (str | Unset): The summary details of the item.
     """

    title: str
    url: str
    icon: Icon | Unset = UNSET
    status: Status | Unset = UNSET
    summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.icon import Icon
        from ..models.status import Status
        title = self.title

        url = self.url

        icon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        summary = self.summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "title": title,
            "url": url,
        })
        if icon is not UNSET:
            field_dict["icon"] = icon
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.icon import Icon
        from ..models.status import Status
        d = dict(src_dict)
        title = d.pop("title")

        url = d.pop("url")

        _icon = d.pop("icon", UNSET)
        icon: Icon | Unset
        if isinstance(_icon,  Unset):
            icon = UNSET
        else:
            icon = Icon.from_dict(_icon)




        _status = d.pop("status", UNSET)
        status: Status | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = Status.from_dict(_status)




        summary = d.pop("summary", UNSET)

        remote_object = cls(
            title=title,
            url=url,
            icon=icon,
            status=status,
            summary=summary,
        )


        remote_object.additional_properties = d
        return remote_object

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
