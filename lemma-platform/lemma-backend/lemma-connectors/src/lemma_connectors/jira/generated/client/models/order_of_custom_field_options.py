from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.order_of_custom_field_options_position import OrderOfCustomFieldOptionsPosition
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OrderOfCustomFieldOptions")



@_attrs_define
class OrderOfCustomFieldOptions:
    """ An ordered list of custom field option IDs and information on where to move them.

        Attributes:
            custom_field_option_ids (list[str]): A list of IDs of custom field options to move. The order of the custom
                field option IDs in the list is the order they are given after the move. The list must contain custom field
                options or cascading options, but not both.
            after (str | Unset): The ID of the custom field option or cascading option to place the moved options after.
                Required if `position` isn't provided.
            position (OrderOfCustomFieldOptionsPosition | Unset): The position the custom field options should be moved to.
                Required if `after` isn't provided.
     """

    custom_field_option_ids: list[str]
    after: str | Unset = UNSET
    position: OrderOfCustomFieldOptionsPosition | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        custom_field_option_ids = self.custom_field_option_ids



        after = self.after

        position: str | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "customFieldOptionIds": custom_field_option_ids,
        })
        if after is not UNSET:
            field_dict["after"] = after
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_field_option_ids = cast(list[str], d.pop("customFieldOptionIds"))


        after = d.pop("after", UNSET)

        _position = d.pop("position", UNSET)
        position: OrderOfCustomFieldOptionsPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = OrderOfCustomFieldOptionsPosition(_position)




        order_of_custom_field_options = cls(
            custom_field_option_ids=custom_field_option_ids,
            after=after,
            position=position,
        )

        return order_of_custom_field_options

