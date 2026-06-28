from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_field_option_update import CustomFieldOptionUpdate





T = TypeVar("T", bound="CustomFieldUpdatedContextOptionsList")



@_attrs_define
class CustomFieldUpdatedContextOptionsList:
    """ A list of custom field options for a context.

        Attributes:
            options (list[CustomFieldOptionUpdate] | Unset): The updated custom field options.
     """

    options: list[CustomFieldOptionUpdate] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_field_option_update import CustomFieldOptionUpdate
        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_option_update import CustomFieldOptionUpdate
        d = dict(src_dict)
        _options = d.pop("options", UNSET)
        options: list[CustomFieldOptionUpdate] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CustomFieldOptionUpdate.from_dict(options_item_data)



                options.append(options_item)


        custom_field_updated_context_options_list = cls(
            options=options,
        )

        return custom_field_updated_context_options_list

