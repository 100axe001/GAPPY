from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ObjsTeamProfileFieldOption")



@_attrs_define
class ObjsTeamProfileFieldOption:
    """ 
        Attributes:
            is_custom (bool | None | Unset):
            is_multiple_entry (bool | None | Unset):
            is_protected (bool | None | Unset):
            is_scim (bool | None | Unset):
     """

    is_custom: bool | None | Unset = UNSET
    is_multiple_entry: bool | None | Unset = UNSET
    is_protected: bool | None | Unset = UNSET
    is_scim: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_custom: bool | None | Unset
        if isinstance(self.is_custom, Unset):
            is_custom = UNSET
        else:
            is_custom = self.is_custom

        is_multiple_entry: bool | None | Unset
        if isinstance(self.is_multiple_entry, Unset):
            is_multiple_entry = UNSET
        else:
            is_multiple_entry = self.is_multiple_entry

        is_protected: bool | None | Unset
        if isinstance(self.is_protected, Unset):
            is_protected = UNSET
        else:
            is_protected = self.is_protected

        is_scim: bool | None | Unset
        if isinstance(self.is_scim, Unset):
            is_scim = UNSET
        else:
            is_scim = self.is_scim


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_custom is not UNSET:
            field_dict["is_custom"] = is_custom
        if is_multiple_entry is not UNSET:
            field_dict["is_multiple_entry"] = is_multiple_entry
        if is_protected is not UNSET:
            field_dict["is_protected"] = is_protected
        if is_scim is not UNSET:
            field_dict["is_scim"] = is_scim

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_is_custom(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_custom = _parse_is_custom(d.pop("is_custom", UNSET))


        def _parse_is_multiple_entry(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_multiple_entry = _parse_is_multiple_entry(d.pop("is_multiple_entry", UNSET))


        def _parse_is_protected(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_protected = _parse_is_protected(d.pop("is_protected", UNSET))


        def _parse_is_scim(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_scim = _parse_is_scim(d.pop("is_scim", UNSET))


        objs_team_profile_field_option = cls(
            is_custom=is_custom,
            is_multiple_entry=is_multiple_entry,
            is_protected=is_protected,
            is_scim=is_scim,
        )

        return objs_team_profile_field_option

