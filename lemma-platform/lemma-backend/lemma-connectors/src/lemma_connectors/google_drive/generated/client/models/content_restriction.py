from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.user import User





T = TypeVar("T", bound="ContentRestriction")



@_attrs_define
class ContentRestriction:
    """ A restriction for accessing the content of the file.

        Attributes:
            read_only (bool | Unset): Whether the content of the file is read-only. If a file is read-only, a new revision
                of the file may not be added, comments may not be added or modified, and the title of the file may not be
                modified.
            reason (str | Unset): Reason for why the content of the file is restricted. This is only mutable on requests
                that also set readOnly=true.
            restricting_user (User | Unset): Information about a Drive user.
            restriction_time (datetime.datetime | Unset): The time at which the content restriction was set (formatted RFC
                3339 timestamp). Only populated if readOnly is true.
            type_ (str | Unset): The type of the content restriction. Currently the only possible value is
                globalContentRestriction.
     """

    read_only: bool | Unset = UNSET
    reason: str | Unset = UNSET
    restricting_user: User | Unset = UNSET
    restriction_time: datetime.datetime | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User
        read_only = self.read_only

        reason = self.reason

        restricting_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restricting_user, Unset):
            restricting_user = self.restricting_user.to_dict()

        restriction_time: str | Unset = UNSET
        if not isinstance(self.restriction_time, Unset):
            restriction_time = self.restriction_time.isoformat()

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if reason is not UNSET:
            field_dict["reason"] = reason
        if restricting_user is not UNSET:
            field_dict["restrictingUser"] = restricting_user
        if restriction_time is not UNSET:
            field_dict["restrictionTime"] = restriction_time
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        d = dict(src_dict)
        read_only = d.pop("readOnly", UNSET)

        reason = d.pop("reason", UNSET)

        _restricting_user = d.pop("restrictingUser", UNSET)
        restricting_user: User | Unset
        if isinstance(_restricting_user,  Unset):
            restricting_user = UNSET
        else:
            restricting_user = User.from_dict(_restricting_user)




        _restriction_time = d.pop("restrictionTime", UNSET)
        restriction_time: datetime.datetime | Unset
        if isinstance(_restriction_time,  Unset):
            restriction_time = UNSET
        else:
            restriction_time = isoparse(_restriction_time)




        type_ = d.pop("type", UNSET)

        content_restriction = cls(
            read_only=read_only,
            reason=reason,
            restricting_user=restricting_user,
            restriction_time=restriction_time,
            type_=type_,
        )


        content_restriction.additional_properties = d
        return content_restriction

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
