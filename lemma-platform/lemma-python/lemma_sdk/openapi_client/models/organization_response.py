from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.organization_join_policy import OrganizationJoinPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationResponse")


@_attrs_define
class OrganizationResponse:
    """Organization response schema.

    Attributes:
        created_at (datetime.datetime):
        id (UUID):
        join_policy (OrganizationJoinPolicy): Who may self-join an organization, ordered from closed to open.
        name (str):
        slug (str):
        updated_at (datetime.datetime):
        email_domain (None | str | Unset):
    """

    created_at: datetime.datetime
    id: UUID
    join_policy: OrganizationJoinPolicy
    name: str
    slug: str
    updated_at: datetime.datetime
    email_domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        join_policy = self.join_policy.value

        name = self.name

        slug = self.slug

        updated_at = self.updated_at.isoformat()

        email_domain: None | str | Unset
        if isinstance(self.email_domain, Unset):
            email_domain = UNSET
        else:
            email_domain = self.email_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "join_policy": join_policy,
                "name": name,
                "slug": slug,
                "updated_at": updated_at,
            }
        )
        if email_domain is not UNSET:
            field_dict["email_domain"] = email_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        id = UUID(d.pop("id"))

        join_policy = OrganizationJoinPolicy(d.pop("join_policy"))

        name = d.pop("name")

        slug = d.pop("slug")

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_email_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_domain = _parse_email_domain(d.pop("email_domain", UNSET))

        organization_response = cls(
            created_at=created_at,
            id=id,
            join_policy=join_policy,
            name=name,
            slug=slug,
            updated_at=updated_at,
            email_domain=email_domain,
        )

        organization_response.additional_properties = d
        return organization_response

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
