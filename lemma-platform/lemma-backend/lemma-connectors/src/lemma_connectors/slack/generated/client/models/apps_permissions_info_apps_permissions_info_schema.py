from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.apps_permissions_info_apps_permissions_info_schema_info import AppsPermissionsInfoAppsPermissionsInfoSchemaInfo





T = TypeVar("T", bound="AppsPermissionsInfoAppsPermissionsInfoSchema")



@_attrs_define
class AppsPermissionsInfoAppsPermissionsInfoSchema:
    """ Schema for successful response from apps.permissions.info method

        Attributes:
            info (AppsPermissionsInfoAppsPermissionsInfoSchemaInfo):
            ok (bool):
     """

    info: AppsPermissionsInfoAppsPermissionsInfoSchemaInfo
    ok: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.apps_permissions_info_apps_permissions_info_schema_info import AppsPermissionsInfoAppsPermissionsInfoSchemaInfo
        info = self.info.to_dict()

        ok = self.ok


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "info": info,
            "ok": ok,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apps_permissions_info_apps_permissions_info_schema_info import AppsPermissionsInfoAppsPermissionsInfoSchemaInfo
        d = dict(src_dict)
        info = AppsPermissionsInfoAppsPermissionsInfoSchemaInfo.from_dict(d.pop("info"))




        ok = d.pop("ok")

        apps_permissions_info_apps_permissions_info_schema = cls(
            info=info,
            ok=ok,
        )

        return apps_permissions_info_apps_permissions_info_schema

