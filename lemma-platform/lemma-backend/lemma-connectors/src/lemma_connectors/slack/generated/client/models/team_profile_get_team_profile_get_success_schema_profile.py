from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.objs_team_profile_field import ObjsTeamProfileField





T = TypeVar("T", bound="TeamProfileGetTeamProfileGetSuccessSchemaProfile")



@_attrs_define
class TeamProfileGetTeamProfileGetSuccessSchemaProfile:
    """ 
        Attributes:
            fields (list[ObjsTeamProfileField]):
     """

    fields: list[ObjsTeamProfileField]





    def to_dict(self) -> dict[str, Any]:
        from ..models.objs_team_profile_field import ObjsTeamProfileField
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fields": fields,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.objs_team_profile_field import ObjsTeamProfileField
        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in (_fields):
            fields_item = ObjsTeamProfileField.from_dict(fields_item_data)



            fields.append(fields_item)


        team_profile_get_team_profile_get_success_schema_profile = cls(
            fields=fields,
        )

        return team_profile_get_team_profile_get_success_schema_profile

