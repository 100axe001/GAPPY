from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.harness_kind import HarnessKind
from ..models.runtime_profile_scope import RuntimeProfileScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserDaemonRuntimeProfileRequest")


@_attrs_define
class CreateUserDaemonRuntimeProfileRequest:
    """
    Attributes:
        daemon_id (UUID):
        harness_kind (HarnessKind): Runtime framework used to execute an agent.
        name (str):
        default_model_name (None | str | Unset):
        description (None | str | Unset):
        scope (RuntimeProfileScope | Unset):
        source (Literal['USER_DAEMON'] | Unset):  Default: 'USER_DAEMON'.
    """

    daemon_id: UUID
    harness_kind: HarnessKind
    name: str
    default_model_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    scope: RuntimeProfileScope | Unset = UNSET
    source: Literal["USER_DAEMON"] | Unset = "USER_DAEMON"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daemon_id = str(self.daemon_id)

        harness_kind = self.harness_kind.value

        name = self.name

        default_model_name: None | str | Unset
        if isinstance(self.default_model_name, Unset):
            default_model_name = UNSET
        else:
            default_model_name = self.default_model_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "daemon_id": daemon_id,
                "harness_kind": harness_kind,
                "name": name,
            }
        )
        if default_model_name is not UNSET:
            field_dict["default_model_name"] = default_model_name
        if description is not UNSET:
            field_dict["description"] = description
        if scope is not UNSET:
            field_dict["scope"] = scope
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        daemon_id = UUID(d.pop("daemon_id"))

        harness_kind = HarnessKind(d.pop("harness_kind"))

        name = d.pop("name")

        def _parse_default_model_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_model_name = _parse_default_model_name(
            d.pop("default_model_name", UNSET)
        )

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _scope = d.pop("scope", UNSET)
        scope: RuntimeProfileScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RuntimeProfileScope(_scope)

        source = cast(Literal["USER_DAEMON"] | Unset, d.pop("source", UNSET))
        if source != "USER_DAEMON" and not isinstance(source, Unset):
            raise ValueError(f"source must match const 'USER_DAEMON', got '{source}'")

        create_user_daemon_runtime_profile_request = cls(
            daemon_id=daemon_id,
            harness_kind=harness_kind,
            name=name,
            default_model_name=default_model_name,
            description=description,
            scope=scope,
            source=source,
        )

        create_user_daemon_runtime_profile_request.additional_properties = d
        return create_user_daemon_runtime_profile_request

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
