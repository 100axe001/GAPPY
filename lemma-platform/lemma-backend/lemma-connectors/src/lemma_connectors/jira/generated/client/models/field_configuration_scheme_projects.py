from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.field_configuration_scheme import FieldConfigurationScheme





T = TypeVar("T", bound="FieldConfigurationSchemeProjects")



@_attrs_define
class FieldConfigurationSchemeProjects:
    """ Project list with assigned field configuration schema.

        Attributes:
            project_ids (list[str]): The IDs of projects using the field configuration scheme.
            field_configuration_scheme (FieldConfigurationScheme | Unset): Details of a field configuration scheme.
     """

    project_ids: list[str]
    field_configuration_scheme: FieldConfigurationScheme | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_configuration_scheme import FieldConfigurationScheme
        project_ids = self.project_ids



        field_configuration_scheme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_configuration_scheme, Unset):
            field_configuration_scheme = self.field_configuration_scheme.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "projectIds": project_ids,
        })
        if field_configuration_scheme is not UNSET:
            field_dict["fieldConfigurationScheme"] = field_configuration_scheme

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_configuration_scheme import FieldConfigurationScheme
        d = dict(src_dict)
        project_ids = cast(list[str], d.pop("projectIds"))


        _field_configuration_scheme = d.pop("fieldConfigurationScheme", UNSET)
        field_configuration_scheme: FieldConfigurationScheme | Unset
        if isinstance(_field_configuration_scheme,  Unset):
            field_configuration_scheme = UNSET
        else:
            field_configuration_scheme = FieldConfigurationScheme.from_dict(_field_configuration_scheme)




        field_configuration_scheme_projects = cls(
            project_ids=project_ids,
            field_configuration_scheme=field_configuration_scheme,
        )

        return field_configuration_scheme_projects

