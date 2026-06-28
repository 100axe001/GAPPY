from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IssueTypeScreenSchemeMapping")



@_attrs_define
class IssueTypeScreenSchemeMapping:
    """ The IDs of the screen schemes for the issue type IDs.

        Attributes:
            issue_type_id (str): The ID of the issue type or *default*. Only issue types used in classic projects are
                accepted. An entry for *default* must be provided and defines the mapping for all issue types without a screen
                scheme.
            screen_scheme_id (str): The ID of the screen scheme. Only screen schemes used in classic projects are accepted.
     """

    issue_type_id: str
    screen_scheme_id: str





    def to_dict(self) -> dict[str, Any]:
        issue_type_id = self.issue_type_id

        screen_scheme_id = self.screen_scheme_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeId": issue_type_id,
            "screenSchemeId": screen_scheme_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_id = d.pop("issueTypeId")

        screen_scheme_id = d.pop("screenSchemeId")

        issue_type_screen_scheme_mapping = cls(
            issue_type_id=issue_type_id,
            screen_scheme_id=screen_scheme_id,
        )

        return issue_type_screen_scheme_mapping

