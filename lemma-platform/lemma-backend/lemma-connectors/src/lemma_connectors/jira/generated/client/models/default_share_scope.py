from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.default_share_scope_scope import DefaultShareScopeScope






T = TypeVar("T", bound="DefaultShareScope")



@_attrs_define
class DefaultShareScope:
    """ Details of the scope of the default sharing for new filters and dashboards.

        Attributes:
            scope (DefaultShareScopeScope): The scope of the default sharing for new filters and dashboards:

                 *  `AUTHENTICATED` Shared with all logged-in users.
                 *  `GLOBAL` Shared with all logged-in users. This shows as `AUTHENTICATED` in the response.
                 *  `PRIVATE` Not shared with any users.
     """

    scope: DefaultShareScopeScope





    def to_dict(self) -> dict[str, Any]:
        scope = self.scope.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "scope": scope,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope = DefaultShareScopeScope(d.pop("scope"))




        default_share_scope = cls(
            scope=scope,
        )

        return default_share_scope

