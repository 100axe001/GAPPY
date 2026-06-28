from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.multiple_custom_field_values_update import MultipleCustomFieldValuesUpdate





T = TypeVar("T", bound="MultipleCustomFieldValuesUpdateDetails")



@_attrs_define
class MultipleCustomFieldValuesUpdateDetails:
    """ List of updates for a custom fields.

        Attributes:
            updates (list[MultipleCustomFieldValuesUpdate] | Unset):
     """

    updates: list[MultipleCustomFieldValuesUpdate] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.multiple_custom_field_values_update import MultipleCustomFieldValuesUpdate
        updates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.updates, Unset):
            updates = []
            for updates_item_data in self.updates:
                updates_item = updates_item_data.to_dict()
                updates.append(updates_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if updates is not UNSET:
            field_dict["updates"] = updates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multiple_custom_field_values_update import MultipleCustomFieldValuesUpdate
        d = dict(src_dict)
        _updates = d.pop("updates", UNSET)
        updates: list[MultipleCustomFieldValuesUpdate] | Unset = UNSET
        if _updates is not UNSET:
            updates = []
            for updates_item_data in _updates:
                updates_item = MultipleCustomFieldValuesUpdate.from_dict(updates_item_data)



                updates.append(updates_item)


        multiple_custom_field_values_update_details = cls(
            updates=updates,
        )

        return multiple_custom_field_values_update_details

