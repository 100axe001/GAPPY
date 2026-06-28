from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.label_modification import LabelModification





T = TypeVar("T", bound="ModifyLabelsRequest")



@_attrs_define
class ModifyLabelsRequest:
    """ A request to modify the set of labels on a file. This request may contain many modifications that will either all
    succeed or all fail transactionally.

        Attributes:
            kind (str | Unset): This is always drive#modifyLabelsRequest Default: 'drive#modifyLabelsRequest'.
            label_modifications (list[LabelModification] | Unset): The list of modifications to apply to the labels on the
                file.
     """

    kind: str | Unset = 'drive#modifyLabelsRequest'
    label_modifications: list[LabelModification] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.label_modification import LabelModification
        kind = self.kind

        label_modifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.label_modifications, Unset):
            label_modifications = []
            for label_modifications_item_data in self.label_modifications:
                label_modifications_item = label_modifications_item_data.to_dict()
                label_modifications.append(label_modifications_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label_modifications is not UNSET:
            field_dict["labelModifications"] = label_modifications

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_modification import LabelModification
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        _label_modifications = d.pop("labelModifications", UNSET)
        label_modifications: list[LabelModification] | Unset = UNSET
        if _label_modifications is not UNSET:
            label_modifications = []
            for label_modifications_item_data in _label_modifications:
                label_modifications_item = LabelModification.from_dict(label_modifications_item_data)



                label_modifications.append(label_modifications_item)


        modify_labels_request = cls(
            kind=kind,
            label_modifications=label_modifications,
        )


        modify_labels_request.additional_properties = d
        return modify_labels_request

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
