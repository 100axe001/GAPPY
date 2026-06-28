from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.resources_in_info_from_apps_permissions_info import ResourcesInInfoFromAppsPermissionsInfo





T = TypeVar("T", bound="AppsPermissionsInfoAppsPermissionsInfoSchemaInfoIm")



@_attrs_define
class AppsPermissionsInfoAppsPermissionsInfoSchemaInfoIm:
    """ 
        Attributes:
            resources (ResourcesInInfoFromAppsPermissionsInfo | Unset):
            scopes (list[str] | Unset):
     """

    resources: ResourcesInInfoFromAppsPermissionsInfo | Unset = UNSET
    scopes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.resources_in_info_from_apps_permissions_info import ResourcesInInfoFromAppsPermissionsInfo
        resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if resources is not UNSET:
            field_dict["resources"] = resources
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resources_in_info_from_apps_permissions_info import ResourcesInInfoFromAppsPermissionsInfo
        d = dict(src_dict)
        _resources = d.pop("resources", UNSET)
        resources: ResourcesInInfoFromAppsPermissionsInfo | Unset
        if isinstance(_resources,  Unset):
            resources = UNSET
        else:
            resources = ResourcesInInfoFromAppsPermissionsInfo.from_dict(_resources)




        scopes = cast(list[str], d.pop("scopes", UNSET))


        apps_permissions_info_apps_permissions_info_schema_info_im = cls(
            resources=resources,
            scopes=scopes,
        )


        apps_permissions_info_apps_permissions_info_schema_info_im.additional_properties = d
        return apps_permissions_info_apps_permissions_info_schema_info_im

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
