from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IssueTypeScreenSchemeItem")



@_attrs_define
class IssueTypeScreenSchemeItem:
    """ The screen scheme for an issue type.

        Attributes:
            issue_type_id (str): The ID of the issue type or *default*. Only issue types used in classic projects are
                accepted. When creating an issue screen scheme, an entry for *default* must be provided and defines the mapping
                for all issue types without a screen scheme. Otherwise, a *default* entry can't be provided.
            issue_type_screen_scheme_id (str): The ID of the issue type screen scheme.
            screen_scheme_id (str): The ID of the screen scheme.
     """

    issue_type_id: str
    issue_type_screen_scheme_id: str
    screen_scheme_id: str





    def to_dict(self) -> dict[str, Any]:
        issue_type_id = self.issue_type_id

        issue_type_screen_scheme_id = self.issue_type_screen_scheme_id

        screen_scheme_id = self.screen_scheme_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issueTypeId": issue_type_id,
            "issueTypeScreenSchemeId": issue_type_screen_scheme_id,
            "screenSchemeId": screen_scheme_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type_id = d.pop("issueTypeId")

        issue_type_screen_scheme_id = d.pop("issueTypeScreenSchemeId")

        screen_scheme_id = d.pop("screenSchemeId")

        issue_type_screen_scheme_item = cls(
            issue_type_id=issue_type_id,
            issue_type_screen_scheme_id=issue_type_screen_scheme_id,
            screen_scheme_id=screen_scheme_id,
        )

        return issue_type_screen_scheme_item

