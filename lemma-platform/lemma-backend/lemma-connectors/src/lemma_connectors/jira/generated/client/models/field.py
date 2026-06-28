from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.field_last_used import FieldLastUsed
  from ..models.json_type_bean import JsonTypeBean





T = TypeVar("T", bound="Field")



@_attrs_define
class Field:
    """ Details of a field.

        Attributes:
            id (str): The ID of the field.
            name (str): The name of the field.
            schema (JsonTypeBean): The schema of a field.
            contexts_count (int | Unset): Number of contexts where the field is used.
            description (str | Unset): The description of the field.
            is_locked (bool | Unset): Whether the field is locked.
            is_unscreenable (bool | Unset): Whether the field is shown on screen or not.
            key (str | Unset): The key of the field.
            last_used (FieldLastUsed | Unset): Information about the most recent use of a field.
            projects_count (int | Unset): Number of projects where the field is used.
            screens_count (int | Unset): Number of screens where the field is used.
            searcher_key (str | Unset): The searcher key of the field. Returned for custom fields.
     """

    id: str
    name: str
    schema: JsonTypeBean
    contexts_count: int | Unset = UNSET
    description: str | Unset = UNSET
    is_locked: bool | Unset = UNSET
    is_unscreenable: bool | Unset = UNSET
    key: str | Unset = UNSET
    last_used: FieldLastUsed | Unset = UNSET
    projects_count: int | Unset = UNSET
    screens_count: int | Unset = UNSET
    searcher_key: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_last_used import FieldLastUsed
        from ..models.json_type_bean import JsonTypeBean
        id = self.id

        name = self.name

        schema = self.schema.to_dict()

        contexts_count = self.contexts_count

        description = self.description

        is_locked = self.is_locked

        is_unscreenable = self.is_unscreenable

        key = self.key

        last_used: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.to_dict()

        projects_count = self.projects_count

        screens_count = self.screens_count

        searcher_key = self.searcher_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "schema": schema,
        })
        if contexts_count is not UNSET:
            field_dict["contextsCount"] = contexts_count
        if description is not UNSET:
            field_dict["description"] = description
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if is_unscreenable is not UNSET:
            field_dict["isUnscreenable"] = is_unscreenable
        if key is not UNSET:
            field_dict["key"] = key
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if projects_count is not UNSET:
            field_dict["projectsCount"] = projects_count
        if screens_count is not UNSET:
            field_dict["screensCount"] = screens_count
        if searcher_key is not UNSET:
            field_dict["searcherKey"] = searcher_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_last_used import FieldLastUsed
        from ..models.json_type_bean import JsonTypeBean
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        schema = JsonTypeBean.from_dict(d.pop("schema"))




        contexts_count = d.pop("contextsCount", UNSET)

        description = d.pop("description", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        is_unscreenable = d.pop("isUnscreenable", UNSET)

        key = d.pop("key", UNSET)

        _last_used = d.pop("lastUsed", UNSET)
        last_used: FieldLastUsed | Unset
        if isinstance(_last_used,  Unset):
            last_used = UNSET
        else:
            last_used = FieldLastUsed.from_dict(_last_used)




        projects_count = d.pop("projectsCount", UNSET)

        screens_count = d.pop("screensCount", UNSET)

        searcher_key = d.pop("searcherKey", UNSET)

        field = cls(
            id=id,
            name=name,
            schema=schema,
            contexts_count=contexts_count,
            description=description,
            is_locked=is_locked,
            is_unscreenable=is_unscreenable,
            key=key,
            last_used=last_used,
            projects_count=projects_count,
            screens_count=screens_count,
            searcher_key=searcher_key,
        )

        return field

