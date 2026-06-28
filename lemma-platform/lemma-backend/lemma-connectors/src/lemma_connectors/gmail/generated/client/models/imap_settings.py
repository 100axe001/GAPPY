from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.imap_settings_expunge_behavior import ImapSettingsExpungeBehavior
from ..types import UNSET, Unset






T = TypeVar("T", bound="ImapSettings")



@_attrs_define
class ImapSettings:
    """ IMAP settings for an account.

        Attributes:
            auto_expunge (bool | Unset): If this value is true, Gmail will immediately expunge a message when it is marked
                as deleted in IMAP. Otherwise, Gmail will wait for an update from the client before expunging messages marked as
                deleted.
            enabled (bool | Unset): Whether IMAP is enabled for the account.
            expunge_behavior (ImapSettingsExpungeBehavior | Unset): The action that will be executed on a message when it is
                marked as deleted and expunged from the last visible IMAP folder.
            max_folder_size (int | Unset): An optional limit on the number of messages that an IMAP folder may contain.
                Legal values are 0, 1000, 2000, 5000 or 10000. A value of zero is interpreted to mean that there is no limit.
     """

    auto_expunge: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    expunge_behavior: ImapSettingsExpungeBehavior | Unset = UNSET
    max_folder_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        auto_expunge = self.auto_expunge

        enabled = self.enabled

        expunge_behavior: str | Unset = UNSET
        if not isinstance(self.expunge_behavior, Unset):
            expunge_behavior = self.expunge_behavior.value


        max_folder_size = self.max_folder_size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if auto_expunge is not UNSET:
            field_dict["autoExpunge"] = auto_expunge
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if expunge_behavior is not UNSET:
            field_dict["expungeBehavior"] = expunge_behavior
        if max_folder_size is not UNSET:
            field_dict["maxFolderSize"] = max_folder_size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_expunge = d.pop("autoExpunge", UNSET)

        enabled = d.pop("enabled", UNSET)

        _expunge_behavior = d.pop("expungeBehavior", UNSET)
        expunge_behavior: ImapSettingsExpungeBehavior | Unset
        if isinstance(_expunge_behavior,  Unset):
            expunge_behavior = UNSET
        else:
            expunge_behavior = ImapSettingsExpungeBehavior(_expunge_behavior)




        max_folder_size = d.pop("maxFolderSize", UNSET)

        imap_settings = cls(
            auto_expunge=auto_expunge,
            enabled=enabled,
            expunge_behavior=expunge_behavior,
            max_folder_size=max_folder_size,
        )


        imap_settings.additional_properties = d
        return imap_settings

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
