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





T = TypeVar("T", bound="ModifyLabelsResponse")



@_attrs_define
class ModifyLabelsResponse:
    """ Response to a ModifyLabels request. This contains only those labels which were added or updated by the request.

        Attributes:
            kind (str | Unset): This is always drive#modifyLabelsResponse Default: 'drive#modifyLabelsResponse'.
            modified_labels (list[Label] | Unset): The list of labels which were added or updated by the request.
     """

    kind: str | Unset = 'drive#modifyLabelsResponse'
    modified_labels: list[Label] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.label import Label
        kind = self.kind

        modified_labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.modified_labels, Unset):
            modified_labels = []
            for modified_labels_item_data in self.modified_labels:
                modified_labels_item = modified_labels_item_data.to_dict()
                modified_labels.append(modified_labels_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if modified_labels is not UNSET:
            field_dict["modifiedLabels"] = modified_labels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label import Label
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        _modified_labels = d.pop("modifiedLabels", UNSET)
        modified_labels: list[Label] | Unset = UNSET
        if _modified_labels is not UNSET:
            modified_labels = []
            for modified_labels_item_data in _modified_labels:
                modified_labels_item = Label.from_dict(modified_labels_item_data)



                modified_labels.append(modified_labels_item)


        modify_labels_response = cls(
            kind=kind,
            modified_labels=modified_labels,
        )


        modify_labels_response.additional_properties = d
        return modify_labels_response

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
