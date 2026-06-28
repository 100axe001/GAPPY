from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="JqlFunctionPrecomputationUpdateBean")



@_attrs_define
class JqlFunctionPrecomputationUpdateBean:
    """ Precomputation id and its new value.

        Attributes:
            id (int):
            value (str):
     """

    id: int
    value: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        value = d.pop("value")

        jql_function_precomputation_update_bean = cls(
            id=id,
            value=value,
        )

        return jql_function_precomputation_update_bean

