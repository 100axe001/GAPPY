from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.apps_permissions_resources_list_apps_permissions_resources_list_error_schema_error import AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchemaError
from ..types import UNSET, Unset






T = TypeVar("T", bound="AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema")



@_attrs_define
class AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema:
    """ Schema for error response from apps.permissions.resources.list method

        Attributes:
            error (AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchemaError):
            ok (bool):
            callstack (str | Unset): Note: PHP callstack is only visible in dev/qa
     """

    error: AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchemaError
    ok: bool
    callstack: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        ok = self.ok

        callstack = self.callstack


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "ok": ok,
        })
        if callstack is not UNSET:
            field_dict["callstack"] = callstack

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchemaError(d.pop("error"))




        ok = d.pop("ok")

        callstack = d.pop("callstack", UNSET)

        apps_permissions_resources_list_apps_permissions_resources_list_error_schema = cls(
            error=error,
            ok=ok,
            callstack=callstack,
        )

        return apps_permissions_resources_list_apps_permissions_resources_list_error_schema

