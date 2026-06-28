from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.label import Label





T = TypeVar("T", bound="LabelList")



@_attrs_define
class LabelList:
    """ A list of labels.

        Attributes:
            kind (str | Unset): This is always drive#labelList Default: 'drive#labelList'.
            labels (list[Label] | Unset): The list of labels.
            next_page_token (str | Unset): The page token for the next page of labels. This field will be absent if the end
                of the list has been reached. If the token is rejected for any reason, it should be discarded, and pagination
                should be restarted from the first page of results.
     """

    kind: str | Unset = 'drive#labelList'
    labels: list[Label] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.label import Label
        kind = self.kind

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)



        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if labels is not UNSET:
            field_dict["labels"] = labels
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label import Label
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[Label] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = Label.from_dict(labels_item_data)



                labels.append(labels_item)


        next_page_token = d.pop("nextPageToken", UNSET)

        label_list = cls(
            kind=kind,
            labels=labels,
            next_page_token=next_page_token,
        )


        label_list.additional_properties = d
        return label_list

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
