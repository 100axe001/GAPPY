from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.field_reference_data_auto import FieldReferenceDataAuto
from ..models.field_reference_data_deprecated import FieldReferenceDataDeprecated
from ..models.field_reference_data_orderable import FieldReferenceDataOrderable
from ..models.field_reference_data_searchable import FieldReferenceDataSearchable
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FieldReferenceData")



@_attrs_define
class FieldReferenceData:
    """ Details of a field that can be used in advanced searches.

        Attributes:
            auto (FieldReferenceDataAuto | Unset): Whether the field provide auto-complete suggestions.
            cfid (str | Unset): If the item is a custom field, the ID of the custom field.
            deprecated (FieldReferenceDataDeprecated | Unset): Whether this field has been deprecated.
            deprecated_searcher_key (str | Unset): The searcher key of the field, only passed when the field is deprecated.
            display_name (str | Unset): The display name contains the following:

                 *  for system fields, the field name. For example, `Summary`.
                 *  for collapsed custom fields, the field name followed by a hyphen and then the field name and field type. For
                example, `Component - Component[Dropdown]`.
                 *  for other custom fields, the field name followed by a hyphen and then the custom field ID. For example,
                `Component - cf[10061]`.
            operators (list[str] | Unset): The valid search operators for the field.
            orderable (FieldReferenceDataOrderable | Unset): Whether the field can be used in a query's `ORDER BY` clause.
            searchable (FieldReferenceDataSearchable | Unset): Whether the content of this field can be searched.
            types (list[str] | Unset): The data types of items in the field.
            value (str | Unset): The field identifier.
     """

    auto: FieldReferenceDataAuto | Unset = UNSET
    cfid: str | Unset = UNSET
    deprecated: FieldReferenceDataDeprecated | Unset = UNSET
    deprecated_searcher_key: str | Unset = UNSET
    display_name: str | Unset = UNSET
    operators: list[str] | Unset = UNSET
    orderable: FieldReferenceDataOrderable | Unset = UNSET
    searchable: FieldReferenceDataSearchable | Unset = UNSET
    types: list[str] | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        auto: str | Unset = UNSET
        if not isinstance(self.auto, Unset):
            auto = self.auto.value


        cfid = self.cfid

        deprecated: str | Unset = UNSET
        if not isinstance(self.deprecated, Unset):
            deprecated = self.deprecated.value


        deprecated_searcher_key = self.deprecated_searcher_key

        display_name = self.display_name

        operators: list[str] | Unset = UNSET
        if not isinstance(self.operators, Unset):
            operators = self.operators



        orderable: str | Unset = UNSET
        if not isinstance(self.orderable, Unset):
            orderable = self.orderable.value


        searchable: str | Unset = UNSET
        if not isinstance(self.searchable, Unset):
            searchable = self.searchable.value


        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = self.types



        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if auto is not UNSET:
            field_dict["auto"] = auto
        if cfid is not UNSET:
            field_dict["cfid"] = cfid
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if deprecated_searcher_key is not UNSET:
            field_dict["deprecatedSearcherKey"] = deprecated_searcher_key
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if operators is not UNSET:
            field_dict["operators"] = operators
        if orderable is not UNSET:
            field_dict["orderable"] = orderable
        if searchable is not UNSET:
            field_dict["searchable"] = searchable
        if types is not UNSET:
            field_dict["types"] = types
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _auto = d.pop("auto", UNSET)
        auto: FieldReferenceDataAuto | Unset
        if isinstance(_auto,  Unset):
            auto = UNSET
        else:
            auto = FieldReferenceDataAuto(_auto)




        cfid = d.pop("cfid", UNSET)

        _deprecated = d.pop("deprecated", UNSET)
        deprecated: FieldReferenceDataDeprecated | Unset
        if isinstance(_deprecated,  Unset):
            deprecated = UNSET
        else:
            deprecated = FieldReferenceDataDeprecated(_deprecated)




        deprecated_searcher_key = d.pop("deprecatedSearcherKey", UNSET)

        display_name = d.pop("displayName", UNSET)

        operators = cast(list[str], d.pop("operators", UNSET))


        _orderable = d.pop("orderable", UNSET)
        orderable: FieldReferenceDataOrderable | Unset
        if isinstance(_orderable,  Unset):
            orderable = UNSET
        else:
            orderable = FieldReferenceDataOrderable(_orderable)




        _searchable = d.pop("searchable", UNSET)
        searchable: FieldReferenceDataSearchable | Unset
        if isinstance(_searchable,  Unset):
            searchable = UNSET
        else:
            searchable = FieldReferenceDataSearchable(_searchable)




        types = cast(list[str], d.pop("types", UNSET))


        value = d.pop("value", UNSET)

        field_reference_data = cls(
            auto=auto,
            cfid=cfid,
            deprecated=deprecated,
            deprecated_searcher_key=deprecated_searcher_key,
            display_name=display_name,
            operators=operators,
            orderable=orderable,
            searchable=searchable,
            types=types,
            value=value,
        )

        return field_reference_data

