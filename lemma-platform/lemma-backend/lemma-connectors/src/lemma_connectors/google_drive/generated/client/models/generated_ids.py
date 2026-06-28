from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GeneratedIds")



@_attrs_define
class GeneratedIds:
    """ A list of generated file IDs which can be provided in create requests.

        Attributes:
            ids (list[str] | Unset): The IDs generated for the requesting user in the specified space.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#generatedIds".
                Default: 'drive#generatedIds'.
            space (str | Unset): The type of file that can be created with these IDs.
     """

    ids: list[str] | Unset = UNSET
    kind: str | Unset = 'drive#generatedIds'
    space: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids



        kind = self.kind

        space = self.space


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ids is not UNSET:
            field_dict["ids"] = ids
        if kind is not UNSET:
            field_dict["kind"] = kind
        if space is not UNSET:
            field_dict["space"] = space

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids", UNSET))


        kind = d.pop("kind", UNSET)

        space = d.pop("space", UNSET)

        generated_ids = cls(
            ids=ids,
            kind=kind,
            space=space,
        )


        generated_ids.additional_properties = d
        return generated_ids

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
