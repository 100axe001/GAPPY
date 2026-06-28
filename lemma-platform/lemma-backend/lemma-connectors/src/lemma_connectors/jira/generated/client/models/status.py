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





T = TypeVar("T", bound="Status")



@_attrs_define
class Status:
    """ The status of the item.

        Attributes:
            icon (Icon | Unset): An icon. If no icon is defined:

                 *  for a status icon, no status icon displays in Jira.
                 *  for the remote object icon, the default link icon displays in Jira.
            resolved (bool | Unset): Whether the item is resolved. If set to "true", the link to the issue is displayed in a
                strikethrough font, otherwise the link displays in normal font.
     """

    icon: Icon | Unset = UNSET
    resolved: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.icon import Icon
        icon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.to_dict()

        resolved = self.resolved


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if icon is not UNSET:
            field_dict["icon"] = icon
        if resolved is not UNSET:
            field_dict["resolved"] = resolved

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.icon import Icon
        d = dict(src_dict)
        _icon = d.pop("icon", UNSET)
        icon: Icon | Unset
        if isinstance(_icon,  Unset):
            icon = UNSET
        else:
            icon = Icon.from_dict(_icon)




        resolved = d.pop("resolved", UNSET)

        status = cls(
            icon=icon,
            resolved=resolved,
        )


        status.additional_properties = d
        return status

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
