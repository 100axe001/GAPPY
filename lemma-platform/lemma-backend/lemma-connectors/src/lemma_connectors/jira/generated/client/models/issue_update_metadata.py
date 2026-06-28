from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_update_metadata_fields import IssueUpdateMetadataFields





T = TypeVar("T", bound="IssueUpdateMetadata")



@_attrs_define
class IssueUpdateMetadata:
    """ A list of editable field details.

        Attributes:
            fields (IssueUpdateMetadataFields | Unset):
     """

    fields: IssueUpdateMetadataFields | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_update_metadata_fields import IssueUpdateMetadataFields
        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_update_metadata_fields import IssueUpdateMetadataFields
        d = dict(src_dict)
        _fields = d.pop("fields", UNSET)
        fields: IssueUpdateMetadataFields | Unset
        if isinstance(_fields,  Unset):
            fields = UNSET
        else:
            fields = IssueUpdateMetadataFields.from_dict(_fields)




        issue_update_metadata = cls(
            fields=fields,
        )


        issue_update_metadata.additional_properties = d
        return issue_update_metadata

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
