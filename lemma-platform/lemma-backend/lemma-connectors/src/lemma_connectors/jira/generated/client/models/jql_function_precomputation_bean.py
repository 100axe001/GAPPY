from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="JqlFunctionPrecomputationBean")



@_attrs_define
class JqlFunctionPrecomputationBean:
    """ Jql function precomputation.

        Attributes:
            arguments (list[str] | Unset):
            created (datetime.datetime | Unset):
            field (str | Unset):
            function_key (str | Unset):
            function_name (str | Unset):
            id (str | Unset):
            operator (str | Unset):
            updated (datetime.datetime | Unset):
            used (datetime.datetime | Unset):
            value (str | Unset):
     """

    arguments: list[str] | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    field: str | Unset = UNSET
    function_key: str | Unset = UNSET
    function_name: str | Unset = UNSET
    id: str | Unset = UNSET
    operator: str | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    used: datetime.datetime | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        arguments: list[str] | Unset = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments



        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field = self.field

        function_key = self.function_key

        function_name = self.function_name

        id = self.id

        operator = self.operator

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        used: str | Unset = UNSET
        if not isinstance(self.used, Unset):
            used = self.used.isoformat()

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if created is not UNSET:
            field_dict["created"] = created
        if field is not UNSET:
            field_dict["field"] = field
        if function_key is not UNSET:
            field_dict["functionKey"] = function_key
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if id is not UNSET:
            field_dict["id"] = id
        if operator is not UNSET:
            field_dict["operator"] = operator
        if updated is not UNSET:
            field_dict["updated"] = updated
        if used is not UNSET:
            field_dict["used"] = used
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arguments = cast(list[str], d.pop("arguments", UNSET))


        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        field = d.pop("field", UNSET)

        function_key = d.pop("functionKey", UNSET)

        function_name = d.pop("functionName", UNSET)

        id = d.pop("id", UNSET)

        operator = d.pop("operator", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated,  Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)




        _used = d.pop("used", UNSET)
        used: datetime.datetime | Unset
        if isinstance(_used,  Unset):
            used = UNSET
        else:
            used = isoparse(_used)




        value = d.pop("value", UNSET)

        jql_function_precomputation_bean = cls(
            arguments=arguments,
            created=created,
            field=field,
            function_key=function_key,
            function_name=function_name,
            id=id,
            operator=operator,
            updated=updated,
            used=used,
            value=value,
        )

        return jql_function_precomputation_bean

