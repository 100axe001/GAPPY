from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.label_fields import LabelFields





T = TypeVar("T", bound="Label")



@_attrs_define
class Label:
    """ Representation of a label and its fields.

        Attributes:
            fields (LabelFields | Unset): A map of the label's fields keyed by the field ID.
            id (str | Unset): The ID of the label.
            kind (str | Unset): This is always drive#label Default: 'drive#label'.
            revision_id (str | Unset): The revision ID of the label.
     """

    fields: LabelFields | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'drive#label'
    revision_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.label_fields import LabelFields
        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        id = self.id

        kind = self.kind

        revision_id = self.revision_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_fields import LabelFields
        d = dict(src_dict)
        _fields = d.pop("fields", UNSET)
        fields: LabelFields | Unset
        if isinstance(_fields,  Unset):
            fields = UNSET
        else:
            fields = LabelFields.from_dict(_fields)




        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        label = cls(
            fields=fields,
            id=id,
            kind=kind,
            revision_id=revision_id,
        )


        label.additional_properties = d
        return label

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
