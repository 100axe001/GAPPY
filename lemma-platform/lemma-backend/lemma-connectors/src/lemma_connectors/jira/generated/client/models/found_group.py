from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.group_label import GroupLabel





T = TypeVar("T", bound="FoundGroup")



@_attrs_define
class FoundGroup:
    """ A group found in a search.

        Attributes:
            group_id (str | Unset): The ID of the group, which uniquely identifies the group across all Atlassian products.
                For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*.
            html (str | Unset): The group name with the matched query string highlighted with the HTML bold tag.
            labels (list[GroupLabel] | Unset):
            name (str | Unset): The name of the group. The name of a group is mutable, to reliably identify a group use
                ``groupId`.`
     """

    group_id: str | Unset = UNSET
    html: str | Unset = UNSET
    labels: list[GroupLabel] | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.group_label import GroupLabel
        group_id = self.group_id

        html = self.html

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)



        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if html is not UNSET:
            field_dict["html"] = html
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_label import GroupLabel
        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        html = d.pop("html", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[GroupLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = GroupLabel.from_dict(labels_item_data)



                labels.append(labels_item)


        name = d.pop("name", UNSET)

        found_group = cls(
            group_id=group_id,
            html=html,
            labels=labels,
            name=name,
        )

        return found_group

