from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.label_field_modification import LabelFieldModification





T = TypeVar("T", bound="LabelModification")



@_attrs_define
class LabelModification:
    """ A modification to a label on a file. A LabelModification can be used to apply a label to a file, update an existing
    label on a file, or remove a label from a file.

        Attributes:
            field_modifications (list[LabelFieldModification] | Unset): The list of modifications to this label's fields.
            kind (str | Unset): This is always drive#labelModification. Default: 'drive#labelModification'.
            label_id (str | Unset): The ID of the label to modify.
            remove_label (bool | Unset): If true, the label will be removed from the file.
     """

    field_modifications: list[LabelFieldModification] | Unset = UNSET
    kind: str | Unset = 'drive#labelModification'
    label_id: str | Unset = UNSET
    remove_label: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.label_field_modification import LabelFieldModification
        field_modifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_modifications, Unset):
            field_modifications = []
            for field_modifications_item_data in self.field_modifications:
                field_modifications_item = field_modifications_item_data.to_dict()
                field_modifications.append(field_modifications_item)



        kind = self.kind

        label_id = self.label_id

        remove_label = self.remove_label


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if field_modifications is not UNSET:
            field_dict["fieldModifications"] = field_modifications
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label_id is not UNSET:
            field_dict["labelId"] = label_id
        if remove_label is not UNSET:
            field_dict["removeLabel"] = remove_label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_field_modification import LabelFieldModification
        d = dict(src_dict)
        _field_modifications = d.pop("fieldModifications", UNSET)
        field_modifications: list[LabelFieldModification] | Unset = UNSET
        if _field_modifications is not UNSET:
            field_modifications = []
            for field_modifications_item_data in _field_modifications:
                field_modifications_item = LabelFieldModification.from_dict(field_modifications_item_data)



                field_modifications.append(field_modifications_item)


        kind = d.pop("kind", UNSET)

        label_id = d.pop("labelId", UNSET)

        remove_label = d.pop("removeLabel", UNSET)

        label_modification = cls(
            field_modifications=field_modifications,
            kind=kind,
            label_id=label_id,
            remove_label=remove_label,
        )


        label_modification.additional_properties = d
        return label_modification

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
