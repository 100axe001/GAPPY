from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.jql_query import JqlQuery





T = TypeVar("T", bound="ParsedJqlQuery")



@_attrs_define
class ParsedJqlQuery:
    """ Details of a parsed JQL query.

        Attributes:
            query (str): The JQL query that was parsed and validated.
            errors (list[str] | Unset): The list of syntax or validation errors.
            structure (JqlQuery | Unset): A parsed JQL query.
     """

    query: str
    errors: list[str] | Unset = UNSET
    structure: JqlQuery | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.jql_query import JqlQuery
        query = self.query

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors



        structure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.structure, Unset):
            structure = self.structure.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "query": query,
        })
        if errors is not UNSET:
            field_dict["errors"] = errors
        if structure is not UNSET:
            field_dict["structure"] = structure

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jql_query import JqlQuery
        d = dict(src_dict)
        query = d.pop("query")

        errors = cast(list[str], d.pop("errors", UNSET))


        _structure = d.pop("structure", UNSET)
        structure: JqlQuery | Unset
        if isinstance(_structure,  Unset):
            structure = UNSET
        else:
            structure = JqlQuery.from_dict(_structure)




        parsed_jql_query = cls(
            query=query,
            errors=errors,
            structure=structure,
        )

        return parsed_jql_query

