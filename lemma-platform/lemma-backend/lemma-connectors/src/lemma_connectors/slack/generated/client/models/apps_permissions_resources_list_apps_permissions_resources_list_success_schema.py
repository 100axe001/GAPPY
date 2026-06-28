from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.apps_permissions_resources_list_apps_permissions_resources_list_success_schema_resources_item import AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResourcesItem
  from ..models.apps_permissions_resources_list_apps_permissions_resources_list_success_schema_response_metadata import AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResponseMetadata





T = TypeVar("T", bound="AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema")



@_attrs_define
class AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema:
    """ Schema for successful response apps.permissions.resources.list method

        Attributes:
            ok (bool):
            resources (list[AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResourcesItem]):
            response_metadata (AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResponseMetadata |
                Unset):
     """

    ok: bool
    resources: list[AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResourcesItem]
    response_metadata: AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResponseMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.apps_permissions_resources_list_apps_permissions_resources_list_success_schema_resources_item import AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResourcesItem
        from ..models.apps_permissions_resources_list_apps_permissions_resources_list_success_schema_response_metadata import AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResponseMetadata
        ok = self.ok

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)



        response_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_metadata, Unset):
            response_metadata = self.response_metadata.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ok": ok,
            "resources": resources,
        })
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apps_permissions_resources_list_apps_permissions_resources_list_success_schema_resources_item import AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResourcesItem
        from ..models.apps_permissions_resources_list_apps_permissions_resources_list_success_schema_response_metadata import AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResponseMetadata
        d = dict(src_dict)
        ok = d.pop("ok")

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in (_resources):
            resources_item = AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResourcesItem.from_dict(resources_item_data)



            resources.append(resources_item)


        _response_metadata = d.pop("response_metadata", UNSET)
        response_metadata: AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResponseMetadata | Unset
        if isinstance(_response_metadata,  Unset):
            response_metadata = UNSET
        else:
            response_metadata = AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchemaResponseMetadata.from_dict(_response_metadata)




        apps_permissions_resources_list_apps_permissions_resources_list_success_schema = cls(
            ok=ok,
            resources=resources,
            response_metadata=response_metadata,
        )


        apps_permissions_resources_list_apps_permissions_resources_list_success_schema.additional_properties = d
        return apps_permissions_resources_list_apps_permissions_resources_list_success_schema

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
