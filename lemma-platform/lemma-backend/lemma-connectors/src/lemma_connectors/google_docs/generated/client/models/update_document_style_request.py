from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.document_style import DocumentStyle





T = TypeVar("T", bound="UpdateDocumentStyleRequest")



@_attrs_define
class UpdateDocumentStyleRequest:
    """ Updates the DocumentStyle.

        Attributes:
            document_style (DocumentStyle | Unset): The style of the document.
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `document_style` is implied and should not be specified. A single `"*"` can be used as short-hand for listing
                every field. For example to update the background, set `fields` to `"background"`.
     """

    document_style: DocumentStyle | Unset = UNSET
    fields: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.document_style import DocumentStyle
        document_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_style, Unset):
            document_style = self.document_style.to_dict()

        fields = self.fields


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if document_style is not UNSET:
            field_dict["documentStyle"] = document_style
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_style import DocumentStyle
        d = dict(src_dict)
        _document_style = d.pop("documentStyle", UNSET)
        document_style: DocumentStyle | Unset
        if isinstance(_document_style,  Unset):
            document_style = UNSET
        else:
            document_style = DocumentStyle.from_dict(_document_style)




        fields = d.pop("fields", UNSET)

        update_document_style_request = cls(
            document_style=document_style,
            fields=fields,
        )


        update_document_style_request.additional_properties = d
        return update_document_style_request

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
