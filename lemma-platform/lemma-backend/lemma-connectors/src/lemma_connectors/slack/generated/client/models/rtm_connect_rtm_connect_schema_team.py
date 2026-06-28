from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RtmConnectRtmConnectSchemaTeam")



@_attrs_define
class RtmConnectRtmConnectSchemaTeam:
    """ 
        Attributes:
            domain (str):
            id (str):
            name (str):
     """

    domain: str
    id: str
    name: str





    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "domain": domain,
            "id": id,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        id = d.pop("id")

        name = d.pop("name")

        rtm_connect_rtm_connect_schema_team = cls(
            domain=domain,
            id=id,
            name=name,
        )

        return rtm_connect_rtm_connect_schema_team

