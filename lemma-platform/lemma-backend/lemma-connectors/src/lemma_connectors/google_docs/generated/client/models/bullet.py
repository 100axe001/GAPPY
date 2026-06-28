from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.text_style import TextStyle





T = TypeVar("T", bound="Bullet")



@_attrs_define
class Bullet:
    """ Describes the bullet of a paragraph.

        Attributes:
            list_id (str | Unset): The ID of the list this paragraph belongs to.
            nesting_level (int | Unset): The nesting level of this paragraph in the list.
            text_style (TextStyle | Unset): Represents the styling that can be applied to text. Inherited text styles are
                represented as unset fields in this message. A text style's parent depends on where the text style is defined: *
                The TextStyle of text in a Paragraph inherits from the paragraph's corresponding named style type. * The
                TextStyle on a named style inherits from the normal text named style. * The TextStyle of the normal text named
                style inherits from the default text style in the Docs editor. * The TextStyle on a Paragraph element that's
                contained in a table may inherit its text style from the table style. If the text style does not inherit from a
                parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.
     """

    list_id: str | Unset = UNSET
    nesting_level: int | Unset = UNSET
    text_style: TextStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_style import TextStyle
        list_id = self.list_id

        nesting_level = self.nesting_level

        text_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style, Unset):
            text_style = self.text_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if list_id is not UNSET:
            field_dict["listId"] = list_id
        if nesting_level is not UNSET:
            field_dict["nestingLevel"] = nesting_level
        if text_style is not UNSET:
            field_dict["textStyle"] = text_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_style import TextStyle
        d = dict(src_dict)
        list_id = d.pop("listId", UNSET)

        nesting_level = d.pop("nestingLevel", UNSET)

        _text_style = d.pop("textStyle", UNSET)
        text_style: TextStyle | Unset
        if isinstance(_text_style,  Unset):
            text_style = UNSET
        else:
            text_style = TextStyle.from_dict(_text_style)




        bullet = cls(
            list_id=list_id,
            nesting_level=nesting_level,
            text_style=text_style,
        )


        bullet.additional_properties = d
        return bullet

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
