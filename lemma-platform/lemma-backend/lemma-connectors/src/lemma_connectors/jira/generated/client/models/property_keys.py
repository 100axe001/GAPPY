from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.property_key import PropertyKey





T = TypeVar("T", bound="PropertyKeys")



@_attrs_define
class PropertyKeys:
    """ List of property keys.

        Attributes:
            keys (list[PropertyKey] | Unset): Property key details.
     """

    keys: list[PropertyKey] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.property_key import PropertyKey
        keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item = keys_item_data.to_dict()
                keys.append(keys_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.property_key import PropertyKey
        d = dict(src_dict)
        _keys = d.pop("keys", UNSET)
        keys: list[PropertyKey] | Unset = UNSET
        if _keys is not UNSET:
            keys = []
            for keys_item_data in _keys:
                keys_item = PropertyKey.from_dict(keys_item_data)



                keys.append(keys_item)


        property_keys = cls(
            keys=keys,
        )

        return property_keys

