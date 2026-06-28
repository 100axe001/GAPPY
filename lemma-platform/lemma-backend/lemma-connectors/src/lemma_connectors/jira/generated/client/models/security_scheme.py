from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.security_level import SecurityLevel





T = TypeVar("T", bound="SecurityScheme")



@_attrs_define
class SecurityScheme:
    """ Details about a security scheme.

        Attributes:
            default_security_level_id (int | Unset): The ID of the default security level.
            description (str | Unset): The description of the issue security scheme.
            id (int | Unset): The ID of the issue security scheme.
            levels (list[SecurityLevel] | Unset):
            name (str | Unset): The name of the issue security scheme.
            self_ (str | Unset): The URL of the issue security scheme.
     """

    default_security_level_id: int | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    levels: list[SecurityLevel] | Unset = UNSET
    name: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.security_level import SecurityLevel
        default_security_level_id = self.default_security_level_id

        description = self.description

        id = self.id

        levels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.levels, Unset):
            levels = []
            for levels_item_data in self.levels:
                levels_item = levels_item_data.to_dict()
                levels.append(levels_item)



        name = self.name

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if default_security_level_id is not UNSET:
            field_dict["defaultSecurityLevelId"] = default_security_level_id
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if levels is not UNSET:
            field_dict["levels"] = levels
        if name is not UNSET:
            field_dict["name"] = name
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.security_level import SecurityLevel
        d = dict(src_dict)
        default_security_level_id = d.pop("defaultSecurityLevelId", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _levels = d.pop("levels", UNSET)
        levels: list[SecurityLevel] | Unset = UNSET
        if _levels is not UNSET:
            levels = []
            for levels_item_data in _levels:
                levels_item = SecurityLevel.from_dict(levels_item_data)



                levels.append(levels_item)


        name = d.pop("name", UNSET)

        self_ = d.pop("self", UNSET)

        security_scheme = cls(
            default_security_level_id=default_security_level_id,
            description=description,
            id=id,
            levels=levels,
            name=name,
            self_=self_,
        )

        return security_scheme

