from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pop_settings_access_window import PopSettingsAccessWindow
from ..models.pop_settings_disposition import PopSettingsDisposition
from ..types import UNSET, Unset






T = TypeVar("T", bound="PopSettings")



@_attrs_define
class PopSettings:
    """ POP settings for an account.

        Attributes:
            access_window (PopSettingsAccessWindow | Unset): The range of messages which are accessible via POP.
            disposition (PopSettingsDisposition | Unset): The action that will be executed on a message after it has been
                fetched via POP.
     """

    access_window: PopSettingsAccessWindow | Unset = UNSET
    disposition: PopSettingsDisposition | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_window: str | Unset = UNSET
        if not isinstance(self.access_window, Unset):
            access_window = self.access_window.value


        disposition: str | Unset = UNSET
        if not isinstance(self.disposition, Unset):
            disposition = self.disposition.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_window is not UNSET:
            field_dict["accessWindow"] = access_window
        if disposition is not UNSET:
            field_dict["disposition"] = disposition

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _access_window = d.pop("accessWindow", UNSET)
        access_window: PopSettingsAccessWindow | Unset
        if isinstance(_access_window,  Unset):
            access_window = UNSET
        else:
            access_window = PopSettingsAccessWindow(_access_window)




        _disposition = d.pop("disposition", UNSET)
        disposition: PopSettingsDisposition | Unset
        if isinstance(_disposition,  Unset):
            disposition = UNSET
        else:
            disposition = PopSettingsDisposition(_disposition)




        pop_settings = cls(
            access_window=access_window,
            disposition=disposition,
        )


        pop_settings.additional_properties = d
        return pop_settings

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
