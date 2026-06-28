from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.objs_team_profile_field_type import ObjsTeamProfileFieldType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ObjsTeamProfileField")



@_attrs_define
class ObjsTeamProfileField:
    """ 
        Attributes:
            hint (str):
            id (str):
            label (str):
            ordering (float):
            type_ (ObjsTeamProfileFieldType):
            field_name (None | str | Unset):
            is_hidden (bool | Unset):
            options (Any | Unset):
            possible_values (list[str] | None | Unset):
     """

    hint: str
    id: str
    label: str
    ordering: float
    type_: ObjsTeamProfileFieldType
    field_name: None | str | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    options: Any | Unset = UNSET
    possible_values: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        hint = self.hint

        id = self.id

        label = self.label

        ordering = self.ordering

        type_ = self.type_.value

        field_name: None | str | Unset
        if isinstance(self.field_name, Unset):
            field_name = UNSET
        else:
            field_name = self.field_name

        is_hidden = self.is_hidden

        options = self.options

        possible_values: list[str] | None | Unset
        if isinstance(self.possible_values, Unset):
            possible_values = UNSET
        elif isinstance(self.possible_values, list):
            possible_values = self.possible_values


        else:
            possible_values = self.possible_values


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "hint": hint,
            "id": id,
            "label": label,
            "ordering": ordering,
            "type": type_,
        })
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if is_hidden is not UNSET:
            field_dict["is_hidden"] = is_hidden
        if options is not UNSET:
            field_dict["options"] = options
        if possible_values is not UNSET:
            field_dict["possible_values"] = possible_values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hint = d.pop("hint")

        id = d.pop("id")

        label = d.pop("label")

        ordering = d.pop("ordering")

        type_ = ObjsTeamProfileFieldType(d.pop("type"))




        def _parse_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_name = _parse_field_name(d.pop("field_name", UNSET))


        is_hidden = d.pop("is_hidden", UNSET)

        options = d.pop("options", UNSET)

        def _parse_possible_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                possible_values_type_0 = cast(list[str], data)

                return possible_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        possible_values = _parse_possible_values(d.pop("possible_values", UNSET))


        objs_team_profile_field = cls(
            hint=hint,
            id=id,
            label=label,
            ordering=ordering,
            type_=type_,
            field_name=field_name,
            is_hidden=is_hidden,
            options=options,
            possible_values=possible_values,
        )

        return objs_team_profile_field

