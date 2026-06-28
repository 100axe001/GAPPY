from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VersionIssuesStatus")



@_attrs_define
class VersionIssuesStatus:
    """ Counts of the number of issues in various statuses.

        Attributes:
            done (int | Unset): Count of issues with status *done*.
            in_progress (int | Unset): Count of issues with status *in progress*.
            to_do (int | Unset): Count of issues with status *to do*.
            unmapped (int | Unset): Count of issues with a status other than *to do*, *in progress*, and *done*.
     """

    done: int | Unset = UNSET
    in_progress: int | Unset = UNSET
    to_do: int | Unset = UNSET
    unmapped: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        done = self.done

        in_progress = self.in_progress

        to_do = self.to_do

        unmapped = self.unmapped


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if done is not UNSET:
            field_dict["done"] = done
        if in_progress is not UNSET:
            field_dict["inProgress"] = in_progress
        if to_do is not UNSET:
            field_dict["toDo"] = to_do
        if unmapped is not UNSET:
            field_dict["unmapped"] = unmapped

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        done = d.pop("done", UNSET)

        in_progress = d.pop("inProgress", UNSET)

        to_do = d.pop("toDo", UNSET)

        unmapped = d.pop("unmapped", UNSET)

        version_issues_status = cls(
            done=done,
            in_progress=in_progress,
            to_do=to_do,
            unmapped=unmapped,
        )


        version_issues_status.additional_properties = d
        return version_issues_status

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
