from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.function_operand import FunctionOperand
  from ..models.keyword_operand import KeywordOperand
  from ..models.value_operand import ValueOperand





T = TypeVar("T", bound="ListOperand")



@_attrs_define
class ListOperand:
    """ An operand that is a list of values.

        Attributes:
            values (list[FunctionOperand | KeywordOperand | ValueOperand]): The list of operand values.
            encoded_operand (str | Unset): Encoded operand, which can be used directly in a JQL query.
     """

    values: list[FunctionOperand | KeywordOperand | ValueOperand]
    encoded_operand: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_operand import FunctionOperand
        from ..models.keyword_operand import KeywordOperand
        from ..models.value_operand import ValueOperand
        values = []
        for values_item_data in self.values:
            values_item: dict[str, Any]
            if isinstance(values_item_data, ValueOperand):
                values_item = values_item_data.to_dict()
            elif isinstance(values_item_data, FunctionOperand):
                values_item = values_item_data.to_dict()
            else:
                values_item = values_item_data.to_dict()

            values.append(values_item)



        encoded_operand = self.encoded_operand


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "values": values,
        })
        if encoded_operand is not UNSET:
            field_dict["encodedOperand"] = encoded_operand

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_operand import FunctionOperand
        from ..models.keyword_operand import KeywordOperand
        from ..models.value_operand import ValueOperand
        d = dict(src_dict)
        values = []
        _values = d.pop("values")
        for values_item_data in (_values):
            def _parse_values_item(data: object) -> FunctionOperand | KeywordOperand | ValueOperand:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_jql_query_unitary_operand_type_0 = ValueOperand.from_dict(data)



                    return componentsschemas_jql_query_unitary_operand_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_jql_query_unitary_operand_type_1 = FunctionOperand.from_dict(data)



                    return componentsschemas_jql_query_unitary_operand_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_jql_query_unitary_operand_type_2 = KeywordOperand.from_dict(data)



                return componentsschemas_jql_query_unitary_operand_type_2

            values_item = _parse_values_item(values_item_data)

            values.append(values_item)


        encoded_operand = d.pop("encodedOperand", UNSET)

        list_operand = cls(
            values=values,
            encoded_operand=encoded_operand,
        )


        list_operand.additional_properties = d
        return list_operand

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
