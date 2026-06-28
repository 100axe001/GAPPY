from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.runtime_model_capability import RuntimeModelCapability
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.runtime_model_catalog_entry_default_model_settings import (
        RuntimeModelCatalogEntryDefaultModelSettings,
    )
    from ..models.runtime_model_catalog_entry_metadata import (
        RuntimeModelCatalogEntryMetadata,
    )


T = TypeVar("T", bound="RuntimeModelCatalogEntry")


@_attrs_define
class RuntimeModelCatalogEntry:
    """
    Attributes:
        name (str):
        provider_model_name (str):
        capabilities (list[RuntimeModelCapability] | Unset):
        default_model_settings (RuntimeModelCatalogEntryDefaultModelSettings | Unset):
        display_name (None | str | Unset):
        metadata (RuntimeModelCatalogEntryMetadata | Unset):
    """

    name: str
    provider_model_name: str
    capabilities: list[RuntimeModelCapability] | Unset = UNSET
    default_model_settings: RuntimeModelCatalogEntryDefaultModelSettings | Unset = UNSET
    display_name: None | str | Unset = UNSET
    metadata: RuntimeModelCatalogEntryMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        provider_model_name = self.provider_model_name

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = []
            for capabilities_item_data in self.capabilities:
                capabilities_item = capabilities_item_data.value
                capabilities.append(capabilities_item)

        default_model_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_model_settings, Unset):
            default_model_settings = self.default_model_settings.to_dict()

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "provider_model_name": provider_model_name,
            }
        )
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if default_model_settings is not UNSET:
            field_dict["default_model_settings"] = default_model_settings
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.runtime_model_catalog_entry_default_model_settings import (
            RuntimeModelCatalogEntryDefaultModelSettings,
        )
        from ..models.runtime_model_catalog_entry_metadata import (
            RuntimeModelCatalogEntryMetadata,
        )

        d = dict(src_dict)
        name = d.pop("name")

        provider_model_name = d.pop("provider_model_name")

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: list[RuntimeModelCapability] | Unset = UNSET
        if _capabilities is not UNSET:
            capabilities = []
            for capabilities_item_data in _capabilities:
                capabilities_item = RuntimeModelCapability(capabilities_item_data)

                capabilities.append(capabilities_item)

        _default_model_settings = d.pop("default_model_settings", UNSET)
        default_model_settings: RuntimeModelCatalogEntryDefaultModelSettings | Unset
        if isinstance(_default_model_settings, Unset):
            default_model_settings = UNSET
        else:
            default_model_settings = (
                RuntimeModelCatalogEntryDefaultModelSettings.from_dict(
                    _default_model_settings
                )
            )

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: RuntimeModelCatalogEntryMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RuntimeModelCatalogEntryMetadata.from_dict(_metadata)

        runtime_model_catalog_entry = cls(
            name=name,
            provider_model_name=provider_model_name,
            capabilities=capabilities,
            default_model_settings=default_model_settings,
            display_name=display_name,
            metadata=metadata,
        )

        runtime_model_catalog_entry.additional_properties = d
        return runtime_model_catalog_entry

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
