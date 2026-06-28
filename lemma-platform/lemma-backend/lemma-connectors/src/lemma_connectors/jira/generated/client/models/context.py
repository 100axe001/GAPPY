from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scope import Scope





T = TypeVar("T", bound="Context")



@_attrs_define
class Context:
    """ A context.

        Attributes:
            id (int | Unset): The ID of the context.
            name (str | Unset): The name of the context.
            scope (Scope | Unset): The projects the item is associated with. Indicated for items associated with [next-gen
                projects](https://confluence.atlassian.com/x/loMyO).
     """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    scope: Scope | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.scope import Scope
        id = self.id

        name = self.name

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scope import Scope
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = Scope.from_dict(_scope)




        context = cls(
            id=id,
            name=name,
            scope=scope,
        )

        return context

