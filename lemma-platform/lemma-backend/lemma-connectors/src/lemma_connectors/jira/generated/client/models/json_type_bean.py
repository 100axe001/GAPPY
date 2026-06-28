from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.json_type_bean_configuration import JsonTypeBeanConfiguration





T = TypeVar("T", bound="JsonTypeBean")



@_attrs_define
class JsonTypeBean:
    """ The schema of a field.

        Attributes:
            type_ (str): The data type of the field.
            configuration (JsonTypeBeanConfiguration | Unset): If the field is a custom field, the configuration of the
                field.
            custom (str | Unset): If the field is a custom field, the URI of the field.
            custom_id (int | Unset): If the field is a custom field, the custom ID of the field.
            items (str | Unset): When the data type is an array, the name of the field items within the array.
            system (str | Unset): If the field is a system field, the name of the field.
     """

    type_: str
    configuration: JsonTypeBeanConfiguration | Unset = UNSET
    custom: str | Unset = UNSET
    custom_id: int | Unset = UNSET
    items: str | Unset = UNSET
    system: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.json_type_bean_configuration import JsonTypeBeanConfiguration
        type_ = self.type_

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        custom = self.custom

        custom_id = self.custom_id

        items = self.items

        system = self.system


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if custom is not UNSET:
            field_dict["custom"] = custom
        if custom_id is not UNSET:
            field_dict["customId"] = custom_id
        if items is not UNSET:
            field_dict["items"] = items
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_type_bean_configuration import JsonTypeBeanConfiguration
        d = dict(src_dict)
        type_ = d.pop("type")

        _configuration = d.pop("configuration", UNSET)
        configuration: JsonTypeBeanConfiguration | Unset
        if isinstance(_configuration,  Unset):
            configuration = UNSET
        else:
            configuration = JsonTypeBeanConfiguration.from_dict(_configuration)




        custom = d.pop("custom", UNSET)

        custom_id = d.pop("customId", UNSET)

        items = d.pop("items", UNSET)

        system = d.pop("system", UNSET)

        json_type_bean = cls(
            type_=type_,
            configuration=configuration,
            custom=custom,
            custom_id=custom_id,
            items=items,
            system=system,
        )

        return json_type_bean

