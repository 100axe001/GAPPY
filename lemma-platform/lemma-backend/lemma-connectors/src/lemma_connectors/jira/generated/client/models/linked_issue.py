from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.fields import Fields





T = TypeVar("T", bound="LinkedIssue")



@_attrs_define
class LinkedIssue:
    """ The ID or key of a linked issue.

        Attributes:
            fields (Fields | Unset): Key fields from the linked issue.
            id (str | Unset): The ID of an issue. Required if `key` isn't provided.
            key (str | Unset): The key of an issue. Required if `id` isn't provided.
            self_ (str | Unset): The URL of the issue.
     """

    fields: Fields | Unset = UNSET
    id: str | Unset = UNSET
    key: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.fields import Fields
        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        id = self.id

        key = self.key

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fields import Fields
        d = dict(src_dict)
        _fields = d.pop("fields", UNSET)
        fields: Fields | Unset
        if isinstance(_fields,  Unset):
            fields = UNSET
        else:
            fields = Fields.from_dict(_fields)




        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        self_ = d.pop("self", UNSET)

        linked_issue = cls(
            fields=fields,
            id=id,
            key=key,
            self_=self_,
        )

        return linked_issue

