from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IncludedFields")



@_attrs_define
class IncludedFields:
    """ 
        Attributes:
            actually_included (list[str] | Unset):
            excluded (list[str] | Unset):
            included (list[str] | Unset):
     """

    actually_included: list[str] | Unset = UNSET
    excluded: list[str] | Unset = UNSET
    included: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        actually_included: list[str] | Unset = UNSET
        if not isinstance(self.actually_included, Unset):
            actually_included = self.actually_included



        excluded: list[str] | Unset = UNSET
        if not isinstance(self.excluded, Unset):
            excluded = self.excluded



        included: list[str] | Unset = UNSET
        if not isinstance(self.included, Unset):
            included = self.included




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if actually_included is not UNSET:
            field_dict["actuallyIncluded"] = actually_included
        if excluded is not UNSET:
            field_dict["excluded"] = excluded
        if included is not UNSET:
            field_dict["included"] = included

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actually_included = cast(list[str], d.pop("actuallyIncluded", UNSET))


        excluded = cast(list[str], d.pop("excluded", UNSET))


        included = cast(list[str], d.pop("included", UNSET))


        included_fields = cls(
            actually_included=actually_included,
            excluded=excluded,
            included=included,
        )

        return included_fields

