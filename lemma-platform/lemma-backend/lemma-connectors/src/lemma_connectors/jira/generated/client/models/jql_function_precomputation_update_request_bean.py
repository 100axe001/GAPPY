from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jql_function_precomputation_update_bean import JqlFunctionPrecomputationUpdateBean





T = TypeVar("T", bound="JqlFunctionPrecomputationUpdateRequestBean")



@_attrs_define
class JqlFunctionPrecomputationUpdateRequestBean:
    """ List of pairs (id and value) for precomputation updates.

        Attributes:
            values (list[JqlFunctionPrecomputationUpdateBean] | Unset):
     """

    values: list[JqlFunctionPrecomputationUpdateBean] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jql_function_precomputation_update_bean import JqlFunctionPrecomputationUpdateBean
        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jql_function_precomputation_update_bean import JqlFunctionPrecomputationUpdateBean
        d = dict(src_dict)
        _values = d.pop("values", UNSET)
        values: list[JqlFunctionPrecomputationUpdateBean] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = JqlFunctionPrecomputationUpdateBean.from_dict(values_item_data)



                values.append(values_item)


        jql_function_precomputation_update_request_bean = cls(
            values=values,
        )

        return jql_function_precomputation_update_request_bean

