from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ResourcesInInfoFromAppsPermissionsInfo")



@_attrs_define
class ResourcesInInfoFromAppsPermissionsInfo:
    """ 
        Attributes:
            ids (list[Any]):
            excluded_ids (list[Any] | Unset):
            wildcard (bool | Unset):
     """

    ids: list[Any]
    excluded_ids: list[Any] | Unset = UNSET
    wildcard: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ids = self.ids



        excluded_ids: list[Any] | Unset = UNSET
        if not isinstance(self.excluded_ids, Unset):
            excluded_ids = self.excluded_ids



        wildcard = self.wildcard


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ids": ids,
        })
        if excluded_ids is not UNSET:
            field_dict["excluded_ids"] = excluded_ids
        if wildcard is not UNSET:
            field_dict["wildcard"] = wildcard

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[Any], d.pop("ids"))


        excluded_ids = cast(list[Any], d.pop("excluded_ids", UNSET))


        wildcard = d.pop("wildcard", UNSET)

        resources_in_info_from_apps_permissions_info = cls(
            ids=ids,
            excluded_ids=excluded_ids,
            wildcard=wildcard,
        )

        return resources_in_info_from_apps_permissions_info

