from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FileLinkShareMetadata")



@_attrs_define
class FileLinkShareMetadata:
    """ Contains details about the link URLs that clients are using to refer to this item.

        Attributes:
            security_update_eligible (bool | Unset): Whether the file is eligible for security update.
            security_update_enabled (bool | Unset): Whether the security update is enabled for this file.
     """

    security_update_eligible: bool | Unset = UNSET
    security_update_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        security_update_eligible = self.security_update_eligible

        security_update_enabled = self.security_update_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if security_update_eligible is not UNSET:
            field_dict["securityUpdateEligible"] = security_update_eligible
        if security_update_enabled is not UNSET:
            field_dict["securityUpdateEnabled"] = security_update_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        security_update_eligible = d.pop("securityUpdateEligible", UNSET)

        security_update_enabled = d.pop("securityUpdateEnabled", UNSET)

        file_link_share_metadata = cls(
            security_update_eligible=security_update_eligible,
            security_update_enabled=security_update_enabled,
        )


        file_link_share_metadata.additional_properties = d
        return file_link_share_metadata

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
