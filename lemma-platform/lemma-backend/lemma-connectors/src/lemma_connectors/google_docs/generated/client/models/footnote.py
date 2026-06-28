from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.structural_element import StructuralElement





T = TypeVar("T", bound="Footnote")



@_attrs_define
class Footnote:
    """ A document footnote.

        Attributes:
            content (list[StructuralElement] | Unset): The contents of the footnote. The indexes for a footnote's content
                begin at zero.
            footnote_id (str | Unset): The ID of the footnote.
     """

    content: list[StructuralElement] | Unset = UNSET
    footnote_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.structural_element import StructuralElement
        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)



        footnote_id = self.footnote_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if footnote_id is not UNSET:
            field_dict["footnoteId"] = footnote_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structural_element import StructuralElement
        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: list[StructuralElement] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = StructuralElement.from_dict(content_item_data)



                content.append(content_item)


        footnote_id = d.pop("footnoteId", UNSET)

        footnote = cls(
            content=content,
            footnote_id=footnote_id,
        )


        footnote.additional_properties = d
        return footnote

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
