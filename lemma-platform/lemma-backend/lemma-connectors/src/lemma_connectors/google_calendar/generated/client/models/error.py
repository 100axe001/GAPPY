from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Error")



@_attrs_define
class Error:
    """ 
        Attributes:
            domain (str | Unset): Domain, or broad category, of the error.
            reason (str | Unset): Specific reason for the error. Some of the possible values are:
                - "groupTooBig" - The group of users requested is too large for a single query.
                - "tooManyCalendarsRequested" - The number of calendars requested is too large for a single query.
                - "notFound" - The requested resource was not found.
                - "internalError" - The API service has encountered an internal error.  Additional error types may be added in
                the future, so clients should gracefully handle additional error statuses not included in this list.
     """

    domain: str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if domain is not UNSET:
            field_dict["domain"] = domain
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain", UNSET)

        reason = d.pop("reason", UNSET)

        error = cls(
            domain=domain,
            reason=reason,
        )


        error.additional_properties = d
        return error

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
