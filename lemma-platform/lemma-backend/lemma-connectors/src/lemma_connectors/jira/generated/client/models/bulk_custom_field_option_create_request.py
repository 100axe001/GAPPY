from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_field_option_create import CustomFieldOptionCreate





T = TypeVar("T", bound="BulkCustomFieldOptionCreateRequest")



@_attrs_define
class BulkCustomFieldOptionCreateRequest:
    """ Details of the options to create for a custom field.

        Attributes:
            options (list[CustomFieldOptionCreate] | Unset): Details of options to create.
     """

    options: list[CustomFieldOptionCreate] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_field_option_create import CustomFieldOptionCreate
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
        from ..models.custom_field_option_create import CustomFieldOptionCreate
        d = dict(src_dict)
        _options = d.pop("options", UNSET)
        options: list[CustomFieldOptionCreate] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CustomFieldOptionCreate.from_dict(options_item_data)



                options.append(options_item)


        bulk_custom_field_option_create_request = cls(
            options=options,
        )

        return bulk_custom_field_option_create_request

