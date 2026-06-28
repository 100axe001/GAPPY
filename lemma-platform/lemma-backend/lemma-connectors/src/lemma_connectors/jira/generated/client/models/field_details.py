from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.json_type_bean import JsonTypeBean
  from ..models.scope import Scope





T = TypeVar("T", bound="FieldDetails")



@_attrs_define
class FieldDetails:
    """ Details about a field.

        Attributes:
            clause_names (list[str] | Unset): The names that can be used to reference the field in an advanced search. For
                more information, see [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ).
            custom (bool | Unset): Whether the field is a custom field.
            id (str | Unset): The ID of the field.
            key (str | Unset): The key of the field.
            name (str | Unset): The name of the field.
            navigable (bool | Unset): Whether the field can be used as a column on the issue navigator.
            orderable (bool | Unset): Whether the content of the field can be used to order lists.
            schema (JsonTypeBean | Unset): The schema of a field.
            scope (Scope | Unset): The projects the item is associated with. Indicated for items associated with [next-gen
                projects](https://confluence.atlassian.com/x/loMyO).
            searchable (bool | Unset): Whether the content of the field can be searched.
     """

    clause_names: list[str] | Unset = UNSET
    custom: bool | Unset = UNSET
    id: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    navigable: bool | Unset = UNSET
    orderable: bool | Unset = UNSET
    schema: JsonTypeBean | Unset = UNSET
    scope: Scope | Unset = UNSET
    searchable: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.json_type_bean import JsonTypeBean
        from ..models.scope import Scope
        clause_names: list[str] | Unset = UNSET
        if not isinstance(self.clause_names, Unset):
            clause_names = self.clause_names



        custom = self.custom

        id = self.id

        key = self.key

        name = self.name

        navigable = self.navigable

        orderable = self.orderable

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        searchable = self.searchable


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if clause_names is not UNSET:
            field_dict["clauseNames"] = clause_names
        if custom is not UNSET:
            field_dict["custom"] = custom
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if navigable is not UNSET:
            field_dict["navigable"] = navigable
        if orderable is not UNSET:
            field_dict["orderable"] = orderable
        if schema is not UNSET:
            field_dict["schema"] = schema
        if scope is not UNSET:
            field_dict["scope"] = scope
        if searchable is not UNSET:
            field_dict["searchable"] = searchable

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_type_bean import JsonTypeBean
        from ..models.scope import Scope
        d = dict(src_dict)
        clause_names = cast(list[str], d.pop("clauseNames", UNSET))


        custom = d.pop("custom", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        navigable = d.pop("navigable", UNSET)

        orderable = d.pop("orderable", UNSET)

        _schema = d.pop("schema", UNSET)
        schema: JsonTypeBean | Unset
        if isinstance(_schema,  Unset):
            schema = UNSET
        else:
            schema = JsonTypeBean.from_dict(_schema)




        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = Scope.from_dict(_scope)




        searchable = d.pop("searchable", UNSET)

        field_details = cls(
            clause_names=clause_names,
            custom=custom,
            id=id,
            key=key,
            name=name,
            navigable=navigable,
            orderable=orderable,
            schema=schema,
            scope=scope,
            searchable=searchable,
        )

        return field_details

