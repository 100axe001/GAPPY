from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.field_reference_data import FieldReferenceData
  from ..models.function_reference_data import FunctionReferenceData





T = TypeVar("T", bound="JQLReferenceData")



@_attrs_define
class JQLReferenceData:
    """ Lists of JQL reference data.

        Attributes:
            jql_reserved_words (list[str] | Unset): List of JQL query reserved words.
            visible_field_names (list[FieldReferenceData] | Unset): List of fields usable in JQL queries.
            visible_function_names (list[FunctionReferenceData] | Unset): List of functions usable in JQL queries.
     """

    jql_reserved_words: list[str] | Unset = UNSET
    visible_field_names: list[FieldReferenceData] | Unset = UNSET
    visible_function_names: list[FunctionReferenceData] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_reference_data import FieldReferenceData
        from ..models.function_reference_data import FunctionReferenceData
        jql_reserved_words: list[str] | Unset = UNSET
        if not isinstance(self.jql_reserved_words, Unset):
            jql_reserved_words = self.jql_reserved_words



        visible_field_names: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.visible_field_names, Unset):
            visible_field_names = []
            for visible_field_names_item_data in self.visible_field_names:
                visible_field_names_item = visible_field_names_item_data.to_dict()
                visible_field_names.append(visible_field_names_item)



        visible_function_names: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.visible_function_names, Unset):
            visible_function_names = []
            for visible_function_names_item_data in self.visible_function_names:
                visible_function_names_item = visible_function_names_item_data.to_dict()
                visible_function_names.append(visible_function_names_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if jql_reserved_words is not UNSET:
            field_dict["jqlReservedWords"] = jql_reserved_words
        if visible_field_names is not UNSET:
            field_dict["visibleFieldNames"] = visible_field_names
        if visible_function_names is not UNSET:
            field_dict["visibleFunctionNames"] = visible_function_names

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_reference_data import FieldReferenceData
        from ..models.function_reference_data import FunctionReferenceData
        d = dict(src_dict)
        jql_reserved_words = cast(list[str], d.pop("jqlReservedWords", UNSET))


        _visible_field_names = d.pop("visibleFieldNames", UNSET)
        visible_field_names: list[FieldReferenceData] | Unset = UNSET
        if _visible_field_names is not UNSET:
            visible_field_names = []
            for visible_field_names_item_data in _visible_field_names:
                visible_field_names_item = FieldReferenceData.from_dict(visible_field_names_item_data)



                visible_field_names.append(visible_field_names_item)


        _visible_function_names = d.pop("visibleFunctionNames", UNSET)
        visible_function_names: list[FunctionReferenceData] | Unset = UNSET
        if _visible_function_names is not UNSET:
            visible_function_names = []
            for visible_function_names_item_data in _visible_function_names:
                visible_function_names_item = FunctionReferenceData.from_dict(visible_function_names_item_data)



                visible_function_names.append(visible_function_names_item)


        jql_reference_data = cls(
            jql_reserved_words=jql_reserved_words,
            visible_field_names=visible_field_names,
            visible_function_names=visible_function_names,
        )

        return jql_reference_data

