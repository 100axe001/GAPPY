from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SecurityLevel")



@_attrs_define
class SecurityLevel:
    """ Details of an issue level security item.

        Attributes:
            description (str | Unset): The description of the issue level security item.
            id (str | Unset): The ID of the issue level security item.
            is_default (bool | Unset): Whether the issue level security item is the default.
            issue_security_scheme_id (str | Unset): The ID of the issue level security scheme.
            name (str | Unset): The name of the issue level security item.
            self_ (str | Unset): The URL of the issue level security item.
     """

    description: str | Unset = UNSET
    id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    issue_security_scheme_id: str | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        is_default = self.is_default

        issue_security_scheme_id = self.issue_security_scheme_id

        name = self.name

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if issue_security_scheme_id is not UNSET:
            field_dict["issueSecuritySchemeId"] = issue_security_scheme_id
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        is_default = d.pop("isDefault", UNSET)

        issue_security_scheme_id = d.pop("issueSecuritySchemeId", UNSET)

        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        security_level = cls(
            description=description,
            id=id,
            is_default=is_default,
            issue_security_scheme_id=issue_security_scheme_id,
            name=name,
            self_=self_,
        )

        return security_level

