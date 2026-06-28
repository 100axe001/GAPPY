from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.field_metadata_configuration import FieldMetadataConfiguration
  from ..models.json_type_bean import JsonTypeBean





T = TypeVar("T", bound="FieldMetadata")



@_attrs_define
class FieldMetadata:
    """ The metadata describing an issue field.

        Attributes:
            key (str): The key of the field.
            name (str): The name of the field.
            operations (list[str]): The list of operations that can be performed on the field.
            required (bool): Whether the field is required.
            schema (JsonTypeBean): The schema of a field.
            allowed_values (list[Any] | Unset): The list of values allowed in the field.
            auto_complete_url (str | Unset): The URL that can be used to automatically complete the field.
            configuration (FieldMetadataConfiguration | Unset): The configuration properties.
            default_value (Any | Unset): The default value of the field.
            has_default_value (bool | Unset): Whether the field has a default value.
     """

    key: str
    name: str
    operations: list[str]
    required: bool
    schema: JsonTypeBean
    allowed_values: list[Any] | Unset = UNSET
    auto_complete_url: str | Unset = UNSET
    configuration: FieldMetadataConfiguration | Unset = UNSET
    default_value: Any | Unset = UNSET
    has_default_value: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_metadata_configuration import FieldMetadataConfiguration
        from ..models.json_type_bean import JsonTypeBean
        key = self.key

        name = self.name

        operations = self.operations



        required = self.required

        schema = self.schema.to_dict()

        allowed_values: list[Any] | Unset = UNSET
        if not isinstance(self.allowed_values, Unset):
            allowed_values = self.allowed_values



        auto_complete_url = self.auto_complete_url

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        default_value = self.default_value

        has_default_value = self.has_default_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "name": name,
            "operations": operations,
            "required": required,
            "schema": schema,
        })
        if allowed_values is not UNSET:
            field_dict["allowedValues"] = allowed_values
        if auto_complete_url is not UNSET:
            field_dict["autoCompleteUrl"] = auto_complete_url
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if has_default_value is not UNSET:
            field_dict["hasDefaultValue"] = has_default_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_metadata_configuration import FieldMetadataConfiguration
        from ..models.json_type_bean import JsonTypeBean
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        operations = cast(list[str], d.pop("operations"))


        required = d.pop("required")

        schema = JsonTypeBean.from_dict(d.pop("schema"))




        allowed_values = cast(list[Any], d.pop("allowedValues", UNSET))


        auto_complete_url = d.pop("autoCompleteUrl", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: FieldMetadataConfiguration | Unset
        if isinstance(_configuration,  Unset):
            configuration = UNSET
        else:
            configuration = FieldMetadataConfiguration.from_dict(_configuration)




        default_value = d.pop("defaultValue", UNSET)

        has_default_value = d.pop("hasDefaultValue", UNSET)

        field_metadata = cls(
            key=key,
            name=name,
            operations=operations,
            required=required,
            schema=schema,
            allowed_values=allowed_values,
            auto_complete_url=auto_complete_url,
            configuration=configuration,
            default_value=default_value,
            has_default_value=has_default_value,
        )

        return field_metadata

