from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FieldConfigurationSchemeProjectAssociation")



@_attrs_define
class FieldConfigurationSchemeProjectAssociation:
    """ Associated field configuration scheme and project.

        Attributes:
            project_id (str): The ID of the project.
            field_configuration_scheme_id (str | Unset): The ID of the field configuration scheme. If the field
                configuration scheme ID is `null`, the operation assigns the default field configuration scheme.
     """

    project_id: str
    field_configuration_scheme_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        field_configuration_scheme_id = self.field_configuration_scheme_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "projectId": project_id,
        })
        if field_configuration_scheme_id is not UNSET:
            field_dict["fieldConfigurationSchemeId"] = field_configuration_scheme_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        field_configuration_scheme_id = d.pop("fieldConfigurationSchemeId", UNSET)

        field_configuration_scheme_project_association = cls(
            project_id=project_id,
            field_configuration_scheme_id=field_configuration_scheme_id,
        )

        return field_configuration_scheme_project_association

