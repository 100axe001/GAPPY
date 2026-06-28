from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.connected_account_summary import ConnectedAccountSummary
    from ..models.installed_app_summary import InstalledAppSummary


T = TypeVar("T", bound="ConnectorStatusResponse")


@_attrs_define
class ConnectorStatusResponse:
    """
    Attributes:
        accounts (list[ConnectedAccountSummary]):
        installed (list[InstalledAppSummary]):
    """

    accounts: list[ConnectedAccountSummary]
    installed: list[InstalledAppSummary]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)

        installed = []
        for installed_item_data in self.installed:
            installed_item = installed_item_data.to_dict()
            installed.append(installed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
                "installed": installed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connected_account_summary import ConnectedAccountSummary
        from ..models.installed_app_summary import InstalledAppSummary

        d = dict(src_dict)
        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = ConnectedAccountSummary.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        installed = []
        _installed = d.pop("installed")
        for installed_item_data in _installed:
            installed_item = InstalledAppSummary.from_dict(installed_item_data)

            installed.append(installed_item)

        connector_status_response = cls(
            accounts=accounts,
            installed=installed,
        )

        connector_status_response.additional_properties = d
        return connector_status_response

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
