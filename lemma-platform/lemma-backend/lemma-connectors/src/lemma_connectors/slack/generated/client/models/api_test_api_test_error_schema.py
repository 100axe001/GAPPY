from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_test_api_test_error_schema_additional_property import ApiTestApiTestErrorSchemaAdditionalProperty





T = TypeVar("T", bound="ApiTestApiTestErrorSchema")



@_attrs_define
class ApiTestApiTestErrorSchema:
    """ Schema for error response api.test method

        Attributes:
            error (str):
            ok (bool):
     """

    error: str
    ok: bool
    additional_properties: dict[str, ApiTestApiTestErrorSchemaAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.api_test_api_test_error_schema_additional_property import ApiTestApiTestErrorSchemaAdditionalProperty
        error = self.error

        ok = self.ok


        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({
            "error": error,
            "ok": ok,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_test_api_test_error_schema_additional_property import ApiTestApiTestErrorSchemaAdditionalProperty
        d = dict(src_dict)
        error = d.pop("error")

        ok = d.pop("ok")

        api_test_api_test_error_schema = cls(
            error=error,
            ok=ok,
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ApiTestApiTestErrorSchemaAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        api_test_api_test_error_schema.additional_properties = additional_properties
        return api_test_api_test_error_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ApiTestApiTestErrorSchemaAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ApiTestApiTestErrorSchemaAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
