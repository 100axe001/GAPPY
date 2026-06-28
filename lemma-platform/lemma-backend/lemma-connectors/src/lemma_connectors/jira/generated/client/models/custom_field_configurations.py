from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.contextual_configuration import ContextualConfiguration





T = TypeVar("T", bound="CustomFieldConfigurations")



@_attrs_define
class CustomFieldConfigurations:
    """ Details of configurations for a custom field.

        Attributes:
            configurations (list[ContextualConfiguration]): The list of custom field configuration details.
     """

    configurations: list[ContextualConfiguration]





    def to_dict(self) -> dict[str, Any]:
        from ..models.contextual_configuration import ContextualConfiguration
        configurations = []
        for configurations_item_data in self.configurations:
            configurations_item = configurations_item_data.to_dict()
            configurations.append(configurations_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "configurations": configurations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contextual_configuration import ContextualConfiguration
        d = dict(src_dict)
        configurations = []
        _configurations = d.pop("configurations")
        for configurations_item_data in (_configurations):
            configurations_item = ContextualConfiguration.from_dict(configurations_item_data)



            configurations.append(configurations_item)


        custom_field_configurations = cls(
            configurations=configurations,
        )

        return custom_field_configurations

