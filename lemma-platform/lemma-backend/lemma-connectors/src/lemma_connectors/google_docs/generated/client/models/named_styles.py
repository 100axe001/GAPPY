from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.named_style import NamedStyle





T = TypeVar("T", bound="NamedStyles")



@_attrs_define
class NamedStyles:
    """ The named styles. Paragraphs in the document can inherit their TextStyle and ParagraphStyle from these named styles.

        Attributes:
            styles (list[NamedStyle] | Unset): The named styles. There's an entry for each of the possible named style
                types.
     """

    styles: list[NamedStyle] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.named_style import NamedStyle
        styles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.styles, Unset):
            styles = []
            for styles_item_data in self.styles:
                styles_item = styles_item_data.to_dict()
                styles.append(styles_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if styles is not UNSET:
            field_dict["styles"] = styles

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.named_style import NamedStyle
        d = dict(src_dict)
        _styles = d.pop("styles", UNSET)
        styles: list[NamedStyle] | Unset = UNSET
        if _styles is not UNSET:
            styles = []
            for styles_item_data in _styles:
                styles_item = NamedStyle.from_dict(styles_item_data)



                styles.append(styles_item)


        named_styles = cls(
            styles=styles,
        )


        named_styles.additional_properties = d
        return named_styles

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
