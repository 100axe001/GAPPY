from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RemoteIssueLinkIdentifies")



@_attrs_define
class RemoteIssueLinkIdentifies:
    """ Details of the identifiers for a created or updated remote issue link.

        Attributes:
            id (int | Unset): The ID of the remote issue link, such as the ID of the item on the remote system.
            self_ (str | Unset): The URL of the remote issue link.
     """

    id: int | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        self_ = d.pop("self", UNSET)

        remote_issue_link_identifies = cls(
            id=id,
            self_=self_,
        )

        return remote_issue_link_identifies

