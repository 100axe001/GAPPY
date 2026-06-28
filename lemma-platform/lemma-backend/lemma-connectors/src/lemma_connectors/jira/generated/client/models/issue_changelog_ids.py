from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="IssueChangelogIds")



@_attrs_define
class IssueChangelogIds:
    """ A list of changelog IDs.

        Attributes:
            changelog_ids (list[int]): The list of changelog IDs.
     """

    changelog_ids: list[int]





    def to_dict(self) -> dict[str, Any]:
        changelog_ids = self.changelog_ids




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "changelogIds": changelog_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        changelog_ids = cast(list[int], d.pop("changelogIds"))


        issue_changelog_ids = cls(
            changelog_ids=changelog_ids,
        )

        return issue_changelog_ids

