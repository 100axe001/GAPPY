from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_field_context_option import CustomFieldContextOption





T = TypeVar("T", bound="CustomFieldCreatedContextOptionsList")



@_attrs_define
class CustomFieldCreatedContextOptionsList:
    """ A list of custom field options for a context.

        Attributes:
            options (list[CustomFieldContextOption] | Unset): The created custom field options.
     """

    options: list[CustomFieldContextOption] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_field_context_option import CustomFieldContextOption
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
        from ..models.custom_field_context_option import CustomFieldContextOption
        d = dict(src_dict)
        _options = d.pop("options", UNSET)
        options: list[CustomFieldContextOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CustomFieldContextOption.from_dict(options_item_data)



                options.append(options_item)


        custom_field_created_context_options_list = cls(
            options=options,
        )

        return custom_field_created_context_options_list

