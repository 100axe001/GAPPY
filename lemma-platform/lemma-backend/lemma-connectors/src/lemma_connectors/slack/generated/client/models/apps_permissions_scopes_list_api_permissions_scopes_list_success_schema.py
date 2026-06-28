from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.apps_permissions_scopes_list_api_permissions_scopes_list_success_schema_scopes import AppsPermissionsScopesListApiPermissionsScopesListSuccessSchemaScopes





T = TypeVar("T", bound="AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema")



@_attrs_define
class AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema:
    """ Schema for successful response api.permissions.scopes.list method

        Attributes:
            ok (bool):
            scopes (AppsPermissionsScopesListApiPermissionsScopesListSuccessSchemaScopes):
     """

    ok: bool
    scopes: AppsPermissionsScopesListApiPermissionsScopesListSuccessSchemaScopes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.apps_permissions_scopes_list_api_permissions_scopes_list_success_schema_scopes import AppsPermissionsScopesListApiPermissionsScopesListSuccessSchemaScopes
        ok = self.ok

        scopes = self.scopes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ok": ok,
            "scopes": scopes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apps_permissions_scopes_list_api_permissions_scopes_list_success_schema_scopes import AppsPermissionsScopesListApiPermissionsScopesListSuccessSchemaScopes
        d = dict(src_dict)
        ok = d.pop("ok")

        scopes = AppsPermissionsScopesListApiPermissionsScopesListSuccessSchemaScopes.from_dict(d.pop("scopes"))




        apps_permissions_scopes_list_api_permissions_scopes_list_success_schema = cls(
            ok=ok,
            scopes=scopes,
        )


        apps_permissions_scopes_list_api_permissions_scopes_list_success_schema.additional_properties = d
        return apps_permissions_scopes_list_api_permissions_scopes_list_success_schema

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
